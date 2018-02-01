question_list = []

def check_question():
    if "?" not in response:
        print ("I’m sorry, I can only answer questions")

while True:
    response = input("What is your question?")
    if response =="quit":
        break
    check_question()
