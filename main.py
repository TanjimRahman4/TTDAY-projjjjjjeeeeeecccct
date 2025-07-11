for b in range(21):
    if b % 10 == 0:
        print(b)
        continue
    print("the value is: ", b)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue

    print('\nCurrent Variable value: ', var)
print("\nGood bye!")


for x in range(10):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")

    else:
        print(x)
        
a = input("Enter a word: ")

for i in a:
    if (i == 'A'):
        print("A is found")
        break
    else:
        print("A not found")