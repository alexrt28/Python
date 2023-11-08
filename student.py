# ----------------------------------------------------------------
# Author:
# Date:
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(s_id, c_roster):
    # ------------------------------------------------------------
    # This function displays all the courses, indicates which ones
    # in which the student is enrolled, and counts the courses a
    # student has registered for. It has two parameters: s_id is the
    # ID of the student; c_roster is the list of class rosters.
    # This function has no return value.
    # -------------------------------------------------------------
    pass  # temporarily avoid empty function definition


def add_course(s_id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: s_id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    pass  # temporarily avoid empty function definition


def drop_course(s_id, c_roster):
    # Ask the user to enter the course they want to drop
    course_to_drop = input("Enter the course you want to drop: ")

    # Check if the course is not offered
    if course_to_drop not in c_roster:
        print("Course not found")
        return

    # Check if the student is not enrolled in that course
    if s_id not in c_roster[course_to_drop]:
        print("You are not enrolled in that course.")
        return

    # Remove the student ID from the course's roster
    c_roster[course_to_drop].remove(s_id)
    print("Course dropped")
