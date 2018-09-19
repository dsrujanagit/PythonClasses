#The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most 
#other languages (for example, Pascal or C); parentheses (()) can be used for grouping. For example:

2 + 2
50 - 5*6 # PEMDAS  - Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction
(50 - 5*6) / 4

8 / 5  # division always returns a floating point number

#The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.
#Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:

17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder

#With Python, it is possible to use the ** operator to calculate powers [1]:

5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7


#The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

width = 20
height = 5 * 9
width * height

#If a variable is not “defined” (assigned a value), trying to use it will give you an error:

n  # try to access an undefined variable

#There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

4 * 3.75 - 1

#In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)

