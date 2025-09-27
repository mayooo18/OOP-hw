#global constant
KM_TO_MI = 0.621371


def show_miles(kilometers):
    miles = kilometers * KM_TO_MI
    print(f"{kilometers:.2f} kilometers is equal to {miles:.2f} miles.")


def main():
    km = float(input("Enter the distance in kilometers: "))
    show_miles(km)


if __name__ == "__main__":
    main()