print('작업을 선택하세요.\n1. 입력\n2. 계산\n')
yeah = int(input())

hakk = 0
py = 0

if yeah == 1:

    print('몇 과목을 입력하실 건가요?\n')
    global number
    number = int(input())

    print('F인 과목이 몇개인가요?\n')
    global F
    F = int(input())
    a = 1
    global totalF
    totalF = 0
    print('F인 과목의 학점을 하나씩 입력해주세요')
    while a <= F:
        totalF += int(input())
        a += 1

    t = 1
    while t <= number:
        print('학점을 입력하세요:\n')
        hak = int(input())
        hakk += hak

        print('평점을 입력하세요:\n')
        pyeong = input()

        print('입력되었습니다.')

        if pyeong == 'A+':
            py += 4.5
        elif pyeong == 'A':
            py += 4.0
        elif pyeong == 'B+':
            py += 3.5
        elif pyeong == 'B':
            py += 3.0
        elif pyeong == 'C+':
            py += 2.5
        elif pyeong == 'C':
            py += 2.0
        elif pyeong == 'D+':
            py += 1.5
        elif pyeong == 'D':
            py += 1.0
        elif pyeong == 'F':
            py += 0.0

        t += 1

    print("학점을 계산하시겠습니까? : (Y / N)\n")
    answer = input()
    if answer == 'N':
        print("프로그램을 종료합니다.\n")
    elif answer == 'Y':
        print("메뉴에서 2번을 선택해주세요.")
        print('1. 입력\n2. 계산\n')
        yeah = int(input())
    else:
        print("올바르게 입력해주세요.\n")


elif yeah == 2:
    print('제출용:' + str(hakk - totalF) + '학점')
    print('(GPA: ' + (py / str(number - F)) + ')')
    print('열람용:' + str(hakk) + '학점')
    print('(GPA: ' + (py / number) + ')')
    print('\n프로그램을 종료합니다.')

else:
    print('올바른 숫자를 입력해주세요.\n 프로그램을 종료합니다.')