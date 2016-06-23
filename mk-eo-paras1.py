#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-paras1.py
# 2016-06-24 1.4
# test toolbase for SSYP-2016 eo
# by finding neibars' words in given text

from mk_eo_tools import *

txt1 = "En la mondon venis nova sento."
txt2 = "Tri vortoj plaĉis al mi."

#~ finame = "normalalingvo.txt"
finame = "espero.txt"

txt3 = open(finame).read().split(".")

txts = [txt1, txt2]
#~ txts = txt3

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
            need = False


def main(args):
    """ main dispatcher """

    #~ print ("numeraloj: ", EO_NUMS)
    #~ print ("pronomoj: ", EO_PRONOMOJ)

    test1 (txts)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
