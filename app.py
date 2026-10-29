from flask import Flask, render_template, request, redirect, url_for
from database import add_task, get_tasks, complete_task
app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/complete-task/<int:task_id>", methods=["POST"])
def complete_task_route(task_id):
    complete_task(task_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)