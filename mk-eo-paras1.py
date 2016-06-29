#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-paras1.py
# 2016-06-29 1.11
# (C) Mikhail (myke) Kolodin
# test toolbase for SSYP-2016 eo
# by finding neibars' words in given text

import collections
import pickle
import re
#~ from pprint import pprint as pp

from mk_eo_tools import *

txt1 = "En la mondon venis nova sento."
txt2 = "Tri vortoj plaĉis al mi en la mondo."

#~ finame = "ojstro.txt"
#~ finame = "stelship.txt"
#~ finame = "cutty.txt"
#~ finame = "normalalingvo.txt"
finame = "espero.txt"

finame = finame if finame else "none" # :)

# save to file:
datapickle = finame + ".pickle"

#txt3 = open(finame).read().split(".")
txt3 = open(finame).read()
txt3 = re.split (r'([^.!?]]+)', txt3)

# improve splitter:  . ! ? ...
# but not mr. inc. etc etc
# maybe better external splitter to be used

#~ txts = [txt1, txt2]
txts = txt3

pred = collections.defaultdict(int)
post = collections.defaultdict(int)

def test1(frases):
    """ test given phrase """
    #~ print (frases)

    for ip, txt in enumerate(frases):
        print ("\ndonata %4d:  %s" % (ip, txt))

        if txt == "":
            print ("nule!")
            continue

        s = eo_split(txt)
        st = [base_form(x) for x in s if x != ""]
        print ("rezulta    : ", st)
        enparu (st)

    return st

def enparu (st):
    """ make pairs of all words in given text,
    with exception of stop-words etc"""

    print ("enparu:")

    lenst = len(st)

    for i, w1 in enumerate(st):
        if w1 in EO_ART or w1 in EO_NUMS or w1 in EO_UNIO or  w1 in EO_PREP:
            continue

        need = True
        j = i+1
        while need:
            if j>=lenst:
                break
            w2 = st[j]
            if w2 in EO_STOP:
                j += 1
                continue

            print ("paro: ", i, w1, j, w2)
            act (w1, w2)
            need = False

def act (w1, w2):
    """ account pair (w1, w2)"""

    pred [(w1, w2)] += 1
    post [(w2, w1)] += 1

def showres ():
    """ show results of test """

    print ("\npred = ", pred)
    print ("\npost = ", post)

    #~ oftens = sorted (list(pred), key = lambda l: l[1]) [:10]
    loft = [(x[0], x[1]) for x in pred.items()]
    loft.sort (key = lambda l: l[1], reverse = True)
    print ("\noftens:", loft[:20])
    #~ print ("oftens:", oftens)


def savepickles():
    """ save data outeren """

    try:
        mass = [(x[0][0], x[0][1], x[1]) for x in pred.items() ]
        mass.sort (key = lambda l: l[2], reverse = True)
    except:
        pass

    print ("\nmass = ", mass[:40], "...")

    try:
        with open(datapickle, 'wb') as fp:
            pickle.dump (mass, fp, pickle.HIGHEST_PROTOCOL)
    except:
        print (mass)

def main(args):
    """ main dispatcher """

    #~ print ("numeraloj: ", EO_NUMS)
    #~ print ("pronomoj: ", EO_PRONOMOJ)

    test1 (txts)
    showres()
    savepickles()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
