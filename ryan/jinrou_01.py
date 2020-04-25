import random
import copy
import math
from time import sleep

side_list = ('市民', '人狼', '騎士', '占い師', '端山')
citizen_list = ('市民', '騎士', '占い師')
jinrou_list = ('人狼',)

player_list = []
use_list = []

player_list_backup = []
use_list_backup = []

citizen_player = []
jinrou_player = []

vote_list = ['@0',]
death_list = []

enter_yes = ['yes', 'y', 'ｙ']
enter_no = ['no', 'n', 'ｎ']


class jinrou_game :

    def __init__ (self, start) :
        print(start)
        sleep(1)

    '''名前を入力する処理'''
    def player_setting (self, number_of_player) :
        player_name = 0
        while player_name < number_of_player :
            player = str(input('{}人目の名前を入力してください --> '.format(player_name + 1)))
            if (player in player_list) == False :
                player_list.append(player)
                player_name += 1
            else:
                print('※ すでに登録されている名前です。同じ名前は避けてください。\n')

    '''役職を設定する処理'''
    def side_setting (self, number_of_player) :
        print('\n役職設定\n下記の中から役職を選んでください。\n')
        print('[市民側の役職]')
        for index in range(len(citizen_list)) :
            print(' ・', citizen_list[index])
        print('[人狼側の役職]')
        for index in range(len(jinrou_list)) :
            print(' ・', jinrou_list[index])
        while True :
            select = input('役職名を入力してください --> ')
            if (select in citizen_list) == True or (select in jinrou_list) == True:
                use_list.append(select)
                if number_of_player == len(use_list) :
                    if ('人狼' in use_list) == True:
                        break
                    else :
                        print('※ 人狼が一匹以上いないとゲームが始められません…')
                        print('もう一度設定しなおしてください\n')
                        use_list.clear()
            else :
                print('※ 正確に役職名を入力しないと追加されません…\n')

    '''会議時間を決める処理'''
    def timer_setting (self, ) :
        while True :
            print('\n会議時間を決めてください。')
            timer = input('なお、入力された数値は秒数として設定されます。')
            if (timer.isnumeric()) == True :
                break
            else :
                print('\n※ 数値を入力してください。')
        timer_set = int(timer)
        print(timer_set, '秒を会議時間として設定しました。')
        return timer_set

    '''会議時間の制御'''
    def discussion_turn(self, timer) :
        while timer != 0 :
            sleep(1)
            timer -= 1
            if (timer % 300 == 0 or timer == 60) and timer != 0 :
                remaining_time = timer / 60
                print('残り時間は', math.floor(remaining_time, '分です。'))
        print('時間切れです\n')
        sleep(1)

    '''初日死亡の翁'''
    def first_day_death (self, ) :
        first_death = random.choice(player_list)
        self.death_player(first_death)
        return first_death

    '''朝の処理'''
    def morning_turn(self, dead) :
        print('おそろしいいいいいいい\n昨晩の犠牲者は…', end = '')
        sleep(2)
        if dead != 'nothing' :
            print('[[{}]]さんです。{}さんは幽霊となり今後一切の発言を禁じます。'.format(dead, dead))
        else :
            print('いませんでした。')

    '''投票の処理'''
    def vote_turn(self, ) :
        print('投票の時間です。\n')
        vote_list.clear()
        while len(vote_list) < len(player_list) :
            vote_list.append(0)
        vote_member = 'nothing'
        for index in range(len(player_list)) :
            while True :
                print(player_list[index], 'さんの投票の時間です。')
                vote_member = input('投票する人物の名前を入力してください。 --> ')
                if vote_member == player_list[index] :
                    print('※ 自分以外の名前を入力してください\n')
                else:
                    print()
                    break
            vote_index = player_list.index(vote_member)
            votes = int(vote_list[vote_index])
            votes += 1
            vote_list[vote_index] = votes
        punishment_player = player_list[vote_list.index(max(vote_list))]
        sleep(2)
        print('今日処刑される人は…', end = '')
        sleep(2)
        print(punishment_player, 'さんです。{}さんは幽霊となり今後一切の発言を禁じます。'.format(punishment_player))
        sleep(2)
        self.death_player(punishment_player)

    '''死体処理'''
    def death_player (self, death) :
        death_index = player_list.index(death)
        use_list.remove(death_index)
        death_list.append(death)
        player_list.remove(death)

        if (death in citizen_player) == True :
            citizen_player.remove(death)
        else :
            jinrou_player.remove(death)

    '''人狼の行動処理'''
    def jinrou_action (self, ) :
        print('\nここからは人狼の夜のアクションです')
        sleep(2)
        print('[今回の人狼リスト]')
        for index in range(len(jinrou_player)) :
            print(' ・', jinrou_player[index], 'さん')
        print('\n[捕食対象者リスト]')
        for index in range(len(citizen_player)) :
            print(' ・', citizen_player[index], 'さん')
        while True :
            eat_player = input('\n今夜襲い掛かる人物の名前を入力してください：')
            if (eat_player in citizen_player) != True :
                print('※ 捕食対象者リストの中から選んでください。\n')
                sleep(1)
            else :
                print(eat_player, 'さんで本当によろしいですか？')
                y_or_n = input('（ｙ／ｎ） --> ')
                if (y_or_n in enter_yes) == True :
                    break
                elif (y_or_n in enter_no) == True :
                    pass
                else :
                    print('あ  ま  り  調  子  に  乗  る  な  よ  ？')
                    sleep(2)
        print(eat_player, 'さんを食べちゃった☆彡てへぺろ')
        self.death_player(eat_player)
        return eat_player

    '''ゲーム終了後の処理'''
    def game_set (self) :
        if len(citizen_player) > len(jinrou_player) :
            print('\n人狼全滅じゃんやったぜ☆彡\n村人側の勝利です。')
        else :
            print('\n村人は死に絶えたのだ…\n人狼側の勝利です。')
        print()
        print('\n[[役職確認]]\n [市民サイド]')
        for index in range(len(citizen_player_backup)) :
            player_index = player_list_backup.index(citizen_player_backup[index])
            print(' ・', player_list_backup[player_index], 'さん -->', use_list_backup[player_index])
        print('\n[人狼サイド]')
        for index in range(len(jinrou_player_backup)) :
            player_index = player_list_backup.index(jinrou_player_backup[index])
            print(' ・', player_list_backup[player_index], 'さん -->', use_list_backup[player_index])

    def knight_acction (self, death) :
        protect_member = 'nothing'
        if ('騎士' in use_list) != True :
            pass
        else :
            print('\nここからは騎士のアクションです。')
            knight_index = use_list.index('騎士')
            print('今回の騎士 -->', player_list[knight_index])
            print('[[現在生き残っているメンバーリスト]]')
            for index in range(len(player_list)) :
                if index != knight_index :
                    print(' ・', player_list[index])
            while True :
                protect_member = input('\nリストの中から、今晩守るメンバーを選択してください。 --> ')
                if protect_member == player_list[knight_index] :
                    print('※ 自分以外の名前を入力してください。')
                    sleep(1)
                else :
                    if (protect_member in player_list) == True :
                        print(protect_member, 'さんでよろしいですか？')
                        y_or_n = input('（ｙ／ｎ） --> ')
                        if (y_or_n in enter_yes) == True :
                            print('今晩は、', protect_member, 'さんを守ります。')
                            break
                        elif (y_or_n in enter_no) == True :
                            sleep(1)
                        else :
                            print('ｙかｎ以外を入力してもｎを選択されたことになります\n')
                            sleep(1)
                    else :
                        print('※ リストの中の人物の名前を入力してください。\n')
                        sleep(1)
        if protect_member == death :
            death = 'nothing'
        return death

'''
    def diviner_acction (self,) :
        if ('占い師' in use_list) != True :
            pass
        else :
            print('\nここからは占い師のアクションです。')
            diviner_index = use_list.index('占い師')
            print('今回の占い師 -->', player_list[diviner_index])
            print('[[現在生き残っているメンバーリスト]]')
            for index in range(len(player_list)):
                if index != diviner_index :
                    print(' ・', player_list[index])
            while True :

'''



set_game = jinrou_game('\n人狼ゲームの初期設定を行います。\n')

while True :
    number_of_player = int(input('プレイヤー人数を入力してください：'))
    set_game.player_setting(number_of_player)
    set_up = str(input('\n参加人数： {}人'.format(number_of_player)))
    print("参加メンバー：")
    for index in range(len(player_list)) :
        print(player_list[index], 'さん')
    print('以上の設定でよろしかったですか？')
    y_or_n = input('（ｙ／ｎ） --> ')
    if (y_or_n in enter_yes) == True :
        break
    elif (y_or_n in enter_no) == True :
        player_list.clear()
    else :
        print('ｙかｎ以外を入力してもｎを選択されたことになります')
        player_list.clear()

while True :
    set_game.side_setting(number_of_player)
    print('[役職リスト]')
    for index in range(len(use_list)) :
        print(' ・', use_list[index])
    print('以上の設定でよろしかったですか？')
    y_or_n = input('（ｙ／ｎ） --> ')
    if (y_or_n in enter_yes) == True :
        break
    elif (y_or_n in enter_no) == True :
        use_list.clear()
    else :
        print('ｙかｎ以外を入力してもｎを選択されたことになります')
        use_list.clear()


random.shuffle(use_list)
player_list_backup = copy.copy(player_list)
use_list_backup = copy.copy(use_list)

for index in range(len(player_list)):
    #print('{} さんの役職 --> {}'.format(player_list[index], use_list[index]))
    if '人狼' != use_list[index] :
        citizen_player.append(player_list[index])
    else :
        jinrou_player.append(player_list[index])

citizen_player_backup = copy.copy(citizen_player)
jinrou_player_backup = copy.copy(jinrou_player)

timer_set = set_game.timer_setting()
print('\n初日の死亡を加えますか？')
first_dead = input('（ｙ／ｎ） --> ')

if (first_dead in enter_yes) == True :
    print('初日の被害をありにしました。\n')
elif (first_dead in enter_no) == True :
    dead = 'nothing'
    print('初日の被害をなしにしました。\n')
else :
    print('（ｙ／ｎ）以外を入力した場合、自動的にｎの処理になります。')
    dead = 'nothing'

print('\n初日の占いは加えますか？')
first_divination = input('（ｙ／ｎ） --> ')

if (first_dead in enter_yes) == True :
    print('初日の占いをありにしました。\n')
elif (first_dead in enter_no) == True :
    print('初日の占いをなしにしました。\n')
else :
    print('（ｙ／ｎ）以外を入力した場合、自動的にｎの処理になります。')

sleep(2)
print('人狼ゲームを始めます。')
sleep(1)

if (first_dead in enter_yes) == True :
    dead = set_game.jinrou_action()

while True :
    set_game.morning_turn(dead)
    if len(citizen_player) <= len(jinrou_player) :
        break
    print('それでは話し合いを始めてください。')
    set_game.discussion_turn(timer_set)
    sleep(1)
    set_game.vote_turn()
    if len(citizen_player) <= len(jinrou_player) :
        break
    elif len(jinrou_player) == 0:
        break
    dead = set_game.jinrou_action()
    dead = set_game.knight_acction(dead)

set_game.game_set()