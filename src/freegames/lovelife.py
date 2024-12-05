print("Choose Your own love life game (Any way you choose is bound to fail sooner or later...play untill that happens.)")


def start_game():
    print("You meet a hot boy/girl.")
    print("Do you want to:")
    print("A) Act normal")
    print("B) Start flirting")

    choice = input("> ")

    if choice.upper() == "A":
        act_normal()
    elif choice.upper() == "B":
        print("He/She smirks and tells their freind how naive you are. Your love life has failed.")
        print("Try again!")
        start_game()
    else:
        print("Invalid choice. Try again.")
        start_game()

def act_normal():
    print("He/She falls for you.")
    print("Do you want to:")
    print("A) Make conversation")
    print("B) Say a dirty joke")

    choice = input("> ")

    if choice.upper() == "A":
        print("He/She gets bored and leaves. Your love life has failed.")
        print("Try again!")
        start_game()
    elif choice.upper() == "B":
        say_joke()
    else:
        print("Invalid choice. Try again.")
        cave_entrance()

def say_joke():
    print("He/She founds you funny. They ask you out.")
    print("For the next 10 years your love life rocks!")
    print("Turns out your lover is a mafia gangster that tricks you out of your life savings and then vanishes!!!! Your love life has failed")
    print("The end!")

start_game()