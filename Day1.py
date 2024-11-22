"""Question for the day: (Topic Covered: Conditional Statements)
You are given a 4-digit integer. Your task is to determine if the number is a "special number". A number is considered special if the sum of the first two digits is equal to the sum of the last two digits. You must use if-else statements to solve this.
Difficulty :  Easy


Example:
Input:
1423
Output:
Yes, it is a special number.

Input:
1231
Output:
No, it is not a special number."""

# Function to check if the number is special
def is_special_number(number):
    # Convert the number to a string to easily access individual digits
    num_str = str(number)
    
    # Extract the digits
    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    third_digit = int(num_str[2])
    fourth_digit = int(num_str[3])
    
    # Calculate the sums
    sum_first_two = first_digit + second_digit
    sum_last_two = third_digit + fourth_digit
    
    # Check if the sums are equal
    if sum_first_two == sum_last_two:
        return "Yes, it is a special number."
    else:
        return "No, it is not a special number."

# Input
number = int(input("Enter a 4-digit integer: "))

# Output
print(is_special_number(number))
