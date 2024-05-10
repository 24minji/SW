'''
작성일 : 2024년 5월 10일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 1부터 100사이의 정수형 난수를 10개 생성하여 리스트에 저장하고,
        리스트에서 가장 큰 값과 작은 값을 출력한 뒤,
        리스트 값의 합계와 오름차순으로 정렬된 리스트를 출력하시오.
    
    [문제분석]
        랜덤 수는 import random을 포함시켜야 한다.
        랜덤 수 생성하기 위해서는 메소드 random.radint(1,100)을 사용한다.
        
    [알고리즘]
        1. 빈 리스트 생성.
        2. 10번 반복하면서
            2-1. 랜덤 수 생성하여 리스트에 추가.
        3. 가장 큰 값과 작은 값, 합계, 오름차순 정렬 출력
'''
# random 모듈 사용 선언
import random

num = []    # 빈 리스트 생성.

for i in range(10) :
    num.append(random.randint(1,100))
    
print("생성된 리스트 :", num)
print("가장 큰 값:", max(num))
print("가장 작은 값:", min(num))
print("전체 요소의 합 :", sum(num))

num.sort()
print("오름차순 정렬 :", num)