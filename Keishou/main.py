import human

# human01 = human.Human('ああああああ', 20)
# human02 = human.Human('いいいいいい', 30)
# human01.introduce()
# human02.introduce()

# human03 = human.Student('うううううう', 40)
# human04 = human.Student('ええええええ', 50)
# human03.introduce()
# human04.introduce()

human_list = [
    human.Human('Aさん', 10),
    human.Student('Bさん', 20),
    human.Human('Cさん', 30),
    human.Student('Dさん', 40)
]

for h in human_list:
    h.introduce()