'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''
class Contact(object):
    def __init__(self, name, phone_number, email, address) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def print(self):
        print(f"이름: {self.name}\n전화번호: {self.phone_number}\n이메일: {self.email}\n주소: {self.address}")

    def print_info(self):
        print(self.name,self.phone_number,self.email,self.address)
       
    @staticmethod
    def new_contact():
        name = input("이름: ")
        phone_number = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        return Contact(name, phone_number, email, address)

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 연락처 종료")
        menu = input("메뉴선택")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print("### 연락처 등록 ###")
                contact = Contact.new_contact()
                ls.append(contact)
            elif menu == 2:
                print("### 연락처 출력 ###") 
                contact.get_contacts(ls)   
            elif menu == 3:
                print("### 연락처 삭제 ###")
            elif menu == 4:
                print("### 주소록 어플을 종료합니다... ###")
                break

Contact.main()