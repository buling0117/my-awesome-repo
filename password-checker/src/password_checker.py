import re

def check_password(password):
    if len(password) < 8:
        return "密码长度需至少8位！"
    
    checks = {
        "大写字母": re.search(r'[A-Z]', password),
        "小写字母": re.search(r'[a-z]', password),
        "数字": re.search(r'[0-9]', password),
        "特殊符号": re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    }
    
    missing = [key for key, value in checks.items() if not value]
    if missing:
        return f"密码缺少以下要求: {', '.join(missing)}"
    else:
        return "密码符合要求！"

if __name__ == "__main__":
    password = input("输入要检查的密码: ")
    print(check_password(password))
