import sys
from TripleShuffle import Cipher

if len(sys.argv) < 5:
    print("Arguments: <enc|dec> <indexA> <indexB> <text>")
    sys.exit(1)

mode = sys.argv[1]
indexA = sys.argv[2]
indexB = sys.argv[3]
text = sys.argv[4]

output = "-"
try:
    cipher = Cipher(indexA, indexB)
    if mode == "enc":
        output = cipher.encipher(text)
    elif mode == "dec":
        output = cipher.decipher(text)
except:
    print("Sorry, error occured. Check your arguments.")

print(text)
print(output)