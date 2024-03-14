from flask import Flask, render_template, request, send_file
import json
import datetime

app = Flask(__name__)

# Load tasks
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Add task
@app.route('/add_task', methods=['POST'])
def add_task():
    tasks = load_tasks()
    title = request.form['title']
    description = request.form['description']
    tasks.append({'title': title, 'description': description, 'completed': False, 'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    save_tasks(tasks)
    return 'Task added successfully!'

# Download tasks history
@app.route('/download_history')
def download_history():
    tasks = load_tasks()
    with open('task_history.txt', 'w') as file:
        for task in tasks:
            file.write(f"Title: {task['title']}\n")
            file.write(f"Description: {task['description']}\n")
            file.write(f"Date: {task['date']}\n")
            file.write(f"Status: {'Completed' if task['completed'] else 'Incomplete'}\n\n")
    return send_file('task_history.txt', as_attachment=True)

# Render homepage
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
