import csv

# Зчитування даних з файлу
students = []
with open(r'student.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append({"name": row["name"], "score": int(row["score"])})

# Сортуємо студентів за оцінкою у порядку спадання
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

print("Students sorted by score (highest to lowest):")
for idx, student in enumerate(sorted_students, start=1):
    print(f"{idx}. {student['name']}: {student['score']}")

# Фільтрація: студенти з оцінкою >= 80
high_achievers = [s for s in students if s["score"] >= 80]

print("\nStudents with score >= 80:")
for student in high_achievers:
    print(f"{student['name']}: {student['score']}")
