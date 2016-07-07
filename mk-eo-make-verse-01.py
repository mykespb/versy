#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-make-verse-01.py
# 2016-07-07 0.1
# (C) Mikhail (myke) Kolodin
# make simple texts
# 4 lines * 4 sentences * 2 words (a, n) * horej

from pprint import pprint as pp
import random

infile = "eo-vortaro-2-list3s.txt"
LINES = 4
STROPHS = 4
PIC = "+-"
PROVOJ = 1000

gm = []

def getdata():
    """ read input file, store al in list"""
    global gm
    with open (infile) as inf:
        for line in inf:
            wo, pm, pd, sill, pic, stress = line.strip().split()
            try:
                sill = int(sill)
            except:
                sill = 0
            gm += [[wo, pm, sill, pic]]
    pp (gm[:30])

def makeverse():
    global gm

    w1 = [w[0] for w in gm if w[1] == "A" and w[3] == PIC]
    w2 = [w[0] for w in gm if w[1] == "O" and w[3] == PIC]

    #~ pp (w1[:20])
    #~ pp (w2[:20])

    for provo in range(PROVOJ):
        vers = []
        for ln in range(LINES):
            s = ""
            for sph in range(STROPHS):
                s += random.choice(w1).capitalize() + " " + random.choice(w2) + ". "
            vers += [s]
        if  vers[0][-4:] == vers[2][-4:] and vers[1][-4:] == vers[3][-4:]:
            for p in vers:
                print (p)
            break
    else:
        print ("Mi fiaskis...")


def main(args):
    getdata()
    makeverse()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

Prava ĉeso. Pluta filmo. Liga tempo. Stila ĥoro.
Kara vintro. Sesa treto. Fota masko. Pruva plano.
Sorta loĝo. Nombra urbo. Larda noto. Naŭa ĉambro.
Membra ŝanco. Pekla dego. Prata monto. Kia gajno.

