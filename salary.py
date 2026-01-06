import sys

def calculate_bonus(performance_rating, bonus_percentage, annual_salary, else_value=0):
    """Calculates bonus based on performance rating.
    Returns else_value if rating is below threshold."""
    if performance_rating < 3:
        print("No bonus awarded: performance rating below threshold.")
        return else_value
    else:
        print("Bonus eligible: calculating bonus.")
        return (bonus_percentage /100) * annual_salary

def main():
    if len(sys.argv) ==5:
        employee_name = sys.argv[1]
        try:
            performance_rating = float(sys.argv[2])
            bonus_percentage = float(sys.argv[3])
            annual_salary = float(sys.argv[4])
        except ValueError:
            print("Error: performance_rating, bonus_percentage, and annual_salary must be numeric.")
            sys.exit(1)
    else:
        print("No command-line arguments provided. Using default values...\n")
        # Default values
        employee_name = "Yashaswi"
        performance_rating = 4.2
        bonus_percentage =10
        annual_salary =850000.00

    bonus = calculate_bonus(performance_rating, bonus_percentage, annual_salary, else_value=0)
    total_salary = annual_salary + bonus

    print(f"\nEmployee Name: {employee_name}")
    print(f"Performance Rating: {performance_rating}")
    print(f"Bonus Percentage: {bonus_percentage}%")
    print(f"Annual Salary: INR {annual_salary:,.2f}")
    if bonus ==0:
        print("Bonus Amount: INR 0.00")
        print("Note: No bonus awarded due to performance rating below threshold.")
    else:
        print(f"Bonus Amount: INR {bonus:,.2f}")
        print(f"Total Salary (with Bonus): INR {total_salary:,.2f}")

if __name__ == "__main__":
    main()