def mark_absent():
    data = load_data()

    date = input("Enter date (YYYY-MM-DD): ")

    for student in data:

        # Check whether the student already has an attendance
        # record for this date.
        exists = False

        for record in student["attendance"]:
            if record["date"] == date:
                exists = True
                break

        if not exists:
            student["attendance"].append({
                "date": date,
                "time": "",
                "status": "Absent"
            })

    save_data(data)
    print("Missing students marked as Absent.")


def attendance_rate(student):
    attendance = student["attendance"]

    if len(attendance) == 0:
        return 0

    present_days = 0

    for record in attendance:
        if record["status"] in ["Present", "Late"]:
            present_days += 1

    return (present_days / len(attendance)) * 100


def attendance_report():
    data = load_data()

    print("\n--- Attendance Report ---")

    for student in data:
        rate = attendance_rate(student)

        print(
            f"{student['student_id']} - "
            f"{student['name']} : "
            f"{rate:.2f}%"
        )


def chronic_absence_report():
    data = load_data()

    print("\n--- Chronically Absent Students ---")

    found = False

    for student in data:
        rate = attendance_rate(student)

        if rate < 85:
            print(
                f"{student['student_id']} - "
                f"{student['name']} - "
                f"{rate:.2f}%"
            )
            found = True

    if not found:
        print("No students are below 85%.")


def absence_streak(student):
    records = sorted(
        student["attendance"],
        key=lambda x: x["date"]
    )

    streak = 0
    longest_streak = 0

    for record in records:
        if record["status"] == "Absent":
            streak += 1
            longest_streak = max(longest_streak, streak)
        else:
            streak = 0

    return longest_streak


def absence_patterns():
    data = load_data()

    print("\n--- Absence Patterns ---")

    for student in data:
        streak = absence_streak(student)

        print(
            f"{student['name']} - "
            f"Longest absence streak: {streak} day(s)"
        )