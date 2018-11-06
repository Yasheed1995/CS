import binascii
import sys
file = open("data", "r") 
l = []
while True:
	input = file.read(4)
	ii = input.find('=')
	if ii >= 0:
		break 
	s = [0]*len(input)
	for i in range(len(input)):
		if ord(input[i]) >= 97:
			s[i] = 26+(ord(input[i]) - ord('a'))
		elif ord(input[i]) < 65:
			s[i] = 52+(ord(input[i]) - ord('0'))
		else:	
			s[i] = (ord(input[i]) - ord('A'))
	a = (s[0]*4 + ((s[1] >> 4) & 3)) & 0xff
	b = (s[1]*16 + ((s[2] >> 2) & 0xf)) & 0xff
	c = ((s[2] << 6) + s[3]) & 0xff
	l.append(a)
	l.append(b)
	l.append(c)
	#sys.stdout.write(binascii.unhexlify(hex(a)[2:] + hex(b)[2:] + hex(c)[2:]))
l.append(120)
f = [0]*len(l)
for i in range(len(l)):
	if l[i] == 109: # m
		f[i] = 3
	elif l[i] == 66: #B
		f[i] = 1
	elif l[i] == 79: #O
		f[i] = 6
	elif l[i] == 70: #F
		f[i] = 7
	elif l[i] == 97: #a
		f[i] = 2
	elif l[i] == 98: #b
		f[i] = 4
	elif l[i] == 120: #x
		f[i] = 8
	else:
		f[i] = 5
j = [0]*len(l)
stack = []
for i in range(len(l)):
	if f[i] == 7:
		stack.append(i)
	elif f[i] == 8:
		tmp = stack.pop()
		j[i] = tmp
		j[tmp] = i
m = [0]*10000
index = 0
input_len = 0
my_input = "this is flag that your input"
i = 0
while i < len(f):
	#print("iteration: " + str(i) + ", operation: " + str(f[i]) + ", jump_to: " + str(j[i]) + ", index: " + str(index) + ", m[]: " + str(hex(m[index])))
        if f[i] == 0:
                print('f[i] has 0')
                break
        if index > 65534:
                print('index > 65534')
                break
        if f[i] > 8:
                print('f[i] > 8')
                break
        if f[i] == 1:
                index = (index + 1) % 65536
        elif f[i] == 2:
                index = (index - 1) % 65536
        elif f[i] == 3:
                m[index] = (m[index] + 1) % 65536
        elif f[i] == 4:
                m[index] = (m[index] - 1) % 65536
        elif f[i] == 5:
                sys.stdout.write(str(hex(m[index] % 65536))[2:].decode('hex'))
        elif f[i] == 6:
		m[index] = ord(my_input[input_len])
		input_len += 1
        elif f[i] == 7:
                if m[index] == 0:
                        i = j[i]
        elif f[i] == 8:
                if m[index] != 0:
                        i = j[i]
        i = i + 1

# brainfuck dump
'''for i in range(len(f)):
        if f[i] == 1:
                sys.stdout.write('>')
        elif f[i] == 2:
                sys.stdout.write('<')
        elif f[i] == 3:
                sys.stdout.write('+')
        elif f[i] == 4:
                sys.stdout.write('-')
        elif f[i] == 5:
                sys.stdout.write('.')
        elif f[i] == 6:
                sys.stdout.write(',')
        elif f[i] == 7:
                sys.stdout.write('[')
        elif f[i] == 8:
                sys.stdout.write(']')
m = [0]*65536'''
