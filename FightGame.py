import random
import Character

player:Character = Character.Character('ぷぷぷ')
player.hp = 12
enemy:Character = Character.Character('てき')

gide:str = 'モンスターエンカウント！\n戦闘開始！'
print(gide)
i = 1
while True:
    if i > 1:
        input(f'\n{i}ターン目')
    if player.attack(enemy):
        print(f'\n{player.name}が{player.attack_v}の攻撃！')
        print(f'{enemy.name}のHPは{enemy.hp}\n  {enemy.name}は生き残った')
    else:
        print(f'\n{player.name}が{player.attack_v}の攻撃！')
        print(f'\n{enemy.name}を倒した')
        break

    if enemy.attack(player):
        print(f'\n{enemy.name}の攻撃、{enemy.attack_v}のダメージ！')
        print(f'{player.name}のHPは{player.hp}\n  {player.name}は生き残った')
    else:
        print(f'\n{enemy.name}の攻撃、{enemy.attack_v}のダメージ！')
        print(f'\n{player.name}は負けた')
        break
    i += 1
print('\n対戦終了')
        