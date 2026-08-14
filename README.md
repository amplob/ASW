# ASW (Aplicacions i Serveis Web)

Grau en Enginyeria Informàtica · FIB · UPC

 **Continguts** oficials de l'assignatura, tal com apareixen a la
[fitxa de l'assignatura a la web de la FIB](https://www.fib.upc.edu/ca/graus/grau-en-enginyeria-informatica/pla-destudis/assignatures/ASW).

L'assignatura tracta com es construeixen sistemes que s'executen *sobre el Web*:
d'una banda les **aplicacions web**, pensades perquè hi interactuï una persona a
través d'un navegador; de l'altra els **serveis web**, pensats perquè hi
interactuï una altra màquina (un altre programa) a través d'una API. Tot i que
comparteixen infraestructura (URIs, HTTP, formats d'intercanvi), les decisions
de disseny que se'n deriven són ben diferents, i aquest contrast és el fil
conductor de tot el temari.

---

## Continguts

### 1. Introducció

> Diferències entre aplicacions web i serveis web. Evolució històrica.
> Característiques principals de les aplicacions i serveis web.

Punt de partida de l'assignatura: fixar el vocabulari i situar-nos
històricament. Es recorre el camí que va del Web original de documents
estàtics enllaçats, al Web de contingut generat dinàmicament al servidor, al
Web d'aplicacions riques que executen lògica al client, i finalment al Web
com a plataforma d'integració entre sistemes (les API).

Idees clau que arrossegarem a la resta del temari:

- **Aplicació web vs. servei web**: qui és el consumidor (persona o programa),
  i què implica això per a la interfície, la representació de les dades i la
  gestió d'errors.
- **Client–servidor i sense estat**: el servidor no recorda res entre peticions;
  qualsevol noció de "sessió" s'ha de construir a sobre.
- **Escalabilitat, latència i cache** com a condicionants presents des del
  primer dia, no com a optimitzacions posteriors.

### 2. Protocols, llenguatges i tecnologies Web

> - El nucli: URIs i HTTP
> - En el client: HTML, CSS, JavaScript, DOM, AJAX
> - En el servidor: PHP, Java Servlets, JSPs, ...
> - Formats d'intercanvi de dades: XML, JSON
> - Serveis Web: SOAP+WSDL, REST

El "com" tecnològic. És el tema més ampli i el que dona la base per poder
parlar amb precisió d'arquitectura i disseny.

- **El nucli**: les **URIs** identifiquen recursos i **HTTP** és el protocol
  uniforme per operar-hi. Cal dominar mètodes (GET, POST, PUT, PATCH, DELETE),
  codis d'estat (2xx, 3xx, 4xx, 5xx), capçaleres, negociació de contingut,
  cache, i les propietats de **seguretat** (*safe*) i **idempotència** dels
  mètodes.
- **En el client**: **HTML** per a l'estructura, **CSS** per a la presentació,
  **JavaScript** + **DOM** per al comportament, i **AJAX** com a punt d'inflexió
  que permet actualitzar part d'una pàgina sense recarregar-la sencera.
- **En el servidor**: les diferents generacions de tecnologia per generar
  respostes dinàmicament (CGI, PHP, Servlets/JSP, frameworks MVC moderns) i el
  patró comú que hi ha per sota: encaminar una petició cap a codi que consulta
  el domini i renderitza una vista.
- **Formats d'intercanvi**: **XML** (amb el seu ecosistema d'esquemes i
  validació) i **JSON** (lleuger i natiu al navegador), i quan convé cadascun.
- **Serveis web**: l'estil **SOAP+WSDL**, basat en contracte i orientat a
  operacions, davant l'estil **REST**, basat en recursos i en l'ús uniforme
  d'HTTP.

### 3. Arquitectures per a Aplicacions i Serveis Web

> Arquitectura Lògica vs. Arquitectura Física. Especificitats i condicionants de
> les aplicacions i serveis web. Components d'una arquitectura web genèrica.
> Patrons d'arquitectures físiques.

Separació fonamental del tema:

- **Arquitectura lògica**: com organitzem el programari en capes
  (presentació, domini, gestió de dades) i quines responsabilitats i
  dependències hi ha entre elles.
- **Arquitectura física**: on s'executa cada peça (navegador, servidor web,
  servidor d'aplicacions, SGBD, cache, CDN) i com es reparteix entre nodes.

S'estudien els components d'una arquitectura web genèrica i els **patrons
d'arquitectura física** habituals per respondre a requisits no funcionals:
balanceig de càrrega, replicació, separació entre contingut estàtic i dinàmic,
capes de cache, i les conseqüències de cada opció sobre disponibilitat,
rendiment i cost.

### 4. Disseny d'Aplicacions Web

> Arquitectura i disseny d'aplicacions web.

Com es dissenya la part visible per a una persona. Es treballa en dos nivells
complementaris:

- **UX Model** (disseny extern): quines **pantalles** (*screens*) hi ha, quina
  informació conté cadascuna, quines operacions ofereix, i quins són els
  **camins de navegació** entre elles. S'hi afegeixen **storyboards**
  (diagrames d'escenari d'interacció) per il·lustrar recorreguts concrets.
- **Disseny intern de la capa de presentació**: com s'implementa el que
  descriu l'UX Model, típicament amb el patró **MVC** (i el *front
  controller* que encamina les peticions), incloent-hi el mapatge de rutes
  HTTP a accions de controlador, el pas de dades a les vistes i patrons com
  **POST/Redirect/GET**.

### 5. Disseny de Serveis Web

> Arquitectura i disseny de serveis web.

L'equivalent del tema anterior quan el consumidor és un programa. Aquí el
disseny consisteix a definir una **API**: identificar els **recursos**,
assignar-los **URIs**, decidir quins **mètodes HTTP** admet cadascun, quines
**representacions** (normalment JSON) s'intercanvien, i com es comuniquen els
errors mitjançant codis d'estat. S'hi tracten també qüestions com el
versionat, la paginació, la hipermèdia (HATEOAS) i el nivell de maduresa de
l'API.

### 6. Seguretat, Usabilitat i Proves d'Aplicacions i Serveis Web

> Aspectes relacionats amb la seguretat, l'usabilitat i l'automatització de
> proves d'aplicacions i serveis web.

Els requisits de qualitat que travessen tot el que s'ha dissenyat:

- **Seguretat**: autenticació i autorització, gestió de sessions, HTTPS, i les
  vulnerabilitats típiques del Web (injecció, XSS, CSRF, exposició de dades),
  amb les contramesures corresponents.
- **Usabilitat**: accessibilitat, disseny adaptatiu, retroacció a l'usuari i
  gestió comprensible dels errors.
- **Proves**: automatització a diferents nivells — unitàries, d'integració,
  d'API i d'interfície d'usuari (fi a fi) — i el seu encaix en un flux
  d'integració contínua.

---

## Organització de la carpeta

| Fitxer | Contingut |
| --- | --- |
| `README.md` | Aquest document: introducció i índex dels continguts |

Els apunts de cada tema s'aniran afegint com a fitxers separats seguint la
numeració dels continguts (`01-introduccio.md`, `02-protocols-i-tecnologies.md`,
i així successivament).

Les solucions dels controls es troben a les carpetes `control1/` i `control2/`
de l'arrel del repositori.
