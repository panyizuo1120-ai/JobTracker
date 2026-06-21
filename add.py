import json

def add_application(applications):
    company = input("Company: ")
    position = input("Position: ")

    applications.append({
        "company": company,
        "position": position
    })

    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)

    print("Application added!")