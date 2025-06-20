import pandas as pd
df = pd.read_csv('SIS.csv')
import csv

class StudentClassifier:
    def __init__(self, filename):
        self.filename = filename
        self.pirates = []
        self.yankees = []
        self.bulls = []
        self.invalid = []

    def classify_students(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        age = int(row['Age'])  # Make sure your CSV has a column named 'age'
                        if 14 < age < 18:
                            self.pirates.append(row)
                        elif 18 < age < 22:
                            self.yankees.append(row)
                        elif 22 < age < 25:
                            self.bulls.append(row)
                        elif age > 25:
                            self.invalid.append(row)
                    except ValueError:
                        print(f"Invalid age value for row: {row}")
        except FileNotFoundError:
            print("CSV file not found.")

    def save_and_display(self):
        self._save_to_csv("The_Pirates.csv", self.pirates, "The Pirates")
        self._save_to_csv("The_Yankees.csv", self.yankees, "The Yankees")
        self._save_to_csv("The_Bulls.csv", self.bulls, "The Bulls")
        if self.invalid:
            self._handle_invalid()

    def _save_to_csv(self, filename, data, group_name):
        if data:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"{group_name}:\n", data)

    def _handle_invalid(self):
        print("\nEncapsulated Request: Student age is too high. Use getter to retrieve error.")
        print("Error: Invalid student age > 25")

# === RUN CODE ===
classifier = StudentClassifier("SIS.csv")
classifier.classify_students()
classifier.save_and_display()
