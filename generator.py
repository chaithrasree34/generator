# generator
# Python program to calculate generated EMF of a DC generator

P = int(input("Enter number of poles (P): "))
phi = float(input("Enter flux per pole (Wb): "))
Z = int(input("Enter total number of armature conductors (Z): "))
N = float(input("Enter speed of generator (RPM): "))
A = int(input("Enter number of parallel paths (A): "))

# Calculate generated EMF
Eg = (P * phi * Z * N) / (60 * A)

print("\nDC Generator Calculation")
print("Generated EMF =", round(Eg, 2), "V")
