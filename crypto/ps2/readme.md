# PS2

We have a lot of XOR encrypted lines and we know that the key length is 1 byte.

We know that one clear text line must beggin with `CHTB{` so we create an script to search the flag.

```python
#!/usr/bin/python3
from itertools import cycle  
import string
import binascii
import codecs
import sys


def xor_decrypt_string(data, key):
   xored = ''
   for (x,y) in zip(data, cycle(key)):
      decrypt = (int(x,16) ^ int(y, 16))
      xored = xored + ((hex(decrypt)[2:]))
   
   return xored


f = open("output.txt", "r")
lineas = f.read().splitlines()

decode_hex = codecs.getdecoder("hex_codec")

conseguido = 0

for line in lineas:
   for clave in string.ascii_letters:
      clave_hexadecimal = clave.encode("utf-8").hex()

      descifrado = xor_decrypt_string(line, clave_hexadecimal)
      try:
         descifrado_ascii = decode_hex(descifrado)[0].decode('utf-8')
         if(descifrado_ascii[:5] == "CHTB{"):
            conseguido = 1
      except:
         pass


      if(conseguido == 1):
         print("\nMensaje cifrado: "+line)
         print("Clave: "+clave_hexadecimal)
         print("Descifrado en hexadecimal: " +descifrado)
         print("Descifrado en ASCII: " + descifrado_ascii)
         sys.exit(0)

```

```shell
$ python3 xor_solve.py

Mensaje cifrado: 060d11073e2b76762129761a742b1a711a2d713c363171262e38
Clave: 45
Descifrado en hexadecimal: 434854427b6e3333646c335f316e5f345f683479737434636b7d
Descifrado en ASCII: CHTB{n33dl3_1n_4_h4yst4ck}

```