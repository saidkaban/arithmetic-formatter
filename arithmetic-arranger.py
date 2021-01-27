def arithmetic_arranger(problems, show_answer = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_line = "" 
    second_line = ""
    dash_line = ""
    third_line = "" 
    for problem in problems:
        split_problem = problem.split()
        first = split_problem[0]
        sign = split_problem[1]
        second = split_problem[2]
        if sign not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        alignment_length = max(len(first), len(second)) + 2
        first_line = first_line + first.rjust(alignment_length) + "    "
        second_line = second_line + sign + second.rjust(alignment_length - 1) + "    "
        dash_line = dash_line + ((max(len(first), len(second)) + 2) * "-").rjust(alignment_length) + "    "
        sum_value = str(int(first) + int(second))
        third_line = third_line + sum_value.rjust(alignment_length) + "    "
    arranged_problems = first_line + "\n" + second_line + "\n" + dash_line + "\n" + third_line * show_answer
    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))