# This file was *autogenerated* from the file L04-plot01.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)#!/usr/bin/env

p = plot(_sage_const_1 -_sage_const_2 *x,x,_sage_const_0 ,_sage_const_1 ,legend_label="$u_1(r_1,\sigma_2)$", color='red')
p += plot(_sage_const_2 *x-_sage_const_1 ,x,_sage_const_0 ,_sage_const_1 ,legend_label="$u_1(r_2, \sigma_2)$", color='blue')
p.axes_labels(['$x$','$u$'])
p.save("L04-plot01.png")
