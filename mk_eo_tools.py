#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-tools.py
# 2016-06-23 0.1
# toolbase for SSYP-2016 eo

ALFA_EO_UP = "ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ"
ALFA_EO_DN = "abcĉdefgĝhĥijĵklmnoprsŝtuŭvz"

ALFA_EN_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_EN_DN = "abcdefghijklmnopqrstuvwxyz"

EO_VOVELOJ = "aeiou"

EO_NUMS  = "unu du tri kvar kvin ses sep ok naŭ dek cent mil miliono miliardo".split()

EO_PRONOMOJ_S = "mi ci li ŝi ŝhi ĝi onu".split()
EO_PRONOMOJ_P = "ni vi ili".split()
EO_PRONOMOJ = EO_PRONOMOJ_P + EO_PRONOMOJ_S

def base_form (w):
    """ finds base form for given word """
    return w
