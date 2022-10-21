# You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
# Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

# Sample Input:

# student_course_pairs_1 = [
#   ["58", "Software Design"],
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
# ]

# Sample Output (pseudocode, in any order):

# find_pairs(student_course_pairs_1) =>
# {
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
#   [17, 94]: []
#   [17, 25]: []
# }

# Additional test cases:

# Sample Input:

# student_course_pairs_2 = [
#   ["42", "Software Design"],
#   ["0", "Advanced Mechanics"],
#   ["9", "Art History"],
# ]

# Sample output:

# find_pairs(student_course_pairs_2) =>
# {
#   [0, 42]: []
#   [0, 9]: []
#   [9, 42]: []
# }

import collections


class Solution:
    def find_pairs(self, records):
        course_student = collections.defaultdict(list)
        students = set()

        for record in records:
            course_student[record[1]] += [record[0]]
            students.add(record[0])

        shared_courses = {}
        students = list(students)
        for index, s1 in enumerate(students):
            for s2 in students[index + 1:]:
                shared_courses[str([s1, s2])] = []

        for cour, stu in course_student.items():
            for index, s1 in enumerate(stu):
                for s2 in stu[index + 1:]:
                    if str([s1, s2]) in shared_courses:
                        shared_courses[str([s1, s2])] += [cour]
                    else:
                        shared_courses[str([s2, s1])] += [cour]

        return shared_courses


sol = Solution()
student_course_pairs_1 = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
]
print(sol.find_pairs(student_course_pairs_1))

student_course_pairs_2 = [
    ["42", "Software Design"],
    ["0", "Advanced Mechanics"],
    ["9", "Art History"],
]

print(sol.find_pairs(student_course_pairs_2))
