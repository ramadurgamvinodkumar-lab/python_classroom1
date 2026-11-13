units = int(input("enter number units used:"))
if units <=100:
    bill = units * 1
elif units <=200:
    bill = 100 * 1 + (units-100)*2
else:
    bill = 100*1 + 100*2 + (units-200)*5
    print("electricity bill is:",bill)
# # a = int(input("enter first angle:") )
# # b = int(input("enter second angle:") )
# # c = int(input("enter third angle:") )
# # if a==b and b==c and c==a:
# #     print("it is an equilateral triangle")
# # elif a==b or b==c or a==c:
# #     print("it is an isosceles triangle")
# # else:
# #         print("scalene triangle")
# # age = 20
# # has_id =False
# # if age >=18:
# #     if has_id:
# #         print("enter allowed")
# #     else:
# #         print("show your id card")
# #     else:
# #         print("too young for entry" )
# age = 20
# has_id = False

# if age >= 18:
#     if has_id:
#         print("enter allowed")
#     else:
#         print("show your id card")
# else:
#     print("too young for entry")
