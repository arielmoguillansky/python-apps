# This program converts smiley faces to emojis
def main():
    string = input()
    print(convert(string))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()
