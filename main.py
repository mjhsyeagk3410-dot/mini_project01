# 미니 프로젝트 발제 — 쇼핑몰 장바구니 & 할인 쿠폰

# 1. 상품 클래스
class Product:
    def __init__(self):
        pass

    def reduce_stock(self):
        # 결제 시 재고 감소 함수
        pass

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