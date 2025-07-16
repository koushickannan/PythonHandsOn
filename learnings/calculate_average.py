def calculate_average(values):
    if type(values) is not str:
        if "__iter__" in dir(values):
            sum_expr = "+".join(str(v) for v in values)
            avg_expr = f"({sum_expr}) / {len(values)}"
            average = eval(avg_expr)
            return average
        else:
            return None
    return values


items = "[11,23,09,36,55]"

results = calculate_average(items)

print(results)
