import random

question_list = []

def ask_question():
    response = input("What is your question?")
    question_list.append(response)

answer_list = ["it is certain", "It is decidedly so", "Without a doubt",
"Yes definitely", "You may rely on it","As I see it, yes",
"Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Better not tell you now", "Cannot predict now",
"Concentrate and ask again", "Don't count on it", "My reply is no",
"My sources say no", "Outlook not so good", "Very doubtful"]

def pick_answer():
    print(random.choice(answer_list))

pick_answer()
