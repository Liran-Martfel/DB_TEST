from db import run_query_select, run_update_query

run_update_query("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL)""")

run_update_query("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 90))
run_update_query("INSERT INTO students (name, grade) VALUES (?, ?)", ("Bob", 82))
run_update_query("INSERT INTO students (name, grade) VALUES (?, ?)", ("Carol", 95))

students = run_query_select("SELECT * FROM students")
for s in students:
    print(s)

run_update_query("UPDATE students SET grade = ? WHERE name = ?", (88, "Bob"))
run_update_query("DELETE FROM students WHERE name = ?", ("Alice",))

students = run_query_select("SELECT * FROM students ORDER BY grade DESC")
for s in students:
    print(s)