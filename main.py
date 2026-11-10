# AI 도움 받지 않았을때 순수 실력
# (도움받은건, cheatkey.py에 있습니다)

# 미니 프로젝트 발제 — 쇼핑몰 장바구니 & 할인 쿠폰

# 1. 상품 클래스
class Product:
    def __init__(self, name, price):
        self.name = name                     # 상품 이름
        self.price = price                   # 가격

# 2. 쿠폰 부모 클래스 
class Discount:
    def __init__(self, name):
        self.name = name

# 3. 쿠폰 자식 클래스1
class RateDiscount(Discount):
    def __init__(self):

    def discount_amount(self):
    
# 4. 쿠폰 자식 클래스2
class FixedDiscount(Discount):
    def __init__(self):

# 5. 장바구니 클래스: 상품 담기, 빼기, 총금액 계산
class Cart:
    def __init__(self): 

    def remove_item(self):

    def calculate_total(self):

    def show_cart(self):


# 6. 쇼핑몰 메인 클래스: 전체 흐름 제어 및 사용자 인터페이스(터미널)
class ShoppingMall:
    def __init__(self):
        self.products = [
            Product("무선 이어폰", 89000, 3),
            Product("텀블러", 15000, 10),
            Product("보조배터리", 32000, 5),
            Product("마우스패드", 9000, 0),
            Product("USB 허브", 18000, 4)
        ]

        while True: 
            print("\n-----------------------------")
            print("1. 상품목록  2. 담기  3. 빼기  4. 장바구니 5. 쿠폰 6. 결제  q.종료")
            print("-------------------------------")
            choice = input("선택: ").strip() 

            if choice == '1':
                self.show_products()
            elif choice == '2':
                self.add_to_cart_process()
            elif choice == '3':
                self.remove_from_cart_process()
            elif choice == '4':
                self.cart.show_cart()
            elif choice == '5':
                self.select_coupon_process()
            elif choice == '6':
                self.checkout_process()
            elif choice == 'q' or choice == 'Q':
                print("프로그램을 종료합니다. 이용해주셔서 감사합니다!")
                break
            else:
                print("[오류] 올바른 번호를 입력해주세요.")

    def show_products(self):

    def add_to_cart_process(self):

    def remove_from_cart_process(self):

    def select_coupon_process(self):
    