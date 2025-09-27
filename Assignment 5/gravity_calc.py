

def falling_distance(time):
    distance = (9.8 * time * time )/2
    return distance

def main():
    time = float(input("Enter the time in seconds: "))
    print(" Time |  Falling Distance")
    print("---------------------------")
    for t in range(1, int(time)+1):
        distance = falling_distance(t)
        print(f"{t}".rjust(5), "|", f"{distance:.2f}".rjust(11))


if __name__ == "__main__":
    main()