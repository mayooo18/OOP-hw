def main():
    filename= input("Enter the filename to read numbers from: ")

    try:
        file = open(filename, 'r')
        total = 0
        count = 0

        for line in file:
            total += int(line)
            count += 1
        file.close()
        average = total / count

        print(f"The average of the numbers in {filename} is {average:.2f}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except ValueError:
        print("The file contains non-numeric data.")
    except ZeroDivisionError:
        print("The file is empty.") 

    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()