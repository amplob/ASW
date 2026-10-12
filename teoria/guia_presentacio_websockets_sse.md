# Guia de presentació — WebSockets i Server-Sent Events

Com exposar el tema, repartit entre 5 persones.

Acompanya les transparències i el document de teoria
([`presentacio_websockets_sse.md`](presentacio_websockets_sse.md)).

---

## ⚠️ Abans de res: dos xocs amb la rúbrica

He contrastat la presentació amb
[`Rúbrica d'Avaluació de la Presentació.md`](Rúbrica%20d'Avaluació%20de%20la%20Presentació.md)
i hi ha **dues coses del que m'has dit que la rúbrica contradiu**. No les puc
decidir jo, però val més saber-les abans d'assajar.

### 1. La rúbrica diu **màxim dos oradors**

> *Oradors: Un màxim de dos alumnes han exposat oralment la presentació.*
> — Qualitat de l'exposició oral, primer criteri

Tu em dius que **la presentaran 5 persones**. Si ho feu així, incompliu aquest
criteri. Com que l'apartat es puntua per criteris satisfets *completament*:

| Criteris satisfets | Nota de l'apartat | Pes a la presentació |
| --- | --- | --- |
| 7 de 7 | 4/4 | 25% |
| 6 de 7 | 3/4 | 25% |

O sigui: parlar 5 persones en comptes de 2 us baixa aquest apartat **d'un 4 a un
3**, i amb un pes del 25% això és **0,25 punts sobre 4** de la nota de la
presentació. No és catastròfic, però és regalat.

**Què faria jo:** pregunteu-ho al professor abans d'assajar. Hi ha dues
lectures possibles i només ell les pot resoldre — que la norma sigui literal, o
que sigui una rúbrica reaprofitada d'un enunciat anterior.

**Mentrestant, aquesta guia està muntada perquè funcioni de les dues maneres.**
Els 5 blocs són independents: si al final han de parlar 2 persones, l'orador A
fa els blocs 1–2–3 i l'orador B els blocs 4–5, i no cal tocar res més. Ho tens
detallat al final, a *Pla B*.

### 2. La rúbrica diu **14 minuts (±1)**, no 10–15

> *Gestió del temps: La presentació ha durat 14 (+/- 1) minuts.*

Tu em dius 10–15 minuts. **La finestra bona és 13:00–15:00.** Si acabeu en 10
minuts, suspeneu aquest criteri igual que si us passeu de 15.

Tot el cronometratge d'aquesta guia **apunta a 13:50**, perquè una presentació
assajada sempre s'allarga una mica el dia bo i així caieu al mig de la
finestra.

---

## Com està muntada la presentació

16 diapositives, 5 blocs. Cada bloc és un orador i tanca una idea completa, de
manera que el traspàs no parteix cap explicació per la meitat.

| Bloc | Diapositives | De què va |
| --- | --- | --- |
| 1 | Portada · Què són · Evolució | El problema i d'on venen les dues tecnologies |
| 2 | SSE: què és · format · reconnexió | La primera tecnologia, sencera |
| 3 | WS: handshake · frames · comparativa | La segona, i les dues una al costat de l'altra |
| 4 | Punts forts · Punts febles · Arquitectura | La valoració equilibrada |
| 5 | Quan cada un · Conclusions · Referències · Distribució | El criteri i el tancament |

---

## Què he canviat, i per què

La versió anterior estava pensada per a un sol orador i **no cobria la
rúbrica**. Li faltaven elements obligatoris. Ara:

| Canvi | Motiu |
| --- | --- |
| **Portada amb els 5 noms** | «Títol i autors»: la portada ha d'incloure els noms de **tots** els membres |
| **Nova: "Què són, i per què calen"** | «Introducció»: faltava una diapositiva que respongués explícitament *Què és?* |
| **Nova: "Com hi hem arribat"** | «Evolució»: **faltava del tot**. És 1 dels 7 elements de contingut |
| **Nova: "Punts forts"** | Estaven escampats; la rúbrica els vol «de manera organitzada i concisa» |
| **Nova: "Punts febles i crítiques"** | Igual, i absorbeix la diapositiva de seguretat (el CSWSH és la crítica forta) |
| **Conclusions reescrites** | Hi faltava la **valoració personal, recomanacions i prediccions** |
| **Nova: "Distribució de tasques", l'última** | La rúbrica demana que sigui **l'última transparència** |
| Fusionades «El problema» i «Abans ho simulàvem» | El seu contingut viu ara a la introducció i a l'evolució, que és on toca |

**Hauràs de reexportar el `.pptx`**: el que tens al repo és de la versió
anterior.

### Mapatge rúbrica → diapositiva

Per si voleu repassar que no falta res. Contingut (45%):

| Element de la rúbrica | On és |
| --- | --- |
| Introducció | *Què són, i per què calen* |
| **Evolució** | *Com hi hem arribat* |
| Característiques clau | *SSE: què és*, *El format del cable*, *WS: handshake*, *Després del 101* |
| Exemples de codi/funcionament | Codi a 4 diapositives: EventSource, format del cable, handshake, WebSocket |
| Punts forts | *Punts forts* |
| Punts febles i crítiques | *Punts febles i crítiques* |
| Conclusions i valoració personal | *Conclusions i valoració* (recomanació + sorpresa + predicció) |

Transparències (30%): portada amb títol i 5 autors ✓ · referències ✓ ·
distribució de tasques com a última ✓ · cap text per sota de 24 px ✓ ·
contrast alt i molt espai en blanc ✓.

---

## Repartiment i cronometratge

Objectiu: **13:50**. Cronometreu els assajos de debò, amb mòbil a la vista.

| Bloc | Orador | Diapositiva | Temps | Acumulat |
| --- | --- | --- | --- | --- |
| **1** | A | Portada | 0:15 | 0:15 |
| | | Què són, i per què calen | 1:15 | 1:30 |
| | | Com hi hem arribat | 1:20 | **2:50** |
| **2** | B | SSE: què és | 0:55 | 3:45 |
| | | El format del cable | 0:55 | 4:40 |
| | | La reconnexió ve de regal | 0:55 | **5:35** |
| **3** | C | WS comença parlant HTTP | 1:00 | 6:35 |
| | | Després del 101 ja no és HTTP | 0:55 | 7:30 |
| | | Un al costat de l'altre | 1:00 | **8:30** |
| **4** | D | Punts forts | 0:45 | 9:15 |
| | | Punts febles i crítiques | 1:05 | 10:20 |
| | | Què li fa això a l'arquitectura | 1:00 | **11:20** |
| **5** | E | Quan fer servir cadascun | 0:50 | 12:10 |
| | | Conclusions i valoració | 1:10 | 13:20 |
| | | Referències | 0:10 | 13:30 |
| | | Distribució de tasques | 0:20 | **13:50** |

Blocs: 2:50 · 2:45 · 2:55 · 2:50 · 2:30. La diferència entre el més llarg i el
més curt és de 25 segons.

**Si aneu llargs** (passeu de 11:20 al final del bloc 4): l'orador E retalla
*Quan fer servir cadascun* a dues frases i va directe a conclusions.
**Si aneu curts** (no arribeu a 10:00 al final del bloc 4): l'orador E
desenvolupa els exemples de casos d'ús un per un.

---

## Guió, diapositiva a diapositiva

No us ho aprengueu de memòria. Per a cada diapositiva teniu **la idea única**
que ha de quedar, els punts a tocar, i què no fer.

### Bloc 1 — Orador A

#### Portada · 0:15

- Títol, i "som l'equip" amb un gest cap als noms. **No llegiu els cinc noms un
  per un**, es menja 20 segons i no aporta res.
- Anuncieu l'estructura en una frase: *«Primer veurem què són i d'on vénen,
  després cadascuna per separat, i acabarem amb la comparativa i el criteri per
  triar.»*

#### Què són, i per què calen · 1:15

> **Idea única:** HTTP no deixa que el servidor parli primer, i aquestes dues
> tecnologies són les que omplen aquell buit.

- Definició en una frase: dues tecnologies estàndard del navegador perquè el
  servidor enviï dades **sense que el client les demani**.
- El perquè: HTTP és petició-resposta. Llegiu la cita del tema 2 — **ancora la
  xerrada a l'assignatura i això es nota en la nota**.
- Assenyaleu la fletxa grisa del diagrama: *«aquesta direcció, a HTTP, no
  existeix»*.
- Tanqueu amb els exemples quotidians: xats, notificacions, dashboards, i el
  text que un model de llenguatge va escrivint. *«Tothom d'aquesta sala ho ha
  fet servir avui.»*

**No feu:** entrar en detall tècnic. Aquí només esteu plantant el problema.

#### Com hi hem arribat · 1:20

> **Idea única:** primer van venir els pedaços, després els dos estàndards, i
> ara ja se'n veu el relleu.

- **Els pedaços** (la banda de dalt): *polling* és preguntar cada N segons i
  rebre buit gairebé sempre; *long polling* és que el servidor retingui la
  petició. Totes dues **simulen** el push amb peticions del client.
- **Les dues columnes.** El detall que val la pena remarcar: **SSE es va pensar
  abans però es va estandarditzar després**. WebSockets neix el 2008 i ja té el
  seu RFC el 2011; SSE ve del 2004–2006 i no té recomanació del W3C fins al
  2015.
- **Les dues capses fosques.** El *server push* d'HTTP/2 va fracassar — menys de
  l'1,3% d'ús — i WebTransport ja és a tots els navegadors. Digueu que hi
  tornareu al final.

**No feu:** llegir les deu fites. Dieu-ne quatre: 2006 Opera prova SSE, 2008
neix el nom WebSocket, 2011 RFC 6455, 2015 recomanació d'SSE.

> **Traspàs a B:** *«Comencem per la més senzilla de les dues. [Nom B], què és
> exactament Server-Sent Events?»*

### Bloc 2 — Orador B

#### SSE: què és · 0:55

> **Idea única:** no hi ha cap protocol nou. És una resposta HTTP que no s'acaba
> mai.

- Un sol canal, **de servidor a client**.
- La frase que ha de quedar: *«El client fa un GET normal, i el servidor, en
  comptes de respondre i tancar, deixa la resposta oberta i hi va escrivint.»*
- `Content-Type: text/event-stream`. Només text UTF-8.
- Assenyaleu el codi: **quatre línies** i ja tens un client funcionant.

#### El format del cable · 0:55

> **Idea única:** el protocol sencer són quatre camps i una línia en blanc.

- Reciteu els quatre camps assenyalant-los: `event`, `data`, `id`, `retry`.
- **La línia en blanc tanca cada esdeveniment.** És literalment tot el protocol.
- *«Això es pot generar a mà des de qualsevol llenguatge, sense cap llibreria.»*
- Deixeu caure el camp `id`, que és el que enllaça amb la diapositiva següent.

**No feu:** llegir la taula de la dreta sencera. És per quan repassin després.

#### La reconnexió ve de regal · 0:55

> **Idea única:** això és el que SSE té i WebSockets no.

- Les tres capses, en 10 segons cadascuna: cau la connexió → el navegador torna
  sol → reprèn amb `Last-Event-ID`.
- *«Amb WebSockets tot això te l'escrius tu, amb el seu backoff, i és una font
  d'errors coneguda.»*
- **El parany de les 6 connexions.** Dieu-lo: amb HTTP/1.1 el navegador n'obre
  unes 6 per host comptant totes les pestanyes, i un SSE n'ocupa una de fixa.
  És el típic error que es descobreix en producció. Amb HTTP/2 desapareix.

> **Traspàs a C:** *«Fins aquí, un sentit. Però què passa quan el client també
> ha de parlar? [Nom C].»*

### Bloc 3 — Orador C

#### WebSockets comença parlant HTTP · 1:00

> **Idea única:** WebSockets no obre res de nou; segresta una connexió HTTP.

- Els dos blocs de codi, esquerra i dreta: el client demana `Upgrade`, el
  servidor respon **101 Switching Protocols**.
- La frase que ha de quedar: *«El 101 és la frontera. La connexió TCP ja estava
  oberta i es queda oberta, però a partir d'aquí hi viatja un altre protocol.»*
- Per què importa: com que comença com a HTTP i va pel 443 amb `wss://`,
  **travessa la majoria de firewalls**.
- Si teniu temps: `Sec-WebSocket-Key` **no és seguretat**, només demostra que
  l'altre extrem entén el protocol.

#### Després del 101 ja no és HTTP · 0:55

> **Idea única:** WebSockets no és "HTTP bidireccional". HTTP desapareix.

- *Full duplex*: tots dos extrems envien quan volen, alhora.
- Text **i** binari.
- El punt que més es confon: **ni URLs, ni mètodes, ni codis d'estat, ni
  correlació entre pregunta i resposta.** Si voleu saber quina resposta
  correspon a quina pregunta, hi poseu identificadors vosaltres.
- *«Aquesta llibertat és la seva força i també el seu cost.»*

#### Un al costat de l'altre · 1:00

> **Idea única:** tres files decideixen; la resta són matisos.

- **No llegiu la taula sencera.** Assenyaleu tres files i expliqueu-les:
  **sentit** (si només en necessites un, no paguis per dos), **reconnexió**
  (feina que t'estalvies) i **complexitat** (la conseqüència de tot plegat).
- Digueu explícitament: *«les altres quatre files les teniu aquí per quan
  repasseu la presentació».* Això satisfà el criteri de «suport a l'explicació
  oral» sense llegir-ho tot.

> **Traspàs a D:** *«Amb la taula al davant ja es veu que cadascuna té el seu
> preu. [Nom D] ens els desglossa.»*

### Bloc 4 — Orador D

#### Punts forts · 0:45

> **Idea única:** d'SSE, la simplicitat; de WebSockets, la latència.

- **Dos de cada, no vuit.** D'SSE: la simplicitat radical, i que **hereta tota
  la infraestructura HTTP** (caches, CORS, compressió, HTTP/2) — això és el que
  la gent infravalora. De WebSockets: bidireccional simultani, i que **els
  frames no porten capçaleres HTTP**, cosa que importa quan envies milers de
  missatges petits en un joc.

#### Punts febles i crítiques · 1:05

> **Idea única:** el handshake de WebSocket se salta la Same-Origin Policy.

- Les dues columnes, ràpides: d'SSE, només text i el límit de connexions; de
  WebSockets, que la reconnexió i el protocol de missatges són cosa teva.
- **Pareu-vos a la banda fosca i digueu-la a poc a poc.** La Same-Origin Policy
  protegeix `fetch` i `XHR`, però **el handshake de WebSocket se n'escapa**:
  qualsevol pàgina pot obrir una connexió al vostre servidor i **les cookies hi
  viatgen**. Si no valideu `Origin`, tens *Cross-Site WebSocket Hijacking*.
- La comparació que ho fa entendre: *«és l'equivalent del CSRF, però per a
  WebSockets».*

**Aquesta és la diapositiva que demostra «perspectiva equilibrada», que la
rúbrica demana explícitament.** No la passeu de pressa.

#### Què li fa això a l'arquitectura · 1:00

> **Idea única:** el servidor deixa de ser sense estat, i aquí és on això costa
> diners.

- Tots dos mantenen una **connexió oberta** → el servidor té estat per client.
- Les tres capses: amb servidors replicats cal un **bus de pub/sub** entre
  nodes; el balancejador ha de mantenir connexions llargues; cada connexió és
  memòria i un descriptor de fitxer.
- **La banda final és la que connecta amb l'assignatura i val punts:** és el
  mateix problema de *state maintenance* del tema 3 — *session affinity* o
  *session migration* — però amb connexions obertes, **que no es poden migrar**.
  Si cau el node, cau la connexió. *«Per això el client sempre ha de saber
  reconnectar, i per això SSE regala aquesta part.»*

> **Traspàs a E:** *«Amb tot això sobre la taula, com es tria? [Nom E].»*

### Bloc 5 — Orador E

#### Quan fer servir cadascun · 0:50

> **Idea única:** mireu qui parla, no què sona més modern.

- Columna esquerra: **només el servidor té novetats** → SSE.
- Columna dreta: **el client també parla sovint** → WebSockets.
- **El gancho, i dieu-lo mirant la sala:** *«Quan ChatGPT o Claude us escriuen
  paraula a paraula, això és SSE, no WebSockets. Un cop heu enviat la pregunta,
  només parla el servidor.»* Feu una pausa d'un segon aquí.

#### Conclusions i valoració · 1:10

> **Idea única:** la regla per triar, i què en pensem nosaltres.

- Les dues frases de dalt, a poc a poc.
- **Les tres capses són opinió de l'equip i s'han de dir com a tal:** *«la
  nostra recomanació és…», «a nosaltres ens ha sorprès que…», «nosaltres creiem
  que…»*. La rúbrica demana valoració **personal**, recomanacions i prediccions:
  si ho recitis com un fet, no compta.
- **Feu-les vostres.** Si l'equip no està d'acord amb alguna, canvieu-la. L'únic
  que ha d'haver-hi són les tres coses: recomanació, valoració i predicció.

#### Referències · 0:10

- Una frase: *«aquestes són les fonts; les primàries són el RFC 6455 i el HTML
  Living Standard.»* Passar.

#### Distribució de tasques · 0:20

- *«Ens hem repartit la feina així, i la recerca i la revisió les hem fet entre
  tots.»*
- **Deixeu aquesta diapositiva a la pantalla durant les preguntes.**
- ⚠️ **La taula ha de dir la veritat del que heu fet realment**, no el que diu
  la plantilla que us he deixat.

---

## Les transicions entre oradors

És un criteri propi de la rúbrica («transició suau i ben coordinada»), i és el
que més es nota quan està mal fet. Amb 5 persones en teniu **4 de traspàs**, o
sigui que és on més us hi jugueu.

**La regla:** qui surt **no diu "ara parlarà en Pere"**. Qui surt **planteja la
pregunta** que la diapositiva següent respon, i **nomena** qui la respondrà. Qui
entra comença **responent aquella pregunta**, no saludant.

Les quatre frases ja les teniu al guió de cada bloc. Afegiu-hi la part física:

- **Poseu-vos tots els 5 al davant** des del principi, en semicercle. Entrar i
  sortir de l'escenari quatre vegades es menja 40 segons i trenca el ritme.
- Qui parla fa un pas endavant; quan acaba, fa un pas enrere **mentre el següent
  ja ha començat**. El solapament és el que fa que es vegi assajat.
- **Un sol passador**, i que sigui qui parla. Res de demanar "següent, si us
  plau".
- Qui no parla **mira qui parla**, no la pantalla ni el mòbil. El jurat us mira
  a tots cinc tota l'estona.

---

## Gestió de preguntes

També és criteri de la rúbrica. **Repartiu-vos els temes abans** i decidiu qui
respon què; així no us mireu entre vosaltres quan en caigui una.

| Tema | Respon |
| --- | --- |
| Història, estàndards, RFC | A |
| SSE: format, reconnexió, límits | B |
| WebSockets: handshake, frames, codi | C |
| Seguretat, punts febles, arquitectura | D |
| Casos d'ús, criteri, futur | E |

### Preguntes probables, amb la resposta

**«Per què no fer servir sempre WebSockets, si fa més coses?»**
Perquè pagues complexitat per un canal que sovint no faràs servir: reconnexió
manual, protocol de missatges propi, i infraestructura que de vegades el
bloqueja. Si només parla el servidor, SSE fa la feina amb una desena part del
codi.

**«HTTP/2 no havia resolt això amb el server push?»**
No. El *server push* d'HTTP/2 empenyia **recursos a la cache** (CSS, imatges),
no missatges d'aplicació. I a més Chrome el va desactivar per defecte el 2022
perquè l'usava menys de l'1,3% dels llocs i no donava un guany clar de
rendiment.

**«Com escala això a milions d'usuaris?»**
No escala com HTTP. Cada usuari és una connexió oberta amb estat al servidor.
Cal un bus de publicació i subscripció entre nodes i servidors d'E/S no
bloquejant. És un cost d'arquitectura, no de codi.

**«Què passa si l'usuari perd cobertura?»**
Amb SSE el navegador reconnecta sol i envia `Last-Event-ID`, i el servidor li
dona el que s'ha perdut. Amb WebSockets depèn del codi que hagueu escrit
vosaltres.

**«SSE funciona a tots els navegadors?»**
Sí, a tots els moderns. L'únic que no el va implementar mai va ser Internet
Explorer.

**«I WebTransport, substituirà WebSockets?»**
Ja és a tots els navegadors principals des d'aquest any. Creiem que s'endurà els
casos de jocs i mèdia, perquè va sobre QUIC i permet enviaments no fiables. Però
no veiem que es mengi SSE: per rebre notificacions, SSE seguirà sent més simple.

**Si no sabeu una resposta:** *«No ho sabem del cert; el que sí que sabem és
que…»* i enllaceu amb el que sí domineu. No us inventeu res — el criteri diu
«respostes correctes i convincents», i inventar-se'n una i que et caci costa més
que admetre-ho.

---

## Assaig: llista de comprovació

**Dos assajos complets mínim**, un d'ells amb el projector de debò.

- [ ] Cronometrat sencer i **entre 13:00 i 15:00**. Apunteu el temps de cada bloc.
- [ ] Portada amb els **5 noms reals** i la data. Ara hi ha marcadors `[Nom…]`.
- [ ] Taula de distribució de tasques **omplerta amb la veritat**.
- [ ] Les tres capses de la valoració **dites com a opinió vostra**, no recitades.
- [ ] Les 4 frases de traspàs **assajades en veu alta** i amb el pas endavant.
- [ ] Qui respon quin tipus de pregunta, **decidit**.
- [ ] Mirat **des de l'última fila de l'aula**: tot el text ha de ser llegible.
      (Res baixa de 24 px, però comproveu-ho igualment amb el projector real.)
- [ ] `.pptx` **reexportat** de la versió nova.
- [ ] Una còpia en PDF al portàtil, per si falla el que sigui.

---

## Errors que costen punts

- **Llegir les transparències.** És el que més es penalitza a «explicació de les
  transparències» i a «qualitat de la parla». Les diapositives estan fetes amb
  poc text precisament perquè no es puguin llegir.
- **Córrer a la comparativa.** És la diapositiva amb més densitat i la que més
  es recorda. Un minut sencer, tres files explicades.
- **Dir la valoració com si fos un fet.** La rúbrica vol saber què en penseu
  **vosaltres**.
- **Passar de llarg la distribució de tasques.** És criteri obligatori i és
  l'última cosa que veuen abans de puntuar.
- **Acabar en 10 minuts.** Amb la rúbrica a la mà, això és suspendre la gestió
  del temps igual que passar-se.

---

## Pla B: si han de parlar només dos

Si confirmeu que la norma dels dos oradors és literal, **no cal tocar les
transparències**. Els blocs ja són independents:

| Orador | Blocs | Diapositives | Temps |
| --- | --- | --- | --- |
| **A** | 1, 2, 3 | Portada → Un al costat de l'altre | 8:30 |
| **B** | 4, 5 | Punts forts → Distribució de tasques | 5:20 |

Un sol traspàs, el del bloc 3 al 4, que ja teniu escrit. Els altres tres
desapareixen i guanyeu uns 20 segons, que podeu posar a la comparativa i a les
conclusions.

Els altres tres membres hi consten igualment: **a la portada com a autors i a la
diapositiva de distribució de tasques**, que és on la rúbrica vol veure el
treball d'equip. Expliciteu a la taula què va fer cadascú en la preparació —
recerca, transparències, proves de codi, revisió — perquè és exactament el que
aquell criteri vol comprovar.
