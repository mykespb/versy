#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-vortaro2-getwords3.py
# 2016-05-22 2.3.1
# using eo-vortaro-2-list1.txt (sic!) make eo-vortaro-2-list13txt (sic!)
# with maiimal number of words' variants (only main forms)
# with specificatioons: word part-of-speech,variant
# will be launched with mk-eo-001.sh

from collections import Counter

infile  = "eo-vortaro-2-list1.txt"
outfile = "eo-vortaro-2-list3.txt"

ALFA_EO_UP = "ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ"
ALFA_EO_DN = "abcĉdefgĝhĥijĵklmnoprsŝtuŭvz"

ALFA_EN_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_EN_DN = "abcdefghijklmnopqrstuvwxyz"

EO_VOVELOJ = "aeiou"

EO_NUMS  = "unu du tri kvar kvin ses sep ok naŭ dek cent mil miliono miliardo".split()

part_stat = Counter()       # counter for parts of speech

avortoj = set()                # list of a-vortoj
ovortoj = set()                # list of o-vortoj
evortoj = set()                # list of e-vortoj

total = 0                   # toital number of words

fout = 0

def eo_part (w):
    """ determine part of speech for eo word"""

    if w in EO_NUMS:
        return "numeralo"
    if w.endswith("i"):
        return "verbo"
    if w.endswith("o"):
        return "o-vorto"
    if w.endswith("a"):
        return "a-vorto"
    if w.endswith("e") or w.endswith("aŭ") or w.endswith("eŭ") :
        return "e-vorto"
    return "ktp"


def count_syll (w):
    """ count syllables in eo word"""
    cv = 0
    for c in w:
        if c in EO_VOVELOJ:
            cv += 1
    return cv


def eo_picto (cv):
    """ draw picture of word"""
    if cv == 0:
        return "."
    if cv == 1:
        return "+"
    ep = "-" * (cv-2) + "+-"
    return ep


def main(args):
    """ main task """
    global part_stat, total, ovortoj, avortoj, evortoj, fout

    with open (infile, "r", encoding="utf-8") as inf:

        fout = open (outfile, "w", encoding="utf-8")
        print ("open OK")
        print ("#vorto parto spec sillen pikto deriva", file=fout)

        for line in inf:
            l = line.strip()
            if len(l) <2 : continue

            vorto, parto, silla, pikto = l.split()
            root, fin = vorto[:-1], vorto[-1:]
            print (parto[0], end="")

            # ------------------------------------------o-vortoj
            if parto == "o-vorto":
                part_stat["O"] += 1
                tipa = "O,cn,ns"
                ovortoj |= {vorto}
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

                avorto = root + "a"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,do"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                ovorto = root + "eto"
                if ovorto not in ovortoj:
                    part_stat["O"] += 1
                    tipa = "O,cn,ns,do"
                    ovortoj |= {ovorto}
                    derive = 2
                    silla = count_syll (ovorto)
                    pikto = eo_picto (silla)
                    print (ovorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                ovorto = root + "ego"
                if ovorto not in ovortoj:
                    part_stat["O"] += 1
                    tipa = "O,cn,ns,do"
                    ovortoj |= {ovorto}
                    derive = 2
                    silla = count_syll (ovorto)
                    pikto = eo_picto (silla)
                    print (ovorto, tipa[0], tipa, silla, pikto, 2, file=fout)

            # ------------------------------------------a-vortoj
            elif parto == "a-vorto":
                part_stat["A"] += 1
                tipa = "A,cn,ns,pa"
                avortoj |= {vorto}
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

            # ------------------------------------------e-vortoj
            elif parto == "e-vorto":
                part_stat["E"] += 1
                tipa = "E,pe" if fin == "ŭ" else "E,pd"
                evortoj |= {vorto}
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

            # ------------------------------------------verboj
            elif parto == "verbo":
                part_stat["V"] += 1
                tipa = "V,fi"
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

                ovorto = root + "o"
                if ovorto not in ovortoj:
                    part_stat["O"] += 1
                    tipa = "O,cn,ns,dv"
                    ovortoj |= {ovorto}
                    derive = 2
                    silla = count_syll (ovorto)
                    pikto = eo_picto (silla)
                    print (ovorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "a"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "ita"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "inta"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "ata"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "anta"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "ota"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "onta"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "uta"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                avorto = root + "unta"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pp,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "e"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "ite"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "inte"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "ate"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "ante"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "ote"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "onte"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "ute"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

                evorto = root + "unte"
                if evorto not in evortoj:
                    part_stat["E"] += 1
                    tipa = "E,pp,dv"
                    evortoj |= {evorto}
                    derive = 2
                    silla = count_syll (evorto)
                    pikto = eo_picto (silla)
                    print (evorto, tipa[0], tipa, silla, pikto, 2, file=fout)

            # ------------------------------------------numeraloj
            elif parto == "numeralo":
                part_stat["N"] += 1
                tipa = "N,cn,pc"
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

                avorto = vorto + "a"
                if avorto not in avortoj:
                    part_stat["A"] += 1
                    tipa = "A,cn,ns,pn,dv"
                    avortoj |= {avorto}
                    derive = 2
                    silla = count_syll (avorto)
                    pikto = eo_picto (silla)
                    print (avorto, tipa[0], tipa, silla, pikto, 2, file=fout)

            # ------------------------------------------etc
            elif parto == "etc":
                part_stat["K"] += 1
                derive = 1
                print (vorto, tipa[0], tipa, silla, pikto, 1, file=fout)

            # ------------------------------------------else
            else:
                pass

        print ("\nresults:")
        for k, v in part_stat.items():
            print ("{:10s} - {:5d}" .format(k, v))

    fout.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
