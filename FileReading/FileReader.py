f = open("demofile.txt")
print(f.read(6) + '\n')
f.seek(0)

f = open("demofile.txt")
print(f.read())
f.seek(0)
print('\n')

f = open("demofile.txt")
for x in f:
    print(x)
f.close()