def get_status(score):
    if score >= 90:
        status = "excellent"
    elif 70 <=  score <= 90:
        status = "good"
    elif 55 <= score <= 70:
        status = "average"
    elif score < 55:
        status = "fail"
    else:
        status = "unknown"
    return status


def is_valid_age(age):
    if isinstance(age, int):
        return 0 < age < 120
    else:
        return False


def get_greeting(hour):
    greeting = ''
    if 5 <= hour <= 12:
        greeting = "Good morning"
    elif 12 <= hour <= 17:
        greeting = "Good afternoon"
    if 17 <= hour <= 21:
        greeting = "Good evening"
    if 21 <= hour <= 5:
        greeting = "Good night"
    return greeting
