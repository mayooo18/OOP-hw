MONTHS = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def parse_date(date_str: str):
    parts = date_str.strip().split("/")

    if len(parts) != 3:
        raise ValueError("Date must be in 'DD Month YYYY' format.")
    day_str, month_str, year_str = parts

    if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
        raise ValueError("Date must be in 'DD Month YYYY' format.")
    
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)

    if not (1 <= day <=31):
        raise ValueError("Day must be between 1 and 31.")
    
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    
    if not(1 <= year <= 9999):
        raise ValueError("Year must be between 1 and 9999.")
    
    return day , month, year

def main():
    date_input = input("Enter a date (DD/MM/YYYY): ")

    try:
        day, month, year = parse_date(date_input)
        print(f"Parsed Date: Day: {day}, Month: {MONTHS[month]}, Year: {year}") 
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()