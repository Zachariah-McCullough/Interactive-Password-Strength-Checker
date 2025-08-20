# 🔐 Interactive Password Strength Checker

An interactive **GUI-based password strength analyzer** built with Python and Tkinter.  
This tool helps users understand how secure their passwords are by estimating **entropy**, **crack time**, and providing **improvement suggestions** in real time.  

---

## 🚀 Features

- **Real-time analysis** as you type  
- Estimates **entropy** of your password  
- Calculates estimated **offline crack time** (assuming 10 billion guesses/second)  
- Rates password strength: Very Weak, Weak, Medium, Strong  
- **Color-coded feedback** (red → green)  
- Actionable **suggestions** to improve password security  

---

## 🖥️ Demo

When you enter a password:  

- `"password"` → Very Weak, cracked in seconds  
- `"MyStr0ngP@ssw0rd!"` → Strong, estimated crack time in billions of years  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-checker.git
   cd password-checker

    Run the script:

    python password_checker.py

📊 How It Works

    Character Set Detection

        Lowercase (26)

        Uppercase (26)

        Numbers (10)

        Symbols (~32, depending on your system)

    Entropy Calculation

    entropy = length × log2(character_set_size)

    Crack Time Estimate

        Assumes 10 billion guesses per second (fast offline attack)

        Converts into human-readable time (seconds, minutes, hours, years)

    Strength Classification

        < 28 bits → Very Weak

        28–35 bits → Weak

        36–59 bits → Medium

        60+ bits → Strong

📌 Example

Enter Password: TrickyP@ssw0rd
Strength: Strong
Estimated offline crack time: 12.55 billion years
Suggestions:

🔮 Future Enhancements

    Add a visual progress bar for strength feedback

    Compare against a list of common leaked passwords

    Option to toggle show/hide password

    Export reports for security awareness training

🛡️ Disclaimer

This tool is for educational and awareness purposes only.
It does not guarantee absolute password security. Always use strong, unique passwords with a password manager.
