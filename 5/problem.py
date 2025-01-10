import random

people = range(1,21)

people = list(people)

random.shuffle(people)
print(people)

p_1=random.sample(people,4)
print(p_1)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {p_1[0]}")
print(f"커피 당첨자 : {p_1[1:]}")
print("-- 축하드립니다! --")