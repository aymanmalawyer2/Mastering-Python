#--------------------------------------------
# [01] Write Down All Types Of Numbers
# [02] Get The Imaginary Part For The Complex Number "1+2j"
# [03] Get The Real Part For The Complex Number "1+2j"
# [04] Convert Number 10 To Floating Point Number With 10 Number After Decimal
# [05] Convert Floating Number 159.650 To Integer
# [06] Function
# --- Create Function Accepts Three Parameters ( num1, num2, operation )
# --- Check if Given Arguments Is Integers
# --- Return The Results of Addition if Third Parameter is ( add )
# --- Return The Results of Multiplication if Third Parameter is ( multiply )
# [07] Get The Same Result Without Use The Exponents 3 ** 8
# [08] Whats The Different Between 21 / 2 And 21 // 2 "Write Soultion With Comment"
#--------------------------------------------

# [01] Write Down All Types Of Numbers
print(100)
print(50.50)
print(1+2j)

print(type(100))  # Int
print(type(50.50))  # Float
print(type(1+2j))  # Complex

# [02] Get The Imaginary Part For The Complex Number "1+2j"
complexNumber = 1+2j

print(1+2j.imag)
print(1+2j.real)
# or This below
print("Imaginary Part Is : {}".format(complexNumber.imag))

# [03] Get The Real Part For The Complex Number "1+2j"
print("Real Part Is : {}".format(complexNumber.real))

# [04] Convert Number 10 To Floating Point Number With 10 Number After Decimal
print("{:.10f}".format(10))
# Or This Below
num = 10
print(f"{num:.10f}")

# [05] Convert Floating Number 159.650 To Integer
print(int(159.650))

#[06] Function
# --- Create Function Accepts Three Parameters ( num1, num2, operation )
# --- Check if Given Arguments Is Integers
# --- Return The Results of Addition if Third Parameter is ( add )
# --- Return The Results of Multiplication if Third Parameter is ( multiply )

num1=5
num2=3

def calc(num1, num2, Operation):
    if Operation=='+':
        r = num1 + num2
    else:
        r = num1 * num2
    return r

print(isinstance(num1, int))
print(isinstance(num2, int))

r1 = calc(5, 3,"+")
r2 = calc(5, 3, "*")
print(r1)
print(r2)

# [07] Get The Same Result Without Use The Exponents 3 ** 8
print(3*3*3*3*3*3*3*3)

# [08] Whats The Different Between 21 / 2 And 21 // 2 "Write Soultion With Comment"
# the Difference Is: In Division 21/2 = 11 & Here We Also Can Return Float Number
# But In Floor Division 21//2 = 10 & Here We Can't Return Float Number. We Can Return the integral part of the quotient
