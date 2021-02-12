# 파이썬에서 함수를 정의할 때 def라는 키워드를 썼던 것처럼 파이썬에서
# 클래스를 정의하려면 class 라는 키워드를 사용합니다.
# 클래스를 사용하는 목적이 변수와 함수를 묶어서 하나의 새로운 객체(타입)로
# 만드는 것이기 때문에 당연히 클래스에 변수나 함수를 포함시켜 클래스를 정의할 수 있습니다.
# 다만 위 코드에서는 가장 간단한 형태의 클래스 정의를 보여주기 위해 변수나 함수를 넣지
# 않고 pass라는 키워드만 사용했습니다.
# pass 키워드를 사용하면 클래스 내부에 아무것도 넣지 않은 상태로 클래스를 정의할 수 있습니다.

# 파이썬에서 클래스를 정의한다는 것은 새로운 데이터 타입을 정의한 것이기 때문에
# 이를 실제로 사용하려면 인스턴스라는 것을 생성해야 합니다.
# 클래스와 인스턴스의 관계를 붕어빵을 만드는 작업에 비유해 보면
# 클래스를 정의하는 것은 붕어빵을 만들 때 사용하는 기본 틀을 제작하는 것에 해당합니다.
# 잉어빵, 황금 붕어빵과 같은 차별화된 붕어빵을 만들기 위해 틀을 잘 정의하는 것이지요.
# 그러나 아무리 틀을 예쁘고 정교하게 만들었다고 해서 붕어빵이 나오는 것은 아닙니다.
# 실제로 먹을 수 있는 붕어빵을 만들려면 붕어빵 틀에 반죽을 넣고 붕어빵을 구워야 합니다.
# 이처럼 붕어빵 틀에 반죽을 넣어서 만들어진 붕어빵이 인스턴스에 해당합니다.

# BusinessCard 클래스에 사용자로부터 데이터를 입력받고 이를 저장하는 기능을 수행하는 함수를
# 추가해보겠습니다.
# 참고로 클래스 내부에 정의돼 있는 함수를 특별히 메서드(method)라고 합니다.
# 다음 코드는 BusinessCard 클래스에 set_info라는 메서드를 추가한 것입니다.
# 메서드를 정의할 때도 함수를 정의할 때와 마찬가지로 def 키워드를 사용합니다.
# set_info 메서드는 네 개의 인자를 받는데, 그중 name, email, addr은 사용자로부터 입력받은
# 데이터를 메서드로 전달할 때 사용하는 인자입니다.

# 내부에 정의된 함수인 메서드의 첫 번째 인자는 반드시 self 여야 한다고 외우길 바랍니다.
# 위 코드에서 메서드 내부를 살펴보면 메서드 인자로 전달된 name, email, addr 값을
# self.name, self. email, self.addr이라는 변수에 대입하는 것을 볼 수 있습니다.
# 앞서 여러 번 설명한 것처럼 파이썬에서 대입은 바인딩을 의미합니다.
# 따라서 set_info 메서드의 동작은  메서드 인자인 name, email, addr이라는 변수가 가리키고 있던 값을
# self.name, self.email, self.addr이 바인딩하는 것입니다.

class BusinessCard:  # class명 첫자는 항상 대문자로 쓴다.
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


member1 = BusinessCard()
type(member1)

member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")
member1.name
member1.email
member1.addr

member2 = BusinessCard()
member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")


class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("--------------------")


member1.print_info()

# 자동 생성되는 메서드 : _init_ ================


class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("--------------------")


member = BusinessCard('Sarang Lee', 'sarang.lee@naver.com', 'Kyunggi')
member.print_info()


### 주소록 만들기 ####
# TEST version
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def run():
    kim = Contact('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    kim.print_info()


if __name__ == '__main__':
    run()

# 사용자 data input version


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    print(name, phone_number, e_mail, addr)


def run():
    set_contact()


if __name__ == '__main__':
    run()

# 메인메뉴 구성하기
# TEST version


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def run():
    while 1:
        menu = print_menu()
        if menu == 4:
            break


run()

# 연락처 입력 함수 ================================
# 저장 함수
# 다시 불러오기
# final.


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()


def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()


def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def print_contact(contact_list, name):
    for contact in contact_list:
        if contact.name == name:
            contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        if menu == 2:
            name = input("Name: ")
            print_contact(contact_list, name)
        if menu == 3:
            name = input("Name: ")

        elif menu == 4:
            store_contact(contact_list)
            break


if __name__ == "__main__":
    run()


### 클래스와 함수 #######################################

# 1. 함수 생성 ======================================
def mat(name, current=0, value=0):
    print('종목명 : %s \n 현재금액 : %s \n 거래량 : %s' % (name, current, value))
    # pass #아무것도 안하고 통과


mat('키움증권', 5000, 100000)

####


def condition(name=None, current=0):
    if current > 4000:
        print('종목명: %s, 현재가 : %s' % (name, current))


a_dict = {'종목명': '삼성', '현재가': 5000}
condition(name=a_dict['종목명'], current=a_dict['현재가'])

# 2. 클래스 생성========================================
# self : 임시 data 저장소


class B_school():
    def __init__(self):
        print('B 클래스입니다.')
        print(dir(self))


B_school()
###


class B_school():
    def __init__(self):
        print('B 클래스입니다.')
        self.student_name = '원빈'


B_school().student_name


class A_school():
    def __init__(self):
        print('A 클래스입니다.')
        bb = B_school()
        self.student_name = bb.student_name
        print(self.student_name)


A_school()


###
class B_school():
    def __init__(self):
        print('B 클래스입니다.')

    def stock(self, student_name):
        print('증권자동화입니다.')
        print(student_name)

        return '증권'


B_school().stock('수한')
bb = B_school()  # B_school 클래스 인스턴스화
result = bb.stock('수한')

# 3. 상속 (supper)========================================
# 다른 class가 가지고 있는 self의 변수값들을 받아서 사용하도록만듬


class Parent():
    def __init__(self):
        print('부모 클래스')
        self.money = 5000000000

    def book(self):
        print('부모의 서재입니다.')


class Child_1(Parent):  # (상속받을 대상)
    def __init__(self):
        super().__init__()  # __init__ 에 대한 상속명령어
        print('첫번째 자식입니다.')
        print(self.money)
        self.book()


class Child_2(Parent):
    def __init__(self):
        print('두번째 자식입니다.')
        self.book()
        print(self.money)


class Child_3():
    def __init__(self):
        print('세번째 자식입니다.')
        self.book()
        print(self.money)


Child_1()
Child_2()
Child_3()
