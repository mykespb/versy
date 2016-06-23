#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-eo-paras1.py
# 2016-06-23 0.1
# test toolbase for SSYP-2016 eo
# by finding neibars' words in given text

from mk_eo_tools import *

txt1 = "en la mondon venis nova sento"
txt2 = "tri sonoj ŝxajnis al mi"

txts = [txt1, txt2]

def test1(f):
    """ test given phrase """
    for txt in f:
        print ("\ndonata:  ", txt)
        s = eo_split(txt)
        st = [base_form(x) for x in s]
        print ("rezulta: ", st)

def main(args):
    print ("numeraloj: ", EO_NUMS)
    print ("pronomoj: ", EO_PRONOMOJ)
    test1(txts)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
