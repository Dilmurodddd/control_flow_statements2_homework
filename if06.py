def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=(n%10)
    b=((n%100)//10)
    c=((n%1000)//100)
    d=((n%10000)/1000)
    k=0
    if k<=d:
        k=d
    if k<=c:
        k=c
    if k<=b:
        k=b
    if k<=a:
        k=a
    
    

    return str(n).index(str(k))
 
print(main(12345))