def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b<c:
        a=c
    if a<b>c:
        a=b
    if a>b>c:
        a=a
    return a
print(main(1,12,3))