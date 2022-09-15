#!/usr/bin/env python3

plaintext = "1001001001101101100100100110"
ciphertext = "1011110000110001001010110001"
result = ""

# Loop through each element in the plaintext and ciphertext
for x in range(0, len(plaintext)):
    # If only one of the current element is 1, then return 1 for that index
    if ( int(plaintext[x]) + int(ciphertext[x]) == 1 ):
        result = result + str(1)
    # If both or none of the current element is 1, then return 0 for that index
    else:
        result = result + str(0)

# Print the result of the XOR operation
print(result)