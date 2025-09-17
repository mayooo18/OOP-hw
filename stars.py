while not ((star := int(input("Enter the number of stars to print: "))) > 0):
    print("Please enter a positive integer.")


for i in range(star, 0, -1):
    for x in range(i):
        print('*', end='')

    print()