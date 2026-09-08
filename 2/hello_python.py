name = input("Таны нэр хэн бэ?\n")

if len(name) > 0:
    print(f"Сайн байна уу, {name}! Python хэл сурч байгаад амжилт хүсье.")
else:
    print("Та нэрээ оруулсангүй.")


print("\n1-ээс 5 хүртэл тоолж байна:")
for i in range(1, 6):
    print(f"Тоо: {i}")