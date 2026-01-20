# grade_calculator.py
# This program calculates grade based on marks entered by the user

def calculate_grade(marks):
    """
    Determines grade based on marks
    """

    # Handling invalid marks
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Please enter a value between 0 and 100."

    # Nested conditions to simulate real business rules
    if marks >= 90 and marks <= 100:
        return "🎉 Grade A+ : Outstanding performance"
    
    elif marks >= 80 and marks < 90:
        return "⭐ Grade A : Excellent performance"
    
    elif marks >= 70 and marks < 80:
        return "👍 Grade B : Good performance"
    
    elif marks >= 60 and marks < 70:
        return "🙂 Grade C : Average performance"
    
    elif marks >= 40 and marks < 60:
        return "⚠️ Grade D : Needs improvement"
    
    else:
        return "❌ Grade F : Failed"


# Main execution starts here
def main():
    try:
        # Taking input from user
        marks = float(input("Enter your marks (0 - 100): "))

        # Calculating and displaying grade
        result = calculate_grade(marks)
        print(result)

    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")


# Calling main function
if __name__ == "__main__":
    main()
