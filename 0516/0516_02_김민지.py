'''
작성일 : 2024년 5월 16일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 다음과 같은 튜플을 생성하고,
        각 요소(숫자)가 튜플에 몇 개 있는지 출력하시오.
        
    len(), count(), 0번지부터
    
    개수를 찾은 숫자는 리스트에 따로 저장한다.
    이미 찾은 숫자는 또 개수를 찾을 필요가 없다.
'''
num = (1,5,4,9,7,8,3,2,1,6,5,9,7,1)
print("생성된 튜플 :", num)

for i in range(len(num)) : 
    print(num[i], "의 개수 :", num.count(num[i]))
    
print()
print("중복 제거하고 개수 찾기")

num_list = []   # 중복 출력하지 않기 위한 빈 리스트 생성.

# 리스트에 숫자가 있는지 없는지 판단.
# 만약 숫자가 리스트에 있으면 패스
# 없으면 개수 찾고, 리스트에 추가. => 다음 수가 있는지 체크
for i in range(len(num)) :
    if num[i] in num_list :
        continue    #돌아가시오. 반복의 처음으로
    else :
        print(num[i], "의 개수 :", num.count(num[i]))
        num_list.append(num[i])  # 리스트에 추가.
        
print()
num_list = []   # 초기화

for i in range(len(num)) :
    if num[i] not in num_list :  # 리스트에 숫자가 없으면
        print(num[i], "의 개수 :", num.count(num[i]))
        num_list.append(num[i])  # 리스트에 추가.