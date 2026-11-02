# Guia del Primer Control — ASW

Abstracció dels 8 controls que hi ha a `control1/`, més la **notació oficial**
extreta de la solució del professor (`teoria/Exercici 4.1 sol.pdf`).

> ⚠️ **Llegeix primer això.** Les solucions que havíem escrit a
> `202526q1_control1_sol.md` i `202526q2_control1_sol.md` tenen **l'anàlisi
> correcta però la notació equivocada**. La solució oficial del professor fa
> servir una notació força diferent, i és la que es corregeix. La secció 2
> d'aquest document és la bona.

---

## 1. L'examen és SEMPRE el mateix

He mirat els 8 controls. **Els quatre apartats i la seva puntuació no han
canviat mai**, ni l'enunciat de les preguntes:

| | Apartat | Punts |
| --- | --- | --- |
| **a)** | Diagrama de flux de navegació complet (*screens and navigational paths*). «Indiqueu clarament quina informació conté cada screen i quines operacions té» | **2** |
| **b)** | Diagrama d'escenari d'interacció (*storyboard sequence*) d'un escenari concret | **1** |
| **c)** | Diagrama de classes del disseny intern de la capa de presentació **amb el patró MVC**, per a l'escenari de b) | **2** |
| **d)** | Diagrama de seqüència del disseny intern de la capa de presentació, per a l'escenari de b) | **2** |
| | | **7** |

Sempre comença igual: *«Us demanen de dissenyar l'UX Model i el Disseny Intern
per a alguna de les funcionalitats que ofereix…»*, i sempre inclou la clàusula
*«Les accions (possibles "clics") no descrites queden fora de l'abast»*.

**El que canvia és només l'aplicació i l'escenari.** O sigui: no cal que
estudiïs «temari», cal que **dominis la notació i el procediment**.

### Els 8 enunciats

| Curs | Aplicació | Escenari de l'apartat b) | Operació CRUD |
| --- | --- | --- | --- |
| 22-23 Q1 | Login / Profile | Usuari nou es crea un compte, després afegeix email i *about* al perfil | **Create + Update** |
| 22-23 Q2 | Preguntes per categoria | Veu les preguntes de «Presentacions» i esborra les marcades *sense pensar-s'ho dues vegades* | **Delete múltiple, sense confirmació** |
| 23-24 Q1 | Perfil | Veu el seu perfil i reescriu la biografia, amb èxit | **Update** |
| 23-24 Q2 | Hotels / Reviews | La Maria mira l'hotel on s'ha allotjat i hi afegeix un review. Ruta inicial donada: `GET /hotels/6789/reviews` | **Create, recurs imbricat** |
| 24-25 Q1 | Comentaris | Pazuzu esborra el seu últim comentari *sense pensar-s'ho dues vegades* | **Delete simple, sense confirmació** |
| 24-25 Q2 | Statuses d'un IT | Jared crea un status nou, «On hold», **entre** dos existents | **Create amb posició** |
| 25-26 Q1 | programming.dev | Veu el seu perfil i canvia la contrasenya, amb èxit | **Update** |
| 25-26 Q2 | Directori de Contactes | Elimina tres contactes alhora, encertant la contrasenya. Ruta inicial donada: `GET /contactes?grup=Missatgers` | **Delete múltiple amb confirmació** |

**Patrons que es repeteixen:**

- L'usuari **ja està loguejat** (excepte 22-23 Q1, on el cas és precisament
  registrar-se).
- L'escenari de b) és **sempre el camí feliç**: «sense errors», «amb èxit»,
  «sense equivocar-se», «sense pensar-s'ho dues vegades».
- **De vegades et donen la ruta inicial.** Si te la donen, **fes-la servir tal
  qual**; si no, te l'inventes tu però que sigui RESTful.
- La meitat dels escenaris són **esborrar** i l'altra meitat **crear o
  modificar**. Prepara't les dues famílies.

---

## 2. LA NOTACIÓ OFICIAL

Això és el que més punts val i el que no es pot improvisar. Tot el que ve a
continuació està tret de la solució del professor a l'Exercici 4.1.

### a) UX Model: Screens & Navigational Paths

**No és un diagrama de flux. És un diagrama de classes UML.**

**Els elements:**

| Element | Com es dibuixa |
| --- | --- |
| **Screen** | Classe amb estereotip **`«screen»`**. Compartiment d'atributs = **la informació que mostra**. Compartiment d'operacions = **les accions que ofereix l'usuari** |
| **Contingut** | Classes **sense estereotip** (p. ex. `Notice`, `Full Notice`), **agregades** a la screen amb un rombe buit i multiplicitat (`*`, `1`) |
| **Variants del contingut** | **Herència** entre classes de contingut: `Full Notice` hereta de `Notice` i hi afegeix `message` — serveix per distingir la versió resumida (a la llista) de la completa (a la pàgina de detall) |
| **Camí de navegació** | **Associació dirigida** entre screens, **etiquetada amb el nom de l'acció** (`View`, `Edit`, `Delete / Back`) |
| **Formulari** | Classe amb estereotip **`«input form»`**, enganxada amb **línia discontínua a l'associació** (no a la screen): és una **classe associativa** |

**Tipus dels camps d'un `«input form»`:** `text`, `textarea`, `date`,
`password`, `checkbox [*]`. El `[*]` vol dir que el camp **es repeteix** tantes
vegades com elements hi hagi — és la manera de dir que el formulari és dinàmic.

**Exemple real (solució oficial, Exercici 4.1):**

```
          ┌──────────────────────┐              ┌──────────────┐
   Delete │  «screen»            │              │   Notice     │
  ┌──────▶│  Notices             │◇────────────▶│ title:String │
  │       ├──────────────────────┤      *       │ from:date    │
  └───────│ course_name : String │              │ to:date      │
          ├──────────────────────┤              └──────▲───────┘
   ┌─────▶│ view()               │                     │ (herència)
   ┊      │ edit()               │              ┌──────┴───────┐
   ┊      │ delete()             │              │ Full Notice  │
   ┊      │ delete selected()    │              │ message:String│
   ┊      └──────────────────────┘              └──────────────┘
   ┊            │ View    ▲ Delete/Back
┌──┴──────────┐ ▼         │
│ «input form»│ ┌───────────────────┐        ┌──────────────────┐
│ Delete      │ │  «screen»         │  Edit  │  «screen»        │
│ selected    │ │  View notice      │───────▶│  Edit notice     │
├─────────────┤ ├───────────────────┤        ├──────────────────┤
│selectNotice │ │ course_name:String│◀───────│ save()           │
│ : checkbox[*]│ ├───────────────────┤  Edit  └──────────────────┘
└─────────────┘ │ edit() delete()   │              ┊
                │ back()            │     ┌────────┴────────┐
                └───────────────────┘     │  «input form»   │
                                          │  Edit Form      │
                                          ├─────────────────┤
                                          │ title : text    │
                                          │ message:textarea│
                                          │ from : date     │
                                          └─────────────────┘
```

### b) Storyboard Sequence

**Diagrama de seqüència amb les screens com a objectes.**

| Element | Com es dibuixa |
| --- | --- |
| Actor | `: User` amb el ninot |
| Screens | Lifelines **d'instància**: `«screen» : Notices` (amb els dos punts al davant) |
| Acció de l'usuari | Missatge de `: User` a la screen, **amb el nom de l'operació** de la screen: `view()`, `edit()`, `save()` |
| Canvi de pantalla | Missatge **`navigate()` de la screen actual a la següent** |
| Omplir un formulari | Missatge etiquetat **`/ fill form /`** (entre barres) |
| Screen repetida | **Una segona lifeline** amb el mateix nom |

**No hi ha fletxes de retorn.** Ni respostes, ni línies discontínues de tornada.

```
: User      : Notices    : View notice   : Edit notice   : View notice
   │  navigate()│              │               │               │
   │───────────▶│              │               │               │
   │   view()   │  navigate()  │               │               │
   │───────────▶│─────────────▶│               │               │
   │        edit()             │  navigate     │               │
   │──────────────────────────▶│──────────────▶│               │
   │        / fill form /                      │               │
   │──────────────────────────────────────────▶│               │
   │        save()                             │   navigate    │
   │──────────────────────────────────────────▶│──────────────▶│
```

### c) Disseny intern: diagrama de classes (WAE2 + MVC)

**⚠️ Es dibuixa UN DIAGRAMA PER CADA PETICIÓ HTTP de l'escenari.** La solució
oficial de l'Exercici 4.1 en té quatre (1/4, 2/4, 3/4, 4/4) perquè l'escenari té
quatre peticions. No facis un únic diagrama gegant.

**Estereotips de classe:**

| Estereotip | Què és |
| --- | --- |
| `«client page»` | La pàgina HTML que rep el navegador (`notices.html`) |
| `«form»` | Un formulari dins d'una client page (hi va **composat**, rombe ple) |
| `«controller»` | El controlador (`NoticeCtrl`), amb les **accions** com a operacions (`index()`, `edit()`, `update()`) |
| `«view»` | La plantilla (`NoticesView`, `EditNoticeView`) |
| `«model»` | La classe de domini (`Notice`), amb atributs **i** operacions tipus ActiveRecord: `findById(id)`, `findByCourse(…)`, `save()` |
| `Session` | Classe **sense estereotip**, amb el que es manté a la sessió |

**Estereotips d'associació:**

| Associació | Origen → Destí | Nota |
| --- | --- | --- |
| `«GET» /ruta` | (fora) → controller | La petició que entra, al començament |
| `«link» /ruta` | client page → controller | Un enllaç |
| `«submit» /ruta` | form → controller | L'enviament d'un formulari |
| `«render» {@ivar: Tipus}` | controller → view | **Amb les variables d'instància entre claus!** `{@notices: Set(Notice)}`, `{@notice: Notice}` |
| `«builds»` | view → client page | L'HTML que es genera |
| `«redirect» /ruta` | controller → controller | **Bucle sobre el mateix controlador.** Sense vista |
| `«use»` | discontínua, cap al model i cap a Session | Dependència |

**El diagrama d'una petició que NOMÉS llegeix:**

```
«GET» /notices    ┌──────────────┐  «render»            ┌─────────────┐  «builds»  ┌───────────────┐
─────────────────▶│ «controller» │  {@notices:Set(Notice)}│  «view»     │──────────▶│ «client page» │
                  │  NoticeCtrl  │─────────────────────▶│ NoticesView │           │ notices.html  │
                  │  index()     │                      └─────────────┘           └───────────────┘
                  └──────┬───────┘        ┊«use»                ┊«use»
                         ┊«use»           ▼                     ▼
                         ▼          ┌──────────┐          ┌──────────────┐
                   ┌──────────┐     │ Session  │          │  «model»     │
                   │ «model»  │     └──────────┘          │  Notice      │
                   │ Notice   │                          └──────────────┘
                   └──────────┘
```

**El diagrama d'una petició que MODIFICA (PRG):**

```
┌──────────┐ «submit» /notices/:id  ┌──────────────┐   «use»    ┌──────────┐
│ «form»   │───────────────────────▶│ «controller» │┄┄┄┄┄┄┄┄┄┄▶│ «model»  │
│ EditForm │                        │  NoticeCtrl  │            │  Notice  │
└──────────┘                        │  update()    │            │  save()  │
                                    └──────┬───────┘            └──────────┘
                                           │  «redirect» /notices/:id
                                           └────────┘  (bucle, CAP vista)
```

### d) Disseny intern: diagrama de seqüència

**També un per petició.**

| Lifeline | Notació |
| --- | --- |
| Usuari | `: User` amb ninot |
| Formulari | `«form» : EditNoticeForm` |
| Controlador | `«controller» : NoticeCtrl` |
| Model, **com a classe** | `«model» Notice` — per als *finders*: `findById()`, `findByCourse()` |
| Model, **com a instància** | `«model» n : Notice` — per als setters i `save()` |

**Els missatges HTTP porten `#` al davant:** `#GET /notices`, `#PUT /notices/:id`,
`# submit /notices/:id`, `#redirect /notices/:id`.

El controlador es fa una **autocrida** amb el nom de l'acció (`update()`), i els
retorns van amb **fletxa discontínua**.

```
: User    «form»        «controller»    «model»      «model»
          :EditForm     :NoticeCtrl     Notice       n : Notice
  │ #submit /notices/:id │                 │              │
  │────────────▶│        │                 │              │
  │             │ #PUT /notices/:id        │              │
  │             │───────▶│  update()       │              │
  │             │        │──┐              │              │
  │             │        │◀─┘              │              │
  │             │        │ findById(id=)   │              │
  │             │        │────────────────▶│              │
  │             │        │◀┄┄┄┄┄ n ┄┄┄┄┄┄┄│              │
  │             │        │      set*(*)    │              │
  │             │        │───────────────────────────────▶│
  │             │        │◀┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
  │             │        │      save()     │              │
  │             │        │───────────────────────────────▶│
  │             │        │◀┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
  │◀┄┄┄┄┄ #redirect /notices/:id ┄┄┄┄┄┄┄┄┄│              │
```

---

## 3. La taula de rutes REST (memoritza-la)

Tema 4.2, diapositiva 19. És la base dels apartats c) i d):

| Operació | Mètode i URI | Acció | Vista |
| --- | --- | --- | --- |
| Llistar | `GET /posts` | `index` | IndexPostsView |
| Mostrar-ne un | `GET /posts/:id` | `show` | ShowPostView |
| Formulari de creació | `GET /posts/new` | `new` | NewPostView |
| Crear | `POST /posts` | `create` | **— (PRG)** |
| Formulari d'edició | `GET /posts/:id/edit` | `edit` | EditPostView |
| Desar canvis | `PUT /posts/:id` | `update` | **— (PRG)** |
| Esborrar | `DELETE /posts/:id` | `destroy` | **— (PRG)** |

**Les tres que escriuen no renderitzen vista: redirigeixen.** Això és el que
has de dibuixar amb el bucle `«redirect»`.

**Recursos imbricats** (com el 23-24 Q2, hotels/reviews):
`GET /hotels/:hotel_id/reviews` → `ReviewCtrl#index`,
`POST /hotels/:hotel_id/reviews` → `ReviewCtrl#create`.

---

## 4. Procediment per atacar l'examen

**Abans de dibuixar res, fes aquestes quatre llistes en brut** (5 minuts ben
invertits):

1. **Screens.** Una per cada captura de pantalla de l'enunciat. Normalment
   **3**, de vegades 2 o 4.
2. **Per screen: quina informació mostra** → seran els atributs, i les classes
   de contingut agregades.
3. **Per screen: quines accions descriu l'enunciat** → seran les operacions.
   Compta els pics (•) de l'enunciat: cada pic sol ser una operació.
4. **Per cada acció: a quina screen et porta**, i amb quina condició.

Llavors:

- **a)** Dibuixa les screens com a classes, les classes de contingut amb les
  agregacions, les fletxes etiquetades, i penja els `«input form»` de les
  fletxes on s'envien dades.
- **b)** Segueix l'escenari pas a pas. Cada «clic» = una operació de la screen;
  cada canvi de pantalla = un `navigate()`.
- **c)** Converteix cada pas de b) en **una petició HTTP** i fes **un diagrama
  per petició**. Les de lectura porten `«render»` + `«builds»`; les d'escriptura
  porten `«redirect»`.
- **d)** El mateix, però en seqüència, amb els `#` als missatges HTTP.

---

## 5. Les trampes que es repeteixen

**No inventis res que l'enunciat no digui.** La frase *«les accions no descrites
queden fora de l'abast»* hi és a tots els controls, i serveix per retallar: si
veus botons a la captura que l'enunciat no descriu, **no els modelis**.

**«Sense pensar-s'ho dues vegades» = NO hi ha pàgina de confirmació.** Surt al
22-23 Q2 i al 24-25 Q1. Si poses una screen de confirmació que l'enunciat no
descriu, et desquadra tot l'apartat a).

**Però de vegades SÍ que n'hi ha.** Al 25-26 Q2 la confirmació existeix i a més
demana contrasenya. **Llegeix, no apliquis plantilles.**

**Camins d'error: només els que l'enunciat descrigui.** A l'Exercici 4.1 el
formulari d'edició **no en té cap**, i per tant la screen té una sola operació i
cap bucle. Al 25-26 Q1 i Q2, en canvi, els formularis **sí** que es tornen a
mostrar amb missatge d'error.

**Dos clics que fan el mateix = UNA operació.** Al 4.1, clicar el títol d'un
avís i clicar la icona de l'ull porten tots dos a *View notice*: **un sol camí
de navegació**.

**Si et donen la ruta inicial, fes-la servir.** 23-24 Q2 i 25-26 Q2 te la donen.

**Les contrasenyes van al cos, mai a la URL.**

**Recorda qui valida.** La comprovació de la contrasenya o de les dades la fa el
**model**, no el controlador: és regla de negoci.

---

## 6. Checklist abans d'entregar

- [ ] Les screens porten **`«screen»`** i tenen **atributs i operacions**
- [ ] Cada camí de navegació està **etiquetat** amb el nom de l'acció
- [ ] Els formularis són **`«input form»`** penjats de l'associació, no classes soltes
- [ ] Els camps de formulari tenen **tipus** (`text`, `textarea`, `date`, `checkbox [*]`)
- [ ] Al storyboard, les screens són **instàncies** (`: Notices`) i els canvis de pantalla són **`navigate()`**
- [ ] A c), hi ha **un diagrama per petició HTTP**
- [ ] El `«render»` porta **les variables d'instància entre claus**
- [ ] Les peticions que **escriuen** acaben amb **`«redirect»`**, no amb una vista
- [ ] A d), els missatges HTTP porten **`#`**
- [ ] El model apareix **com a classe** (finders) i **com a instància** (save)
