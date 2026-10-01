# Log Analyzer

A beginner Python project that analyzes log files and finds specific actions performed by specific users.

## What It Does

The program reads a `logs.txt` file and lets you search for:

- A specific action (for example `LOGIN`, `LOGOUT`, `FAILED LOGIN`, or `PASSWORD_CHANGE`)
- A specific username
- Or all users if `no_user` is entered

It then displays the matching log entries and counts how many matches were found.

## Features

- Reads log files using Python
- Searches for specific actions
- Searches for specific users
- Can search for an action without specifying a user
- Counts matching entries
- Displays the date, action, and user of each match
- Handles user input with `.upper()`, `.lower()`, and `.strip()`

## What I Learned

While making this project, I practiced:

- `open()` and reading files
- `for` loops
- `if`, `elif`, and `else`
- `continue`
- `.split()`
- `.upper()`
- `.lower()`
- `.strip()`
- Lists and list indexing
- User input
- Counting results with variables
- Working with structured log data

## Files

```text
log analyzer.py
logs.txt
```

## How to Run

Make sure Python is installed, then run:

```bash
python "log analyzer.py"
```
Also make sure you run this in the folder the logs.txt and log analyzer.py is in otherwise it cant find the txt or py

to run it in the folder is in you first have to know where you downloaded it i will show a example to go to the the downloads folder if its in there

```bash
Cd C:\Users\User\Downloads
```

The program will ask you for:

1. The action you want to search for
2. The username you want to search for

If you want to search for the action regardless of the user, enter:

```text
no_user
```

## Important

This is a learning project created to practice Python and basic log analysis.

Only analyze log files that you own or have permission to access.

## Project Status

**Completed**

This project is part of my journey learning Python and cybersecurity.
