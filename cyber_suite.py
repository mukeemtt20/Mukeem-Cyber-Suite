import os
import shutil
import re
from datetime import datetime

# ========== COLOR SYSTEM ==========
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# ========== LOGGER ==========
def log_event(message):
    with open("cyber_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

# ========== LINK SCANNER ==========
def link_scanner():
    print(f"\n{Colors.CYAN}=== Advanced Link Scanner ==={Colors.RESET}")
    url = input("Enter URL to scan: ")

    warnings = []
    risk_score = 0

    if not url.startswith("https://"):
        warnings.append("Not using HTTPS")
        risk_score += 2

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        warnings.append("IP address used instead of domain")
        risk_score += 3

    suspicious_words = ["login", "verify", "secure", "update", "bank", "free", "bonus"]

    for word in suspicious_words:
        if word in url.lower():
            warnings.append(f"Suspicious keyword: {word}")
            risk_score += 1

    if len(url) > 75:
        warnings.append("URL unusually long")
        risk_score += 1

    if "@" in url:
        warnings.append("@ symbol detected (redirect trick)")
        risk_score += 2

    print("\nScan Result:")

    if warnings:
        for w in warnings:
            print(f"{Colors.YELLOW}⚠ {w}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}✅ No obvious red flags{Colors.RESET}")

    print(f"\nRisk Score: {risk_score}")

    if risk_score >= 5:
        print(f"{Colors.RED}🔴 High Risk{Colors.RESET}")
    elif risk_score >= 3:
        print(f"{Colors.YELLOW}🟠 Medium Risk{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}🟢 Low Risk{Colors.RESET}")

    log_event(f"Scanned URL: {url} | Risk Score: {risk_score}")

# ========== FILE ORGANIZER ==========
def file_organizer():
    print(f"\n{Colors.CYAN}=== Smart File Organizer ==={Colors.RESET}")

    folder_path = input("Enter folder path (Enter = current): ")
    if folder_path == "":
        folder_path = os.getcwd()

    file_types = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "PDFs": [".pdf"],
        "Python": [".py"],
        "Text": [".txt"],
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in file_types.items():
                for ext in extensions:
                    if filename.lower().endswith(ext):
                        new_folder = os.path.join(folder_path, folder)

                        if not os.path.exists(new_folder):
                            os.makedirs(new_folder)

                        shutil.move(file_path, os.path.join(new_folder, filename))
                        print(f"{Colors.GREEN}Moved {filename} → {folder}{Colors.RESET}")
                        moved = True
                        break

                if moved:
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"{Colors.YELLOW}Moved {filename} → Others{Colors.RESET}")

    print(f"{Colors.GREEN}Organization Complete ✅{Colors.RESET}")
    log_event(f"Organized folder: {folder_path}")

# ========== PASSWORD CHECKER ==========
def password_checker():
    print(f"\n{Colors.CYAN}=== Password Strength Checker ==={Colors.RESET}")
    password = input("Enter password: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print(f"\nStrength Score: {score}/5")

    if score <= 2:
        print(f"{Colors.RED}Weak Password 🔴{Colors.RESET}")
    elif score == 3 or score == 4:
        print(f"{Colors.YELLOW}Moderate Password 🟠{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}Strong Password 🟢{Colors.RESET}")

    log_event("Password checked")

# ========== MAIN MENU ==========
def main():
    while True:
        print(f"""
{Colors.CYAN}=== Mukeem Cyber Suite ==={Colors.RESET}
1 → Advanced Link Scanner
2 → File Organizer
3 → Password Strength Checker
4 → View Log File
exit → Quit
""")

        choice = input("Choose option: ")

        if choice == "1":
            link_scanner()
        elif choice == "2":
            file_organizer()
        elif choice == "3":
            password_checker()
        elif choice == "4":
            if os.path.exists("cyber_log.txt"):
                with open("cyber_log.txt", "r") as log:
                    print("\n=== Log File ===")
                    print(log.read())
            else:
                print("No logs yet.")
        elif choice.lower() == "exit":
            print("Exiting Cyber Suite...")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
