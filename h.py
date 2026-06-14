r=int(input("Enter the number of rows: "))
for i in range(r):
    for j in range(i+1):
        print("⭐", end=' ')
    print()

len=r*2
dl="-"*len
print(dl)

for i in range(r):
    for j in range(i,r):
        print("⭐", end=' ')
    print()