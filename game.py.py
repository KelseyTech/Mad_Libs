import random

def play_game():
    verb = input("Please input a verb: ")
    adjective = input("Please input a adjective: ")
    noun = input("Please input a noun: ")

    s1 = f"The {adjective} cat {verb} over the {noun}."
    s2 = f"I {verb} to the store and bought a {adjective} {noun}."
    s3 = f"She ate a {adjective} {noun} and felt {adjective}."
    s4 = f"The {noun} {verb} through the {adjective} forest."

    all_sentences = s1 + s2 + s3 + s4
    sentence_list = all_sentences.split(".")
    print(random.choice(sentence_list))



# Interactive Loop
exit = False
while not exit:
    user_input = input("p to play / q to quit: ")
    if user_input == "q":
        exit = True
    elif user_input == "p":
        play_game()
    else:
        print("You need to enter either q or p")


    

