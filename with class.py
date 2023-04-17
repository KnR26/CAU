#학점 계산기
#학점, 평점 이벽 -> 2가지에 저장
#입력단 -> 스코어단 -> 출력단
#GPA : 학점*평점/학점
#누계 : 학점 누계를 계쏙 하다가, 평점 할 때만 나눠서 누계 만들어주기


#함수 정의
def convert_score(grade):  #a문자열로 방ㄷ앗다
    match grade:
        case 'A+':
            score = 4.5
        case 'A':
            score = 4.0
        case 'B+':
            score = 3.5
        case 'B':
            score = 3.0
        case 'C+':
            score = 2.5
        case 'C':
            score = 2.0
        case 'D+':
            score = 1.5
        case 'D':
            score = 1.0
        case 'F':
            score = 0.0
    return score

#반복
submit_credit, archive_credit = 0,0
submit_gpa, archive_gpa = 0.0, 0.0
course_name_dict = {}
course_list = []
show_all = str()

while True:
    print('작업을 선택하세요.')
    print('     1. 입력')
    print('     2. 출력')
    print('     3. 계산')

    user_value = input()
    value = int(user_value)

    match value:
        case 1:
            #입력
            print('과목명을 입력하세요:')
            user_value = input()
            course_name = str(user_value)

            print('학점을 입력하세요:')
            user_value = input()
            credit = int(user_value)

            print('평점을 입력하세요:')
            user_value = input()
            Gpa = str(user_value)
            gpa = convert_score(user_value)

            print('입력되었습니다.\n')

            #계산
            if gpa > 0:
                submit_credit += credit
                submit_gpa += gpa * credit
            archive_credit += credit
            archive_gpa += gpa * credit

            #정보저장
            course_code = 10000 + 1*len(course_name_dict)
            course_name_dict[course_code] = course_name
            credit_information = (course_code,credit,Gpa)
            course_list.append(credit_information)

            #출력준비
            show = '[' + course_name + '] ' + str(credit) + '학점: ' + Gpa + '\n'
            show_all += show




        case 2:
            # 출력
            print (show_all)


        case 3:
            # 계산
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit
            print('제출용: '+ str(submit_credit)+' (GPA:'+ str(submit_gpa)+')')
            print('열람용: '+ str(archive_credit) + ' (GPA:' + str(archive_gpa) + ')')

            print('\n프로그램을 종료합니다.')


            ...
            break
