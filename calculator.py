def add_numbers(a, b):
    """Cộng hai số và trả về kết quả."""
    return a + b

def subtract_numbers(a, b):
    """Trừ hai số và trả về kết quả."""
    return a - b

if __name__ == "__main__":
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))

    print("Tổng:", add_numbers(num1, num2))
    print("Hiệu:", subtract_numbers(num1, num2))
