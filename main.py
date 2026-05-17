from db import run_query_select, run_update_query
run_update_query("DROP TABLE IF EXISTS employees;")
run_update_query("DROP TABLE IF EXISTS departments;")
run_update_query("""CREATE TABLE IF NOT EXISTS departments (
  id        INTEGER PRIMARY KEY,
  dept_name TEXT    NOT NULL,
  budget    REAL    NOT NULL);""")

run_update_query("INSERT INTO departments (id, dept_name, budget) VALUES (?,?,?)", (1,'Engineering',150000))
run_update_query("INSERT INTO departments (id, dept_name, budget) VALUES (?,?,?)", (2,'Marketing',80000))
run_update_query("INSERT INTO departments (id, dept_name, budget) VALUES (?,?,?)", (3,'Sales',60000))
run_update_query("INSERT INTO departments (id, dept_name, budget) VALUES (?,?,?)", (4,'HR',45000))


run_update_query("""CREATE TABLE IF NOT EXISTS employees (
  id         INTEGER PRIMARY KEY,
  name       TEXT    NOT NULL,
  dept_id    INTEGER,
  salary     REAL    NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES departments(id));""")

run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)", (1,'Dana',1,9000))
run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)", (2,'Omar',2,7200))
run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)",  (3,'Noa',1,6800))
run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)", (4,'Liam',3,5500))
run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)", (5,'Rina',None,6000))
run_update_query("INSERT INTO employees (id, name, dept_id, salary) VALUES (?,?,?,?)", (6,'Kai',2,7000))


employees = run_query_select("SELECT name,dept_name, budget FROM departments INNER JOIN employees ON employees.dept_id = departments.id")
for e in employees:
    print(e)

#question
id_employee = int(input("Enter employee ID: "))
if run_query_select(f'select * from employees where id = ?;',(id_employee,)):
    print("Employee already exists!")
else:
    print("Employee does not exist!")