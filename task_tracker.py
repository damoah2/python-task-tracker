"""
Task Tracker

Author: Dennis Amoah
"""

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    # Load tasks from the JSON file, or return an empty list if file doesn't exist.
    if not os.path.isfile(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # If something is wrong with the file, start fresh
        print("⚠️ Could not read tasks.json, starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📭 No tasks yet. You're free! 😄")
        return

    print("\n📝 Your Tasks:")
    print("--------------")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        created = task.get("created_at", "N/A")
        print(f"{idx}. {status} {task['title']} (created: {created})")
        if task.get("description"):
            print(f"   ↳ {task['description']}")
    print()


def add_task(tasks):
    """Add a new task."""
    print("\n➕ Add a New Task")
    print("-----------------")
    title = input("Task title: ").strip()
    if not title:
        print("⚠️ Task title cannot be empty.")
        return

    description = input("Optional description (press Enter to skip): ").strip()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    task = {
        "title": title,
        "description": description,
        "done": False,
        "created_at": created_at,
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✔️ Task added!")


def mark_task_done(tasks):
    """Mark a task as done."""
    if not tasks:
        print("\n⚠️ No tasks to update.")
        return

    show_tasks(tasks)
    choice = input("Enter the task number to mark as done: ").strip()

    if not choice.isdigit():
        print("⚠️ Please enter a valid number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("⚠️ Invalid task number.")
        return

    if tasks[index]["done"]:
        print("ℹ️ That task is already marked as done.")
    else:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as done!")


def delete_task(tasks):
    """Delete a task by its number."""
    if not tasks:
        print("\n⚠️ No tasks to delete.")
        return

    show_tasks(tasks)
    choice = input("Enter the task number to delete: ").strip()

    if not choice.isdigit():
        print("⚠️ Please enter a valid number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("⚠️ Invalid task number.")
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️ Deleted task: {removed['title']}")


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    tasks = load_tasks()

    while True:
        print("📋 Task Tracker")
        print("----------------")
        print("1) View tasks")
        print("2) Add task")
        print("3) Mark task as done")
        print("4) Delete task")
        print("5) Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1–5.")

        if choice != "5":
            input("\nPress Enter to continue...")
            clear_screen()


if __name__ == "__main__":
    main()
