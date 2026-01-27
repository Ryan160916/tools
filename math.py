name = input('请输入一个算式，例如： 2 + 3: ')

left_oper_right = name.split(" ")
# print(left_oper_right)

left = float(left_oper_right[0])
oper = left_oper_right[1]
right = float(left_oper_right[2])

if oper == '+':
    print(left + right)
elif oper == '-':
    print(left - right)
elif oper == '*':
    print(left * right)
elif oper == '/':
    print(left / right)
elif oper == '%':
    print(left % right)
else:
    print("输入错误")
