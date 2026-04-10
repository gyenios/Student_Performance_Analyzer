def extract_scores(scores_dict):
    return list(scores_dict.values())


def compute_total(scores):
    return sum(scores)


def compute_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def assign_grade(average_score):
    if average_score >= 80:
        return 'A'
    elif average_score >= 70:
        return 'B'
    elif average_score >= 60:
        return 'C'
    elif average_score >= 50:
        return 'D'
    else:
        return 'F'


def compute_student_metrics(student):
    scores_dict = student["Scores"]
    scores = extract_scores(scores_dict)

    total_score = compute_total(scores)
    average_score = compute_average(scores)
    grade = assign_grade(average_score)

    return {
        **student,
        "total": total_score,
        "average": average_score,
        "grade": grade
    }


def compute_all_students(data):
    results = {}

    for student_id, student in data.items():
        results[student_id] = compute_student_metrics(student)

    return results