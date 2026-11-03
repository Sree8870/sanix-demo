
import json, os
from datetime import date, timedelta

FILE = "habits.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def streak(dates):
    days = set(dates)
    day = date.today()
    if str(day) not in days:
        day -= timedelta(days=1)
    count = 0
    while str(day) in days:
        count += 1
        day -= timedelta(days=1)
    return count

def main():
    data = load()
    while True:
        print("\n1.Add habit  2.Check in today  3.View streaks  4.Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Habit name: ").strip()
            data.setdefault(name, [])
        elif choice == "2":
            name = input("Habit name: ").strip()
            if name in data:
                today = str(date.today())
                if today not in data[name]:
                    data[name].append(today)
                print("Done!")
            else:
                print("Habit not found.")
        elif choice == "3":
            for name, dates in data.items():
                print(f"{name}: {streak(dates)} day streak")
        elif choice == "4":
            break
        save(data)

main()