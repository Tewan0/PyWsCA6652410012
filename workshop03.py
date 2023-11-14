import calarea
import calcube

def show() :
    while True :
        print("1. พื้นที่สี่เหลี่ยม")
        print("2. พื้นที่วงกลม")
        print("3. ปริมาตรทรงสี่เหลี่ยม")
        print("4. ปริมาตรทรงกลม")
        print("0. ออกจากการทํางาน")
        
        choice = input("เลือกเมนู: ")
        choice = int(choice)

        if choice == 1 :
            width = float(input("ป้อนค่าความกว้าง: "))
            length = float(input("ป้อนค่าความยาว: "))
            print("พื้นที่สี่เหลี่ยม = ", calarea.area_square(width, length), "ตารางหน่วย")
        elif choice == 2:
            radius = float(input("ป้อนรัศมี: "))
            print("พื้นที่วงกลม = ", calarea.area_circle(radius), "ตารางหน่วย")
        elif choice == 3:
            width = float(input("ป้อนค่าความกว้าง: "))
            length = float(input("ป้อนค่าความยาว: "))
            height = float(input("ป้อนค่าความสูง: "))
            print("ปริมาตรทรงสี่เหลี่ยม = ", calcube.volume_cube(width, length, height), "ลูกบาศก์หน่วย")
        elif choice == 4:
            radius = float(input("ป้อนรัศมี: "))
            print("ปริมาตรทรงกลม = ", calcube.volume_sphere(radius), "ลูกบาศก์หน่วย")
        elif choice == 0:
            print("ออกจากการทํางาน")
            break
        else:
            print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0เท่านั้น")
            

if __name__ == "__main__":
    show()
