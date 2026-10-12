# WebSockets i Server-Sent Events

Material de suport per a la presentació de 15 minuts (Presentació 1).

La presentació en si està a part, com a *deck*. Aquest document és la teoria
sencera: hi ha més del que cap en 15 minuts, a posta, perquè et serveixi per
preparar-te i per respondre preguntes.

---

## 1. El problema

HTTP és **petició-resposta**. El client pregunta, el servidor contesta, i
s'acaba. El servidor **no pot iniciar una conversa**: no té manera de dir-li res
al navegador si aquest no ha demanat res abans.

Això surt literalment a les transparències de l'assignatura:

> *HTTP is one-way: Clearly separated roles: Clients —Web browsers— make
> requests to —Web— Servers, no vice versa.*
> — ASW, tema 2, diapositiva 26

I xoca amb mig Web modern: un xat, una notificació, un marcador esportiu, un
dashboard que s'actualitza sol, una barra de progrés d'una tasca llarga. En tots
aquests casos **qui té la novetat és el servidor**, i amb HTTP pur no la pot
lliurar.

---

## 2. D'on venen: evolució i apanys anteriors

Abans que existís res estàndard, el *push* se simulava amb peticions del client.

### Polling

El client pregunta cada N segons: *hi ha res nou?*

```
cada 5s:  GET /avisos?desde=1043  →  200 OK  []
cada 5s:  GET /avisos?desde=1043  →  200 OK  []
cada 5s:  GET /avisos?desde=1043  →  200 OK  [{...}]
```

- **Latència**: fins a N segons de retard.
- **Malbaratament**: la immensa majoria de peticions tornen buides. Amb 10.000
  usuaris i N=5 són 2.000 peticions per segon per no dir res.
- Baixar N millora la latència i empitjora el malbaratament. No hi ha bon valor.

### Long polling (Comet)

El client fa una petició i el **servidor la reté oberta** fins que té alguna
novetat (o fins que expira el temps). Quan respon, el client en fa una altra
immediatament.

- **Latència**: gairebé zero. Aquest és l'avantatge.
- **Cost**: una connexió i una petició sencera **per cada missatge**.
- El servidor ha de mantenir moltes peticions en espera, cosa que en servidors
  de fil per petició es menja els fils molt de pressa.

Va ser el que va fer possible el xat de Gmail i tota l'onada "Comet" dels anys
2000. Encara el trobaràs a molt codi, sovint com a pla B.

**Totes dues tècniques imiten el push amb peticions del client.** Funcionen,
però són un pedaç. Avui tenim dos protocols pensats expressament per a això.

### Cronologia

Una cosa que crida l'atenció: **SSE es va concebre abans però es va
estandarditzar després**. WebSockets neix el 2008 i ja té RFC el 2011; SSE ve
del 2004–2006 i no arriba a Recomanació del W3C fins al 2015.

| Any | Fita |
| --- | --- |
| 2004–2006 | Ian Hickson especifica els *server-sent DOM events* dins la proposta Web Applications 1.0 del WHATWG. **Opera** n'implementa una versió experimental (Opera 9) |
| ~2005–2008 | Època dels pedaços: AJAX fa possible el *polling* i el *long polling* (Comet), però no hi ha push de debò |
| 2008 | Michael Carter i Ian Hickson encunyen el nom **WebSocket** |
| 2010 | El treball de WebSocket passa al **IETF**. Els primers navegadors l'implementen amb esborranys **incompatibles entre si** (draft-75 i draft-76) |
| Desembre 2011 | **RFC 6455**: WebSocket queda estandarditzat, versió 13. És la que fem servir avui |
| 2010–2011 | Chrome, Safari i Firefox implementen SSE. L'API es redissenya d'un element a l'objecte `EventSource` |
| Febrer 2015 | **Recomanació del W3C** per a Server-Sent Events. Avui l'especificació viu al **HTML Living Standard** del WHATWG |
| 2015 | HTTP/2 (RFC 7540), amb *server push* |
| 2018 i 2022 | **RFC 8441** i **RFC 9220**: WebSockets sobre HTTP/2 i sobre HTTP/3 |
| 2022 | Chrome **desactiva el server push d'HTTP/2** per defecte (Chrome 106) |
| 2026 | **WebTransport** arriba a tots els navegadors principals; el W3C el publica com a Candidate Recommendation |

---

## 3. Server-Sent Events (SSE)

### Què és

Un **canal d'un sol sentit, de servidor a client**, sobre HTTP de tota la vida.

La idea és molt simple: el client fa un `GET` normal, i el servidor, en comptes
de respondre i tancar, **deixa la resposta oberta i hi va escrivint**
esdeveniments a mesura que passen coses.

- Especificat al **HTML Living Standard** del WHATWG (no té RFC propi).
- `Content-Type: text/event-stream`
- Només **text UTF-8**. Res de binari.
- API de navegador dedicada: **`EventSource`**.

### El format del cable

El protocol sencer són quatre noms de camp i una línia en blanc:

```
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive

event: vot
data: {"id":27,"vots":42}
id: 1043

data: això arriba com a "message"

: això és un comentari, serveix de keepalive

retry: 5000

```

| Camp | Què fa |
| --- | --- |
| `event:` | Nom de l'esdeveniment. Si no hi és, al client arriba com a `message` |
| `data:` | El contingut. Diverses línies `data:` seguides es concatenen amb `\n` |
| `id:` | Marca aquest esdeveniment, per poder reprendre després d'un tall |
| `retry:` | Mil·lisegons que ha d'esperar el client abans de reconnectar |

Una **línia en blanc** tanca cada esdeveniment. Una línia que comença amb `:` és
un comentari i serveix per mantenir viva la connexió sense enviar res.

És tan simple que es pot generar a mà des de qualsevol llenguatge, sense cap
llibreria.

### Al client

```js
const es = new EventSource("/avisos");

// esdeveniments sense nom
es.onmessage = e => console.log(e.data);

// esdeveniments amb nom
es.addEventListener("vot", e => {
  const { id, vots } = JSON.parse(e.data);
  actualitzaComptador(id, vots);
});

es.onerror = () => {
  // informatiu: el navegador ja reconnecta sol
  console.log("connexió perduda, reintentant...");
};

es.close(); // per tancar-lo tu
```

### Al servidor (exemple amb Node/Express)

```js
app.get("/avisos", (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive"
  });

  const desDe = req.header("Last-Event-ID");   // represa
  if (desDe) enviaElsQueFalten(res, desDe);

  const envia = avis => {
    res.write(`event: vot\n`);
    res.write(`data: ${JSON.stringify(avis)}\n`);
    res.write(`id: ${avis.seq}\n\n`);          // la línia en blanc final
  };

  bus.on("vot", envia);
  req.on("close", () => bus.off("vot", envia)); // neteja, imprescindible
});
```

### Reconnexió automàtica: l'argument fort

Això és el que SSE té i WebSockets no:

1. **Cau la connexió** — passa constantment: Wi-Fi, túnels, proxies que tallen
   per inactivitat.
2. **El navegador torna a connectar sol**, sense que escriguis ni una línia.
   L'espera la fixa `retry:` (per defecte uns 3 segons, segons el navegador).
3. **Reprèn on era**: a la nova petició el navegador envia la capçalera
   `Last-Event-ID: 1043`, i el servidor sap per on continuar.

Amb WebSockets tot això te l'escrius tu, amb el seu *backoff* exponencial, i és
una font d'errors coneguda.

### Limitacions

- **Només text.** Per enviar binari l'has de codificar (base64), cosa que
  l'infla un 33%.
- **Un sol sentit.** Per enviar coses al servidor fas servir `fetch` com sempre.
- **No pots posar capçaleres pròpies** a `EventSource`. L'autenticació va per
  cookie (`withCredentials: true`) o per paràmetre a la URL.
- **El límit de connexions per domini.** Amb HTTP/1.1 el navegador n'obre unes
  **6 per host**, comptant totes les pestanyes, i un SSE n'ocupa una de fixa. Si
  l'usuari obre set pestanyes, la setena es queda penjada. **Amb HTTP/2 el
  multiplexatge ho resol** (uns 100 fluxos concurrents per defecte). És el
  parany clàssic, i es descobreix en producció.

---

## 4. WebSockets

### Què és

Un **canal bidireccional i simultani** (*full duplex*) entre client i servidor,
sobre la mateixa connexió TCP que havia començat sent HTTP.

Especificat al **RFC 6455** (IETF, 2011).

### El handshake

WebSockets **no obre res de nou**. Aprofita una petició HTTP normal i demana un
canvi de protocol:

```
GET /xat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
Origin: https://example.com
```

I el servidor accepta:

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

- El **codi 101** és la frontera. La connexió TCP ja estava oberta i es queda
  oberta, però a partir d'aquí hi viatja un altre protocol.
- `Sec-WebSocket-Accept` és `base64(SHA1(clau + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"))`,
  amb una constant fixa del RFC. **No és seguretat**: només demostra que l'altre
  extrem entén el protocol i no és un proxy despistat que repeteix capçaleres.
- Com que comença com a HTTP i va pel port 443 amb `wss://`, travessa la majoria
  de firewalls.

### Després del 101

- La connexió transporta **frames** binaris amb un *opcode*: `0x1` text, `0x2`
  binari, `0x8` tancar, `0x9` ping, `0xA` pong.
- **Full duplex**: els dos extrems envien quan volen, alhora.
- Els frames que van del client al servidor han d'anar **emmascarats** (per
  evitar enverinament de caches intermèdies).
- **No hi ha semàntica HTTP**: ni URLs, ni mètodes, ni codis d'estat, ni
  correlació entre el que envies i el que reps. Si vols saber quina resposta
  correspon a quina pregunta, hi poses identificadors tu.
- `Sec-WebSocket-Protocol` permet negociar un **subprotocol** (per exemple
  `graphql-ws` o un de teu).
- `permessage-deflate` és l'extensió de compressió.

### Al client

```js
const ws = new WebSocket("wss://example.com/xat");

ws.onopen = () => ws.send(JSON.stringify({ tipus: "hola", sala: 12 }));
ws.onmessage = e => pinta(JSON.parse(e.data));
ws.onclose = e => reconnecta(e.code);   // te l'escrius tu
ws.onerror = e => console.error(e);

ws.send(JSON.stringify({ tipus: "missatge", text: "bon dia" }));
ws.close(1000, "adeu");
```

### Limitacions

- **Cap reconnexió automàtica.** Te la fas tu, amb *backoff*.
- **Cap semàntica de missatges.** El protocol d'aplicació és cosa teva.
- **Tampoc pots posar capçaleres pròpies** des del navegador (la mateixa
  limitació que `EventSource`; és un error comú creure que sí).
- **Alguns proxies corporatius el bloquegen**, sobretot en clar.
- Més peces mòbils: més codi, més coses que fallen.

---

## 5. Comparativa

| | **Server-Sent Events** | **WebSockets** |
| --- | --- | --- |
| Sentit | Servidor → client | Bidireccional, simultani |
| Protocol | HTTP, sense res més | Propi, després del handshake |
| Especificació | HTML Living Standard | RFC 6455 |
| Dades | Només text UTF-8 | Text i binari |
| Reconnexió | **Automàtica, i reprèn** amb `Last-Event-ID` | Te l'has d'escriure tu |
| API al navegador | `EventSource` | `WebSocket` |
| Capçaleres pròpies | No | No (des del navegador) |
| Proxies i firewalls | Hi passa: és HTTP normal | De vegades el bloquegen |
| Límit de connexions | Sí amb HTTP/1.1 (~6 per host) | No |
| Compressió | `gzip` d'HTTP | Extensió `permessage-deflate` |
| Complexitat | Baixa | Alta |

---

## 6. Quan triar cadascun

### SSE — quan **només el servidor té novetats**

Notificacions i avisos · dashboards i mètriques en viu · barres de progrés
d'una tasca llarga · cotitzacions i marcadors · seguiment de logs ·
**streaming de tokens d'un model de llenguatge**.

> El cas més visible d'aquests anys: quan ChatGPT o Claude t'escriuen paraula a
> paraula, **això és SSE**, no WebSockets. Un cop has enviat la pregunta, només
> parla el servidor; pagar la complexitat de WebSockets per un canal que no
> faràs servir no té sentit.

### WebSockets — quan **el client també parla sovint** i la latència importa

Xats i missatgeria · jocs multijugador · edició col·laborativa · trading i
subhastes · pissarres compartides · qualsevol cosa on calgui enviar binari.

### La regla pràctica

Comença per SSE. Passa a WebSockets quan et trobis enviant molts `fetch` del
client cap al servidor per mantenir la conversa, o quan necessitis binari.

---

## 7. Implicacions d'arquitectura

**Aquesta és la part que enllaça amb el tema 3, i la que val la pena destacar
en una assignatura d'arquitectura.**

Tots dos mecanismes mantenen una **connexió oberta**. Això vol dir que el
servidor **deixa de ser sense estat**: passa a tenir estat per cada client
connectat. I tota l'escalabilitat d'HTTP venia precisament de no tenir-ne.

Conseqüències concretes:

- **Servidors replicats.** Quin node té la connexió d'aquest usuari? Si
  l'esdeveniment es genera al node B i l'usuari està connectat al node A, el
  node B no el pot avisar. Cal un **bus de publicació i subscripció** entre
  nodes (Redis Pub/Sub, Kafka, NATS) que difongui els esdeveniments a tots.
- **El balancejador** ha de saber mantenir connexions llargues i, en el cas de
  WebSockets, entendre l'`Upgrade`. Normalment cal **session affinity**.
- **No es poden migrar.** Al tema 3 les dues opcions per a l'estat de sessió són
  *session affinity* i *session migration*. Amb una connexió oberta la segona no
  existeix: si cau el node, cau la connexió. **Per això el client sempre ha de
  saber reconnectar** — i per això SSE regala aquesta part.
- **Límits reals de recursos.** Cada connexió és memòria i un descriptor de
  fitxer. És el problema conegut com a *C10K*. Els servidors d'E/S no bloquejant
  (Node, Go, nginx) ho porten molt millor que els de fil per petició.
- **Timeouts.** Proxies i balancejadors tallen connexions inactives al cap d'uns
  minuts. Cal **keepalive**: comentaris `:` a SSE, frames de ping a WebSockets.

---

## 8. Seguretat

**El punt que sorprèn:** el handshake de WebSocket **no està protegit per la
Same-Origin Policy**. La SOP protegeix `XMLHttpRequest` i `fetch`, però el
handshake se n'escapa: qualsevol pàgina pot obrir un WebSocket cap al teu
servidor, **i les cookies hi viatgen**.

Si el servidor no valida la capçalera `Origin`, tens **Cross-Site WebSocket
Hijacking** (CSWSH), que és l'equivalent del CSRF per a WebSockets. Per això
molts dissenys passen un token al primer missatge en comptes de confiar en la
cookie.

La resta:

- **Sempre xifrat**: `wss://` i HTTPS. En clar, qualsevol xarxa intermèdia ho
  llegeix i ho pot modificar.
- **Autentica al handshake**: és l'únic moment on encara parles HTTP i tens
  capçaleres on posar coses.
- **SSE sí que passa per CORS**, perquè és una petició HTTP normal. Però
  `EventSource` no deixa posar capçaleres, o sigui que l'autenticació va per
  cookie.
- **Valida cada missatge al servidor.** Una connexió oberta no és una connexió
  de confiança: l'usuari pot enviar el que vulgui per un WebSocket ja establert.
- **Limita la mida i la freqüència** dels missatges entrants, o tens una
  denegació de servei barata.

---

## 9. Context i alternatives

- **HTTP/2 Server Push** — la diapositiva 26 del tema 2 diu que *"HTTP 2.0 now
  supports push notifications"*. Compte amb això: el *server push* d'HTTP/2
  servia per **empènyer recursos a la cache del navegador** (CSS, imatges), no
  per enviar missatges d'aplicació. A més **està desactivat a la pràctica**:
  Chrome el va desactivar per defecte a partir de Chrome 106 (2022) perquè
  només l'usava entre el 0,7% i l'1,25% dels llocs amb HTTP/2 i no donava un
  guany clar de rendiment; l'alternativa que recomanen per al cas d'ús real és
  `103 Early Hints`. **No és una alternativa a SSE ni a WebSockets.**
- **WebTransport** (sobre HTTP/3 i QUIC) — bidireccional, amb fluxos fiables
  *i* datagrames no fiables. És el candidat a succeir WebSockets per a jocs i
  temps real exigent. Encara emergent.
- **Socket.IO** — llibreria, no estàndard. Embolcalla WebSockets i cau a long
  polling quan no hi ha manera. Còmoda, però els dos extrems han de fer servir
  la mateixa llibreria.
- **WebRTC Data Channels** — per a comunicació directa entre navegadors, no
  entre navegador i servidor.

---

## 10. Guió i repartiment

El cronometratge i el guió diapositiva a diapositiva, repartit entre els 5
oradors, són a **[`guia_presentacio_websockets_sse.md`](guia_presentacio_websockets_sse.md)**,
juntament amb les frases de traspàs entre oradors, el mapatge amb la rúbrica i
la llista de comprovació per als assajos.

Dos avisos que hi trobaràs desenvolupats i que convé saber ja:

- La rúbrica diu **màxim dos oradors**, no cinc.
- La rúbrica diu **14 minuts ±1**, és a dir una finestra de 13:00 a 15:00:
  acabar en 10 minuts suspèn aquell criteri igual que passar-se de 15.

---

## 11. Preguntes que et poden fer

**Per què no fer servir sempre WebSockets, si fa més coses?**
Perquè pagues complexitat per un canal que sovint no faràs servir: reconnexió
manual, protocol de missatges propi, i una infraestructura que de vegades el
bloqueja. Si només parla el servidor, SSE fa la feina amb una desena part del
codi.

**I HTTP/2 no havia resolt això amb el server push?**
No. El server push d'HTTP/2 empenyia recursos a la cache, no missatges
d'aplicació, i a més Chrome el va desactivar per defecte el 2022 perquè
l'usava menys de l'1,3% dels llocs i no donava un guany clar de rendiment.

**Com escala això a milions d'usuaris?**
No escala com HTTP. Cada usuari és una connexió oberta amb estat al servidor.
Cal un bus de publicació i subscripció entre nodes i servidors d'E/S no
bloquejant. És un cost d'arquitectura, no de codi.

**Què passa si l'usuari té el mòbil a la butxaca i perd cobertura?**
Amb SSE, el navegador reconnecta sol i envia `Last-Event-ID`, i el servidor li
dona el que s'ha perdut. Amb WebSockets, depèn del codi que hagis escrit tu.

**SSE funciona a tots els navegadors?**
Sí, a tots els moderns. L'únic que no el va implementar mai va ser Internet
Explorer, que ja no compta.

---

## 12. Referències

- **RFC 6455** — *The WebSocket Protocol*. IETF, 2011.
- **HTML Living Standard**, secció *Server-sent events*. WHATWG.
- **MDN Web Docs** — `EventSource` i `WebSocket` API.
- **RFC 9113** — *HTTP/2*, secció sobre server push.
- **OWASP** — *Testing WebSockets* i *Cross-Site WebSocket Hijacking*.
- **ASW**, tema 2 (HTTP, diapositiva 26) i tema 3 (arquitectures, diapositiva 19).
