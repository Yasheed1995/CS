from pwn import *
from IPython import embed

context.arch = 'amd64'

r = remote('csie.ctf.tw', 10123)
while(True):

    try:
        a = r.recvuntil('left', drop=True)
        b = r.recvuntil('@', timeout=5)

        print (a)

        print ("============================")
        print (b)
        print ("============================")

        c = b.split()
        c = c[:-1]
        print (c)
        c = [int(x) for x in c]
        d = ''
        for i in sorted(c):
 	       d += str(i)
 	       d += ' '

        r.sendline(d)
    except EOFError:
        print ("HI")
        break
'''
print (a)
#print ("========", a, "==========")
b = r.recv(1000)
print
print ("============================")
print (b)
c = r.recv(1000)
print
print (c)

d = r.recv(1000)
print
print (d)

print ("============================")
'''
r.interactive()
