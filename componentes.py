#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from ula_aux import *


def exe1(a, b, c, q):

    saida1 = Signal(bool(0))
    saida2 = Signal(bool(0))
    saida3 = Signal(bool(0))
    saida4 = Signal(bool(0))
    
    @always_comb
    def comb():

        saida1 = a and b
        saida2 = b or c
        saida3 = b and c
        saida4 = saida2 and saida3

        q.next = saida1 or saida4

    return instances()


def exe2(p, q, r, s):

    saida_s = Signal(bool(0))
    
    @always_comb
    def comb():
        saida_s = not p or (q and r)

        s.next = saida_s

    return instances()

'''
def exe2(p, q, r, s):

    condicao1 = Signal(bool(0))
    condicao2 = Signal(bool(0))
    
    @always_comb
    def comb():
        condicao1 = not p
        condicao2 = q and r

        s.next = condicao1 or condicao2

    return instances()
'''


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = ((not x1) and x0 and (not y1) and y0) or ((not x1) and x0 and y1 and y0) or (x1 and x0 and (not y1) and y0) or (x1 and x0 and y1 and y0)
        z1.next = ((not x1) and x0 and y1 and (not y0)) or ((not x1) and x0 and y1 and y0) or (x1 and (not x0) and (not y1) and y0) or (x1 and (not x0) and y1 and y0)
        z2.next = (x1 and (not x0) and y1 and (not y0)) or (x1 and (not x0) and y1 and y0) or (x1 and x0 and y1 and (not y0))
        z3.next = x1 and x0 and y1 and y0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    @always_comb
    def comb():
        resultado.next = 0

    return instances()
