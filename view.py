def view_applications(applications):
    if len(applications) == 0:
        print("No applications found.")
        return

    for app in applications:
        print(f"{app['company']} - {app['position']}")