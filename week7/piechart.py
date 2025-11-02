import matplotlib.pyplot as plt

def read_expenses(filename="expense.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find '{filename}'. Put it in the same folder.")

    expenses = []
    for i, raw in enumerate(lines, start=1):
        s = raw.strip()
        if not s:
            expenses.append(0.0)
            continue
        try:
            expenses.append(float(s))
        except ValueError:
            raise ValueError(f"Conversion error on line {i}: {s!r} is not a number.")
    return expenses

def main():
    
    labels = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]

    try:
        data = read_expenses("expense.txt")

        
        if len(data) < len(labels):
            labels = labels[:len(data)]
        elif len(data) > len(labels):
            labels += [f"Item {i}" for i in range(len(labels) + 1, len(data) + 1)]

        if not data or sum(data) == 0:
            raise ValueError("All expenses sum to 0. Provide non-zero values in expense.txt.")

        plt.figure()
        plt.title("Monthly Expenses")
        plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.axis("equal")
        plt.show()

        try:
            data.index(-1.0)  
        except ValueError:
            pass

    except FileNotFoundError as e:
        print("Error:", e)
    except IndexError as e:
        print("Error: index out of range while matching labels/data.", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()