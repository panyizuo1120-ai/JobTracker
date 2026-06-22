# JobTracker

A simple Python application for tracking job applications.

## Features

* Add job applications
* View saved applications
* Store application data in JSON format
* Simple command-line interface

## Project Structure

```text
JobTracker/
│
├── main.py
├── add.py
├── view.py
├── applications.json
└── README.md
```

## How to Run

Make sure Python is installed.

Run the application:

```bash
python main.py
```

## Menu

```text
1. Add Application
2. View Applications
3. Exit
```

## Example

Add a new application:

```text
Company: MongoDB
Position: Software Engineer Intern
```

Saved in JSON format:

```json
[
    {
        "company": "Company Name",
        "position": "Software Engineer Intern"
    }
]
```

## Future Improvements

* Delete applications
* Update application status
* Search applications
* SQLite database support
* GUI interface

## Author

Yizuo Pan
