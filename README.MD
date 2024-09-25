# Habit Tracker CLI

A command-line interface (CLI) application for tracking user habits using Python, SQLAlchemy, and Alembic for database management.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)

## Features

- Add and manage users
- Create, edit, and delete habits
- Track completion of habits
- View completion logs and calculate consistency

## Technologies

- Python
- SQLAlchemy
- Alembic
- Click

## Installation

2. Set up a virtual environment:
 python -m venv venv

3. Activate the virtual environment:
 On Windows:
 venv\Scripts\activate

 On macOS/Linux:
 source venv/bin/activate

4. Install dependencies:
 pip install pipenv
 pipenv install

5. Initialize the database:
 alembic upgrade head

## Usage
Run the application using:
 python app.py

## Commands
Add a User:
 python app.py add-user --name "Savio Sentamu" --email "Savio@example.com"

List All Users:
 python app.py list-all-users

Add a Habit:
 python app.py add-habit --name "Exercise" --frequency "daily" <user_id> (you will see the user id when you List all the Users)

List Habits for a User:
 python app.py list-habits <user_id> (you will see the user id when you List all the Users)

Complete a Habit:
 python app.py complete-habit <habit_id> (you will see the habit id when you List all the Users)

View Completion Logs for a Habit:
 python app.py view-logs <habit_id> (you will see the habit id when you List all the Users)

Delete a Habit:
 python app.py delete-habit <habit_id> (you will see the habit id when you List all the Users)

Edit a Habit:
 python app.py edit-habit <habit_id> --name "Running" --frequency "weekly"







