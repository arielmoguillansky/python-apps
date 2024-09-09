# This program calculates the energy of an object given its mass
def main():
    mass = int(input("m: "))
    print(f"E: {getJoules(mass)}")

def getJoules(m):
    return m*pow(300000000,2)

main()
