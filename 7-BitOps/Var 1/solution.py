z1 = 0x28d4 # x & z
print(f"{int(bin(z1)[2:]):016}")
# 0010100011010100
# where 1 z and x has 1
# ??1?1???11?1?1?? 
# and at least one of them in ? has 0

z2 = 0x2852 # x ^ (z << 1)
print(f"{int(bin(z2)[2:]):016}")
# 0010100001010010
# we already have some information about z and x
# x         = ?1111??1111111?0
# z << 1    = ?1010??1101011?0
#           = 0010100001010010
# newx      = ?1111??1111111?0
# newz      = ??1010??1101011?

z3 = 0x5d8c # x & (y << 1)
print(f"{int(bin(z3)[2:]):016}")
# 0101110110001100
# x         = ?11111?1111111?0
# y << 1    = ?10111?1100011?0
# res       = 0101110110001100
# newx      = ?11111?1111111?0
# newy      = ??10111?1100011?

# have new info about x, can reconstract z
# x         = ?11111?1111111?0
# z         = ?10101?1101011?0
# res       = 0010100001010010
# newz      = ??10101?1101011? additional bit found

z4 = 0x6ff7 # y | (z >> 2)
print(f"{int(bin(z4)[2:]):016}")
# 0110111111110111
# y         = 011011111100011?
# z >> 2    = 00?010101?110101
#           = 0110111111110111
# newy      = 011011111100011?
# newz      = ?010101?1101011?


# ----------------------------------
# values updated creating a checkpoint
# x         = ?11111?1111111?0
# y         = 011011111100011?
# z         = ?010101?1101011?
# ----------------------------------


# trying z3 again
# x         = 01111101111111?0
# y << 1    = 11011111100011?0
#           = 0101110110001100
# newx      = 01111101111111?0
# newy      = 011011111100011?


# trying z1 again
# x         = 0111110111111100 # YEAAAAAAAA
# z         = ?01010101101011?
#           = 0010100011010100
# newx      = 0111110111111100
# newz      = ?01010101101011?


# -------------------------------
# x is fine, creating a checkpoint
# x         = 0111110111111100
# y         = 011011111100011?
# z         = ?01010101101011?
# -------------------------------


# Using z4 to complete y
# y         = 011011111100011?
# z >> 2    = 00?0101010110101
#           = 0110111111110111
# SAD (no new information)


# Trying z3 to
# x         = 0111110111111100
# y << 1    = 11011111100011?0
#           = 0101110110001100
# SAD (no new info)

# Trying z2
# x         = 0111110111111100
# z << 1    = 0101010110101110 # YEAAAH
#           = 0010100001010010
# newz      = ?010101011010110

# -------------------------------
# z expanded, creating a checkpoint
# x         = 0111110111111100
# y         = 011011111100011?
# z         = ?010101011010111
# -------------------------------
# видимо больше нельзя
# проверяем ответ

x = int("0111110111111100", 2)
y = int("0110111111000111", 2)
z = int("1010101011010111", 2)

print(hex(x & z))
print(hex(x ^ (z << 1) & 0xffff))
print(hex(x & (y << 1) & 0xffff))
print(hex(y | (z >> 2) & 0xffff))


# короче все варианты подходят
# ответ:
# 0111110111111100
# 011011111100011?
# ?010101011010111