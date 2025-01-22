"""Homework #29. Dockerize everything."""

# Take the HW from SQL Alchemy (Lesson 22) and run via docker PostgreSQL

import csv
import secrets

import db_models
from db_engine import Base, DatabaseEngine


class DatabaseOperations:
    """Class to handle database operations."""

    def __init__(self):
        """Initialize the database engine and session."""
        db_engine = DatabaseEngine()
        self.engine, self.session = db_engine.engine, db_engine.session

    def init_db(self):
        """Create the tables in the database."""
        Base.metadata.create_all(bind=self.engine)

    def load_data_from_csv(self, student_file, course_file):
        """Load data from CSV files and seed the database.

        Args:
            student_file (str): Path to the CSV file containing student data.
            course_file (str): Path to the CSV file containing course data.
        """
        # Load students
        with open(student_file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_student(row['first_name'],
                                 row['last_name'], row['email'])

        # Load courses
        with open(course_file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_course(row['name'])

    def seed_db(self, student_file, course_file):
        """Seed database with students, courses, and enrollments from CSV.

        Args:
            student_file (str): Path to the CSV file containing student data.
            course_file (str): Path to the CSV file containing course data.
        """
        # Load data from CSV
        self.load_data_from_csv(student_file, course_file)

        # Enroll students in courses
        students = self.session.query(db_models.Student).all()
        courses = self.session.query(db_models.Course).all()
        for student in students:
            # Randomly decide how many courses the student will be enrolled in.
            num_courses = secrets.randbelow(5) + 1
            selected_courses = set()

            # Randomly select courses for the student
            while len(selected_courses) < num_courses:
                course = secrets.choice(courses)
                selected_courses.add(course)

            # Enroll student in the selected courses
            for course in selected_courses:
                self.enroll_student(student.email, course.name)

    def add_student(self, first_name, last_name, email):
        """Add a new student to the database.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            email (str): Email address of the student.
        """
        student = db_models.Student(first_name=first_name,
                                    last_name=last_name, email=email)
        self.session.add(student)
        self.session.commit()
        print(f'Student {first_name} {last_name} added to the database.')

    def add_course(self, name):
        """Add a course to the database.

        Args:
            name (str): Name of the course.
        """
        course = db_models.Course(name=name)
        self.session.add(course)
        self.session.commit()
        print(f'Course {name} added to the database.')

    def enroll_student(self, student_email, course_name):
        """Enroll a student in a specific course.

        Args:
            student_email (str): Email of the student to enroll.
            course_name (str): Name of the course to enroll the student in.
        """
        student = self.session.query(db_models.Student).filter_by(
            email=student_email).first()
        course = self.session.query(db_models.Course).filter_by(
            name=course_name).first()

        if student and course:
            student.courses.append(course)
            self.session.commit()
            print(f'Student {student.first_name} '
                  f'{student.last_name} enrolled in {course.name}.')
        else:
            print('Error: Student or Course not found.')

    def students_in_course(self, course_name):
        """Get all students enrolled in a specific course.

        Args:
            course_name (str): Name of the course to check for students.
        """
        course = self.session.query(db_models.Course).filter_by(
            name=course_name).first()
        if course:
            students = course.students
            print(f'Students enrolled in {course.name}:')
            for student in students:
                print(f'{student.first_name} {student.last_name}')
        else:
            print('Course not found.')

    def courses_for_student(self, student_email):
        """Get all courses a specific student is enrolled in.

        Args:
            student_email (str): Email of the student to check for courses.

        """
        student = self.session.query(db_models.Student).filter_by(
            email=student_email).first()
        if student:
            courses = student.courses
            print(f'Courses for student '
                  f'{student.first_name} {student.last_name}:')
            for course in courses:
                print(course.name)
        else:
            print('Student not found.')

    def update_student_email(self, student_email, new_email):
        """Update a student's email.

        Args:
            student_email (str): Current email of the student.
            new_email (str): New email for the student.
        """
        student = self.session.query(db_models.Student).filter_by(
            email=student_email).first()
        if student:
            student.email = new_email
            self.session.commit()
            print(f'Student email updated to {new_email}.')
        else:
            print('Student not found.')

    def delete_student(self, student_email):
        """Delete a student from the database.

        Args:
            student_email (str): Email of the student to delete.
        """
        student = self.session.query(db_models.Student).filter_by(
            email=student_email).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f'Student {student.first_name} '
                  f'{student.last_name} deleted from the database.')
        else:
            print('Student not found.')


# Example of using the class
if __name__ == '__main__':
    db_ops = DatabaseOperations()
    db_ops.init_db()  # Initialize database (create tables)

    # Seed the database with data from CSV
    db_ops.seed_db('students.csv', 'courses.csv')

    print('=' * 50)
    # Get all students enrolled to course
    db_ops.students_in_course('Computer Science')
    print('=' * 50)
    # Get all courses student is enrolled in
    db_ops.courses_for_student('johnny.bravo@smail.com')
    print('=' * 50)
    # Change student email.
    db_ops.update_student_email(
        'quincy.carter@smail.com', 'qcarter@smail.com')
    print('=' * 50)
    # Delete student from DB and verify student is deleted.
    db_ops.delete_student('john.doe@smail.com')
    db_ops.courses_for_student('john.doe@smail.com')
