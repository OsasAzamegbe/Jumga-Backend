import re


def validate_email(email):
    regex = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

    return regex.match(email)

def validate_password(password):
    regex = re.compile("^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*/\\():-~`{}[\]])[a-zA-Z0-9!@#$%^&*/\\():-~`{}[\]]{8,100}$")

    return regex.match(password)

class CustomError(Exception):
    pass