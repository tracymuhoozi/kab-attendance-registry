"""
app.py — KAB Attendance Registry
Main entry point.
"""

from roster import (
    menu_register_student,
    menu_log_attendance,
    menu_todays_summary,
    menu_list_students,
)

def print_menu():
    print("""
  ── ROSTER & CHECK-IN ──────────────
  1. Register a new student
  2. Log attendance
  3. Today's check-in summary
  4. List all students
  0. Exit
""")

def main():
    print("=== KAB ATTENDANCE REGISTRY ===")
    while True:
        print_menu()
        choice = input("Enter option: ").strip()
        if choice == "1":
            menu_register_student()
        elif choice == "2":
            menu_log_attendance()
        elif choice == "3":
            menu_todays_summary()
        elif choice == "4":
            menu_list_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()