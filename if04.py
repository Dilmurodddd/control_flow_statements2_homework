def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    
    if a>b:
        a=a
    if a<b:
        a=b
    if a==b:
        a=0
    return a
print(main(1,1))