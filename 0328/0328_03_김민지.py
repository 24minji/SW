'''
작성일 : 2024년 3월 28일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 정수를 입력받아 양수인지 음수인지 판단하시오.

[문제분석]
    필요한 변수는 무엇?
    "00은 양수입니다.", "00은 음수입니다." 출력
    0보다 큰수 -> 양수
    0보다 작은수 ->음수
    점수를 입력받는다. -> 정수로 변화 -> 변수에 저장
[알고리즘]
    1. 정수를 입력받는다.
    2. 정수가 0보다 크면
        2-1 "00은 양수입니다."
    3. 아니면
        3-1 "00은 음수입니다."
    4. "감사합니다." 출력한다.
          => 조건과 상관없이 무조건 출력
'''
num = int(input("정수를 입력하시오 :"))
if num > 0 :
    print(num, "은 양수입니다.")
else :
    print(num, "은 음수입니다.")
    
print("감사합니다.")