#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculadora de la nota d'ASW (FIB - UPC).

Llegeix `notes.csv`, hi aplica la formula d'avaluacio de l'assignatura i diu:

  - que et jugues a cada item (quants punts de la nota final val)
  - quants punts portes acumulats
  - quina mitjana portes sobre el que ja s'ha avaluat
  - entre quina nota minima i maxima et pots moure encara
  - quina mitjana et cal a tot el que queda per arribar a un objectiu

Formula (tal com la publica l'assignatura):

  Nota final = 50% NTP + 50% NLAB
  NTP  = 20% C1 + 20% C2 + 20% NQ + 20% P1 + 20% P2
  NLAB = 30% IntroLAB + 70% Project

  NQ = mitjana de les N-2 millors quizzes, on N es el nombre de quizzes
       anunciat el primer dia (entre 5 i 7). Si nomes se n'han lliurat N-3 o
       menys, NQ = suma de totes les lliurades / (N-2). Les dues regles son
       la mateixa: suma de les min(lliurades, N-2) millors, dividit per N-2.

Us:
    python3 notes/nota.py                # informe per pantalla + resum.csv
    python3 notes/nota.py --csv altre.csv
    python3 notes/nota.py --sense-resum  # no escriu resum.csv
"""

import argparse
import csv
import sys
from pathlib import Path

NOTA_MAXIMA = 10.0
OBJECTIUS = [("aprovat", 5.0), ("notable", 7.0), ("excel-lent", 9.0)]


# ---------------------------------------------------------------- lectura ---

def num(text):
    """Converteix una cel-la en float. Accepta coma decimal. Buit -> None."""
    text = (text or "").strip().replace(",", ".")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def llegeix(ruta):
    config, finals, blocs, quizzes = {}, {}, {}, []
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            bloc = (fila.get("bloc") or "").strip().upper()
            item = (fila.get("item") or "").strip()
            if not bloc or not item or bloc.startswith("#"):
                continue
            registre = {
                "item": item,
                "desc": (fila.get("descripcio") or "").strip(),
                "pes": num(fila.get("pes_bloc_pct")),
                "nota": num(fila.get("nota")),
            }
            if bloc == "CONFIG":
                config[item.upper()] = registre["nota"]
            elif bloc == "FINAL":
                finals[item] = registre
            elif bloc == "QUIZ":
                quizzes.append(registre)
            else:
                blocs.setdefault(bloc, []).append(registre)
    return config, finals, blocs, quizzes


# ------------------------------------------------------------- calculs NQ ---

def calcula_nq(quizzes, n_quizzes):
    """Retorna (nota_nq_actual, places_omplertes, divisor, notes_que_compten)."""
    divisor = max(1, int(round(n_quizzes)) - 2)
    fetes = sorted([q["nota"] for q in quizzes if q["nota"] is not None], reverse=True)
    places = min(len(fetes), divisor)
    compten = fetes[:places]
    return (sum(compten) / divisor if divisor else 0.0), places, divisor, compten


# ---------------------------------------------------------------- calculs ---

def avalua(config, finals, blocs, quizzes):
    """Calcula, per a cada item, els punts en joc / obtinguts / avaluats."""
    n_quizzes = config.get("N_QUIZZES") or 6
    nq, places, divisor, compten = calcula_nq(quizzes, n_quizzes)

    items = []
    for nom_bloc, registre_bloc in finals.items():
        pes_bloc = (registre_bloc["pes"] or 0.0) / 100.0
        for it in blocs.get(nom_bloc.upper(), []):
            en_joc = (it["pes"] or 0.0) / 100.0 * pes_bloc * NOTA_MAXIMA
            if it["item"].upper() == "NQ":
                # La nota mostrada es la mitjana de les quizzes que compten fins
                # ara; els punts, en canvi, ja porten el divisor N-2 aplicat.
                nota = (sum(compten) / places) if places else None
                obtinguts = nq / NOTA_MAXIMA * en_joc
                avaluats = (places / divisor) * en_joc if divisor else 0.0
                detall = "{}/{} places; NQ={:.2f} si no en fas cap mes".format(
                    places, divisor, nq)
            elif it["nota"] is not None:
                nota = it["nota"]
                obtinguts = nota / NOTA_MAXIMA * en_joc
                avaluats = en_joc
                detall = ""
            else:
                nota, obtinguts, avaluats, detall = None, 0.0, 0.0, ""
            items.append({
                "bloc": nom_bloc,
                "item": it["item"],
                "desc": it["desc"],
                "nota": nota,
                "en_joc": en_joc,
                "obtinguts": obtinguts,
                "avaluats": avaluats,
                "detall": detall,
            })
    return items, {"n": int(round(n_quizzes)), "nq": nq, "places": places,
                   "divisor": divisor, "compten": compten}


def subtotal(items):
    en_joc = sum(i["en_joc"] for i in items)
    obtinguts = sum(i["obtinguts"] for i in items)
    avaluats = sum(i["avaluats"] for i in items)
    return en_joc, obtinguts, avaluats


# ----------------------------------------------------------------- sortida ---

def barra(fraccio, ample=22):
    plens = max(0, min(ample, int(round(fraccio * ample))))
    return "#" * plens + "." * (ample - plens)


def fmt(valor, decimals=2):
    return "-" if valor is None else "{:.{}f}".format(valor, decimals)


def informe(items, info, finals):
    linies = []
    w = 76
    linies.append("=" * w)
    linies.append("  ASW - ESTAT DE LA NOTA")
    linies.append("=" * w)

    for nom_bloc, registre in finals.items():
        del_bloc = [i for i in items if i["bloc"] == nom_bloc]
        if not del_bloc:
            continue
        en_joc, obtinguts, avaluats = subtotal(del_bloc)
        linies.append("")
        linies.append("{} - {} ({:.0f}% de la nota final = {:.2f} punts)".format(
            nom_bloc, registre["desc"], registre["pes"] or 0.0, en_joc))
        linies.append("-" * w)
        linies.append("  {:<10} {:>6} {:>10} {:>10} {:>10}  {}".format(
            "item", "nota", "en joc", "obtinguts", "avaluats", ""))
        for i in del_bloc:
            linies.append("  {:<10} {:>6} {:>10} {:>10} {:>10}  {}".format(
                i["item"], fmt(i["nota"]), fmt(i["en_joc"]),
                fmt(i["obtinguts"]), fmt(i["avaluats"]), i["detall"]))
        mitjana = obtinguts / avaluats * NOTA_MAXIMA if avaluats else None
        linies.append("  {:<10} {:>6} {:>10} {:>10} {:>10}  mitjana del bloc: {}".format(
            "TOTAL", "", fmt(en_joc), fmt(obtinguts), fmt(avaluats), fmt(mitjana)))

    # Detall de les quizzes
    linies.append("")
    linies.append("QUIZZES")
    linies.append("-" * w)
    linies.append("  N anunciat = {}  ->  compten les {} millors, dividit entre {}".format(
        info["n"], info["divisor"], info["divisor"]))
    if info["places"]:
        linies.append("  Notes que compten ara mateix: {}".format(
            ", ".join(fmt(x, 1) for x in info["compten"])))
        linies.append("  Mitjana de les que compten: {}".format(
            fmt(sum(info["compten"]) / info["places"])))
        linies.append("  NQ = {} si no en lliures cap mes ({} de {} places omplertes)".format(
            fmt(info["nq"]), info["places"], info["divisor"]))
    else:
        linies.append("  Encara no hi ha cap quiz amb nota.")

    # Resum global
    en_joc, obtinguts, avaluats = subtotal(items)
    pendents = en_joc - avaluats
    mitjana = obtinguts / avaluats * NOTA_MAXIMA if avaluats else None
    linies.append("")
    linies.append("=" * w)
    linies.append("  RESUM")
    linies.append("=" * w)
    linies.append("  Curs avaluat        [{}]  {:.0f}%  ({:.2f} de {:.2f} punts)".format(
        barra(avaluats / en_joc if en_joc else 0), (avaluats / en_joc * 100) if en_joc else 0,
        avaluats, en_joc))
    linies.append("  Punts acumulats     [{}]  {:.2f} punts sobre 10".format(
        barra(obtinguts / en_joc if en_joc else 0), obtinguts))
    linies.append("  Encara en joc       {:.2f} punts".format(pendents))
    linies.append("")
    linies.append("  Mitjana del que ja s'ha avaluat : {}".format(fmt(mitjana)))
    linies.append("  Nota final si ho suspens tot    : {:.2f}".format(obtinguts))
    linies.append("  Nota final si ho claves tot     : {:.2f}".format(obtinguts + pendents))

    if pendents > 0.001:
        linies.append("")
        linies.append("  Per arribar a...   et cal de mitjana a tot el que queda")
        for etiqueta, objectiu in OBJECTIUS:
            calen = (objectiu - obtinguts) / pendents * NOTA_MAXIMA
            if calen <= 0:
                estat = "ja el tens assegurat"
            elif calen > NOTA_MAXIMA:
                estat = "inassolible (caldria un {:.2f})".format(calen)
            else:
                estat = "{:.2f}".format(calen)
            linies.append("  {:<10} ({:.1f})   {}".format(etiqueta, objectiu, estat))
    linies.append("")
    return "\n".join(linies)


def escriu_resum(items, finals, ruta):
    en_joc_total, obtinguts_total, avaluats_total = subtotal(items)
    files = []
    for i in items:
        files.append({
            "bloc": i["bloc"], "item": i["item"], "descripcio": i["desc"],
            "nota": fmt(i["nota"]),
            "punts_en_joc": fmt(i["en_joc"]),
            "punts_obtinguts": fmt(i["obtinguts"]),
            "punts_avaluats": fmt(i["avaluats"]),
            "punts_pendents": fmt(i["en_joc"] - i["avaluats"]),
            "estat": "avaluat" if i["avaluats"] >= i["en_joc"] - 0.001 else
                     ("parcial" if i["avaluats"] > 0 else "pendent"),
        })
    for nom_bloc, registre in finals.items():
        del_bloc = [i for i in items if i["bloc"] == nom_bloc]
        if not del_bloc:
            continue
        b_joc, b_obt, b_aval = subtotal(del_bloc)
        files.append({
            "bloc": "RESUM", "item": nom_bloc,
            "descripcio": "subtotal " + registre["desc"],
            "nota": fmt(b_obt / b_aval * NOTA_MAXIMA if b_aval else None),
            "punts_en_joc": fmt(b_joc), "punts_obtinguts": fmt(b_obt),
            "punts_avaluats": fmt(b_aval), "punts_pendents": fmt(b_joc - b_aval),
            "estat": "",
        })
    files.append({
        "bloc": "RESUM", "item": "NOTA FINAL", "descripcio": "50% NTP + 50% NLAB",
        "nota": fmt(obtinguts_total / avaluats_total * NOTA_MAXIMA if avaluats_total else None),
        "punts_en_joc": fmt(en_joc_total), "punts_obtinguts": fmt(obtinguts_total),
        "punts_avaluats": fmt(avaluats_total),
        "punts_pendents": fmt(en_joc_total - avaluats_total),
        "estat": "min {} / max {}".format(
            fmt(obtinguts_total), fmt(obtinguts_total + en_joc_total - avaluats_total)),
    })
    camps = ["bloc", "item", "descripcio", "nota", "punts_en_joc",
             "punts_obtinguts", "punts_avaluats", "punts_pendents", "estat"]
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escriptor = csv.DictWriter(f, fieldnames=camps)
        escriptor.writeheader()
        escriptor.writerows(files)


# --------------------------------------------------------------------- main --

def main():
    parser = argparse.ArgumentParser(description="Calculadora de la nota d'ASW")
    parser.add_argument("--csv", default=str(Path(__file__).with_name("notes.csv")),
                        help="fitxer de notes (per defecte notes/notes.csv)")
    parser.add_argument("--sense-resum", action="store_true",
                        help="no escriguis resum.csv")
    args = parser.parse_args()

    ruta = Path(args.csv)
    if not ruta.exists():
        sys.exit("No trobo el fitxer {}".format(ruta))

    config, finals, blocs, quizzes = llegeix(ruta)
    if not finals:
        sys.exit("El CSV no te cap fila amb bloc=FINAL; revisa'l.")

    items, info = avalua(config, finals, blocs, quizzes)
    print(informe(items, info, finals))

    if len(quizzes) != info["n"]:
        print("  Avis: el CSV te {} files QUIZ pero N_QUIZZES val {}.".format(
            len(quizzes), info["n"]))
        print("        Afegeix o treu files QUIZ, o ajusta N_QUIZZES.\n")

    if not args.sense_resum:
        sortida = ruta.with_name("resum.csv")
        escriu_resum(items, finals, sortida)
        print("  Resum escrit a {}\n".format(sortida))


if __name__ == "__main__":
    main()
