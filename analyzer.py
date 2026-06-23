import pandas as pd

# Read CSV file
data = pd.read_csv("data.csv")

# Calculate Total Marks
data["Total"] = data["Maths"] + data["Physics"] + data["Chemistry"]

# Calculate Percentage
data["Percentage"] = round((data["Total"] / 300) * 100, 2)

# Grade Function
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Assign Grades
data["Grade"] = data["Percentage"].apply(get_grade)

# Pass / Fail Function
def get_result(row):
    if row["Maths"] < 30 or row["Physics"] < 30 or row["Chemistry"] < 30:
        return "FAIL"
    else:
        return "PASS"

# Assign Result
data["Result"] = data.apply(get_result, axis=1)

# Rank Students
data["Rank"] = data["Total"].rank(method="dense", ascending=False).astype(int)

# Find Top Scorer
top_student = data.loc[data["Total"].idxmax()]

# Subject Averages
math_avg = round(data["Maths"].mean(), 2)
physics_avg = round(data["Physics"].mean(), 2)
chem_avg = round(data["Chemistry"].mean(), 2)

# Count Pass and Fail
pass_count = len(data[data["Result"] == "PASS"])
fail_count = len(data[data["Result"] == "FAIL"])

# Sort by Rank
report = data[
    ["Rank", "Name", "Total", "Percentage", "Grade", "Result"]
].sort_values("Rank")

# Display Results
print("\n===== STUDENT RESULT ANALYZER =====")

print("\nTop Scorer:")
print(f"{top_student['Name']} - {top_student['Total']}")

print("\nSubject Averages:")
print(f"Maths: {math_avg}")
print(f"Physics: {physics_avg}")
print(f"Chemistry: {chem_avg}")

print(f"\nPass Students: {pass_count}")
print(f"Fail Students: {fail_count}")

print("\nStudent Report:")
print(report.to_string(index=False))