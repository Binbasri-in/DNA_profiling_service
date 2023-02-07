-- Database: dna_str_db


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

