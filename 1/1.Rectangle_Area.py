try:
    width=float(input("Enter Width:"))
    lenght=float(input("Enter Lenght:"))
# int_width=int(width)                   موارد کامنت برای حالت اینتیجر می‌باشد
# int_lenght=int(lenght)
# area=int_width*int_lenght
# print("Rectangle Area= ", area)
# print("Rectangle Area= "+ str(area))
    print("Rectangle Area= ", width*lenght)
except ValueError:
    print("adad bede")