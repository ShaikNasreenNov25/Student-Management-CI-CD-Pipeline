
import pytest

from student_manager import StudentManager


# Test 1: Add student
def test_add_student():

    manager = StudentManager()

    result = manager.add_student("101", "Nasreen", 90)

    assert result == "Student added successfully"


# Test 2: View student
def test_view_student():

    manager = StudentManager()

    manager.add_student("102", "Ayesha", 85)

    student = manager.view_student("102")

    assert student["name"] == "Ayesha"
    assert student["marks"] == 85


# Test 3: Update marks
def test_update_marks():

    manager = StudentManager()

    manager.add_student("103", "Sara", 70)

    result = manager.update_marks("103", 95)

    assert result == "Marks updated successfully"
    assert manager.view_student("103")["marks"] == 95


# Test 4: Delete student
def test_delete_student():

    manager = StudentManager()

    manager.add_student("104", "Riya", 80)

    result = manager.delete_student("104")

    assert result == "Student deleted successfully"

    with pytest.raises(ValueError):
        manager.view_student("104")


# Test 5: Calculate average
def test_calculate_average():

    manager = StudentManager()

    manager.add_student("105", "John", 80)
    manager.add_student("106", "David", 100)

    result = manager.calculate_average()

    assert result == 90


# Test 6: Invalid marks
def test_invalid_marks():

    manager = StudentManager()

    with pytest.raises(ValueError):
        manager.add_student("107", "Sam", 120)
