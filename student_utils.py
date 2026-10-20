# student_utils.py
def parse_student(line):
    parts = line.strip().split(',')
    if len(parts) != 2:
        raise ValueError("字段数量不正确（应为2个）")
    name, score_str = parts
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError("成绩不是有效整数")
    if not (0 <= score <= 100):
        raise ValueError("成绩不在0~100范围内")
    return {"name": name, "score": score}