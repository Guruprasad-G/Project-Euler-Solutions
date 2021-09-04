
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
def sum_of_multiples(n1,n2,limit):
    return sum(set([ i*n1 for i in range(1,int(limit/n1+1)) if i*n1<limit ]).union(set([ i*n2 for i in range(1,int(limit/n2+1)) if i*n2<limit ])))

if __name__ == "__main__":
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    limit = int(input("Enter the number under which the sum has to be found : "))
    print("Answer =",sum_of_multiples(n1,n2,limit))