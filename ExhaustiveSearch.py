def dlp(b, z, n):
    # b^x = z(mod n)

    # first, initialize initial variables
    # base is for comparing to z, exponent is for looping/incrementing through
    base = 1
    exponent = 1
    answer = ""

    # exponent is used for iterating, finding solution
    while exponent < n:
        base = (base * b) % n

        if base == z:
            break

        exponent = exponent + 1

    # made string for answer instead of returning an integer
    # to avoid Python returning "None" when getting "No Result"
    if exponent == n:
        answer = "No result"
    else:
        answer = str(exponent)
        print(str(b) + "^" + str(answer) + " is congruent to " + str(z) + "(modulo " + str(n)+ ")")
    return answer


# blank lines for formatting, giving prompt/formula
print()
print()
print("b^x = z(mod n)")
print("Solving for x")
print()

# user input for above prompt/formula
firstInput = (input("Input first integer, b: "))
try:
    bValue = int(firstInput)
except Exception:
    print("Input is not an integer, please restart script and input an integer")
    raise
secondInput = input("Input second integer, z: ")
try:
    zValue = int(secondInput)
except Exception:
    print("Input is not an integer, please restart script and input an integer")
    raise
thirdInput = input("Input final integer, n: ")
try:
    nValue = int(thirdInput)
except Exception:
    print("Input is not an integer, please restart script and input an integer")
    raise

# formatting
print("Calculating...")
print()

# Answer, more blank lines for cleaner look
print("Solution: " + dlp(bValue, zValue, nValue))
print()
print()
