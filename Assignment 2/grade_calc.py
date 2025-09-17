#CONSTANTS
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2
EXAM_WEIGHT = 0.5



#INPUTS
midterms = input("Enter midterm score: ")
finals = input("Enter final score: ")

assignment1 = input("Enter 1st assignment score: ")
assignment2 = input("Enter 2nd assignment score: ")

quiz1 = input("Enter 1st quiz score: ")
quiz2 = input("Enter 2nd quiz score: ")

#PROCESSING

final_assignement = (float(assignment1) + float(assignment2)) / 2
final_quiz = (float(quiz1) + float(quiz2)) / 2
final_exam = (float(midterms) + float(finals)) / 2

final_score = (final_assignement * ASSIGNMENT_WEIGHT) + (final_quiz * QUIZ_WEIGHT) + (final_exam * EXAM_WEIGHT)

#OUTPUT
print(f" Final Assignment Score: {final_assignement:.2f} ")