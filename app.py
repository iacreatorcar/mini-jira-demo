from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        task = {
    "id": len(tasks) + 1,
    "title": title,
    "description": description,
    "assigned_to": request.form["assigned_to"],
    "due_date": request.form["due_date"],
    "status": "To Do",
    "updates": []
}
        tasks.append(task)
        return redirect(url_for("index"))
    return render_template("add_task.html")

@app.route("/move/<int:task_id>")
def move(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "To Do":
                task["status"] = "In Progress"
            elif task["status"] == "In Progress":
                task["status"] = "Done"
            elif task["status"] == "Done":
                task["status"] = "To Do"
            break
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
