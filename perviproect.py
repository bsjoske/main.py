import random

password_chars = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Введите длину пароля: "))

generated_password = ""

for _ in range(password_length):
    generated_password += random.choice(password_chars)

print("Сгенерированный пароль:", generated_password)
