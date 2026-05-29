# CS361-task-tracker

A command-line task management application developed for Oregon State University's CS361 Software Engineering course.

#Features

- Add tasks with descriptions, due dates, and priority levels
- View active, completed, and deleted tasks
- Mark tasks as complete
- Edit existing tasks
- Delete tasks with confirmation
- Sort tasks by name, due date, or priority
- Persistent task storage using JSON
- Integration with a Flask-based storage microservice
- Automatic fallback to local JSON storage when the microservice is unavailable

#Technologies Used

- Python
- JSON
- Flask
- Requests

#Running the Application

1. Clone the repository.
2. Install required dependencies.
3. Run the task tracker:

python task_tracker.py

To use the storage microservice, start the Flask service before launching the task tracker.

#Course Information
This project was created as part of CS361: Software Engineering.
