import re

def password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        "password": password,
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_criteria": special_criteria,
        "strength_score": strength_score,
        "strength": strength
    }

# Example usage
password = "ExamplePass123!"
assessment = password_strength(password)
print(assessment)
