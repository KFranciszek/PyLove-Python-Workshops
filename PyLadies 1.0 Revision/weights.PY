# Checking how many weights of two types should we use to get the same weight at both sides
def LCD(A,B): #Largest Common Divisor

    while B != 0:
        C = A % B
        A = B
        B = C
    return A

def SCM(A,B): #Smallest Common Multiple
    return 1.0 * (A*B) / LCD(A,B)

def weights(A,B):
    if A == B:
        return "1, 1"
    else:
        scm = SCM(A,B)
        number1 = nww / A
        number2 = nww / B
        return (str(int(number1)) + ", " + str(int(number2)))