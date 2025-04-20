import datetime

health_data = []


def add_daily_metrics(steps, sleep, calories, water):
    today = datetime.date.today().isoformat()
    health_data.append({
        "date": today,
        "steps": steps,
        "sleep": sleep,
        "calories": calories,
        "water": water
    })
    print("Daily metrics recorded successfully.")


def view_week_summary():
    print("\n=== Weekly Summary ===")
    for entry in health_data[-7:]:
        print(entry)


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def daily_calorie_needs(age, weight, height, gender):
    if gender == 'M':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


def plot_progress():
    if not health_data:
        print("No data to show.")
        return

    print("\n=== Health Progress ===")
    print(f"{'Date':<12}{'Steps':<10}{'Sleep':<10}{'Calories':<12}{'Water (L)':<10}")
    print("-" * 54)
    for entry in health_data:
        print(f"{entry['date']:<12}{entry['steps']:<10}{entry['sleep']:<10}{entry['calories']:<12}{entry['water']:<10}")


def hydration_reminder():
    print("\U0001F4A7 Stay hydrated! Drink a glass of water now.")


def main():
    print("=== Health & Fitness Tracker ===")

    while True:
        print("""
        1. Add Daily Health Metrics
        2. View Weekly Summary
        3. Calculate BMI
        4. Estimate Calorie Needs
        5. Show Progress Table
        6. Hydration Reminder
        7. Exit
        """)

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                steps = int(input("Steps: "))
                sleep = float(input("Sleep hours: "))
                calories = int(input("Calories consumed: "))
                water = float(input("Water intake (liters): "))
                add_daily_metrics(steps, sleep, calories, water)

            elif choice == '2':
                view_week_summary()

            elif choice == '3':
                weight = float(input("Weight (kg): "))
                height = float(input("Height (m): "))
                bmi = calculate_bmi(weight, height)
                print(f"Your BMI is {bmi:.2f}")

            elif choice == '4':
                age = int(input("Age: "))
                weight = float(input("Weight (kg): "))
                height = float(input("Height (cm): "))
                gender = input("Gender (M/F): ").upper()
                calories = daily_calorie_needs(age, weight, height, gender)
                print(f"Estimated daily calorie needs: {calories:.0f} kcal")

            elif choice == '5':
                plot_progress()

            elif choice == '6':
                hydration_reminder()

            elif choice == '7':
                print("Stay healthy! Goodbye.")
                break

            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            print("An error occurred:", e)


if _name_ == "_main_":
    main()