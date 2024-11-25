import math
# we imported the math library to use in for precise and accurate calculations regarding the constants of pi in our function

def calculator():

    print("Assalam u Alaikum")
    print("welcome to your calculator application....")
    print("Select an operation, that you would like to proceed with....0")

    #basic arithmetic operations
    print("1.Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

    # the integer part of the division
    # (gives us the dividend)
    print("5. Floor Division/DIV Function")

    print("6. Remainder/MOD Function")

    # (this will always return a float (reaL/decimal) value)
    print("7. Exponentiation/Power Function")

    print("8. Even or Odd")

    #common reciprocal power funtionas
    print("9. Square Root")
    print("10. Cube Root")

    #common power functions
    print("11. Square")
    print("12. Cube")

    #table printer of the number that the user desires upto n terms
    print("13. Table Printer")

    #reciprocal of a number
    print("14. Reciprocal of a number")

    #factorial of a number
    print("15. Factorial")

    #collatz conjecture pattern
    print("16. Collatz Conjecture Pattern")

    #fibonacci sequence upto n terms
    print("17. Fibonacci nth term")

    # fibonacci sequence pattern recursive function
    print("18. Fibonacci Sequence upto nth term")

    # Degree to Radian and viceversa conversions
    print("19. Degree to Radian")
    print("20. Radian to Degree")

    # Sum of roots of a quadratic equation
    print("21. Sum of Roots of a quadratic equation: ")

    # Product of roots of a quadratic equation
    print("22. Product of Roots of a quadratic equation: ")

    # Sum of roots of a Cubic equation
    print("23. Sum of Roots of a cubic equation: ")

    # Product of roots of a Cubic equation
    print("24. Product of Roots of a cubic equation: ")

    # Sum of roots of a polynomial equation - via application of vieta's formulae
    print("25. Sum of Roots of a polynomial equation: ")

    # Product of roots of a polynomial equation
    print("26. Product of Roots of a polynomial equation: ")

    #differentiation and Integration
    print("27. Differentiation")
    print("28. Transpose Of A Matrix")
    print("Press any other key to exit....")

    option = input()

    if option == 1:
        return basicops('+')
    elif option == 2:
        return basicops('-')
    elif option == 3:
        return basicops('/')
    elif option == 4:
        return basicops('*')
    elif option == 5:
        return basicops('//')
    elif option == 6:
        return basicops('%')
    elif option == 7:
        return basicops('**')
    elif option == 8:
        return evenorodd()
    elif option == 9:
        return squareroot()
    elif option == 10:
        return cuberoot()
    elif option == 11:
        return square()
    elif option == 12:
        return cube()
    elif option == 13:
        # we can either of the functions both will perform the same task
        # return tableprinter()
        return tableprintervalueinput()
    elif option == 14:
        return reciprocal()
    elif option == 15:
        # # we can either of the functions both will perform the same task
        # return r_factorial()
        return factorial()
    elif option == 16:
        return collatzconjecture()
    elif option == 17:
        return fibonacci()
    elif option == 18:
        return r_fibonacci_pattern()
    elif option == 19:
        return degrees_into_radians()
    elif option == 20:
        return radians_into_degrees()
    elif option == 21:
        return s_o_r_q()
    elif option == 22:
        return p_o_r_q()
    elif option == 23:
        return s_o_r_c()
    elif option == 24:
        return p_o_r_c()
    elif option == 25:
        return s_o_r_p_i()
    elif option == 26:
        return p_o_r_p_i()
    elif option == 27:
        return differentiation()
    elif option ==  28:
        return matrixtranspose()
    else:
        print("Invalid Choice was entered......")
        print("Exiting program....")
        return None 
        # utilising the none datatype in python

def basicops(sym):

    n1 = float(input("Please enter the first operand: "))
    n2 = float(input("Please enter your second operand: "))

    if sym == '+':
        return n1 + n2
    elif sym == '-':
        return n1 - n2
    elif sym == '*':
        return n1 * n2
    elif sym == '/':
        if n2 == 0:
            print("Math Error! Division by zero (non-numeric values) is infinity....")
            return
        return n1 / n2
    elif sym == '//':
        if n2 == 0:
            print("Math Error! Division by zero (non-numeric values) is infinity....")
            return
        return n1 // n2
    elif sym == '%':
        return n1 % n2
    elif sym == '**':
        return n1 ** n2

def evenorodd():

    print("Please enter a number to check for if the number is even or odd")
    n1 = input()

    print("Even Number.") if n1 % 2 == 0 else print("Odd Number.")

def squareroot():

     n = input("Kindly enter the the number for which you want to find the square root of: ")
     #input function only returns a string so we need to type cast that value to a valid
     #datatype so that we can perform valid mathematical operations with it

     n = float(n)
     return n ** 0.5


def cuberoot():

    n = input("Kindly enter the the number for which you want to find the cube root of: ")
    n = float(n)
    return n ** 1/3


def square():

    n = input("Kindly enter the the number for which you want to find the square of: ")
    n = float(n)
    return n ** 2

def cube():

    n = input("Kindly enter the the number for which you want to find the square of: ")
    n = float(n)
    return n ** 3

def tableprinter():

    #the value for which we want the table of
    print("Kindly tell us the table you would like to print the table of: ")
    num = float(input())

    #the starting index of the table that will be printed
    print("Kindly tell the starting term of your table: ")
    s_i = float(input())

    #alternative code we can use, if the user only knows and wants the specific number of terms of be printed out from the starting index
    #andf if the user does not want to himself calculate the ending index for the table that is to be printed out

    # print("How many number of terms would you like to print out the table for: ")
    # terms = float(input())
    # this part calculates the ending terms itsefl based on the the number of terms the user desires the function to print out from the starting position
    # terms += s_i
    # e_i = terms

    #the ending index of the table that will be printed
    print("Kindly tell the ending term of your table: ")
    e_i = float(input())

    #the step with which we desire each of the successive value to be printed out by our table printer function
    print("Kindly tell me the step for each successive term in your table: ")
    step = float(input())

    for m in range(s_i, e_i + 1, step):
        print("{} x {} = {}" .format(num, s_i, num * s_i))

#Recursive Table printer function
# perform the same task but with recursion

def tableprinterrecursive(n, s, e):

    if s > e:
        return

    print("{0} x {1} = {2}" .format(n, s, n * s))
    tableprinterrecursive(n, s + 1, e)

def tableprintervalueinput():

    print("Please enter the number for which you would like to print the table of: ")
    num = float(input())

    print("Kindly tell the starting term of your table: ")
    s_i = float(input())

    print("Kindly tell the ending term of your table: ")
    e_i = float(input())
    e_i += 1

    tableprinterrecursive(num, s_i, e_i)

def reciprocal():
    print("Kindly enter the number that you would like to find the reciprocal of: ")
    n1 = float(input())
    return n1 ** -1

# Factorial function with loops

def factorial():

    print("Please enter the number of which you would like to print the factorial of: ")
    n = float(input())

    fact = 1

    for m in range(n, 1, -1):
        fact *= n

    print("The factorial for the number is: {0}" .format(fact))

# Recursive Factorial function

def r_f_f(m):

    if m < 0:
        print("The factorial is not defined for negative numbers....")
        return
    elif m == 0 or m == 1:
        return 1
    else:
        return m * r_f_f(m - 1)

def r_factorial():

    print("Please enter the number you would like to figure out the factorial for: ")
    n = float(input())

    print("The factorial of your number is: {0}" .format(r_f_f(n)))

# An interesting and unique pattern in mathematics that no matter what the integer is it will always end in the pattern 8, 4, 2, 1....

def collatzconjecture():

    n = int(input("Please enter the number you would like to apply the collatz conjecture for and print out the pattern for: "))

    while True:
        if n % 2 == 0:
            print("{0}" .format(n))
            n //= 2
        else:
            print("{0}" .format(n))
            n = 3 * n + 1

        if n == 1:
            print("{0}" .format(n))
            break

# A pattern in which the nth term except for the 1st and the last term is the sum of the preceding two terms
# This only calculates the first term

def fibonacci():

    print("Enter the nth term which you would like from the fibonacci sequence: ")
    n = int(input())

    if n < 1:
        print("There least nth term in the availabe sequence is 1. Kindly only enter values that are greater than 1.")
        return

    ans = 0

    for m in range(1, n + 1):

        if m == 1:
            n1 = 0
            ans = n1
        elif m == 2:
            n2 = 1
            ans = n2
        else:
            ans = n2 + n1
            n1 = n2
            n2 = ans

    return

# fibonacci sequence upto nth term pattern - Recursive Approach limited only to calculate the values for the nth term in the fibonacci sequence 
# I was uanbale to figre out/work around a method to use a recursive approach to print the pattern 
# so the only option for printing the pattern at the end was via the usage of a for loop 
# I did try using the recursive approach but it resulted in printing the same value multiple times which was agaisnt my desired output that I wanted to view on the terminal window 

def r_f_p(m, memo={}):
    if m == 1:
        return 0
    elif m == 2:
        return 1

    # prev1 = r_f_p(m - 1)
    # prev2 = r_f_p(m - 2)
    # result = prev1 + prev2
    # print("Term number {0} in the sequence is: {1}" .format(m, result))
    # return result

    # using an advanced python concept, the concept of memoization which prevents recursive call recalculating previously computed values, leveraging
    # the procesing time and saving space on the stack frame

    if m not in memo:
        memo[m] = r_f_p(m - 1, memo) + r_f_p(m - 2, memo)

    return memo[m]


# initial function that calls the function

def r_fibonacci_pattern():
    print("Enter the number of terms upto which you would like the fibonacci sequence printed for: ")
    num = int(input())

    for m in range(1, num + 1):
        print("Term Number {0} has the term in the sequence {1}".format(m, r_f_p(m)))

#conversion Functions

def degrees_into_radians():

    print("Please enter the value in degrees: ")
    n = float(input())

    try:
        print("The value in Radians is: ")
        return n * math.pi / 180
    except ValueError:
        print("Invalid Input, Please enter a numeric value....")
        # we will and can return None as None is also a scalar datatype in python that can only store one value
        # which is a none value
        return None

def radians_into_degrees():

    print("Please enter the value in radians: ")
    n = float(input())

    try:
        print("The value in Degrees is: ")
        return n * 180 / math.pi
    except ValueError:
        print("Invalid Input, Please enter a numeric value....")
        # we will and can return None as None is also a scalar datatype in python that can only store one value
        # which is a none value
        return None

#sum and the product of roots of a quadratic equation

def s_o_r_q():

    print("Please note this technique is only valid if all the co-efficients of the equation are non-zero constants....")

    print("Please enter the co-efficient of x^2 in the quadratic: ")
    n1 = float(input())

    print("Please enter the co-efficient of x in the quadratic: ")
    n2 = float(input())

    print("Please enter the co-efficient of the constant in the quadratic: ")
    n3 = float(input())

    if n1 == 0 or n2 == 0 or n3 == 0:
        print("The technique/shortcut is only valid for non-zero coefficient constants for the equation that you provided")
        print("Exiting Program....")
        return None

    print("The Sum of roots of your quadratic equation are: ")
    return -n2/n1

def p_o_r_q():

    print("Please note this technique is only valid if all the co-efficients of the equation are non-zero constants....")

    print("Please enter the co-efficient of x^2 in the quadratic: ")
    n1 = float(input())

    print("Please enter the co-efficient of x in the quadratic: ")
    n2 = float(input())

    print("Please enter the co-efficient of the constant in the quadratic: ")
    n3 = float(input())

    if n1 == 0 or n2 == 0 or n3 == 0:
        print("The technique/shortcut is only valid for non-zero coefficient constants for the equation that you provided")
        print("Exiting Program....")
        return None

    print("The Product of roots of your quadratic equation are: ")
    return n3/n1


# sum and the product of roots of a cubic equation

def s_o_r_c():

    print("Please note this technique is only valid if all the co-efficients of the equation are non-zero constants....")

    print("Please enter the co-efficient of x^3 in the cubic: ")
    n1 = float(input())

    print("Please enter the co-efficient of x^2 in the cubic: ")
    n2 = float(input())

    print("Please enter the co-efficient of x (the linear factor) in the cubic: ")
    n3 = float(input())

    print("Please enter the co-efficient of the constant in the cubic: ")
    n4 = float(input())

    if n1 == 0 or n2 == 0 or n3 == 0 or n4 == 0:
        print("The technique/shortcut is only valid for non-zero coefficient constants for the equation that you provided")
        print("Exiting Program....")
        return None

    print("The Sum of roots of your cubic equation are: ")
    return -n2 / n1

def p_o_r_c():

    print("Please note this technique is only valid if all the co-efficients of the equation are non-zero constants....")

    print("Please enter the co-efficient of x^3 in the cubic: ")
    n1 = float(input())

    print("Please enter the co-efficient of x^2 in the cubic: ")
    n2 = float(input())

    print("Please enter the co-efficient of x (the linear factor) in the cubic: ")
    n3 = float(input())

    print("Please enter the co-efficient of the constant in the cubic: ")
    n4 = float(input())

    if n1 == 0 or n2 == 0 or n3 == 0 or n4 == 0:
        print("The technique/shortcut is only valid for non-zero coefficient constants for the equation that you provided")
        print("Exiting Program....")
        return None

    print("The Sum of roots of your cubic equation are: ")
    return -n4 / n1

# Calculating the sum of roots of any polynomial based on the vieta's formulae
# The sum of the roots in a polynomial is -a[n-1] / a[n], where:
# a[n-1] is the coefficient of the x^(n-1) term
# a[n] is the coefficient of the x^n term (leading coefficient)

def sum_of_roots_polynomial(coefficients):

    if len(coefficients) < 2:
        #the raise keywordd is used to trigger an exception when any condition is not met
        raise ValueError("Polynomial must have at least two coefficients....")

    l_c = coefficients[0]
    s_l_c = coefficients[1]

    return -s_l_c / l_c

def s_o_r_p_i():

    print("This formulae can correctly process polynomial equations with zero coefficients....")
    print("Please start entering the coefficients of your polynomial equation, starting from the highest power term: ")

    #using a list since they are dynamic and python does not have arrays

    coefficients = []

    while True:

        try:
            c = input("Enter a co-efficient or you may procede with entering 'done' to finish: ")

            #using lower function to convert into lower case

            if c.lower() == 'done':

                if len(coefficients) < 2:
                    print("You must enter at least two coefficients. Please start again")
                else:
                    break
            
                #break statement breaks or exits the while loop

            coefficients.append(float(c))
        except  ValueError:
            print("Invalid input, kindly enter a numeric value or done to stop the append operation to your list....")

    ans = sum_of_roots_polynomial(coefficients)
    print("The sum of roots of the polynomial for your equation is: {0}" .format(ans))


# calculating the product of roots of a polynomial equation based on the vietas formulae relation
# the product of roots can be computed using the relation/formulae (-1)**degreeof polynomial * a[0] / a[len - 1]
# where a represents the list we have
# a[-1] or a[deg] is the coefficient of the constant term
# a[0] is the coefficient of the x^n term (leading coefficient)

def product_of_roots_polynomial(values):

    if len(values) < 2:
        # whilst raising the value error we can type in we can type the prompt we would like to display in quotation marks into the parenthesis of ValueError()
        raise ValueError("Polynomial must have at least two coefficients....")
    
    #compute the degree of our polyomial 
    # we subtract 1 from length because python has 0 based indexing

    deg = len(values) - 1

    numenator = values[0] 

    # denominator = values[-1] 
    # or we can use 
    denominator = values[deg]

    return (-1)**deg * numenator / denominator 

def p_o_r_p_i():

    print("This formulae can correctly process polynomial equations with zero coefficients....")
    print("Please start entering the coefficients of your polynomial equation, starting from the highest power term: ")

    coeff = []

    while True:

        try:
            print("Enter a coefficient or you may proceed with entering 'done' to finish: ")
            d = input()

            if d.lower() == 'done':

                if len(coeff) < 2:
                    print("You must enter at least two coefficients. Please start again")
                else:
                    break
            
            coeff.append(float(d))

        except ValueError:
            print("Invalid Input, kindly enter a numeric value or type in 'done' to halth the append operation to your list....")
    
    ans = product_of_roots_polynomial(coeff)
    print("The product of roots of the polynomial for your equation is:", ans)

# Differentiation 
# The attempt here was to refrain from the utiluisation of any of python's library functions, not inbuilt functions though
# I utilised the finite difference method to compute the dervative of a function f at a given point x
# Please note this is an approximation and might not compute for us the exact values

def diff(function, x_val, h_val):
    
    #reason for utilising h = 1e-5 is that in most cases this would suffice for computing the approximate differential

    return ((function(x_val + h_val)) - (function(x_val - h_val))) / (2 * h_val)
    # division by 2h to obtain the central difference approximation of the derivative

# parent function that callls the child function
# the parent function only serves the purpose of taking inputs

def differentiation():

    print("Kindly enter the equation that you would like to differentiate: ")
    print("Example equations can be: 'x^5 - 3x^4 + 7x^3 + 94x^2 + 643' or '9x - 172' ")
    # input function always returns a sttring value
    eq = input()
    
    print("Enter at which point do you desire  to differentiate: ")
    print("Example inputs can be 'x = 63' ")
    x = float(input())

    print("We will be taking the step size by default as h = 1e-5, we could have chosen a more precise value but that might lead to floating point / decimal number errors: ")
    h = 1e-5

    #try except is used for error handling in python

    try:

        # eval() is a function that takes in a strimng and returns it as a pyhon expression

        equation = lambda x: eval(eq)

        # lambda arguments: expression is the general syntax for the lambda function, whilst lambda is a reserved word in python
        # it creates a small function in python without following the due necessary syntax for that function, and this function does not have a name
        # a dynamic fUnction was created Instead of harDcoding a specific mathematical function, so as to ensure we can handle arbitrary user input in a flexible and concise way

        d = diff(equation, x, h)

        print("The derivative of the provided equation at {0} point x is appproximately: {1} " .format(x, d))
    
    except Exception as e:
    
        print("Error: {0}. Please ensure your equation is correct and try again." .format(e))

def matrixtranspose():

    print("Please specify the number of columns you would like in your matrix: ")
    c = int(input())

    print("Please specify the number of rows you would like in your matrix: ")
    r = int(input())

    mat = [[0 for _ in range(c)] for _ in range(r)]
    transpose = [[0 for _ in range(r)] for _ in range(c)]

    for x in range(r):

        for y in range(c):

            print("Enter element: ")
            mat[x][y] = int(input())

    for x in range(r):

        for y in range(c):

            transpose[y][x] = mat[x][y]

    print("The transpose of your marix is: ")

    # one technique to print out the transposed matrix

    # for x in range(c):

    #     for y in range(r):

    #         print("ELement of transpose matrix at row number {0} and column number {1} is: {2}" .format(x, y, transpose[x][y]))

    # a more better approach

    for row in transpose:
        print(row)

    #this prints out the matrix row by row in a tabular format 

calculator()
