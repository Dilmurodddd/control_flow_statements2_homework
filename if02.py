def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<c<b:
        a=a
    if a>b<c:
        a=b
    if a>b>c:
        a=c
    return a
print(main(1,2,3))