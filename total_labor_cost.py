def operator_hourly_rate_includes_overtime():

    employee_hourly = float(input("What is the hourly rate of the operator for this job? "))
    fringe_rate = 1.38
    pension_cost = 12
    employee_base_cost = float(employee_hourly * fringe_rate + pension_cost)

    job_hours = int(input("How many hours do you expect this job to take? "))
    hours_already_worked = float(input("How many hours has this operator already worked today? "))

    total_hours_worked = job_hours + hours_already_worked

    time_and_half = 0
    double_time = 0

    if total_hours_worked <= 8:
        straight_time = total_hours_worked * employee_base_cost
    elif total_hours_worked <= 10:
        straight_time = (8 * employee_base_cost)
        time_and_half = (total_hours_worked - 8) * employee_base_cost
    else:
        straight_time = (8 * employee_base_cost)
        time_and_half = (2 * employee_base_cost) * 1.5
        double_time = ((total_hours_worked - 10) * employee_base_cost) * 2.0

    operator_overhead = float(straight_time + time_and_half + double_time)
    return operator_overhead

def laborer_cost():
    total_laborer_cost = 0
    fringe_rate = 1.38
    pension_cost = 12
    laborers_needed = int(input("How many laborers will you need for this job? "))
    for i in range(laborers_needed):
        hourly_wage = float(input(f"What is the hourly wage of laborer {i + 1}? "))
        expected_hours = float(input(f"How many hours is laborer {i + 1} expected to work? "))

        # Calculate laborer cost
        base_cost = float((hourly_wage * fringe_rate) + pension_cost)
        total_laborer_cost += float(base_cost * expected_hours)

    return total_laborer_cost