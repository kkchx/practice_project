import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the nature of roots based on the discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root1 = -b / (2*a)
        root2 = root1

    return discriminant, root1, root2

    # Get coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

    # Solve the quadratic equation
discriminant, root1, root2 = solve_quadratic(a, b, c)

    # Print the results
print(f"Discriminant: {discriminant}")
print("Roots:", root1, root2)
