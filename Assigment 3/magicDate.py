month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))
year = int(input("Enter two-digit year (0-99): "))

valid_date = True

if 1 <= month <= 12:
    month = month
else:
    print("Invalid month. Please enter a value between 1 and 12.")
    valid_date = False

if 1 <= day <= 31:
    day = day   
else:
    print("Invalid day. Please enter a value between 1 and 31.")
    valid_date = False


if 0 <= year <= 99:
    year = year
else:
    print("Invalid year. Please enter a two-digit value between 0 and 99.")
    valid_date = False

if valid_date:
    magic_year= month * day

    print(f"The date is {month}/{day}/{year}")


    if magic_year == year:
        print("This is a magic date!")
    else:
        print("this is not a magic date")

