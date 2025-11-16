print("Enter problem")

problem_string = input()

def calculate(problem):
    try:
        result = eval(problem)
    except Exception as e:
        return f"Error: {e}"
    return result

print(calculate(problem_string))

