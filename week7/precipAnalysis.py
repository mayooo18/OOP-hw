def main():

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]


    precipitation = [0.0] * 12

    print("Enter monthly precipitation values:")

    for i, month in enumerate(months):
        while True:
            try:
                value = float(input(f"{month}: "))
                if value < 0:
                    print("Precipitation cannot be negative. Try again.")
                    continue
                precipitation[i] = value
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


    total = sum(precipitation)
    average = total / len(precipitation)
    max_val = max(precipitation)
    min_val = min(precipitation)
    max_month = months[precipitation.index(max_val)]
    min_month = months[precipitation.index(min_val)]


    print("\nPrecipitation Summary")
    print("----------------------")
    print(f"Total Annual Precipitation: {total:.2f}")
    print(f"Average Monthly Precipitation: {average:.2f}")
    print(f"Highest Precipitation: {max_val:.2f} in {max_month}")
    print(f"Lowest Precipitation: {min_val:.2f} in {min_month}")

if __name__ == "__main__":
    main()