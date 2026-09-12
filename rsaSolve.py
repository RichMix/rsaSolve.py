#!/usr/bin/env python3
# Add your own 'n' and 'e' 
# Then add your ciphertext separated by commas like so:
# [ 123, 435, 1355, 654, 987, 777 ]
# But leave indentations if unfamiliar with Python syntax
# As the idea is for this to be a plug and play RSA decoder
n = 
e = 

# Do not alter brackets
ciphertext = [
	#replace_this_with_numbers
	#separated by commas like specified

# Step 1: Set RSA factors (add p = & q =)
p = 
q = 

# Step 2: Euler totient
phi = (p - 1) * (q - 1)

# Step 3: Private exponent
d = pow(e, -1, phi)

print("p =", p)
print("q =", q)
print("phi =", phi)
print("d =", d)

# Step 4: RSA decryption
decoded_numbers = [pow(c, d, n) for c in ciphertext]

print("Decoded integers:", decoded_numbers)

# Step 5: ASCII conversion
plaintext = ''.join(chr(x) for x in decoded_numbers)

print("Plaintext:", plaintext)
