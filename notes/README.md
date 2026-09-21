# Seguiment de la nota — ASW

Dos fitxers:

| Fitxer | Què és |
| --- | --- |
| `notes.csv` | **El que edites.** Hi apuntes les notes a mesura que te les donen |
| `nota.py` | La calculadora: aplica la fórmula de l'assignatura i et diu on ets |
| `resum.csv` | **Generat.** El desglossament item per item, per obrir amb Excel |

## Ús

```bash
python3 notes/nota.py
```

Edita la columna `nota` de `notes.csv` (escala 0–10, deixa-la buida si encara
no la tens) i torna a executar-ho. Res més. Les notes que hi falten no compten
ni a favor ni en contra: queden com a "punts encara en joc".

Opcions: `--csv <ruta>` per fer servir un altre fitxer (útil per simular
escenaris sense tocar el bo) i `--sense-resum` per no reescriure `resum.csv`.

## Què et diu

- **en joc** — quant val cada item en punts de la nota final (sobre 10)
- **obtinguts** — quants d'aquests punts ja tens a la butxaca
- **avaluats** — quants punts ja s'han jugat (tinguis la nota que tinguis)
- **mitjana** — `obtinguts / avaluats`, és a dir la nota que portes del que ja
  s'ha avaluat, que no és el mateix que la nota final projectada
- **mínim / màxim** — entre quins valors es pot moure encara la nota final
- **què et cal** — quina mitjana necessites a tot el que queda per aprovar,
  treure notable o excel·lent

## La fórmula

```
Nota final = 50% NTP + 50% NLAB
NTP  = 20% C1 + 20% C2 + 20% NQ + 20% P1 + 20% P2
NLAB = 30% IntroLAB + 70% Project
```

En punts de la nota final: C1, C2, NQ, P1 i P2 valen **1 punt** cadascun;
IntroLAB val **1,5 punts** i el Project val **3,5 punts**. El projecte sol és
més d'un terç de l'assignatura.

### Les quizzes (NQ)

`N` és el nombre de quizzes anunciat el primer dia de classe (entre 5 i 7).

- Si n'has lliurat `N-2` o més: **NQ = mitjana de les `N-2` millors**.
- Si n'has lliurat `N-3` o menys: **NQ = suma de totes / `N-2`** (o sigui, les
  places buides compten com un zero).

Les dues regles són en realitat la mateixa: la suma de les `min(lliurades, N-2)`
millors, dividida sempre per `N-2`. El script ho fa així.

**Per defecte `N = 6`**, amb sis files `QUIZ` al CSV. Si a classe anuncien un
altre número, canvia el valor de la fila `CONFIG,N_QUIZZES` i afegeix o treu
files `QUIZ` perquè n'hi hagi tantes com `N` (el script t'avisa si no quadra).

A la taula, la columna `nota` de la fila `NQ` mostra la **mitjana de les
quizzes que compten fins ara**; el text del costat et diu quant valdria NQ si
no en lliuressis cap més, que mentre tinguis places buides és més baix.

## Feina en grup

P1, P2 i el Project són en grup, però la nota és **personalitzada**: surt de la
qualitat global de l'entrega, de com valora el professor la teva contribució i
de com la valoren els companys de grup. Al CSV hi poses directament la teva
nota personalitzada, no la del grup.
