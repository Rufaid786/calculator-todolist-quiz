import random

questions=[('What is the capital of Cameroon?',"Yaounde"),('Whats is 9*9?','81'),('What is the currency of Saudi Arabia?','Riyal'),("What is the smallest country in the world?","Vatican City")]


def get_random_question():
    question=random.choice(questions)
    return question


def check_answer(question,answer):
    return answer==question[1]    


def run_quiz():
    question=get_random_question()
    print(question[0])
    user_answer=input('Your answer: ')    
    if check_answer(question=question,answer=user_answer):
        print("Correct")
    else:
        print("Incorrect")    

run_quiz()        