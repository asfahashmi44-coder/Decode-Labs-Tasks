import secrets  # 👈 Replaced 'random' for true cryptographic security!
import string
import tkinter as tk
from datetime import datetime

def check_strength(password):
    """Analyzes the password and returns a strength rating."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length >= 12 and score == 4:
        return "🟢 Strong (Excellent security)"
    elif length >= 8 and score >= 3:
        return "🟡 Medium (Good, but could be stronger)"
    else:
        return "🔴 Weak (Easy to crack)"

def copy_to_clipboard(text):
    """Copies text to the system clipboard using built-in tkinter."""
    try:
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True
    except Exception:
        return False

def log_password_metadata(count, strength_summary):
    """Logs the generation event without saving the actual raw credentials."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("passwords_log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Generated {count} password(s). Top Strength: {strength_summary}\n")
    except Exception as e:
        print(f"⚠️ Note: Could not write to log file: {e}")

def generate_custom_password(length, use_upper, use_lower, use_digits, use_special):
    """Generates a secure password using the cryptographically strong 'secrets' module."""
    pool = []
    all_chars = ""
    
    # Force inject at least 1 character using secrets.choice for absolute security
    if use_lower:
        pool.append(secrets.choice(string.ascii_lowercase))
        all_chars += string.ascii_lowercase
    if use_upper:
        pool.append(secrets.choice(string.ascii_uppercase))
        all_chars += string.ascii_uppercase
    if use_digits:
        pool.append(secrets.choice(string.digits))
        all_chars += string.digits
    if use_special:
        special_set = "!@#$%^&*()-_=+[{]};:,.<>/?"
        pool.append(secrets.choice(special_set))
        all_chars += special_set

    if not all_chars:
        pool.append(secrets.choice(string.ascii_lowercase))
        all_chars += string.ascii_lowercase

    # Fill remaining characters securely
    while len(pool) < length:
        pool.append(secrets.choice(all_chars))
        
    # Shuffle cryptographically to avoid structural patterns
    secrets.SystemRandom().shuffle(pool)
    return ''.join(pool[:length])

def get_toggle_input(prompt_text):
    res = input(prompt_text).strip().lower()
    return res not in ['n', 'no']

def main():
    print("=============================================")
    print("    🛡️  CRYPTOGRAPHIC PASSWORD ENGINE 3.0    ")
    print("=============================================")
    
    while True:
        try:
            user_input = input("\nEnter password length (6 - 128) or 'exit': ").strip()
            
            if user_input.lower() == 'exit':
                print("Exiting program. Secure your credentials! Goodbye.")
                break
                
            length = int(user_input)
            
            if length < 6 or length > 128:
                print("❌ Out of Bounds: Length must be between 6 and 128.")
                continue
            
            # Feature: Bulk option check
            count_input = input("How many passwords do you want to generate? [default: 1]: ").strip()
            count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 1
            
            print("\n--- Customize Password Character Sets ---")
            use_lower = get_toggle_input("Include Lowercase letters? (y/n) [default: y]: ")
            use_upper = get_toggle_input("Include Uppercase letters? (y/n) [default: y]: ")
            use_digits = get_toggle_input("Include Numbers (0-9)?     (y/n) [default: y]: ")
            use_special = get_toggle_input("Include Special Symbols?   (y/n) [default: y]: ")
            
            passwords = []
            strengths = []
            
            # Bulk Generation Loop
            for _ in range(count):
                pwd = generate_custom_password(length, use_upper, use_lower, use_digits, use_special)
                passwords.append(pwd)
                strengths.append(check_strength(pwd))
            
            # UI Outputs
            print("\n---------------------------------------------")
            print("🔑 Generated Password Options:")
            for i, (pwd, strg) in enumerate(zip(passwords, strengths), 1):
                print(f"  {i}. {pwd}  ({strg})")
            print("---------------------------------------------")
            
            # Action Handlers (Copies the first generated option by default)
            copy_to_clipboard(passwords[0])
            log_password_metadata(count, strengths[0])
            
            print("📋 Status             : Option 1 auto-copied to clipboard!")
            print("📝 Session Log        : Metadata appended to 'passwords_log.txt'")
            print("---------------------------------------------")
            
            another = input("\nGenerate another batch? (y/n): ").strip().lower()
            if another not in ['y', 'yes', '']:
                print("Goodbye!")
                break
                
        except ValueError:
            print("❌ Invalid entry! Please enter valid numbers.")

if __name__ == "__main__":
    main()
    
