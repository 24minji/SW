'''
작성일 : 2024년 5월 30일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 두 개의 정수를 입력받아 큰 수를 출력하시오.
        큰 수를 찾는 부분을 함수로 작성합니다.
        
[기존 알고리즘]
    1. 두 수를 입력 받는다.
    2. 비교 판단. num1 > num2
        2-1. num1이 크다.
    3. 아니면 (num1 < num2)
        3-1. num2가 크다.
        
[문제분석]
    큰 수 찾는 부분은 함수로 작성한다.
    결과는 함수를 호출한 메인으로 돌려준다.
    메인은 두 수를 입력 받는다.
    메인에서 결과를 출력한다.
    
[알고리즘]
    1. 함수
        3) 메인으로부터 두 수를 전달 받는다.
        4) 두 수를 가지고 비교한다.
            만약 num1 > num2 :
            4-1) num1을 리턴한다.(돌려준다.)
        5) 아니면
            5-1) num2를 리턴한다.
    
    2. 메인
        1) 두 수를 입력 받는다.
        2) 두 수를 가지고 함수를 호출하고 돌려받은 값을 변수에 저장한다.
        6) 큰 수(돌려 받은 수)를 출력한다.(결과 출력)
        
        2) 두 수를 가지고 함수를 호출하여 돌려 받은 결과를 출력한다.
'''
print(":: 두 개의 정수 중 큰 수 출력 ::")

# 함수 선언
def max_num(num1, num2) :
    if num1 > num2 :
        return num1
    else :
        return num2

# 메인
num1 = int(input("첫번째 수를 입력 :"))
num2 = int(input("두번째 수를 입력 :"))

result = max_num(num1, num2)
print(f"{num1}과 {num2} 중 큰 수는 {result}입니다.")

print()

print(f"{num1}과 {num2} 중 큰 수는 {max_num(num1, num2)}입니다.")