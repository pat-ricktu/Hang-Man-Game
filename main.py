#!/bin/python3
#Name: Patrick Tu
#Purpose: To create a hangman game using python.

import random
from time import sleep as s

print(
    "Let's play Hangman! I have a list of words from which you will have to guess them correctly."
)
s(1)
print(
    "A maximum of 'x+1' wrong answers are allowed, where 'x' is the number of different letters in the word.\nIf you decide to guess the word itself, beware! If you get it wrong, you lose instantly!"
)
s(1)

print("The rest should be easy for you, so here we go!")
s(1)
repeat = ""
fruits = [("apple", 5), ("apricot", 8), ("avocado", 6), ("banana", 4),
          ("blackcurrant", 10), ("blueberry", 7), ("carambola", 8),
          ("cherry", 6), ("coconut", 6), ("cranberry", 8), ("feijoa", 7),
          ("fig", 4), ("gooseberry", 8), ("grapefruit", 10), ("grape", 6),
          ("melon", 6), ("kiwi", 4), ("lemon", 6), ("lime", 5), ("mandarin",
                                                                 7),
          ("mango", 6), ("nectarine", 8), ("orange", 7), ("papaya", 4),
          ("peach", 6), ("pear", 5), ("pineapple", 7), ("plum", 5),
          ("pomegranate", 10), ("pummelo", 7), ("raspberry", 8),
          ("strawberry", 9), ("tangerine", 8), ("watermelon", 10),
          ("blackberry", 8)]
countries = [
    ("Afghanistan", 10),
    ("Albania", 7),
    ("Algeria", 8),
    ("Andorra", 7),
    ("Angola", 7),
    ("Anguilla", 8),
    ("Antarctica", 8),
    ("Argentina", 9),
    ("Armenia", 8),
    ("Aruba", 6),
    ("Australia", 9),
    ("Austria", 8),
    ("Azerbaijan", 10),
    ("Bahamas", 6),
    ("Bahrain", 7),
    ("Bangladesh", 10),
    ("Barbados", 8),
    ("Belarus", 8),
    ("Belgium", 8),
    ("Belize", 6),
    ("Benin", 5),
    ("Bermuda", 8),
    ("Bhutan", 7),
    ("Bolivia", 7),
    ("Botswana", 8),
    ("Brazil", 7),
    ("Brunei", 7),
    ("Bulgaria", 8),
    ("Burundi", 7),
    ("Cambodia", 8),
    ("Cameroon", 8),
    ("Canada", 5),
    ("Chad", 5),
    ("Chile", 6),
    ("China", 6),
    ("Columbia", 9),
    ("Comoros", 6),
    ("Congo", 5),
    ("Croatia", 7),
    ("Cuba", 5),
    ("Cyprus", 7),
    ("Denmark", 8),
    ("Djibouti", 8),
    ("Dominica", 8),
    ("Ecuador", 8),
    ("Egypt", 6),
    ("Eritrea", 7),
    ("Estonia", 8),
    ("Ethiopia", 8),
    ("Fiji", 4),
    ("Finland", 7),
    ("France", 7),
    ("Gabon", 6),
    ("Gambia", 6),
    ("Georgia", 8),
    ("Germany", 8),
    ("Ghana", 5),
    ("Gibraltar", 8),
    ("Greece", 5),
    ("Greenland", 8),
    ("Grenada", 7),
    ("Guadeloupe", 9),
    ("Guatemala", 8),
    ("Guinea", 7),
    ("Guyana", 6),
    ("Haiti", 5),
    ("Vatican", 7),
    ("Honduras", 9),
    ("Hungary", 8),
    ("Iceland", 8),
    ("India", 6),
    ("Indonesia", 9),
    ("Iran", 5),
    ("Iraq", 5),
    ("Ireland", 8),
    ("Israel", 7),
    ("Italy", 6),
    ("Jamaica", 6),
    ("Japan", 5),
    ("Jordan", 7),
    ("Kazakstan", 8),
    ("Kenya", 6),
    ("Kiribati", 7),
    ("North Korea", 10),
    ("South Korea", 11),
    ("Kosovo", 5),
    ("Kuwait", 7),
    ("Kyrgyzstan", 10),
    ("Latvia", 6),
    ("Lebanon", 7),
    ("Lesotho", 7),
    ("Liberia", 7),
    ("Liechtenstein", 9),
    ("Lithuania", 8),
    ("Luxembourg", 10),
    ("Macau", 5),
    ("Macedonia", 9),
    ("Madagascar", 8),
    ("Malaysia", 7),
    ("Maldives", 9),
    ("Mali", 5),
    ("Malta", 5),
    ("Martinique", 10),
    ("Mauritania", 8),
    ("Mexico", 7),
    ("Micronesia", 10),
    ("Moldova", 7),
    ("Monaco", 6),
    ("Mongolia", 8),
    ("Montenegro", 8),
    ("Morocco", 5),
    ("Mozambique", 11),
    ("Myanmar", 7),
    ("Namibia", 6),
    ("Nauru", 5),
    ("Nepal", 6),
    ("Netherlands", 11),
    ("Nicaragua", 8),
    ("Niger", 6),
    ("Norway", 7),
    ("Oman", 5),
    ("Pakistan", 8),
    ("Panama", 5),
    ("Paraguay", 7),
    ("Peru", 5),
    ("Philippines", 9),
    ("Poland", 7),
    ("Portugal", 9),
    ("Qatar", 5),
    ("Reunion", 7),
    ("Romania", 7),
    ("Russia", 6),
    ("Rwanda", 6),
    ("Samoa", 5),
    ("Senegal", 7),
    ("Serbia", 7),
    ("Seychelles", 8),
    ("Singapore", 10),
    ("Slovakia", 8),
    ("Slovenia", 9),
    ("Somalia", 7),
    ("SAR", 4),
    ("Spain", 6),
    ("Sudan", 6),
    ("Suriname", 9),
    ("Swaziland", 9),
    ("Sweden", 6),
    ("Switzerland", 12),
    ("Syria", 6),
    ("Taiwan", 6),
    ("Tajikistan", 9),
    ("Tanzania", 6),
    ("Thailand", 8),
    ("Togo", 4),
    ("Tokelau", 8),
    ("Tonga", 6),
    ("Tunisia", 7),
    ("Turkey", 7),
    ("Turkmenistan", 12),
    ("Tuvalu", 6),
    ("Uganda", 6),
    ("Ukraine", 8),
    ("UAE", 4),
    ("UK", 3),
    ("USA", 4),
    ("Uruguay", 7),
    ("Uzbekistan", 11),
    ("Vanuatu", 6),
    ("Venezuela", 8),
    ("Yemen", 5),
    ("Zambia", 6),
    ("Zimbabwe", 8),
]
mathterms = [("addition", 7), ("subtraction", 11), ("multiplication", 11),
             ("division", 7), ("exponent", 7), ("bracket", 8), ("root", 4),
             ("trigonometry", 10), ("calculus", 6), ("variable", 8),
             ("quadratic", 9), ("fraction", 9), ("index", 6),
             ("coefficient", 8), ("arithmetic", 9), ("geometric", 9),
             ("sequence", 7), ("series", 5), ("infinity", 6), ("pi", 3),
             ("sine", 5), ("cosine", 7), ("tangent", 6), ("function", 7),
             ("logarithm", 10), ("factor", 7), ("radical", 7), ("rational", 8),
             ("whole", 6), ("real", 5), ("negative", 8), ("positive", 8),
             ("irrational", 8), ("reciprocal", 9), ("linear", 7), ("axis", 5),
             ("transformation", 10), ("polynomial", 9), ("monomial", 7),
             ("binomial", 8), ("trinomial", 9)]
themes = [fruits, countries, mathterms]

tick = 0
cross = 0

while repeat == "":
    s(1)
    try:
        r = int(
            input(
                "We have 3 themes to choose from: fruits (easy), countries (medium), or mathterms (hard). Choose 0, 1, or 2 for each theme, respectively:"
            ))
        choice = themes[r]
    except IndexError:
        print(
            "You seem to be over ambitious. Chill and choose only from 0 to 2."
        )
        repeat = ''
        continue
    i = random.choice(choice)
    (word, turns) = i
    word = word.lower()
    s(1.5)
    print("The word is ready! You have", turns,
          "guesses. And that can be quite a hint too!")
    wrong = 0
    guess = ["-"] * len(word)
    letterss = "abcdefghijklmnopqrstuvwxyz"
    while wrong <= turns:
        curr = ''
        print("You got", wrong, "wrongs so far. Choose a letter", end='')
        let = input(":")
        let = let.lower()
        print(let)
        s(1)
        if len(let) > 1:
            print("Apparently you decided to guess the word!")
            s(1)
            if let == word:
                print("You've guessed it!")
                break
            else:
                print("Sorry no more guesses for you!")
                break
        if let.isalpha() == False:
            print("Obviously your character isn't here.")
        elif len(let) > 1:
            print(
                "Sorry but my game doesn't support guessing entire words yet, so be patient."
            )
        elif len(let) == 0:
            print("Did you even enter anything? That's quite careless of you.")
        else:
            if (let in word) and (let in letterss):
                print("Character present in word!")
                letterss = letterss.replace(let, "")
                for count in range(len(word)):
                    if word[count] == let:
                        guess[count] = let
                s(1)
                print("The word now is", sep='')
            else:
                print("Character not present!")
                wrong += 1
                print("Your guess currently is still:", end='')
            for l in guess:
                curr += l
            print(curr)
            if curr == word:
                print("You've guessed it!")
                tick += 1
                cross -= 1
                break
            else:
                print("The full word has not been completely found yet.")
                s(1)
    cross += 1
    print("The word is:", word)
    repeat = input(
        "Hit ENTER to go another round. Type something first to exit")
print("Thank you for playing!")
s(1)
print(
    "Before you go, here are how many words you guessed and how many you didn't. Here they are:"
)
s(0.5)
print("Number of words you found:", cross)
print("Number of words you missed:", tick)