def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b<c:
        a=b
    if b<a<c:
        a=a
    if b<c<a:
        a=c
    return a
print(main(1,2,3))