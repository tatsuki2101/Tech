def calculate_score(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    return grade

score = 85  # 任意のスコア
result = calculate_score(score)
print(f"成績は {result} です")