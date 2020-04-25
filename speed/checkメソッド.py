import random


def create_trump():
    deck = []
    p1_deck = []
    p2_deck = []
    p1_hand = []
    p2_hand = []
    battle_field = []
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for _ in range(4):
        deck += num
    # トランプの半分の数値
    half = int(len(deck) / 2)
    # デッキの半分を二人に配布
    for _ in range(half):
        p1_deck.append(deck.pop(random.randrange(len(deck))))
        p2_deck.append(deck.pop(random.randrange(len(deck))))
    print("deck", deck)
    print("")
    print("p1の山札")
    print(p1_deck)
    print("p2の山札")
    print(p2_deck)
    print("")
    battle_field.append(p1_deck.pop(random.randrange(len(p1_deck))))
    battle_field.append(p2_deck.pop(random.randrange(len(p2_deck))))
    for _ in range(4):
        p1_hand.append(p1_deck.pop(random.randrange(len(p1_deck))))
        p2_hand.append(p2_deck.pop(random.randrange(len(p2_deck))))
    print("バトルゾーン")
    print(battle_field)
    print("p1の手札")
    print(p1_hand)
    print("p2の手札")
    print(p2_hand)
    # 出せるものがまだ存在するかのチェック
    print(check(battle_field, p1_hand, p2_hand))


def check(battle_field, p1_hand, p2_hand):
    check = []
    for left in battle_field:
        for p1 in p1_hand:
            if left + 1 == p1 or left - 1 == p1 or left + 12 == p1 or left - 12 == p1:
                check.append("T")
        for p2 in p2_hand:
            if left + 1 == p2 or left - 1 == p2 or left + 12 == p2 or left - 12 == p2:
                check.append("T")
    if "T" in check:
        return str(len(check)) + "個存在"
    else:
        return "一つも存在しない"


def next_turn():
    print("aaaaaa")


create_trump()
