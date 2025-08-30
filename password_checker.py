import re

def check_password_strength(password: str) -> dict:
    strength = 0
    feedback = []

    # Criteria
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (@$!%*?&).")

   
    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return {
        "score": strength,
        "rating": levels.get(strength, "Very Weak"),
        "feedback": feedback
    }
