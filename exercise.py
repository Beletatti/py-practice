def weeks_left(age):
    # Constants
    total_weeks = 90 * 52  # Total weeks in 90 years
    weeks_per_year = 52
    
    # Calculate weeks lived
    weeks_lived = age * weeks_per_year
    
    # Calculate weeks left
    weeks_remaining = total_weeks - weeks_lived
    
    # Output the result
    return f"You have {weeks_remaining:,} weeks left."

# Input: current age
current_age = int(input("Enter your current age: "))
print(weeks_left(current_age))
