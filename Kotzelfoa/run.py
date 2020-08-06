import sys
from Kotzelfoa import Code

if len(sys.argv) < 2:
    print("Arguments: <enc|dec> <text>")
    sys.exit(1)

mode = sys.argv[1]
text = sys.argv[2]

output = "-"
#try:
code = Code()
if mode == "enc":
    output = code.encode(text)
elif mode == "dec":
    output = code.decode(text)
#except:
#    print("Sorry, error occured. Check your arguments.")

print(text)
print(output)