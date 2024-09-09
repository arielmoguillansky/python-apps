# This program asks the user the answer to the Great Question of Life, the Universe, and Everything
def main():
    resp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    print('Yes') if resp in ['42', 'forty-two', 'forty two'] else print ('No')

main()
