# ==========================================
# ADVANCED TO-DO LIST APPLICATION
# DecodeLabs Project 1
# Developed by: Md. Ahsanur Rahaman
# ==========================================

tasks = []
task_id = 1


def add_task():
    global task_id

    task_name = input("\nEnter Task Name: ").strip()

    if not task_name:
        print("❌ Task cannot be empty!")
        return

    task = {
        "id": task_id,
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)
    task_id += 1

    print("✅ Task added successfully!")


def view_tasks():
    print("\n" + "=" * 60)
    print("                    TASK LIST")
    print("=" * 60)

    if not tasks:
        print("No tasks available.")
        return

    print(f"{'ID':<5}{'Task Name':<35}{'Status'}")
    print("-" * 60)

    for task in tasks:
        print(
            f"{task['id']:<5}"
            f"{task['name']:<35}"
            f"{task['status']}"
        )


def complete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id_input = int(
            input("\nEnter Task ID to mark as completed: ")
        )

        for task in tasks:
            if task["id"] == task_id_input:
                task["status"] = "Completed"
                print("✅ Task marked as completed!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_id_input = int(
            input("\nEnter Task ID to delete: ")
        )

        for task in tasks:
            if task["id"] == task_id_input:
                tasks.remove(task)
                print("✅ Task deleted successfully!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid number.")


def show_summary():
    total = len(tasks)
    completed = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )
    pending = total - completed

    print("\n" + "=" * 40)
    print("TASK SUMMARY")
    print("=" * 40)
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")


def display_menu():
    print("\n" + "=" * 60)
    print("           TO-DO LIST MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Show Summary")
    print("6. Exit")
    print("=" * 60)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("\n🎉 Thank you for using the To-Do List App!")
            print("Good Luck with your DecodeLabs Project!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-6.")


# Program Entry Point
if __name__ == "__main__":
    main()