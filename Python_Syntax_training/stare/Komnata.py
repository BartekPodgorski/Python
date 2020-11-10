import random
from enum import Enum

def find_approximation(value,percent_range):
    lowest_value = (100 - percent_range)/100 * value
    highest_value = (100 + percent_range)/100 * value
    return random.randint(lowest_value, highest_value)


Event = Enum('Event', ['Chest','Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }
event_list = list(eventDictionary.keys())
event_probability = list(eventDictionary.values())

Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomaranczowy',
                           'Purple': "fioletowy",
                           'Gold': 'zloty'
                           }
               )

colours_dictionary = {
                        Colours.Green: 0.75,
                        Colours.Orange: 0.2,
                        Colours.Purple: 0.04,
                        Colours.Gold: 0.01
                     }

chest_colour_list = list(colours_dictionary.keys())
chest_colour_propability = list(colours_dictionary.values())

rewards_for_chests = {
                        chest_colour_list[reward]: (reward + 1) * (reward + 1) *1000
                        for reward in range(len(chest_colour_list))
                     }

game_length = 5

print("Welcome in my game called Chamber")
print("You have only five steps to make , see yourself how much")

gold_required = 0

while game_length >0:
    game_answer = input("Do you want to move forward: ")
    if (game_answer == "yes"):
        print("Great, let's see what you got ...")
        drawn_event = random.choices(event_list,event_probability)[0]
        if (drawn_event == Event.Chest):
            print("You have find a CHEST")
            drawn_chest = random.choices(chest_colour_list,chest_colour_propability)[0]
            print("The colour of you chest is:",drawn_chest.value)
            gamer_rewards = find_approximation(rewards_for_chests[drawn_chest],10)
            gold_required = gold_required + gamer_rewards
        elif(drawn_event ==Event.Empty):
            print("You don't find anything")
    else:
        print("You can go only straight line ...")
        continue
    game_length -= 1

print("Your gold:", gold_required)
