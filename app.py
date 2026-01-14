from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Elenco task predefiniti per esercitazione
tasks = [
    # TO DO
    {
        "id": 1,
        "title": "Port Provisioning",
        "description": "ID: CRUISE-103",
        "assigned_to": "Alice",
        "due_date": "2024-07-01",
        "status": "To Do",
        "updates": ["Task created."]
    },
    {
        "id": 2,
        "title": "Gala Dinner Prep",
        "description": "ID: CRUISE-104",
        "assigned_to": "Bob",
        "due_date": "2024-07-03",
        "status": "To Do",
        "updates": ["Task created."]
    },

    # IN PROGRESS
    {
        "id": 3,
        "title": "AC Repair Suite 704",
        "description": "ID: CRUISE-101",
        "assigned_to": "Charlie",
        "due_date": "2024-06-27",
        "status": "In Progress",
        "updates": ["Technician assigned.", "Diagnostics started."]
    },
    {
        "id": 4,
        "title": "Sound Check: Theater",
        "description": "ID: CRUISE-102",
        "assigned_to": "Diana",
        "due_date": "2024-06-29",
        "status": "In Progress",
        "updates": ["Equipment prepared."]
    },

    # DONE
    {
        "id": 5,
        "title": "Bridge Safety Check",
        "description": "ID: CRUISE-099",
        "assigned_to": "Evan",
        "due_date": "2024-06-20",
        "status": "Done",
        "updates": ["Safety checklist completed.", "All clear."]
    },
    {
        "id": 6,
        "title": "Pool Water Quality Test",
        "description": "ID: CRUISE-095",
        "assigned_to": "Fiona",
        "due_date": "2024-06-22",
        "status": "Done",
        "updates": ["Test passed, water quality optimal."]
    }
]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        assigned_to = request.form["assigned_to"]
        due_date = request.form["due_date"]
        task = {
            "id": len(tasks) + 1,
            "title": title,
            "description": description,
            "assigned_to": assigned_to,
            "due_date": due_date,
            "status": "To Do",
            "updates": ["Task created."]
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