import random
num = random.randint(1, 100)

print(f'ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ')

while True :
    num_guess = input("ป้อนตัวเลขที่ต้องการทาย : ")
    num_guess = int(num_guess)

    if num_guess == num :
        print("ยินดีด้วยคุณทายถูก")
        break
    elif num_guess > num :
        print("คุณทายผิดตัวเลขที่ป้อนมากไป")
    else :
        print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
