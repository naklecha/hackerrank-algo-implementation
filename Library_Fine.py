#!/bin/python

def calcFine(Ddiff, Mdiff, Ydiff):
    fine = 0
    if   Ydiff > 0: fine += 10000
    elif Ydiff < 0: return 0
    elif Mdiff > 0: fine += 500 * Mdiff
    elif Mdiff < 0: return 0
    elif Ddiff > 0: fine += 15 * Ddiff
    else: return 0
    return fine

Da, Ma, Ya = map(int, raw_input().split())
De, Me, Ye = map(int, raw_input().split())
print calcFine(Da - De, Ma - Me, Ya - Ye)
