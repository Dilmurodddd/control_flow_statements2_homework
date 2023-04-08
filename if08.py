def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    a=''
    if number==1:
        a="Monday"
    if number==2:
        a="Tuesday"
    if number==3:
        a="Wednesday"
    if number==4:
        a="Thursday"
    if number==5:
        a="Friday"
    if number==6:
        a="Saturday"
    if number==7:
        a="Sunday"
    if number>7:
        a='eror'
    return a
print(main(7))