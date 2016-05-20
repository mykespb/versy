#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-vortaro2-getwords.py
# 2016-05-20 1.1
# get list of eo words from text vortaro file eo-vortaro-2.txt
# and write it to simple text file mk-eo-vortaro-2-list.txt
#   word part-of-speech
# where parts are: noun verb adjective pronoun numeral preposition adverd conjunction particle

from collections import Counter

infile  = "eo-vortaro-2.txt"
outfile = "eo-vortaro-2-list.txt"

ALFA_EO_UP = "ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ"
ALFA_EO_DN = "Abcĉdefgĝhĥijĵklmnoprsŝtuŭvz"

ALFA_EN_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_EN_DN = "abcdefghijklmnopqrstuvwxyz"

EO_VOVELOJ = "aeiou"

EO_NUMS  = "unu du tri kvar kvin ses sep ok naŭ dek cent mil miliono miliardo".split()

stat = Counter()

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

    with open (infile, "r", encoding="utf-8") as inf,\
         open (outfile, "w", encoding="utf-8") as outf:
        print ("open OK")

        for line in inf:
            l = line.strip()
            if len(l) <2 : continue
            if l.startswith("A B"): continue

            w, desc = l.split(" ", maxsplit=1)

            part = eo_part(w)
            cv   = count_syll(w)
            ep   = eo_picto (cv)

            print (w, part, cv, ep, file=outf)
            print (part[0], end="")

        print ("\nall done.")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
