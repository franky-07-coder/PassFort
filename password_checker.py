import re
import tkinter as tk
from tkinter import ttk

# -------------------------------
# Password Strength Checker Logic
# -------------------------------
def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    # Criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()]", password):   # unified special chars
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*()).")

    # Ratings
    ratings = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return {
        "score": score,
        "rating": ratings.get(score, "Very Weak"),
        "feedback": feedback
    }

# -------------------------------
# GUI Application
# -------------------------------
def evaluate_password():
    password = entry.get()
    result = check_password_strength(password)

    # Clear previous results
    result_label.config(text="")
    suggestions_box.delete("1.0", tk.END)

    # Colors
    colors = {
        "Very Weak": "red",
        "Weak": "orange",
        "Moderate": "yellow",
        "Strong": "lightgreen",
        "Very Strong": "green"
    }

    # Show result
    result_label.config(
        text=f"Strength: {result['rating']} ({result['score']}/5)",
        fg=colors.get(result['rating'], "white")
    )

    # Progress bar
    progress["value"] = result['score'] * 20
    style.configure("TProgressbar", troughcolor="#2b2b3c", background=colors[result['rating']])

    # Feedback
    if result['feedback']:
        suggestions_box.insert(tk.END, "Suggestions:\n\n")
        for f in result['feedback']:
            suggestions_box.insert(tk.END, f"• {f}\n")
    else:
        suggestions_box.insert(tk.END, "✅ Looks good! Your password is strong.")


# -------------------------------
# Main GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x420")
root.config(bg="#1e1e2e")

title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="white")
title.pack(pady=15)

entry = tk.Entry(root, width=30, font=("Arial", 14), show="*")
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", command=evaluate_password,
                      bg="blue", fg="white", font=("Arial", 14, "bold"))
check_btn.pack(pady=10)

style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=25, troughcolor="black", background="red")
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
progress.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#1e1e2e")
result_label.pack(pady=10)

suggestions_box = tk.Text(root, height=6, width=50, font=("Arial", 12),
                          wrap="word", bg="#2b2b3c", fg="white")
suggestions_box.pack(pady=10)

root.mainloop()
