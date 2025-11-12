from club_staff import Coach, Player, Medic

def build_club():
    departments = {}

    def add(member):
        dept = member.get_department()
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(member)

    add(Coach("Pep Guardiola", "Coaching", 5000))
    add(Player("Lionel Messi", "Players", 2500000, 54, 500))
    add(Player("Cristiano Ronaldo", "Players", 2000000, 45, 400))
    add(Medic("Dr. Smith", "Medical", 3000, 10))

    return departments


def display_payroll(departments):
    club_total = 0
    print("Club Payroll Report")

    for dept, staff_list in departments.items():
        print(f"\nDepartment: {dept}")
        dept_total = 0
        print("-" * 30)

        for member in staff_list:
            pay = member.calculate_pay()
            dept_total += pay
            print(f"{member.description():30} Pay: ${pay:,.2f}")

        print(f"Total for {dept}: ${dept_total:,.2f}")
        club_total += dept_total


    print(f"\nOverall Club Payroll: ${club_total:,.2f}")



def main():
    departments = build_club()
    display_payroll(departments)


if __name__ == "__main__":
    main()
