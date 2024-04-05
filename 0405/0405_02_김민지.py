'''
작성일 : 2024년 4월 5일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 윤년 판단

[문제분석]
    필요한 변수 : year
    윤년은
    연도를 4로 나누어 떨어지면 윤년이다.
    연도를 4로 나누어 떨어져도 100으로 나누어 떨어지지 않아야
    연도를 400으로 나누어 떨어지는 해는 무조건 윤년이다.

        
[알고리즘]
    1. 년도를 입력한다.
    2. 만약 연도가 4로 나누어떨어지거나 100으로 나누어 떨어지지않거나 
    400으로 나누어 떨어지면
        2-1. 윤년입니다.
    3. 아니면 
        3-1. 윤년이 아닙니다.
'''

year = int(input("년도를 입력 :"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print(f"{year}년도는 윤년입니다.")
else :
    print(f"{year}년도는 윤년이 아닙니다.")