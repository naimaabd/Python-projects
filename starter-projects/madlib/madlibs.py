main_character = input("Enter a Main Character: ")
title = f"The Coding Adventure of {main_character}\n"

adj1 = input("Adjective: ")
noun1 = input("Noun: ")
activity = input("Activity: ")
noun2 = input("Noun: ")
adj2 = input("Adjective: ")
item = input("Item: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
reward = input("Reward: ")

madlib_story = f"""
Title: {title}

--------------------------------------------------------------------------------

Once upon a time, there was a {adj1} programmer named {main_character}. \
{main_character} lived in a {adj2} city filled with fellow coders and tech \
enthusiasts. One day, while {activity}, {main_character} stumbled upon a \
mysterious {noun2}. Filled with curiosity, {main_character} decided to embark \
on an epic coding journey to decipher the secrets of the {noun2}.

--------------------------------------------------------------------------------

Along the way, they encountered a {adj3} AI algorithm who offered to help \
them in exchange for {item}. Together, {main_character} and their new AI \
companion delved into {adj4} databases, debugged complex algorithms, and \
traversed through countless lines of code until finally reaching the {noun2}'s \
hidden repository. With great determination and problem-solving skills, \
{main_character} confronted the {noun2} and unlocked its ancient {reward}.

--------------------------------------------------------------------------------

As a reward, they were granted {reward} and became renowned as the greatest \
programmer in all of cyberspace. And so, {main_character} returned to their \
coding haven, their heart filled with excitement, ready to share their incredible \
coding tale with fellow developers and tech enthusiasts.

--------------------------------------------------------------------------------
"""

print(madlib_story)
