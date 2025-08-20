import tkinter as tk
from tkinter import ttk
import math
import string

def evaluate_password(pw):
    length = len(pw)
    charsets = [
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw)
    ]
    
    # Correct charset sizes
    charset_sizes = [26, 26, 10, len(string.punctuation)]
    charset_total = sum(charset_sizes[i] for i in range(4) if charsets[i])
    
    entropy = length * math.log2(charset_total) if charset_total > 0 else 0
    
    guesses_per_second = 1e10
    time_seconds = 2 ** entropy / guesses_per_second

    suggestions = []
    if not charsets[0]:
        suggestions.append("Add lowercase letters")
    if not charsets[1]:
        suggestions.append("Add uppercase letters")
    if not charsets[2]:
        suggestions.append("Add numbers")
    if not charsets[3]:
        suggestions.append("Add symbols")
    if length < 12:
        suggestions.append("Make it at least 12 characters long")

    if entropy < 28:
        strength, color = "Very Weak", "red"
    elif entropy < 36:
        strength, color = "Weak", "orange"
    elif entropy < 60:
        strength, color = "Medium", "yellow"
    else:
        strength, color = "Strong", "green"

    return strength, color, time_seconds, suggestions

def format_time(seconds):
    if seconds < 60: return f"{seconds:.2f} seconds"
    minutes = seconds / 60
    if minutes < 60: return f"{minutes:.2f} minutes"
    hours = minutes / 60
    if hours < 24: return f"{hours:.2f} hours"
    days = hours / 24
    if days < 365: return f"{days:.2f} days"
    years = days / 365
    return f"{years:.2f} years"

def update_strength(*args):
    pw = password_var.get()
    if pw:
        strength, color, crack_time, suggestions = evaluate_password(pw)
        strength_label.config(text=f"Strength: {strength}", foreground=color)
        time_label.config(text=f"Estimated offline crack time: {format_time(crack_time)}")
        suggestion_label.config(text="Suggestions:\n" + "\n".join(suggestions))
    else:
        strength_label.config(text="Strength: N/A", foreground="black")
        time_label.config(text="Estimated offline crack time: N/A")
        suggestion_label.config(text="Suggestions:")

# GUI
root = tk.Tk()
root.title("Interactive Password Strength Checker")

password_var = tk.StringVar()
password_var.trace_add('write', update_strength)

ttk.Label(root, text="Enter Password:").pack(pady=5)
ttk.Entry(root, textvariable=password_var, show="*").pack(pady=5, padx=10, fill='x')

strength_label = ttk.Label(root, text="Strength: N/A")
strength_label.pack(pady=5)

time_label = ttk.Label(root, text="Estimated offline crack time: N/A")
time_label.pack(pady=5)

suggestion_label = ttk.Label(root, text="Suggestions:")
suggestion_label.pack(pady=5)

root.mainloop()
