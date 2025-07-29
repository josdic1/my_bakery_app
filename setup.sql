DROP TABLE IF EXISTS ingredients
DROP TABLE IF EXISTS recipes
DROP TABLE IF EXISTS recipe_ingredients
DROP TABLE IF EXISTS employees


CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    UNIQUE(name)
)

CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    steps TEXT,
    UNIQUE(name)
)

CREATE TABLE IF NOT EXISTS recipe_ingredients (
    id INTEGER PRIMARY KEY,
)

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    UNIQUE(name)
)


