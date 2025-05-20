import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

def add_todo(todos):
    task = input("输入待办事项: ")
    todos.append({"task": task, "done": False})
    print("添加成功！")

def list_todos(todos):
    if not todos:
        print("当前没有待办事项。")
        return
    for idx, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        print(f"{idx}. [{status}] {todo['task']}")

def mark_done(todos):
    list_todos(todos)
    try:
        idx = int(input("选择要标记为完成的事项编号: ")) - 1
        if 0 <= idx < len(todos):
            todos[idx]["done"] = True
            print("标记成功！")
        else:
            print("无效的编号！")
    except ValueError:
        print("请输入数字！")

def main():
    todos = load_todos()
    while True:
        print("\n==== 待办事项管理 ====")
        print("1. 添加事项")
        print("2. 列出事项")
        print("3. 标记完成")
        print("4. 退出")
        choice = input("请选择操作: ")
        
        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            list_todos(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("已保存，再见！")
            break
        else:
            print("无效的选项！")

if __name__ == "__main__":
    main()
