# Online Learning Management System Database
- Database practice for LS181 interview

## Scenario

- Design a database for an online learning platform that supports courses, students, instructors, assignments, and grades. How would you implement the various relationships between these entities? Discuss how you would use constraints to enforce business rules (e.g. a student can't be enrolled in the same course twice). How does your design support normalization practices?

### Design

- Identify our entities:
  - Student
  - Instructor
  - Course
  - Assignment
  - Grade

- Identify our relationships:
  - Students have at least one or many instructors, courses, assignments, and grades
  - Instructors have many students, may have many courses, do not have assignments and do not have grades
  - Courses belong to many students, at least one or many instructors, have many assignments and many grades
  - Assignments belong to one course and only one course
  - Grades belong to one course per student and one assignment per course per student

- Utilizing constraints to enforce business rules
  - Utilize the following constraint to enforce valid relationships
  - `student_id` in `course_grade` must match students enrolled in the course for a grade to exist
~~~SQL
ALTER TABLE Course_Grade
ADD CONSTRAINT fk_valid_enrollment FOREIGN KEY (student_id, CourseId)
REFERENCES Students_Courses (student_id, course_id);
~~~

- Utilize proper `ON DELETE` clauses
  - in `course_grade` use `ON DELETE CASCADE` for student_id and course_id FK since a grade cannot exist without belonging to a course and cannot exist without belonging to a student. Use the same for the foreign keys in assignment_grade
  - in `students_courses` use `ON DELETE CASCADE` - to prevent students from being enrolled in classes that don't exist and vice versa
  - In `course` use `ON DELETE SET NULL` for the `instructor_id` FK because we don't want to delete courses just because an instructor left. This would be our queue that a course needs a new instructor
  - Use `ON DELETE CASCADE` for assignment `course_id` FK since assignments cannot exist without belonging to courses

- Potential trade-offs
  - By using `ON DELETE CASCADE` in multiple places we ensure that there will be no dangling entities if stuff is deleted from our learning management system. However, it would prevent a student from viewing past grades on assignemnts if a course is deleted in a future catalog update. It would be wise to implement an archival feature for our database architecture prior to making such updates so historics can still be viewed.

- Can optimize by adding indexes on foreign keys like `student_id` and `course_id` for faster lookups in the students_courses join table