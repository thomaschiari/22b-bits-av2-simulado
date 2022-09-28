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

    a_inv, b_inv, a_out, b_out= Signal(modbv(0)[32:])
    mux_a = mux2way(a_out, a, a_inv, inverte_a)
    mux_b = mux2way(b_out, b, b_inv, inverte_b)
    sum_out = Signal(modbv(0)[32:])
    adder1 = adder(sum_out, c_out, a_out, b_out, c_in)
    and_out, or_out, resultado_out, slt = Signal(modbv(0)[32:])
    # mux4 = mux4way(resultado_out, and_out, or_out, sum_out, slt, selecao)
    zero_out = Signal(bool(0))

    @always_comb
    def comb():

        a_inv = ~a
        b_inv = ~b

        and_out = a_out & b_out
        or_out = a_out | b_out

        if selecao == 0:
            resultado_out = and_out
        elif selecao == 1:
            resultado_out = or_out
        elif selecao == 2:
            resultado_out = sum_out
        else:
            resultado_out = slt

        for i in range(32-1):
            zero_out = resultado_out[i] or resultado_out[i+1]
        
        zero.next = not zero_out

        resultado.next = resultado_out

    return instances()
