
celsiusTarget = input("Enter the number to convert up to in Celsius: ") 


print(" Celsius |  Fahrenheit")
print("-----------------------")
for celsius in range(0,int(celsiusTarget) + 1):
    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius}".rjust(8), "|", f"{fahrenheit}".rjust(11))
          
