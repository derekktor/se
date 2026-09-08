import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Аргумент дутуу эсэхийг шалгах
    if len(sys.argv) < 4:
        print("Хэрэглээ:")
        print("python3 calculator.py <тоо1> <тоо2> <үйлдэл>")
        print("Жишээ: python3 calculator.py 10 5 add")
        sys.exit(1)

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    operation = sys.argv[3]

    if operation == "add":
        print(f"Үр дүн: {add(x, y)}")
    elif operation == "sub":
        print(f"Үр дүн: {subtract(x, y)}")
    else:
        print("Мэдэхгүй үйлдэл байна.")