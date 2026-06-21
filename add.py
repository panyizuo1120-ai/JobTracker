def add_application(applications):
    company = input("Company: ")
    position = input("Position: ")

    applications.append({
        "company": company,
        "position": position
    })

    print("Application added!")
