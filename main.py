from add import add_application
from view import view_applications

applications = []

while True:

    print("""
================================
      JOB TRACKER SYSTEM
================================

1. Add Application
2. View Applications
3. Exit

================================
""")

    choice = input("Select option: ")

    if choice == "1":
        add_application(applications)

    elif choice == "2":
        view_applications(applications)

    elif choice == "3":
        print("Exit Successfully!")
        break

    else:
        print("Invalid Option!")