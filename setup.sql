DROP TABLE IF EXISTS ingredients
DROP TABLE IF EXISTS recipes
DROP TABLE IF EXISTS employees

CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER,
    unit TEXT,
    recipes_found_in TEXT,
    UNIQUE(name),
)

CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    steps TEXT,
    ingredient_list TEXT,
    employee_id INTEGER,
    UNIQUE(name),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
)

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    recipes_managed TEXT
    UNIQUE(name)
)