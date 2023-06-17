import random

def generate_numbers(first_digits):
    numbers = []
    for first_digit in first_digits:
        for _ in range(10):
            number = str(first_digit)
            for _ in range(7):
                number += str(random.randint(0, 9))
            numbers.append(number)
    
    # Concatenate numbers into a string
    numbers_string = "\n".join(numbers)
    return numbers_string

# Call the function with a list of first digits
result = generate_numbers([4, 5])
print(result)

 
