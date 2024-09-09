# This program is a simple example of a chatbot that uses a conditional statement to determine the response based on the user's input. The chatbot will respond with a different message depending on the user's input. The chatbot will respond with a message based on the following conditions: if the user's input contains the word "hello", the chatbot will respond with "$0"; if the user's input starts with the letter "h", the chatbot will respond with "$20"; otherwise, the chatbot will respond with "$100".
def main():
    greeting = input("Greeting: ").strip().lower()

    if 'hello' in greeting:
        print('$0')
    elif greeting.startswith('h'):
        print('$20')
    else:
        print('$100')

main()
