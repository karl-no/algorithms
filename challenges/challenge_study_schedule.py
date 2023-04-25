def study_schedule(permanence_period, target_time):
    number_of_students = 0
    try:
        for permanence in permanence_period:
            if permanence[0] <= target_time <= permanence[1]:
                number_of_students += 1
        return number_of_students
    except TypeError:
        ...
