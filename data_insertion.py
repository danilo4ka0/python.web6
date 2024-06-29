import psycopg2
from faker import Faker
import random

def insert_data():
    try:
        conn = psycopg2.connect(
            dbname="your_db_name", user="your_user", password="your_password", host="localhost"
        )
        cur = conn.cursor()
        fake = Faker()

        # Insert groups
        group_names = ["Group A", "Group B", "Group C"]
        group_ids = []
        for name in group_names:
            cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id;", (name,))
            group_ids.append(cur.fetchone()[0])

        # Insert teachers
        teacher_ids = []
        for _ in range(3):
            first_name = fake.first_name()
            last_name = fake.last_name()
            cur.execute(
                "INSERT INTO teachers (first_name, last_name) VALUES (%s, %s) RETURNING id;",
                (first_name, last_name),
            )
            teacher_ids.append(cur.fetchone()[0])

        # Insert subjects
        subjects = ["Math", "Science", "History", "Art", "Physics", "Chemistry", "Biology", "Literature"]
        subject_ids = []
        for name in subjects:
            teacher_id = random.choice(teacher_ids)
            cur.execute(
                "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id;",
                (name, teacher_id),
            )
            subject_ids.append(cur.fetchone()[0])

        # Insert students
        student_ids = []
        for _ in range(30):
            first_name = fake.first_name()
            last_name = fake.last_name()
            group_id = random.choice(group_ids)
            cur.execute(
                "INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s) RETURNING id;",
                (first_name, last_name, group_id),
            )
            student_ids.append(cur.fetchone()[0])

        # Insert grades
        for student_id in student_ids:
            for _ in range(20):
                subject_id = random.choice(subject_ids)
                grade = random.randint(60, 100)
                date = fake.date_between(start_date='-4y', end_date='today')
                cur.execute(
                    "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s);",
                    (student_id, subject_id, grade, date),
                )

        conn.commit()
        cur.close()
        conn.close()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    insert_data()
