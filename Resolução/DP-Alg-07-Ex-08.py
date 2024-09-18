import random
random_draw_list = random.sample(range(1, 76), 75)
def generate_card():
    card = {
        "B": [],"I": [],"N": [],"G": [],"O": [],}
    min = 1
    max = 15
    for letter in card:
        card[letter] = random.sample(range(min, max), 5)
        min += 15
        max += 15
        if letter == "N":
            card[letter][2] = "0" # free space!
    return card


def print_card(card):
    for letter in card:
        print(letter, end="\t")
        for number in card[letter]:
            print(number, end="\t")
        print("\n")
    print("\n")


def draw(card, list):
    number_drawn = random_draw_list.pop()
    for letter in card:
        i = 0
        for number in card[letter]:
            if number == number_drawn:
                card[letter][i] = "0"
            i += 1
    return number_drawn


def check_win(card):
    win = False
    if card["B"][0] == "0" and card["I"][1] == "0" and card["N"][2] == "0" and card["G"][3] == "0" and card["O"][4] == "0":
        win = True
    elif card["O"][0] == "0" and card["G"][1] == "0" and card["N"][2] == "0" and card["I"][3] == "0" and card["B"][4] == "0":
        win = True
    elif card["B"][0] == "0" and card["O"][4] == "0" and card["B"][4] == "0" and card["O"][0] == "0":
        win = True
    for letter in card:
        if(len(set(card[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in card:
            if card[letter][i] == "0":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win


#main
card = generate_card()
print_card(card)

print("\nContinue apertando enter ou escreva s para sair.\n")
user_input = input()
win = check_win(card)
balls_till_win = 0

while win == False and user_input != "s":
    number_drawn = draw(card, random_draw_list)
    balls_till_win += 1

    print("Number drawn: {number_drawn}".format(number_drawn=number_drawn))
    print(f"Total balls drawn: {balls_till_win}.\n")
    print_card(card)

    win = check_win(card)

    user_input = input()
if win == True:
    print(f"\nBingo! Total balls to win: {balls_till_win}.")
else:
    print("Cartela Perdedora.")