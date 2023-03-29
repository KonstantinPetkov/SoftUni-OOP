import unittest
from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student("Student1")
        self.student_with_course = Student("Student2", {"math": ["note"]})

    def test_valid_initializing(self):
        self.assertEqual("Student1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Student2", self.student_with_course.name)
        self.assertEqual({"math": ["note"]}, self.student_with_course.courses)

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll("math", ["new note"])
        self.assertEqual("new note", self.student_with_course.courses["math"][1])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_to_non_existing_courses_without_third_param(self):
        result = self.student.enroll("math", ["notes"])

        self.assertEqual(self.student.courses["math"][0], "notes")
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_to_non_existing_courses_with_third_param(self):
        result = self.student.enroll("math", ["notes"], "Y")
        self.assertEqual(self.student.courses["math"][0], "notes")
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_new_course_without_add_notes(self):
        result = self.student.enroll("math", ["notes"], "C")
        self.assertEqual(len(self.student.courses["math"]), 0)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("math", "add new note")
        self.assertEqual("add new note", self.student_with_course.courses["math"][-1])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "notes")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")
        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

if __name__ == '__main__':
    unittest.main()