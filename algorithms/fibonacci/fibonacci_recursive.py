# 1. Take the number of terms from the user and store it in a variable.
# 2. Pass the number as an argument to a recursive function named fibonacci.
# 3. Define the base condition as the number to be lesser than or equal to 1.
# 4. Otherwise call the function recursively with the argument as the number
#    minus 1 added to the function called recursively with the argument as the
#    number minus 2.
# 5. Use a for loop and print the returned value which is the fibonacci series.
# 6. Exit.


def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

n = int(input("Enter number of terms: "))

print "Fibonacci sequence: "

for i in range(n):
    print fibonacci(i)


'''

for index in range 0-2:
	print fib(index)

3 is greater than 1, so:
fibonacci(3-1) + (3-2)
			2  +  1	 = 3 (which is the next fib num)
2 is greater than 1, so func runs again		-> 
1 is equal to 1, so func returns 1
(How do we still add zero to the beginning of the sequence?)
-> 



'''

fibonacci(5)