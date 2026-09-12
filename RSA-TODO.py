#!/usr/bin/env python3

import math

print("=" * 60)
print("Interactive RSA Decryption Tool")
print("=" * 60)

# ---------------------------------------------------------
# INPUT RSA PARAMETERS
# ---------------------------------------------------------

n = int(input("Enter n: ").strip())
e = int(input("Enter e: ").strip())
p = int(input("Enter p: ").strip())
q = int(input("Enter q: ").strip())

print()
print("Enter ciphertext integers separated by spaces or commas.")
print("Example:")
print("683 1085 358 1590 507 85")
print()

cipher_input = input("Ciphertext: ").strip()

# Allow either:
# 683 1085 358
# or:
# 683,1085,358
# or:
# 683, 1085, 358

cipher_input = cipher_input.replace(",", " ")

ciphertext = [
    int(x)
    for x in cipher_input.split()
]

# ---------------------------------------------------------
# VERIFY RSA FACTORS
# ---------------------------------------------------------

if p * q != n:
    print()
    print("[!] ERROR")
    print(f"{p} * {q} = {p*q}")
    print(f"but n = {n}")
    raise SystemExit

print()
print("[+] Factors verified:")
print(f"    {p} * {q} = {n}")

# ---------------------------------------------------------
# CALCULATE PHI
# ---------------------------------------------------------

phi = (p - 1) * (q - 1)

print()
print("[+] Euler Totient")
print(f"    phi(n) = {phi}")

# ---------------------------------------------------------
# VERIFY e
# ---------------------------------------------------------

gcd = math.gcd(e, phi)

print()
print("[+] gcd(e, phi)")
print(f"    gcd({e}, {phi}) = {gcd}")

if gcd != 1:
    print()
    print("[!] e and phi(n) are not coprime.")
    print("[!] A standard RSA private exponent cannot be calculated.")
    raise SystemExit

# ---------------------------------------------------------
# CALCULATE PRIVATE EXPONENT d
# ---------------------------------------------------------

d = pow(e, -1, phi)

print()
print("[+] Private exponent")
print(f"    d = {d}")

# ---------------------------------------------------------
# DECRYPT RSA BLOCKS
# ---------------------------------------------------------

decoded_numbers = [
    pow(c, d, n)
    for c in ciphertext
]

print()
print("=" * 60)
print("DECRYPTED INTEGER VALUES")
print("=" * 60)

print(decoded_numbers)

# ---------------------------------------------------------
# OUTPUT 1:
# DIRECT INTEGER -> CHARACTER
#
# Useful when:
# 83 -> S
# 75 -> K
# 89 -> Y
# ---------------------------------------------------------

print()
print("=" * 60)
print("PLAINTEXT METHOD 1")
print("Direct integer -> character")
print("=" * 60)

try:
    direct_plaintext = ''.join(
        chr(x)
        for x in decoded_numbers
    )

    print(direct_plaintext)

except (ValueError, OverflowError):
    print("[!] Could not interpret every integer as a character.")

# ---------------------------------------------------------
# OUTPUT 2:
# INTEGER -> BYTE BLOCKS
#
# Useful when decrypted RSA integers contain more than
# one byte of plaintext.
# ---------------------------------------------------------

print()
print("=" * 60)
print("PLAINTEXT METHOD 2")
print("Integer -> byte blocks")
print("=" * 60)

byte_blocks = []

for value in decoded_numbers:

    byte_length = max(
        1,
        (value.bit_length() + 7) // 8
    )

    block = value.to_bytes(
        byte_length,
        byteorder="big"
    )

    byte_blocks.append(block)

raw_plaintext = b''.join(byte_blocks)

print("Raw bytes:")
print(raw_plaintext)

print()
print("Hex:")
print(raw_plaintext.hex())

print()
print("UTF-8 attempt:")

try:
    print(raw_plaintext.decode("utf-8"))

except UnicodeDecodeError:
    print("[!] Raw bytes are not valid UTF-8.")

    print()
    print("ASCII-safe view:")

    ascii_view = ''.join(
        chr(b) if 32 <= b <= 126 else '.'
        for b in raw_plaintext
    )

    print(ascii_view)

# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------

print()
print("=" * 60)
print("RSA SUMMARY")
print("=" * 60)

print(f"n      = {n}")
print(f"e      = {e}")
print(f"p      = {p}")
print(f"q      = {q}")
print(f"phi(n) = {phi}")
print(f"d      = {d}")

print()
print("Ciphertext blocks:")
print(ciphertext)

print()
print("Decrypted integers:")
print(decoded_numbers)

print()
print("=" * 60)
