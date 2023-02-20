-- create Database: dna_str_db
-- create tables: users, dna_str, dna_str_users

-- create database



-- users table for login
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    count INTEGER NOT NULL DEFAULT 0,
    lab_name TEXT NOT NULL,
    lab_address TEXT NOT NULL,
    lab_city TEXT NOT NULL,
    lab_state TEXT NOT NULL,
    lab_zip TEXT NOT NULL,
    lab_phone TEXT NOT NULL,
    lab_email TEXT NOT NULL,
    PRIMARY KEY(id)
);
CREATE UNIQUE INDEX IF NOT EXISTS username ON users (username);

-- dna str counts table 'dna_str'
CREATE TABLE IF NOT EXISTS dna_str (
    id INTEGER,
    owner_name TEXT NOT NULL,
    hashed INTEGER NOT NULL,
    AGATC INTEGER NOT NULL,
    TTTTTTCT INTEGER NOT NULL,
    AATG INTEGER NOT NULL,
    TCTAG INTEGER NOT NULL,
    GATA INTEGER NOT NULL,
    TATC INTEGER NOT NULL,
    GAAA INTEGER NOT NULL,
    TCTG INTEGER NOT NULL,
    PRIMARY KEY(id)
);
CREATE UNIQUE INDEX IF NOT EXISTS hashed ON dna_str (hashed);

-- many to many relationship table
CREATE TABLE IF NOT EXISTS dna_str_users (
    dna_str_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(dna_str_id) REFERENCES dna_str(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO dna_str_users (dna_str_id, user_id) VALUES (2, 2), (3, 2), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2);