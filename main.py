import random
from lists import *
_CHAPTER_LINE = '=' * 75
fighter_choice = ''
def assign_traits(main_personality_traits, num_traits=4):
    return random.sample(main_personality_traits, num_traits)
def generate_character():
    personality = assign_traits(main_personality_traits, 1)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    height = (possible_heights[random.randint(0, len(possible_heights) - 1)])
    weight = (random.randint(100, 205))
    return {
        'name': fname + lname,
        'traits': personality,
        'weight': weight,
        'height': height
    }

def display_character(character):
    display_string = (
        f"Name: {character['name']}\n"
        f"Height: {character['height']}\n"
        f"Personality: {', '.join(character['traits'])}\n"
        f"Weight: {character['weight']} lbs"
    )
    return display_string
    '''return (f"\n"
            f"Name: {fname}{lname}\n"
            f"Height: {height}\n"
            f"Weight: {weight} lbs\n"
            f"Personality Trait:\n - " + '\n - '.join(personality) + "\n")'''

fighter1 = generate_character()
fighter2 = generate_character()
fighter3 = generate_character()

print(_CHAPTER_LINE)
print("Welcome to Boxing Coach Simulator 20XX!")
print("""In this game, you'll take the role of a boxing coach looking to train
the next boxing champion in the division of your choosing!""")
user_enter = input("Press 'Enter' to begin -> ")
if user_enter == '':
    print(_CHAPTER_LINE)
    menu_input = input("""(A) -> Tutorial
(B) -> Start Game
(C) -> Credits\n""")
    menu_input = menu_input.upper()
    if menu_input == 'A':
        print("""In Boxing Coach Simulator 20XX, you take the role of a 
boxing coach. You will be given a choice between three fighters to choose as
your main pupil. These fighters will have many different stats that 
determine their ability to fight, such as their strengths, weaknesses, 
personality traits, and their 'weapon'. 
A weapon in the context of the game is a fighters main tool that they will 
use to win fights. For example, a 'ghost jab' is a weapon that will let a fighter
catch their opponent off-guard when they use it as they jab with blinding 
speed. You will be given choices to influence your fighter, and their 
success will depend on the way you train them. Carefully consider their 
personality, strengths, weaknesses, and weapons to lead your fighter to the 
champion title!""")
    if menu_input == 'B':
        print("""You enter the Noo-Boxers Gym, scoping out the potential 
fighters around you and trying to search for a prospect who looks promising. 
You spot three distinct fighters.""")
        print(_CHAPTER_LINE)
        print(display_character(fighter1))
        print(_CHAPTER_LINE)
        print(display_character(fighter2))
        print(_CHAPTER_LINE)
        print(display_character(fighter3))
        print(_CHAPTER_LINE)
        while fighter_choice not in ['1', '2', '3']:
            fighter_choice = input("Pick which fighter you'd like to take on!")
            if fighter_choice == '1':
                fighter = fighter1
            elif fighter_choice == '2':
                fighter = fighter2
            elif fighter_choice == '3':
                fighter = fighter3
            else:
                print("Invalid choice! Try again.")
        print(f"You've chosen {fighter['name']} as your main pupil.")
    if menu_input == 'C':
        print(_CHAPTER_LINE)
        print("""This game was made by a solo dev named Preston Knoebel. It 
serves as his first personal project, and was made to express his 
love for the sport of boxing and a joy for simulation games.""")
