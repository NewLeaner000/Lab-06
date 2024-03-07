def welcome_message(name):
    """
    Hiển thị thông báo chào mừng với tên người dùng.
    """
    print(f"Chào mừng, {name}!")

def calculate_square(number):
    """
    Tính bình phương của một số.
    """
    return number ** 2

def main():
    """
    Hàm chính để chạy chương trình.
    """
    name = input("Nhập tên của bạn: ")
    welcome_message(name)

    num = float(input("Nhập một số: "))
    result = calculate_square(num)
    print(f"Bình phương của {num} là {result}.")

if __name__ == "__main__":
    main()

