# Pre-check Script - Router Automation
# Ye commands.txt se commands padh ke router pe chalayega

def main():
    print("=== Router Pre-Check Shuru ===")
    
    # commands.txt se list padhna
    try:
        with open("commands.txt", "r") as f:
            commands = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("commands.txt nahi mili! Pehle usko upload karo.")
        return

    print(f"Total Commands Mili: {len(commands)}")
    print("---")
    for cmd in commands:
        print(f"Chalegi: {cmd}")
    
    print("---")
    print("=== Pre-Check Khatam ===")
    print("Ab isko router se jodna baaki hai - agle step me karenge")

if __name__ == "__main__":
    main()