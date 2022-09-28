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


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = 0
        z1.next = 0
        z2.next = 0
        z3.next = 0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    @always_comb
    def comb():
        resultado.next = 0

    return instances()
