from __future__ import annotations
import random

class Character:
    def __init__(self, name:str='名無しの権兵衛', hp:int=10, str:list=[1,3]):
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
