# 1번 문제

#a
student = ["김철수", "윤", "민수", "지영", "수진"]

student.append("동현")
print(student)

#b
student.remove("민수")
print(student)

#c
student_1 = sorted(student)
print(student_1)

#d
print(student_1[1::2])

#e
min_name = min(student, key=len)
max_name = max(student, key=len)

print("가장 긴 이름은 "+max_name+"입니다.")
print("가장 짧은 이름은 "+min_name+"입니다.")

# 2번 문제

#a
fruit_inventory = {
    "사과": 100,
    "바나나": 1500,
    "포도": 2000,
    "딸기": 3000
}

del fruit_inventory["사과"]

fruit_inventory["오렌지"] = 1500

print(fruit_inventory)

#b
fruit_inventory["수박"] = 5000
print(fruit_inventory)

#c
# 오렌지를 두번째 줄로 어떻게 옮겨야할지 모르겠어요...ㅠㅠ