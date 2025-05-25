import json
import os

# Path to your JSON file (adjust if needed)
json_file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

# Load JSON data into a Python dictionary
with open(json_file_path, "r") as f:
    marks = json.load(f)

# Function to get marks for a list of student names
def get_marks_for_students(names):
    return [marks.get(name, None) for name in names]

# Example usage:
if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie"]
    results = get_marks_for_students(students)
    for name, mark in zip(students, results):
        print(f"{name}: {mark}")
