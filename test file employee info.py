import employee_info as info

def test_get_employee_by_age_range():
    result = info.get_employees_by_age_range(20,30)
    for item in info.employee_data:
        if int(item["age"]) == result:
            assert (result == info.employee_data)

def test_calculate_average_salary():
    result = info.calculate_average_salary()
    for item in info.employee_data:
        if int(item["salary"]) == result:
            assert(result == info.employee_data)

def test_get_employees_by_dept():
    result = info.get_employees_by_dept("Sales")
    for item in info.employee_data:
        if item["department"] == result:
            assert(result == info.employee_data)