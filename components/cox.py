#!/usr/bin/env python
# Contatore Oxford Engine (COX-E)
# Copyright (C) 2021-2022
# BIRBONE PRODUCTIONS
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.

import csv
from components.const import *


def count(text):
    punctuation = ["?", ".", ",", "\"", "\'",
                     "!", ":", ";", "-", "*", "(", ")", "!", "/"]

    def CSVList():
        """Useful method to retrieve the CSV list"""
        file = open(TERMS_LIST)
        csvreader = csv.reader(file, delimiter="\r")
        rows = []
        for row in csvreader:
            rows.append(row)
        return rows
    print("Contatore Oxford Engine (COX-e) Developed by Birbone")
    print("Analisi...")
    textsplit = text.split(' ')
    badword_list = CSVList()
    partialCounter = 0
    pCounter = 0
    for w in textsplit:
        for p in punctuation:
            if (p in w):
                w = w.replace(p, "")
        for moccoli in badword_list:
            if (w.lower() == moccoli[0]):
                partialCounter += 1
                if (w.lower() == "porco" or w.lower() == "porca"):
                    pCounter += 1

    return f"Ci sono {str(partialCounter)} moccoli. Con {str(pCounter)} porchi."


def DeleteSpecialCharacter(text):
    """Delete unwanted characters"""
    punctuation = ["?", ".", ",", "\"", "\'",
                     "!", ":", ";", "-", "*", "(", ")", "!", "/"]
    for p in punctuation:
        if (p in text):
            text = text.replace(p, "")
    return


def RIDEPAS(w1, w2, m):
    """Useful function to recognize a couple of words in succession """
    m = DeleteSpecialCharacter(m)
    textsplit = m.split(' ')
    w_trigger = [w1, w2]
    pp = 0
    t = False
    for w in textsplit:
        # Rilevatore w staccata
        if (w.lower() == w_trigger[0]):
            t = True
        if (w.lower() == w_trigger[1]) and w_trigger[0] == textsplit[pp-1] and t == True:
            return True

        pp += 1
    return False


def AdvancedRIDEPAS(w1, w2, m, pdmm):
    """Useful function to recognize a couple of words in succession with some words in the middle"""
    m = DeleteSpecialCharacter(m)
    textsplit = m.split(' ')
    w_trigger = [w1, w2]
    pp = 0
    for w in textsplit:
        if (w.lower() == w_trigger[0]):
            n = 0
            while n <= pdmm:
                if (textsplit[pp+n] == w_trigger[1]):
                    return True
                n += 1
        pp += 1
    return False
