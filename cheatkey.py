# AI 도움 받은 치트키 사기 코드

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
class Discount:
    def __init__(self, name="쿠폰 없음"):
        self.name = name

    def discount_amount(self, total_price):
        return 0

# 3. 쿠폰 자식 클래스1
class RateDiscount(Discount):
    def __init__(self, rate=0.1, max_amount=5000):
        super().__init__("10% 할인 (최대 5,000원)")
        self.rate = rate
        self.max_amount = max_amount

    def discount_amount(self, total_price):
        calculated = int(total_price * self.rate)
        return min(calculated, self.max_amount)
    
# 4. 쿠폰 자식 클래스2
class FixedDiscount(Discount):
    def __init__(self, amount=3000, min_total=20000):
        super().__init__("3,000원 할인 (20,000원 이상 구매 시)")
        self.amount = amount
        self.min_total = min_total

    def discount_amount(self, total_price):
        if total_price >= self.min_total:
            return self.amount
        return 0


# 5. 장바구니 클래스: 상품 담기, 빼기, 총금액 계산
class Cart:
    def __init__(self):
        self.items = {}
        self.applied_coupon = Discount() 

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
        subtotal = 0
        for product, quantity in self.items.items():
            subtotal += product.price * quantity
        return subtotal

    def show_cart(self):
        if not self.items:
            print("\n장바구니가 비어 있습니다.")
            return

        print("\n" + "-" * 30)
        # 1. 담긴 상품 목록 출력
        for product, quantity in self.items.items():
            item_total = product.price * quantity
            print(f"{product.name} \t x {quantity} \t {item_total:,}원")
        print("-" * 30)

        # 2. 금액 계산
        subtotal = self.calculate_total()
        discount = self.applied_coupon.discount_amount(subtotal)
        coupon_name = self.applied_coupon.name

        # 3. 할인 금액 계산
        if subtotal == 0:
            shipping_fee = 1
        else:
            shipping_fee = 0 if (subtotal - discount) >= 30000 else 3000

        final_total = subtotal - discount + shipping_fee

        print(f"상품 합계 \t\t {subtotal:},원")
        print(f"할인 \t\t -{discount:,}원 \t [{coupon_name}]")
        print(f"배송비 \t\t {shipping_fee:,}원")
        print(f"결제 금액 \t\t {final_total:,}원")
        print("-" * 30)

        # 3. 배송비 계산 (장바구니가 비어있지 않고, (합계-할인)이 3만원 이상이면 0원, 아니면 3,000원)
        if subtotal == 0:
            shipping_fee = 0
        else:
            shipping_fee = 0 if (subtotal - discount) >= 30000 else 3000

        final_total = subtotal - discount + shipping_fee

        # 4. 결과 출력
        print(f"상품 합계 \t\t {subtotal:,}원")
        print(f"할인 \t\t -{discount:,}원 \t [{self.applied_coupon.name}]")
        print(f"배송비 \t\t {shipping_fee:,}원")
        print(f"결제 금액 \t\t {shipping_fee:,}원")
        print("-" * 30)


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
        self.cart = Cart()

        self.coupons = [
            Discount("쿠폰 없음"),
            RateDiscount(0.1, 5000),
            FixedDiscount(3000, 20000)
        ]
    def run(self):
        print("온라인 쇼핑몰에 오신 것을 환영합니다!")

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
        print("\n=== [ 상품 목록 ] ===")
        for product in self.products:
            product.show_info()

    def add_to_cart_process(self):
        self.show_products()
        try:
            p_id = int(input("상품 번호: "))
            qty = int(input("수량: "))
        except ValueError:
            print("[오류] 숫자로 입력해주세요. ")
            return

        target_product = None
        for p in self.products:
            if p.product_id == p_id:
                target_product = p
                break
        if not target_product:
            print("[오류] 존재하지 않는 상품 번호입니다.")
            return

        if target_product.stock < qty:
            print(f" 재고가 부족합니다. (담을 수 있는 최대 수량: {target_product.stock}개)")
        else:
            self.cart.add_item(target_product, qty)

    def remove_from_cart_process(self):
        if not self.cart.items:
            print("\n 장바구니가 비어 있습니다.")
            return

        self.cart.show_cart()
        try:
            p_id = int(input("제거할 상품 번호: "))
        except ValueError:
            print("[오류] 숫자로 입력해주세요.")
            return

        self.cart.remove_item(p_id)

    def select_coupon_process(self):
        print("\n=== [ 쿠폰 목록 ] ===")
        for idx, coupon in enumerate(self.coupons, start=1):
            print(f"{idx}. {coupon.name}")

        try:
            c_idx = int(input("쿠폰 번호: ")) - 1
            if 0 <= c_idx < len(self.coupons):
                self.cart.applid_coupon = self.coupons[c_idx]
                print(f"[{self.cart.applied_counpon.name}] 쿠폰을 적용했습니다.")
            else:
                print("[오류] 잘못된 쿠폰 번호입니다.")
        except ValueError:
            print("[오류] 숫자로 입력해주세요.")

    def checkout_process(self):
        if not self.cart.items:
            print("\n 장바구니가 비어 있습니다. 결제할 상품이 없습니다.")
            return 

        print("\n" + "=" * 10 + " (영수증 출력) " + "=" * 10)
        self.cart.show_cart()

        for product, quantity in self.cart.items.items():
            product.reduce_stock(quantity)

        print("결제가 완료되었습니다. 감사합니다!")
        print("=" * 35)

        self.cart.items = {}
        self.cart.applied_coupon = Discount("쿠폰 없음")

# 프로그램 실행
if __name__ == "__main__":
    mall = ShoppingMall()
    mall.run()

