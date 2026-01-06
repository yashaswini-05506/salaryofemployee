import sys

def calculate_bonus(performance_rating, bonus_percentage, annual_salary, else_value=0):
    """Return bonus if rating ≥ 3, otherwise return else_value."""
    if performance_rating < 3:
        print("No bonus awarded: performance rating below threshold.")
        return else_value
    print("Bonus eligible: calculating bonus.")
    return (bonus_percentage / 100) * annual_salary

def main():
    # Ask if the user wants to use defaults
    use_default = input("Use default values? (y/n): ").strip().lower()
    if use_default == "y":
        employee_name = "Yashaswi"
        performance_rating = 4.2
        bonus_percentage = 10
        annual_salary = 850_000.00
    else:
        try:
            employee_name = input("Employee name: ").strip()
            performance_rating = float(input("Performance rating: "))
            bonus_percentage = float(input("Bonus percentage: "))
            annual_salary = float(input("Annual salary: "))
        except ValueError:
            print("Error: rating, percentage and salary must be numeric.")
            sys.exit(1)

    bonus = calculate_bonus(performance_rating, bonus_percentage,
                            annual_salary, else_value=0)
    total_salary = annual_salary + bonus

    print(f"\nEmployee Name: {employee_name}")
    print(f"Performance Rating: {performance_rating}")
    print(f"Bonus Percentage: {bonus_percentage}%")
    print(f"Annual Salary: INR {annual_salary:,.2f}")

    if bonus == 0:
        print("Bonus Amount: INR 0.00")
        print("Note: No bonus awarded due to performance rating below threshold.")
    else:
        print(f"Bonus Amount: INR {bonus:,.2f}")
        print(f"Total Salary (with Bonus): INR {total_salary:,.2f}")

if __name__ == "__main__":
    main()
