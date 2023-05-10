#학점 계산기
#학점, 평점 이벽 -> 2가지에 저장
#입력단 -> 스코어단 -> 출력단
#GPA : 학점*평점/학점
#누계 : 학점 누계를 계thr 하다가, 평점 할 때만 나눠서 누계 만들어주기

#클래스
class CourseHistory:
    #인스턴스 변수 설정
    def __init__(self):
        self.history = []
        self.course_name_dict = {'code' : 10000}
        self.submit_grade = {}
        self.archive_grade = {}

    #점수 변환 함수 클래스 메소드로 변경
    @classmethod
    #함수 정의
    def convert_score(cls, grade):  #문자열로 받음 #클래스 메소드니까 cls추가
        match grade:
            case 'A+':
                return 4.5
            case 'A':
                return 4.0
            case 'B+':
                return 3.5
            case 'B':
                return 3.0
            case 'C+':
                return 2.5
            case 'C':
                return 2.0
            case 'D+':
                return 1.5
            case 'D':
                return 1.0
            case 'F':
                return 0.0



    #과목 코드 부여 인스턴스 메소드로 빼내기
    def allocate_course_code(self, course_name):
        if course_name not in self.course_name_dict:
            new_code = str(int(self.course_name_dict['code'])+1)
            self.course_name_dict['id'] = new_code  #new 코드 저장
            self.course_name_dict[course_name] = new_code  #이름이 키, 코드가 값
            self.course_name_dict[new_code] = course_name  #코드가 키, 이름이 값

            return new_code

        else:
            return self.course_name_dict[course_name]


    #입력칸 인스턴스 메소드로 빼내기
    def input_process(self):
        course_name = input('과목명을 입력하세요: ')
        course_code = self.allocate_course_code(course_name)

        credit = input('학점을 입력하세요: ')
        credit = int(credit)

        grade = input('평점을 입력하세요: ')
        gpa_score = self.convert_score(grade)

        #열람용 학점 처리
        if course_code in self.archive_grade:
            #재수강
            if gpa_score > self.archive_grade[course_code][1]:
                self.archive_grade[course_code] = (credit, gpa_score)
        else:
            self.archive_grade[course_code] = (credit, gpa_score)

        #제출용 학점 처리
        if gpa_score > 0.0:
            if course_code in self.submit_grade:
                # 재수강 처리
                if gpa_score > self.submit_grade[course_code][1]:
                    self.submit_grade[course_code] = (credit, gpa_score)
            else:
                self.submit_grade[course_code] = (credit, gpa_score)

        self.history.append((course_code, credit, grade))

        print('입력되었습니다.')


    #출력 인스턴스 메소드
    def print_process(self):
        for course in self.history:
            print('[' + self.course_name_dict[course[0]] + ']', end='')
            print(str(course[1]) + '학점: ' + course[2])


    #조회 함수
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')

        for course in self.history:
            if course_name == self.course_name_dict[course[0]]:
                print('[' + self.course_name_dict[course[0]] + '] ', end='')
                print(str(course[1]) + '학점: ' + course[2])
                break
        else:
            print('해당하는 과목이 없습니다.')

    #계산
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0

        for course_code in self.submit_grade:
            submit_gpa += self.submit_grade[course_code][0] * self.submit_grade[course_code][1]
            submit_credit += self.submit_grade[course_code][0]

        for course_code in self.archive_grade:
            archive_gpa += self.archive_grade[course_code][0] * self.archive_grade[course_code][1]
            archive_credit += self.archive_grade[course_code][0]

        submit_gpa /= submit_credit
        archive_gpa /= archive_credit

        print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
        print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')

#실행~~
course_history = CourseHistory() #wow;;



#선택지 루프
while True:
    print('작업을 선택하세요.')
    print('     1. 입력')
    print('     2. 출력')
    print('     3. 조회')
    print('     4. 계산')
    print('     5. 종료')

    user_value = input()


    if user_value == '1':
        course_history.input_process()

    elif user_value == '2':
        course_history.print_process()

    elif user_value == '3':
        course_history.query_process()

    elif user_value == '4':
        course_history.calculate_process()

    elif user_value == '5':
        break

    else:
        continue


print('프로그램 종료.')

