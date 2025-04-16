admitted = []
not_admitted = []
def check_admission():
    print(" Admission Checker")

    # candidate info
    name = input("Enter your name: ")
    jamb_score = int(input("Enter your JAMB score: "))
    credits = int(input("How many credit passes do you have (out of 5 key subjects)? "))
    interview = input("Did you pass the interview? (yes/no): ").lower()

    # Check admission requirements
    if jamb_score >= 250 and credits >= 5 and interview == 'yes':
        print(f"Congratulations {name}! You are admitted to Computer Science.")
        admitted.append(name)
    else:
        print(f"Sorry {name}, you did not meet the admission requirements.")
        not_admitted.append(name)

# Run the program
while True:
    check_admission()
    another = input("Check another candidate? (yes/no): ").lower()
    if another != 'yes':
        break
print("Final Admission Lists:")
print("Admitted:", admitted)
print("Not Admitted:", not_admitted)