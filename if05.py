def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    k = 0
    a=(n%10)
    b=((n%100)//10)
    c=((n%1000)//100)
    d=((n%10000)//1000)
    e=(n//10000)
    if k<=e:
        k=e
    if k<=d:
        k=d
    if k<=c:
        k=c
    if k<=b:
        k=b
    if k<=a:
        k=a
    
    return k
print(main(92845))