# 미니 프로젝트 발제 — 쇼핑몰 장바구니 & 할인 쿠폰

# 1. 상품 클래스
class Product:
    id_counter = 1

    def __init__(self, name, price, stock):
        self.product_id = Product.id_counter # 현재 카운터 번호로 상품 ID를 부여
        Product.id_counter += 1              # 다음 상품을 위해 카운터 1 증가

        self.name = name                     # 상품 이름
        self.price = price                   # 가격
        self.stock = stock                   # 초기 재고

    def reduce_stock(self, quantity):
        # 요청한 수량만큼 재고가 충분한지 확인
        if self.stock >= quantity:
            self.stock -= quantity
            return True # 차감 성공
        else:
            return False    # 재고 부족

    def show_info(self):
        if self.stock == 0:
            print(f"{self.product_id}. {self.name} \t {self.price:,}원 \t (품절)")
        else: 
            print(f"{self.product_id}. {self.name} \t {self.price:,}원 \t (재고 {self.stock}개)")

# 2. 쿠폰 부모 클래스 
class Coupon:
    def __init__(self):
        pass

    def apply_discount(self):
        pass

# 3. 쿠폰 자식 클래스1
class FixedDiscountCoupon(Coupon):
    def __init__(self):
        super().__init__()
        pass

    def apply_discount(self):
        pass

# 4. 쿠폰 자식 클래스2
class RateDisountCoupon(Coupon):
    def __init__(self):
        super().__init__()
        pass

    def apply_discount(self):
        pass 

# 5. 장바구니 클래스: 상품 담기, 빼기, 총금액 계산
class Cart:
    def __init__(self):
        pass

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def calculate_total(self):
        pass 

# 6. 쇼핑몰 메인 클래스: 전체 흐름 제어 및 사용자 인터페이스(터미널)
class ShoppingMall:
    def __init__(self):
        pass

    def run(self):
        pass 

    def show_products(self):
        pass

# 상품 객체 생성 테스트 (번호는 자동으로 1, 2가 붙음 )
p1 = Product("무선 이어폰", 89000, 3)
p2 = Product("텀블러", 15000, 10)

p1.show_info() # 출력 : 1. 무선 이어폰 89000원 (재고 3개)
p2.show_info() # 출력 : 2. 텀블러 15,000원, (재고 10개)