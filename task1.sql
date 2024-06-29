-- students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    group_id INTEGER
);

-- groups table
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

-- teachers table
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- subjects table
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    teacher_id INTEGER REFERENCES teachers(id)
);

-- grades table
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    grade INTEGER,
    date DATE
);
