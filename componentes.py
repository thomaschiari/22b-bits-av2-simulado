#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from ula_aux import *


def exe1(a, b, c, q):
    @always_comb
    def comb():
        q.next = a and b or ((b or c) and (b and c))

    return instances()


def exe2(p, q, r, s):
    @always_comb
    def comb():
        s.next = (not p) or (q and r)

    return instances()


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z3.next = x1 and x0 and y1 and y0
        z2.next = (x1 and (not x0) and y1) or (x1 and x0 and y1 and (not y0))
        z1.next = (
            ((not x1) and x0 and y1)
            or (x1 and (not y1) and y0)
            or (x1 and (not x0) and y0)
            or (x0 and y1 and (not y0))
        )
        z0.next = x0 and y0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    aneg, bneg = [Signal(modbv(0)[32:]) for i in range(2)]
    iaout, ibout = [Signal(modbv(0)[32:]) for i in range(2)]
    addout, orout, andout = [Signal(modbv(0)[32:]) for i in range(3)]
    muxout = Signal(modbv(0)[32:])

    comp_inverte_a = mux2way(iaout, a, aneg, inverte_a)
    comp_inverte_b = mux2way(ibout, b, bneg, inverte_b)
    comp_add = adder(addout, c_out, iaout, ibout, c_in)
    comp_mux = mux4way(muxout, andout, orout, addout, 0, selecao)

    @always_comb
    def comb():
        resultado.next = muxout
        aneg.next = not a
        bneg.next = not b

        andout.next = iaout & ibout
        orout.next = iaout | ibout

        zero_ = False
        for i in range(len(muxout)):
            zero_ = zero_ or muxout[i]
        zero.next = not zero_

    return instances()
