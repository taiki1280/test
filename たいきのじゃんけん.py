import random


win = 0
lose = 0
draw = 0
DICT = {"name": "", "勝敗記録": [win, lose, draw]}


def run():
    DICT["name"] = input("名前を入力してください。")
    i = 1
    print("ただのじゃんけんを開始します。")
    while True:
        cpu_hand = random.randrange(3)
        num = input(
            f"\nじゃんけん第{i}回戦\n"
            + "あなたの手を入力ください。\n"
            + "０：グー\n"
            + "１：チョキ\n"
            + "２：パー\n"
        )
        if num not in ["0", "1", "2"]:
            print("０、１、２以外は受け付けていません。\n")
            continue

        player_hand = int(num)
        print(
            f"貴方の手は{hand(player_hand)}で\n"
            + f"CPUの手は{hand(cpu_hand)}でした。"
        )
        judgement(player_hand, cpu_hand)
        print(
            f"{DICT['name']}さんの記録は\n"
            + f"{DICT['勝敗記録'][0]}勝"
            + f"{DICT['勝敗記録'][1]}敗"
            + f"{DICT['勝敗記録'][2]}分け\n"
            + "です"
        )
        i += 1


def hand(num):
    if num == 0:
        return "グー"
    elif num == 1:
        return "チョキ"
    else:
        return "パー"


def judgement(player_hand, cpu_hand):
    if player_hand == cpu_hand:
        DICT["勝敗記録"][2] += 1
        print("あいこでした！！")
    elif player_hand > cpu_hand or player_hand == 0 and cpu_hand == 2:
        print("貴方の勝ちです！")
        DICT["勝敗記録"][0] += 1
    else:
        print("貴方の負けです！")
        DICT["勝敗記録"][1] += 1


run()
