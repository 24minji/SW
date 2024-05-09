'''
작성일 : 2024년 5월 9일
작성자 : 컴퓨터공학부 202495002 김민지
설명 : 사용자로부터 입력받은 문장에서 스페이스바가 몇 개인지 출력하시오.
        그리고 스페이스바를 없앤 문장을 출력하시오.

[알고리즘]
    1. 문장을 입력받는다.
    2. 스페이스가 몇 개인지 출력한다.
    3. 스페이스를 삭제한 문장을 출력한다.
'''
text = input("문장을 입력하세요. :")
print("문자열에 스페이스가 몇 개 있나요?", text.count(' '))
print("문장에서 스페이스 삭제 :", text.replace(' ', ''))