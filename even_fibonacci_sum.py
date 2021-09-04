#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even_fibonnaci_sum(limit):
    (n1,n2,count,num) = (1,2,2,0)
    while(True):
        num = n1+n2
        (n1,n2) = (n2,num)
        if num>=limit:
            break
        if num%2 == 0:
            count+=num
    return count


if __name__ == "__main__":
    limit = int(input("Enter the limit : "))
    print("Output =",even_fibonnaci_sum(limit))