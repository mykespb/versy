#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-tools.py
# 2016-06-23 1.1
# toolbase for SSYP-2016 eo

#~ import re

ALFA_EO_UP = "ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ"
ALFA_EO_DN = "abcĉdefgĝhĥijĵklmnoprsŝtuŭvz"
ALFA_EO    = ALFA_EO_UP + ALFA_EO_DN

ALFA_EN_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_EN_DN = "abcdefghijklmnopqrstuvwxyz"
ALFA_EN    = ALFA_EN_UP + ALFA_EN_DN

EO_VOVELOJ = "aeiou"

EO_NUMS  = "unu du tri kvar kvin ses sep ok naŭ dek cent mil miliono miliardo".split()

EO_PRONOMOJ_S = "mi ci li ŝi ŝli ĝi oni".split()
EO_PRONOMOJ_P = "ni vi ili".split()
EO_PRONOMOJ = EO_PRONOMOJ_P + EO_PRONOMOJ_S

EO_ART = ["la"]

EO_VERBFIN = "i is as os us u".split()

EO_PREP = "al apud ĉe ĉirkaŭ da de dum en el ekster for inter krom kun per por post preter pri sen sub super sur tra trans".split()

EO_UNIO = "kaj se sed aŭ ju nek des".split()

EO_PREFIX = "eks dis mal mis ek re fi bo ge pra antaŭ kontraŭ".split()

EO_STOP = EO_PREP + EO_UNIO + EO_PREFIX + EO_ART

def base_form (w):
    """ finds base form for given word """

    if w in EO_NUMS or w in EO_PRONOMOJ or w in EO_STOP:
        return w

    if w.endswith("on") or w.endswith("ojn") or w.endswith("an") or w.endswith("ajn"):
        w = w[:-1]

    if w.endswith("j"):
        w = w[:-1]

    if w.endswith("'"):
        w = w[:-1] + "o"

    if w.endswith("o") or w.endswith("a"):
        return w

    for e in EO_VERBFIN:
        if w.endswith(e):
            w = w[:-len(e)] + "i"
    return w

    return w

def eo_split(f):
    """ split phrase en eo into words"""

    f1 = f.split()
    f2 = [eo_strim(x) for x in f1]

    return f2

def eo_strim(w):
    """ delete all non-letter chars from word"""

    s = ""
    for c in w or c in "'-":
        if c in ALFA_EO:
            s += c

    return s

