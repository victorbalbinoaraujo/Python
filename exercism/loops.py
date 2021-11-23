def round_scores(student_scores):
    return list(map(round, student_scores))

def count_failed_students(student_scores):
    return len(list(filter(lambda x: x <= 40, student_scores)))

def above_threshold(student_scores, threshold):
    return list(filter(lambda x: x >= threshold, student_scores))

def factor_letter_grades(highest):
    return highest - ((highest - (highest * 0.25)) + 11) + 1

def letter_grades(highest):
    factor = factor_letter_grades(highest)
    return [int(41 + (i * factor)) for i in range(4)]

def student_ranking(student_scores, student_names):
    return [f'{i+1}. {student_names[i]}: {student_scores[i]}' for i in range(len(student_scores))]

def perfect_score(student_info):
    perfect_student = list(filter(lambda x: x[1] == 100, student_info))
    return perfect_student[0] if perfect_student else []


print(perfect_score([["Charles", 10], ["Tony", 100], ["Alex", 10]]))
