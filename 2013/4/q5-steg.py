f = open("ncss-modified.bmp", "rb").read()
offset = int.from_bytes(f[0xA:0xA+4], 'little')
w = int.from_bytes(f[0x12:0x12+4], 'little')
h = int.from_bytes(f[0x16:0x16+4], 'little')
row_size = int((w * 24 + 31) / 32) * 4
c = ''
for i in range(offset, len(f), row_size):
    for j in range(row_size):
        try:
            c += str(f[i + j] & 1)
        except:
            break
b = []
for i in range(0, len(c), 8):
    try:
        b.append(c[i:i+8][::-1])
    except:
        break

message = bytes(int(i, 2) for i in b)
print(message[:message.index(0)].decode('ascii'))
