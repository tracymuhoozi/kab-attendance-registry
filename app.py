"""
app.py — KAB Attendance Registry
Main entry point.
"""

from reporting import (
    menu_flag_absences,
    menu_attendance_rate,
    menu_chronic_report,
    menu_full_report,
)

def print_menu():
    print("""
  ── ABSENCE & REPORTING ────────────
  1. Flag absences for today
  2. View student attendance rate
  3. Chronic absence report
  4. Full attendance report
  0. Exit
""")

def main():
    print("=== KAB ATTENDANCE REGISTRY ===")
    while True:
        print_menu()
        choice = input("Enter option: ").strip()
        if choice == "1":
            menu_flag_absences()
        elif choice == "2":
            menu_attendance_rate()
        elif choice == "3":
            menu_chronic_report()
        elif choice == "4":
            menu_full_report()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()