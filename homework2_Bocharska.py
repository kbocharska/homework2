import os
import random
import time


cards_hidden = [
    [" ", 1, 2, 3, 4],
    [1, "X", "X", "X", "X"],
    [2, "X", "X", "X", "X"],
    [3, "X", "X", "X", "X"],
    [4, "X", "X", "X", "X"]
]
cards_opened = [
    [" ", 1, 2, 3, 4],
    [1, "X", "X", "X", "X"],
    [2, "X", "X", "X", "X"],
    [3, "X", "X", "X", "X"],
    [4, "X", "X", "X", "X"]
]

def symbol_position():
    symbols = ["!", "@", "#", "$", "%", "&", "*", "("] * 2
    random.shuffle(symbols)
    return symbols

def card_check(coordinates1, coordinates2):
        k1 = coordinates1[0]
        n1 = coordinates1[1]
        k2 = coordinates2[0]
        n2 = coordinates2[1]
        if cards_hidden[k1][n1] == cards_hidden[k2][n2]:
            return True
        return False

def coordinates_validation(coordinates):
    if len(coordinates) != 2:
        return False
    elif not coordinates[0].isdecimal:
        return False
    elif int(coordinates[0])>4:
        return False
    elif not coordinates[1].isdecimal:
        return False
    elif int(coordinates[1])>4:
        return False
    return True

def fill_cards():
    for i in range(5):
        for j in range(5):
            if i == 0 or j == 0:
                pass
            else:
                cards_hidden[i][j] = pairs[j-1 + 4 * (i-1)]


def print_cards(coordinates1, coordinates2):
    for i in range(5):
        for j in range(5):
            if i == coordinates1[0] and j == coordinates1[1] or i == coordinates2[0] and j == coordinates2[1]:
                print(cards_hidden[i][j], end =" ")
            else:
                print(cards_opened[i][j], end = " ")
        print()

def print_grid(grid):
    os.system("clear")
    for i in range(5):
        for j in range(5):
                print(grid[i][j], end = " ")
        print()

matches = 0
guesses = 0
pairs = symbol_position()
fill_cards()
print_grid(cards_hidden)
time.sleep(5)
os.system("clear")

while True:

    card_coordinates1 = input("Enter the coordinates of the first card (row, column) ").split(", ")
    while not coordinates_validation(card_coordinates1):
        card_coordinates1 = input("Wrong coordinates. Try again ").split(", ")
    card_coordinates2 = input("Enter the coordinates of the second card (row, column)").split(", ")
    while not coordinates_validation(card_coordinates2) and card_coordinates1 != card_coordinates2:
        card_coordinates2 = input("Wrong coordinates. Try again ").split(", ")

    card_coordinates1 = [int(i) for i in card_coordinates1]
    card_coordinates2 = [int(i) for i in card_coordinates2]

    print_cards(card_coordinates1, card_coordinates2)
    time.sleep(3)

    i1 = card_coordinates1[0]
    j1 = card_coordinates1[1]
    i2 = card_coordinates2[0]
    j2 = card_coordinates2[1]

    if card_check(card_coordinates1, card_coordinates2):
        matches +=1
        cards_opened[i1][j1] = cards_hidden[i1][j1]
        cards_opened[i2][j2] = cards_hidden[i1][j1]
    else:
        cards_opened[i1][j1] = "X"
        cards_opened[i2][j2] = "X"

    print_grid(cards_opened)

    guesses += 1


    if matches == 8:
        print("You won!\nThe number of guesses is", guesses)
        answer = input("Do you want to play again? (y or n) ")
        while answer != "y" and answer != "n":
            answer = input("Something is wrong. Do you want to play again? (y or n) ")
        if answer == "n":
            break
