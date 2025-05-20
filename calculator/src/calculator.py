def calculate():
    try:
        num1 = float(input("输入第一个数字: "))
        operator = input("输入运算符 (+ - * /): ")
        num2 = float(input("输入第二个数字: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("不能除以零！")
            result = num1 / num2
        else:
            raise ValueError("无效的运算符")
            
        print(f"结果: {result}")
        
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    calculate()
