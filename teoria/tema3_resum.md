# Tema 3 — Web and Service Application Architectures

Resum de `grau_asw03_architecture.pdf` (37 diapositives).

Estructura del tema: **Introducció** → **Arquitectures d'aplicacions web** →
**Arquitectures d'aplicacions de servei** → **Cloud computing**.

> **Nota sobre les figures.** Les diapositives 7, 8, 13, 16, 18, 20, 27, 30 i 35
> són **només diagrames**, sense text extraïble. El resum les situa i n'explica
> el contingut a partir de les diapositives d'avaluació que les acompanyen, però
> els dibuixos els has de mirar al PDF: són justament els que et poden demanar
> que reprodueixis.

---

## 1. Introducció

### Software architecture (slide 3) — definició literal

> *Software architecture of a system is the set of structures needed to reason
> about the system, which comprise software elements, relations among them, and
> properties of both.*

Els tres ingredients: **elements**, **relacions** entre ells i **propietats**
d'ambdós.

### Architectural viewpoints (slide 4) — la distinció clau del tema

| | Què és | Decideix el desplegament? |
| --- | --- | --- |
| **Logical view** | L'organització a gran escala dels components de programari en **packages, subsystems i layers** que separen lògicament la funcionalitat | **No.** Per això es diu "lògica": no hi ha cap decisió sobre com es reparteixen els elements entre nodes |
| **Physical view** | L'organització i **distribució de l'arquitectura lògica entre diferents nodes computacionals** d'una xarxa | Sí |

**Vocabulari que es confon a posta als exàmens**: la vista lògica es compta en
**layers** (capes) i la física en **tiers**. La slide 5 en dona l'exemple:
*3-Layered Logical Architecture* al costat de *2(+)-Tiered Client/Server
Physical Architecture*. Una arquitectura de 3 capes lògiques pot desplegar-se
en 2 tiers físics: no hi ha correspondència 1 a 1.

---

## 2. Arquitectures d'aplicacions web

Slides 7 i 8 (figures): arquitectura lògica-física de les **"classic" web apps**
i de les **single-page apps**. La diferència és on viu la capa de presentació:
a la clàssica el servidor genera l'HTML sencer; a la SPA el client executa la
presentació i el servidor passa a exposar dades.

### Dimensions en el disseny de l'arquitectura física (slide 9)

Tres grups de coses a considerar:

1. **Requisits no funcionals** que busquen un nivell de servei adequat
2. **Restriccions** físiques, financeres i organitzatives que afecten les decisions
3. **Escenaris alternatius** de desplegament

### Requisits no funcionals (slide 10) — 5

| Requisit | Contingut |
| --- | --- |
| **Performance** | Aguantar la càrrega esperada, definida com: nombre màxim d'usuaris concurrents, nombre de peticions de pàgina per unitat de temps, i temps màxim per lliurar una pàgina al client |
| **Scalability** | L'arquitectura ha de ser fàcilment extensible, **idealment afegint més instàncies** (escalat **horitzontal**) |
| **Availability** | Les fallades no han d'afectar significativament el servei |
| **State maintenance** (reliability) | L'estat de la interacció de l'usuari s'ha de preservar, **fins i tot** quan l'aplicació està distribuïda en diverses màquines o hi ha fallades |
| **Security** | Les dades han d'estar protegides; els usuaris identificats i amb accés **només** a les dades i funcions a què tenen dret |

### Restriccions (slide 11) — 3

- **Cost**: cada configuració demana una inversió diferent en processadors,
  infraestructura de xarxa, interfícies i llicències de programari o
  subscripcions al núvol. El pressupost pot limitar què es pot triar.
- **Complexity**: algunes configuracions són més simples de muntar i mantenir.
  La **manca o el cost de perfils tècnics especialitzats** també és una restricció.
- **Corporate standards and infrastructures**: si es desplega dins la
  infraestructura IT d'una empresa, això limita el maquinari i el programari.

### Escenaris de desplegament (slide 12) — 3

| Escenari | Qui té l'equipament | Qui l'opera |
| --- | --- | --- |
| **On-premises** | L'organització, al seu propi centre de dades | El seu departament IT intern |
| **Co-located** | L'organització (és el seu equipament) però **instal·lat en un centre de dades d'un tercer** | Encara el seu departament IT intern |
| **Cloud** | El proveïdor extern | El proveïdor extern, aprovisionat **on demand** (IaaS o PaaS). L'aplicació normalment s'empaqueta com a **contenidors** |

El *co-located* és el que es falla: l'equipament és teu i el gestiones tu; el que
lloguem és només l'espai del centre de dades.

---

### Patrons d'arquitectura física (slides 13-25)

Cinc patrons. De cadascun cal saber **quins requisits no funcionals millora i
quins no**: és el format natural de pregunta.

#### Patró 1 — Single Server (slides 13-15)

Tot en una sola màquina: servidor web, runtime de l'aplicació i SGBD.

| Dimensió | Avaluació |
| --- | --- |
| Performance | Depèn de la configuració del servidor: velocitat de CPU, memòria disponible, latència d'accés a disc. **El SGBD consumeix molta memòria i molta CPU** |
| Scalability | **Limitada per l'arquitectura de maquinari del servidor triat** |
| Availability | **Tot element, de programari i de maquinari, és un single point of failure**: si es trenca, tot el sistema penja. Es pot millorar amb maquinari redundant (múltiples CPU, discos en mirall) i executant múltiples processos amb instàncies diferents del servidor web, el runtime i la base de dades |
| State maintenance | **Cap problema** amb cap de les tres possibilitats (client, servidor o base de dades) |
| Security | **Punt feble.** Un atacant que trenqui el tallafocs i el servidor web pren el control de la màquina i obté **accés directe a la base de dades** |
| Cost | **Baix**, mentre no calgui paral·lelisme massiu |
| Complexity | **Baixa** |

#### Patró 2 — Separate Database (slides 16-17)

La base de dades passa a una màquina pròpia, amb un tallafocs intern entremig.

| Dimensió | Avaluació |
| --- | --- |
| Performance | **Millor**: una màquina extra, i cada tier es pot afinar als requisits del programari que hi corre |
| Scalability | **Més escalable**: es pot actuar separadament sobre cada tier. **Normalment el primer coll d'ampolla és al middle tier** |
| Availability | **NO es millora.** Cada component continua sent un single point of failure |
| Security | **Millorada significativament**: el tallafocs intern pot **prohibir del tot les peticions HTTPS** i deixar passar només peticions de base de dades, cosa que dificulta molt arribar a les dades |

Aquesta és la trampa més probable del tema: **separar la base de dades no
millora la disponibilitat**.

#### Patró 3 — Replicated Web Server (slides 18-19)

Diversos servidors web/aplicació darrere d'un balancejador de càrrega.

| Dimensió | Avaluació |
| --- | --- |
| Performance i scalability | **Millorades**: **load balancing** i **clustering** (un grup de servidors —nodes— que donen una vista unificada dels serveis que ofereixen individualment) |
| Availability | **Millorada**: **fail-over** — si un node del clúster cau, la seva càrrega es pot redistribuir entre els altres nodes del mateix clúster |
| State maintenance | Dues opcions: **session affinity** (*sticky sessions*), on el balancejador envia totes les peticions d'una sessió **al mateix servidor**; o **session migration**, on l'estat de sessió **es comparteix** entre els servidors del clúster |
| Security | Millora la **seguretat en la transmissió de dades**: el TLS **es termina al balancejador** i es torna a xifrar cap als servidors |

#### Patró 4 — Separate Static and Dynamic Content (slides 20-21)

- Millora **performance, scalability i availability**: el tier estàtic i el
  dinàmic es poden **replicar independentment**, de manera que el nombre i la
  configuració de màquines es pot optimitzar per separat. Una configuració ben
  equilibrada **acostuma a demanar més instàncies per al tier dinàmic que per a
  l'estàtic**.
- Els recursos estàtics normalment **s'empenyen a una CDN**, cosa que treu
  aquell trànsit de l'origen del tot.
- **El cost addicional és operatiu**: dues unitats de desplegament a construir,
  publicar i monitorar.

#### Patró 5 — Web Caching (slides 22-25)

**Definició**: emmagatzemar temporalment recursos en una ubicació d'accés ràpid
per recuperar-los més tard.

**Beneficis**: reducció del temps de resposta, i reducció de l'**esforç de
càlcul** quan el recurs es construeix dinàmicament.

**Què es pot cachejar** (4 nivells):
1. Pàgines HTML estàtiques i fitxers multimèdia
2. **Fragments** de pàgina calculats per l'aplicació
3. **Dades intermèdies** que l'aplicació consumeix per produir pàgines, p. ex. documents JSON
4. El **resultat de consultes a la base de dades** o d'altres comandes de l'aplicació

**On es pot cachejar** (slides 23-25):

| Lloc | Descripció |
| --- | --- |
| **Browser cache** | Tot navegador té una cache de pàgines HTML i fitxers multimèdia, per accelerar la representació de pàgines amb objectes ja cachejats |
| **Proxy cache** | Guarda una còpia local dels recursos demanats pels usuaris, evitant l'accés a Internet per a pàgines molt demanades. **Avui són rares, perquè el trànsit va xifrat amb HTTPS** |
| **Reverse proxy cache** | Es posa **davant d'un clúster** de servidors: intercepta peticions, cacheja còpies dels objectes que produeixen els servidors i els serveix a les peticions següents. Inclou **page prefetching**: a partir de l'última petició, carrega a la cache les pàgines que és més probable que es demanin a continuació |
| **CDN** | Externalitza la infraestructura de cache a una xarxa de servidors distribuïts per Internet |

**Productes que cita el tema** (val la pena saber quin va on):

- **Davant dels servidors**: Varnish, NGINX, Apache Traffic Server
- **Al costat de l'aplicació**, per a resultats de consultes i dades de sessió:
  Redis, Memcached

**CDN, detalls concrets** (slide 25):

- Les peticions es ruten al **PoP** (*point of presence*) més proper al client,
  mitjançant **resolució DNS o anycast routing**
- La CDN serveix la petició des de la còpia òptima i **pot executar codi
  d'aplicació a l'edge** (*edge functions*)
- Proveïdors: Akamai, Cloudflare, Amazon CloudFront, Fastly

---

## 3. Arquitectures d'aplicacions de servei (slides 26-31)

- Slide 27 (figura): arquitectura lògica-física de les aplicacions de servei.
- **Slide 28**: els requisits no funcionals, les restriccions i els escenaris de
  desplegament **són els mateixos** que per a les aplicacions web. No cal
  aprendre'n una segona llista.
- **Slide 29**, tres afirmacions:
  - Es poden fer servir **els mateixos patrons** que per a aplicacions web,
    tenint en compte els problemes de rendiment i seguretat **inherents als
    escenaris distribuïts**.
  - **El tier de contingut estàtic no és necessari** quan l'aplicació només
    exposa una API: **totes les peticions van al tier d'aplicació**.
  - Quan **diversos tipus de client** consumeixen els serveis, el patró
    **Backend for Frontend** afegeix **un tier per experiència de client**.

### Patró — Backend for Frontend (BFF) (slides 30-31)

| Aspecte | Contingut |
| --- | --- |
| **Tailored APIs** | Cada client rep una resposta a la seva mida: **ni over-fetching, ni under-fetching**, i cap API única intentant satisfer requisits contradictoris |
| **Independent evolution** | Cada BFF és propietat, es desplega i s'escala per part de **l'equip que té el seu frontend** |
| **Fault isolation** | Una caiguda o una sobrecàrrega d'un BFF **no afecta els altres clients** |
| **Costs i riscos** | Més serveis a construir, desplegar, monitorar i assegurar, i lògica que es pot **duplicar** entre BFFs. **Un BFF ha de ser prim: la lògica de negoci pertany als serveis compartits de sota** |

---

## 4. Cloud computing (slides 32-36)

Tot ve de la **definició del NIST** (SP 800-145). La xifra a recordar és
**5 – 3 – 4**: cinc característiques essencials, tres models de servei, quatre
models de desplegament.

### Definició (slide 33)

> *Cloud computing is a model for enabling ubiquitous, convenient, on-demand
> network access to a shared pool of configurable computing resources (e.g.,
> networks, servers, storage, applications, and services) that can be rapidly
> provisioned and released with minimal management effort or service provider
> interaction.*

### 5 característiques essencials (slide 34)

1. **On-demand self-service** — el consumidor aprovisiona capacitat
   unilateralment, automàticament, **sense interacció humana**
2. **Broad network access** — disponible per xarxa i accessible amb mecanismes
   estàndard
3. **Resource pooling** — recursos físics i virtuals assignats i reassignats
   dinàmicament segons la demanda
4. **Rapid elasticity** — la capacitat es pot aprovisionar ràpidament i
   elàsticament
5. **Measured service** — l'ús de recursos es monitora, controla i informa,
   donant transparència al proveïdor i al consumidor

### 3 models de servei (slide 35, figura)

La diapositiva és un diagrama sense text. Els tres models del NIST són
**IaaS**, **PaaS** i **SaaS**, i el tema ja n'havia citat IaaS i PaaS a la
slide 12 en parlar del desplegament al núvol. El que la figura mostra és el
repartiment de responsabilitats entre proveïdor i client, que va creixent cap
al proveïdor d'IaaS a SaaS. **Mira la figura al PDF** per veure exactament com
ho planteja.

### 4 models de desplegament (slide 36)

| Model | Per a qui |
| --- | --- |
| **Private cloud** | Ús exclusiu d'**una sola organització** |
| **Community cloud** | Ús exclusiu d'una **comunitat concreta** de consumidors d'organitzacions amb **preocupacions compartides** |
| **Public cloud** | Ús obert al **públic general** |
| **Hybrid cloud** | **Composició de dues o més** infraestructures distintes (privada, comunitària o pública) unides per tecnologia estandarditzada o propietària que permet la **portabilitat de dades i aplicacions** |

---

## Què és més probable que caigui al quiz

Ordenat per probabilitat, segons què té definició tancada, llista numerada o
contrast explícit — que és el que es pot preguntar en poc espai.

### Molt probable

1. **Lògica vs. física.** Definir-les, o classificar-hi elements. El detall que
   decideix la resposta: **la vista lògica no decideix el desplegament**.
   Vocabulari: **layers** (lògica) vs. **tiers** (física).
2. **Quin patró millora quin requisit — i quin NO.** Els dos casos que es
   contrasten a posta:
   - **Separate Database NO millora la disponibilitat** (cada component segueix
     sent un SPOF), però **sí que millora molt la seguretat**.
   - **Replicated Web Server SÍ que millora la disponibilitat**, via **fail-over**.
3. **Sticky sessions vs. session migration**: qui decideix què. A *session
   affinity* el **balancejador** envia la sessió sempre al mateix servidor; a
   *session migration* l'estat **es comparteix** entre nodes del clúster.
4. **On es pot cachejar**: browser, proxy, reverse proxy, CDN. I **per què els
   proxy caches són rars avui: HTTPS**.
5. **Les xifres del NIST: 5 característiques, 3 models de servei, 4 models de
   desplegament**, i saber enumerar-les.

### Probable

6. **El primer coll d'ampolla és al middle tier** (slide 17).
7. **On-premises vs. co-located vs. cloud**: qui té l'equipament i **qui
   l'opera**. El *co-located* és el que es falla.
8. **Page prefetching**: què és i on viu (al reverse proxy).
9. **CDN**: què és un **PoP**, com s'hi enruta (**DNS o anycast**) i què són les
   **edge functions**.
10. **BFF**: quin problema resol (**over-fetching i under-fetching**, API única
    amb requisits contradictoris) i la regla que **ha de ser prim**.
11. **El tier estàtic no és necessari si l'aplicació només exposa una API.**
12. **Els 5 requisits no funcionals** i les **3 restriccions**, per enumerar.
13. **TLS es termina al balancejador** i es torna a xifrar cap als servidors.

### Menys probable però barat de recordar

14. La **definició literal** d'arquitectura de programari (elements, relacions,
    propietats).
15. **Escalabilitat = afegir instàncies = escalat horitzontal.**
16. **Varnish / NGINX / Apache Traffic Server** davant dels servidors, i
    **Redis / Memcached** al costat de l'aplicació.
17. Al *separate static and dynamic content*, que el **cost addicional és
    operatiu** (dues unitats de desplegament) i que normalment calen **més
    instàncies per al tier dinàmic**.
18. Que en *single server* **el SGBD és intensiu en memòria i CPU**, i que
    l'estat **no és cap problema** amb cap de les tres opcions.

### Si la pregunta és de disseny i no de memòria

El format probable és: et donen un escenari (una pujada de trànsit, un requisit
de disponibilitat, una API amb clients de tipus diferents) i has de **triar
patró i justificar-lo** amb els requisits no funcionals. La justificació que
compta és nomenar **quin requisit millora i a canvi de què** (cost, complexitat,
unitats de desplegament).
