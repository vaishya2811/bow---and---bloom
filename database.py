import sqlite3


def create_table():
    connection = sqlite3.connect("tasks.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()
def add_task(title):
    connection = sqlite3.connect("tasks.db")

    connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()
    connection.close()
def complete_task(task_id):
    connection = sqlite3.connect("tasks.db")

    connection.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()
def get_tasks():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row

    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return tasks


if __name__ == "__main__":
    create_table()
    print("Bow & Bloom database initialized successfully! 🎀")