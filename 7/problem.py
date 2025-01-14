# def std_weight(height, gender):
#     if gender == "남자" :
#         return height * height * 22
#     elif gender == "여자":
#         return height * height * 21
#     else:
#         print("error")

# height = 175
# weight = height * height * 22
# gender = "남자"
# print(f"키 {height}cm {gender}의 ")

#방법 1

# def get_air_quality(num):
#     if 0 <= num <=30 :
#         return ("좋음")
#     elif 31 <= num <= 80:
#         print("보통")
#     elif 81 <= num <= 150:
#         print("나쁨")
#     elif 151 <= num:
#         print("매우 나쁨")


# print("123",get_air_quality(15))

# #방법 2

# def get_air_quality(num):
#     if 0 <= num <=30 :
#         print("좋음")
#         return 1
#     elif 31 <= num <= 80:
#         print("보통")
#     elif 81 <= num <= 150:
#         print("나쁨")
#     elif 151 <= num:
#         print("매우 나쁨")


# print(get_air_quality(15))

# 4장 selfcheck 첫 글자를 대문자로 만드는 함수, 

def capitalize(sen):
    print(sen.capitalize())

sen = 'the early bird catches the worm.'
capitalize(sen)

