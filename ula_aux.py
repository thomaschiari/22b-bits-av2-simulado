#!/usr/bin/env python3

from myhdl import *


@block
def adder(q, c_out, a, b, c_in):
    @always_comb
    def comb():
        sum = a + b + c_in
        q.next = sum
        if sum > a.max - 1:
            c_out.next = 1
        else:
            c_out.next = 0

    return comb


@block
def mux2way(q, a, b, sel):
    @always_comb
    def comb():
        if sel:
            q.next = b
        else:
            q.next = a

    return comb


@block
def mux4way(q, a, b, c, d, sel):
    @always_comb
    def comb():
        if sel == 0:
            q.next = a
        elif sel == 1:
            q.next = b
        elif sel == 2:
            q.next = c
        else:
            q.next = d

    return comb
