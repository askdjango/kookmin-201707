import json

try:
    with open("students.json", "rt", encoding="utf8") as f:
        json_string = f.read()
    students = json.loads(json_string)
except FileNotFoundError:
    students = []

print("---- 제공메뉴 ----")
print(" 1) 학생 전체목록")
print(" 2) 성적 평균 TOP3")
print(" 3) 학생 추가/수정")
print(" 4) 학생 삭제")
menu_number = input("메뉴 선택 : ")

print("선택한 메뉴 :", menu_number)

if menu_number == "1":
    print()
    print("# 학생 전체 목록")
    for student in students:
        print('{} {} {} {} {}'.format(student['이름'], student['연락처'],
                                      student['국어'], student['영어'], student['수학']))
elif menu_number == "2":
    print()
    print("# 성적 평균 TOP3")
elif menu_number == "3":
    print("학생의 이름/연락처/국어/영어/수학점수를 입력해주세요.")
    print("입력 예) 김파이 01012341234 90 80 60")
    line = input("입력해주세요. : ")
    words = line.split(' ')
    studuent = {
        '이름': words[0],
        '연락처': words[1],
        '국어': words[2],
        '영어': words[3],
        '수학': words[4],
    }
    students.append(studuent)
elif menu_number == "4":
    print()
    print("# 학생 삭제")
else:
    print("에러) 지원하지 않는 메뉴입니다.")

json_string = json.dumps(students, ensure_ascii=False)
with open("students.json", "wt", encoding="utf8") as f:
    f.write(json_string)
print()
print("저장했습니다.")
