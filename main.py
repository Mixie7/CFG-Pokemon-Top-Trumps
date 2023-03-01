# Imports
import random
import requests
from pprint import pprint
from time import sleep
import time
import sys

# delay print - game aesthetics
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬛⬜
⬜⬜⬜⬜⬛⬛⬛⬛🟨🟨⬛⬛🟨🟨⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨⬛⬛🟨🟨⬛⬛⬛⬛
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟥🟥🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨🟨🟨🟥🟥🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛🟨🟥🟥🟥🟥🟨🟨🟨⬛🟥🟥🟥⬛🟨🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨⬛⬛⬛⬜⬛🟨🟥🟥🟥🟥🟨🟨🟨⬛🟥🟥🟥⬛🟨🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟥🟥🟨🟨🟨🟨⬛🟥🟥🟥⬛⬛⬛🟨🟨🟥🟥🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛🟨🟨⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜

░█▀▀█ ░█▀▀▀█ ░█─▄▀ ░█▀▀▀ ░█▀▄▀█ ░█▀▀▀█ ░█▄─░█ 　 ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ 　 ▀▀█▀▀ ░█▀▀█ ░█─░█ ░█▀▄▀█ ░█▀▀█ ░█▀▀▀█ 
░█▄▄█ ░█──░█ ░█▀▄─ ░█▀▀▀ ░█░█░█ ░█──░█ ░█░█░█ 　 ─░█── ░█──░█ ░█▄▄█ 　 ─░█── ░█▄▄▀ ░█─░█ ░█░█░█ ░█▄▄█ ─▀▀▀▄▄ 
░█─── ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█──░█ ░█▄▄▄█ ░█──▀█ 　 ─░█── ░█▄▄▄█ ░█─── 　 ─░█── ░█─░█ ─▀▄▄▀ ░█──░█ ░█─── ░█▄▄▄█
""")

# Game Introduction
delay_print("Hello!")
print("")
name = input("Welcome to Pokemon Top-Trumps! What is your name? ")
Computer_name = "Computer"
input((f"""{name}, here's how to play...
              1. Generate a random Pokemon
              2. Choose the stat you want to compete with
              3. Compare the stats generated from the computers pick
              4. Keep playing until you win!
              5. (Each win is worth 2 points)
              ------PRESS ENTER TO CONTINUE-------"""))
print("You will be playing against " + "the" + " " + Computer_name)
print("Are you ready...")
sleep(1)
print("3");
sleep(1)
print("2");
sleep(1)
print("1");
sleep(1)
delay_print("Let's begin!");
sleep(1)
print("")
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
➖➖🟥🟥🟥🟥🟥
➖🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
 🟥🟥🟥⬛⬛⬛🟥🟥🟥
⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬛⬛⬛⬜⬜⬜
   ⬜⬜⬜⬜⬜⬜⬜⬜⬜
➖⬜⬜⬜⬜⬜⬜⬜
➖➖⬜⬜⬜⬜⬜⠀⠀⠀⠀⠀⠀
⠀""")


# Define random pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'].upper(),
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

# Rounds
rounds = int(input("How many rounds would you like to play? "))
while rounds not in range(1, 5):
    try:
        rounds = int(input("Sorry! I can only play upto 5 rounds. Please try again."))
    except:
        print("ERROR invalid input.")
    if rounds in range(1, 5):
        time.sleep(1)
        print("")
# Define score count
Your_score = 0
Computer_score = 0
Game_Count = 0

# Define one run of game
def run():
    for i in range(rounds):
        global Your_score
        global Computer_score
        global Game_Count
        print("        ")

        delay_print("NEW ROUND")

        print("        ")
        my_pokemon = random_pokemon()
        print('You were given {}'.format(my_pokemon['name']))

        # Show Pokemon stats
        print("Pokemon Stats:")
        sleep(1)
        print("Pokemon ID:", my_pokemon["id"]);
        sleep(1)
        print("Pokemon Height", my_pokemon["height"]);
        sleep(1)
        print("Pokemon Weight:", my_pokemon["weight"]);
        sleep(1)
        stat_choice = input('Which stat do you want to use? (id, height, weight) ');
        sleep(1)

        print("""

        """)
        opponent_pokemon = random_pokemon()

        print('The opponent chose {}'.format(opponent_pokemon['name']));
        sleep(1)
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        if my_stat > opponent_stat:
            Your_score += 2
            Game_Count += 1
            delay_print("*** You Win! ***")

        elif my_stat < opponent_stat:
            Game_Count += 1
            Computer_score += 2
            delay_print("*** You Lose! ***")

        else:
            Your_score += 1
            Computer_score += 1
            Game_Count += 1
            delay_print("*** It's a Draw! ***")
    print("            ")
    print("Total Games Played:", Game_Count);
    sleep(1)
    print("Your Final Score:", Your_score);
    sleep(1)
    print("Computer Score:", Computer_score);
    sleep(1)

run()

# Highscore - written to txt file
file = open('Pokemon Highscores.txt', 'a')
name = name;
score = int(Your_score)
print("")
file.write(name + " - " + str(score) + "\n")
file.close()

# Reading and printing Highscores
file = open('Pokemon Highscores.txt', 'r')
file_contents = file.read()
print(file_contents)
file.close()

# Play again (same number of rounds)
while True:
    print("             ")
    answer = input("Do you want to play again?")
    if answer == "yes":
        run()
    elif answer == "no":
        break
print("End Game")
