"""
roster.py — Roster & Check-In Module
Student A's responsibility
"""

import json
import os
from datetime import datetime

DATA_FILE = "attendance_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}, "school_days": [], "attendance_records": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def today():
    return datetime.now().strftime("%Y-%m-%d")

def create_student_profile(name, student_id):
    data = load_data()
    if student_id in data["students"]:
        return f"ID {student_id} already exists."
    data["students"][student_id] = {
        "name": name,
        "student_id": student_id,
        "registered_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["attendance_records"][student_id] = {}
    save_data(data)
    return f"Student {name} registered successfully."

def log_attendance(student_id, status):
    data = load_data()
    if student_id not in data["students"]:
        return "Student not found."
    if status not in ("Present", "Late"):
        return "Status must be Present or Late."
    date = today()
    if date not in data["school_days"]:
        data["school_days"].append(date)
    data["attendance_records"].setdefault(student_id, {})[date] = {
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_data(data)
    return f"{data['students'][student_id]['name']} marked {status}."

def get_todays_checkins():
    data = load_data()
    date = today()
    results = []
    for sid, records in data["attendance_records"].items():
        if date in records and records[date]["status"] in ("Present", "Late"):
            results.append({
                "name": data["students"][sid]["name"],
                "status": records[date]["status"]
            })
    return results

def menu_register_student():
    name = input("Full name: ")
    sid = input("Student ID: ")
    print(create_student_profile(name, sid))

def menu_log_attendance():
    sid = input("Student ID: ")
    status = input("Status (Present/Late): ")
    print(log_attendance(sid, status))

def menu_todays_summary():
    checkins = get_todays_checkins()
    if not checkins:
        print("No check-ins today.")
        return
    for c in checkins:
        print(f"  {c['name']} — {c['status']}")

def menu_list_students():
    data = load_data()
    for sid, info in data["students"].items():
        print(f"  {info['name']} ({sid})")