from datetime import datetime

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}

def get_median_of_first_week_expenses(expenses):
    all_expenses = []
    
    for time, days in expenses.items():
        for day, categories in days.items():
            year, month = map(int, time.split('-'))
            data = datetime(year, month, int(day))
            week = check_week(data)

            if week == 1:
                for key, values in categories.items():
                    all_expenses.extend(values)

    all_expenses = [value for value in all_expenses if isinstance(value, (int, float))]

    if len(all_expenses) == 0:
        return None

    all_expenses.sort()
    middle = len(all_expenses) // 2

    if len(all_expenses) % 2 == 0:
        result = (all_expenses[middle - 1] + all_expenses[middle]) / 2
    else:
        result = all_expenses[middle]

    return result

def check_week(day):
    day_of_month = day.day
    first_day_of_month = datetime(day.year, day.month, 1).weekday()

    week = (day_of_month + first_day_of_month - 1) // 7 + 1

    return week


print(get_median_of_first_week_expenses(expenses))
