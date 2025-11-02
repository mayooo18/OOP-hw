def main():

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    sales = [0.0] * 7

    print("Enter the sales amount for each day of the week:")

    for i, day in enumerate(days):
        while True:
            try:
                amount = float(input(f"{day}: "))
                if amount < 0:
                    print("Sales cannot be negative. Try again.")
                    continue
                sales[i] = amount
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    weekly_total = sum(sales)


    print(f"\nWeekly Sales Total: ${weekly_total:.2f}")

if __name__ == "__main__":
    main()
