from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a list to store tasks
tasks = []

@app.route('/')
def index():
    # Render the homepage with the list of tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Get the task from the form data
    task = request.form.get('task')
    if task:
        # Add the task to the list
        tasks.append(task)
    # Redirect back to the homepage
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Remove the task at the specified index
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    # Redirect back to the homepage
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
