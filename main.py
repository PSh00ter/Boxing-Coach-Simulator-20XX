import random
from lists import *
_CHAPTER_LINE = '=' * 75
fighter_choice = ''
next_choice = ''
training_sickness = 0
tier = 'tier1'
personality_effects = {
    'Cocky': {'power': 4, 'finesse': -3},
    'Arrogant': {'power': 4, 'finesse': -2},
    'Sleepy': {'power': -3, 'speed': -3},
    'Annoying': {'power': -2, 'finesse': 3},
    'Violent': {'power': 5, 'finesse': -3},
    'Vicious': {'power': 4, 'speed': 3},
    'Prankster': {'finesse': 5, 'speed': 3},
    'Joyful': {'finesse':3, 'speed': 3},
    'Productive': {'speed':2, 'power':2, 'finesse':2},
    'Lazy': {'speed': -3, 'power':2},
    'Empathetic': {'speed':1},
    'Insightful': {'finesse':5},
    'Loyal': {'finesse':3},
    'Competitive': {'power':3, 'speed': 4},
    'Quiet': {'speed':3},
    'Tough': {'power':5},
    'Calculating': {'speed':4},
    'Childish': {'finesse':2},
    'Clumsy': {'finesse':-4, 'power':3},
    'Dull': {'power':-2},
    'Gloomy': {'speed':-2},
    'Hateful': {'power':3},
    'Disobedient': {'finesse':-6, 'power':5},
    'Powerful': {'power':7, 'speed':-1}
}
def assign_traits(main_personality_traits, num_traits=4):
    """this function generates a personality trait from the list...kinda
    useless change later"""
    return random.sample(main_personality_traits, num_traits)
def generate_character():
    """This function generates a fighter for use later when giving the user
    three options for fighters to train, assigning a name, weight, height,
    strength, and main personality trait to them for gameplay"""
    personality = assign_traits(main_personality_traits, 1)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    height = (possible_heights[random.randint(0, len(possible_heights) - 1)])
    weight = (random.randint(100, 205))
    speed = (random.randint(35, 70))
    power = (random.randint(35, 70))
    finesse = (random.randint(35, 70))
    strength = random.choice(strengths)
    '''for trait in personality_effects:
        if trait in personality_effects:
            for stat, effect in personality_effects[trait].items():
                fighter[stat] += effect'''
    return {
        'first_name': fname.strip(),
        'last_name': lname,
        'name': fname + lname,
        'traits': personality,
        'weight': weight,
        'height': height,
        'speed': speed,
        'power': power,
        'finesse': finesse,
        'strength': strength,
        'win_record': 0,
        'lose_record': 0,
        'reputation': 0
    }
def generate_opponent(tier):
    """This function generates an opponent for later use against the fighter, and
    be reused over and over to generate new fighters."""
    personality = assign_traits(main_personality_traits, 1)
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    height = (possible_heights[random.randint(0, len(possible_heights) - 1)])
    weight = (random.randint(100, 205))
    if tier == 'tier1':
        speed = (random.randint(25, 40))
        power = (random.randint(25, 40))
        finesse = (random.randint(25, 40))
    elif tier == 'tier2':
        speed = (random.randint(45, 60))
        power = (random.randint(45, 60))
        finesse = (random.randint(45, 60))
    elif tier == 'tier3':
        speed = (random.randint(65, 80))
        power = (random.randint(65, 80))
        finesse = (random.randint(65, 80))
    strength = random.choice(strengths)
    return {
        'first_name': fname.strip(),
        'last_name': lname,
        'name': fname + lname,
        'traits': personality,
        'weight': weight,
        'height': height,
        'speed': speed,
        'power': power,
        'finesse': finesse,
        'strength': strength
    }
def display_character(character):
    """This function creates a string that actually displays the
    characteristics generated by the generate_character function, and allows
    for displaying specific elements of the fighter to the user"""
    display_string = (
        f"Name: {character['name']}\n"
        f"Height: {character['height']}\n"
        f"Personality: {', '.join(character['traits'])}\n"
        f"Weight: {character['weight']} lbs\n"
        f"Strength: {character['strength']}"
    )
    return display_string

def calculate_win_percentage(fighter, opponent, strategy_modifier=0):
    power_advantage = (fighter['power'] - opponent['power']) / 100
    speed_advantage = (fighter['speed'] - opponent['speed']) / 100
    finesse_advantage = (fighter['finesse'] - opponent['finesse']) / 100
    win_probability = (
        (power_advantage * 0.4) +
        (speed_advantage * 0.3) +
        (finesse_advantage * 0.3)
    ) * 100
    win_probability += strategy_modifier
    win_probability += random.uniform(-3, 3)
    win_probability = max(0, min(100, win_probability))
    if random.randint(0, 100) < win_probability:
        return 'win'
    else:
        return 'lose'

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
        fighter = ''
        while fighter_choice not in ['1', '2', '3']:
            fighter_choice = input("Pick which fighter you'd like to take on! ")
            if fighter_choice == '1':
                fighter = fighter1
            elif fighter_choice == '2':
                fighter = fighter2
            elif fighter_choice == '3':
                fighter = fighter3
            else:
                print("Invalid choice! Try again.")
        print(f"You've chosen {fighter['name']} as your main pupil.")
        print(f"His speciality is {fighter['strength']}")
        print(_CHAPTER_LINE)
        def fight_sequence():
            global win_record, lose_record, tier, training_sickness
            tier1_opponent = generate_opponent(tier)
            print(
                f"""Before the fight, you have the opportunity to give {fighter['first_name']}
advice so that he may beat the opponent.
(A) "Good advice"
(B) "Bad advice" """)
            advice = input("What advice do you give? ")
            advice = advice.upper()
            fight_outcome = ''
            if advice == 'A':
                fight_outcome = calculate_win_percentage(fighter,
                                                         tier1_opponent,10)
            elif advice == 'B':
                fight_outcome = calculate_win_percentage(fighter,
                                                         tier1_opponent, 5)
            if fight_outcome == 'win':
                print(
                    f"{fighter['first_name']} has defeated {tier1_opponent['first_name']} and won!")
                fighter['win_record'] += 1
                print(f"New record:  {fighter['win_record']} - {fighter['lose_record']}")
                if fighter['win_record'] >= 6:
                    tier = 'tier2'
                elif fighter['win_record'] >= 10:
                    tier = 'tier3'
            elif fight_outcome == 'lose':
                print(
                    f"{fighter['first_name']} has been defeated by {tier1_opponent['first_name']} and lost!")
                fighter['lose_record'] += 1
                print(f"New record:  {fighter['win_record']} - {fighter['lose_record']}")
            training_sickness = 0
        def training_sequence():
            global training_sickness
            print(f"""As his fight approaches, {fighter['first_name']} needs guidance for his training.
He asks you what you think he should focus on. You ask him to demonstrate 
either his speed, strength, or finesse:
(SP) : Speed
(P) : Power
(F) : Finesse""")
            stat_demo = ''
            upgrade_stat = ''
            while stat_demo not in ['SP', 'P', 'F']:
                stat_demo = input("Choose which stat you would like to see: ")
                stat_demo = stat_demo.upper()
                if stat_demo == 'SP':
                    print(f"Speed = {fighter['speed']}")
                elif stat_demo == 'P':
                    print(f"Power = {fighter['power']}")
                elif stat_demo == 'F':
                    print(f"Finesse = {fighter['finesse']}")
            if training_sickness < 3:
                while upgrade_stat not in ['SP', 'P', 'F']:
                    upgrade_stat = input(f"Now, choose which stat to work on with "
                                         f"{fighter['first_name']}: ")
                    upgrade_stat = upgrade_stat.upper()
                    if upgrade_stat == 'SP':
                        fighter['speed'] = fighter['speed'] + 5
                        print(f"New Speed = {fighter['speed']}")
                    elif upgrade_stat == 'P':
                        fighter['power'] = fighter['power'] + 5
                        print(f"New Power = {fighter['power']}")
                    elif upgrade_stat == 'F':
                        fighter['finesse'] = fighter['finesse'] + 5
                        print(f"New Finesse = {fighter['finesse']}")
            else:
                print(f"""You've been overdoing it with {fighter['first_name']}'s training!
Give him time to rest before the fight!""")
            training_sickness += 1
        training_sequence()
        print(_CHAPTER_LINE)
        print(f"""After training, it's time to fight.""")
        fight_sequence()
        print(_CHAPTER_LINE)
        print(f"""After his first fight, {fighter['first_name']} seems incredibly motivated
to continue his training. The shots are now yours to 
call on how to proceed with his career. Good luck, Coach!""")
        while next_choice not in [1, 2, 3, 4]:
            print(_CHAPTER_LINE)
            next_choice = input("""Choose your next action: 
(1) Train fighter
(2) Enter fighter into bout
(3) View record
(4) Piss off and die 
""")
            if next_choice == '1':
                training_sequence()
            elif next_choice == '2':
                fight_sequence()
            elif next_choice == '3':
                print(f"Record:  {fighter['win_record']} - {fighter['lose_record']}")
            elif next_choice == '4':
                break
    if menu_input == 'C':
        print(_CHAPTER_LINE)
        print("""This game was made by a solo dev named Preston Knoebel. It 
serves as his first personal project, and was made to express his 
love for the sport of boxing and a joy for simulation games.""")
