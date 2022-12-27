from __future__ import annotations
import random

class Character:
    def __init__(self, name:str='名無しの権兵衛', hp:int=10, str:list=[1,4]):
        self.name:str = name
        self.hp:int = hp
        self.str:list = str
        self.attack_v:int = 0
        
    def attack(self, character:Character) -> bool:
        damage_num:int = random.randint(self.str[0], self.str[1])
        self.attack_v:int = damage_num

        return character.damage(damage_num)

    def damage(self, damage:int) -> bool:
        self.hp -= damage
        if self.hp > 0:
            doA:bool = True
        else:
            doA:bool = False
        return doA

class Fighter(Character):
    def __init__(self, name:str='名無しの権兵衛', hp:int=10, str:list=[1, 3], defence:int=0, sp:int=3):
        super().__init__(name, hp, str)
        self.defence:int = defence
        self.sp:int = sp

    def attack(self, character:Character) -> bool:
        damage_num:int = random.randint(self.str[0], self.str[1])
        print('特殊技を使いますか？使用する場合は「y」を入力、使用しない場合はエンター')
        use_sp = input()
        if use_sp == 'y':
            is_sp = self.reduceSp()
            if is_sp:
                self.attack_v:int = damage_num * 3
            else:
                self.attack_v:int = 0
        else:
            self.attack_v:int = damage_num
        return character.damage(self.attack_v)

    def damage(self, damage:int) -> bool:
        attack_v = damage - self.defence
        super().damage(attack_v)

    def reduceSp(self):
        self.sp -= 1
        if self.sp > 0:
            return True
        else:
            return False