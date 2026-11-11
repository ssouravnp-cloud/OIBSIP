# BMI Calculator

print("==============================")
print("       BMI CALCULATOR")
print("==============================")

try:
    # Get user input
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Input validation
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")

    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display results
        print("\n========== BMI RESULT ==========")
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("================================")

except ValueError:
    print("Error: Please enter valid numeric values.")
