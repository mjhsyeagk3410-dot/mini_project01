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
        self.items = {}

    def add_item(self, product, quantity):
        # 이미 장바구니에 있는 상품인지 확인
        if product in self.items:
            self.items[product] += quantity # 기존 수량에 누적
        else:
            self.items[product] = quantity # 새로 등록
        print(f"'{product.name}' {quantity}개가 장바구니에 담겼습니다.")

    def remove_item(self, product_id):
        target_product = None

        # 장바구니에 담긴 상품 객체들을 순회하며 일치하는 product_id 찾기
        for product in self.items.keys():
            if product.product_id == product_id: 
                target_product == product
                break

        if target_product:
            del self.items[target_product] #딕셔너리에서 해당 상품 제거
            print(f"'{target_product.name}' 상품이 장바구니에서 제거되었습니다.")
        else:
            print("[오류] 장바구니에서 해당 상품을 찾을 수 없습니다.")

    def calculate_total(self):
        total_price = 0

        # 딕셔너리의 items()메서드를 활용해 상품과 수량을 함께 순회
        for product, quantity in self.items.items():
            total_price += product.price * quantity

        return total_price

    def show_cart(self):
        if not self.items:
            print("\n장바구니가 비어 있습니다.")
            return

# 6. 쇼핑몰 메인 클래스: 전체 흐름 제어 및 사용자 인터페이스(터미널)
class ShoppingMall:
    def __init__(self):
        pass

    def run(self):
        pass 

    def show_products(self):
        pass

# 장바구니 기능 테스트 실행
    # 상품 객체 생성
    p1 = Product("무선 이어폰", 89000, 3)
    p2 = Product("텀블러", 15000, 10)
    p3 = Product("보조배터리", 32000, 5)

    print("===[상품 목록 확인]===")
    p1.show_info() # 출력 : 1. 무선 이어폰 89000원 (재고 3개)
    p2.show_info() # 출력 : 2. 텀블러 15,000원, (재고 10개)
    print("-" * 30)

    # 장바구니 객체 생성
    my_cart = Cart()

    # 상품 담기 테스트
    print("\n=== [1. 장바구니 담기] ===")
    my_cart.add_item(p1, 2)
    my_cart.add_item(p2, 1)

    # 총금액 계산 테스트
    print("\n=== [2. 총금액 계산] ===")
    total = my_cart.calculate_total()
    print(f"현재 장바구니 총금액: {total:,}원")

    # 상품 빼기 테스트
    print("\n=== [3. 장바구니 상품 제거] ===")
    my_cart.remove_item(2)

    # 제거 후 다시 총금액 계산
    print("\n=== [4. 제거 후 최종 금액 계산] ===")
    final_total = my_cart.calculate_total()
    print(f"변경 후 장바구니 총금액: {final_total:,}원")