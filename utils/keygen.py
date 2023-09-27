from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)  # Generates a 256-bit random key

import base64

# Convert to Base64
key_base64 = base64.b64encode(key).decode('utf-8')
print(key_base64)
