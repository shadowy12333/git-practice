# -*- coding: utf-8 -*-
"""任务清单的逻辑。

这个文件里有 3 处故意写坏的地方，都用 [BUG] 标了出来。
Task7 的练习就是：用 Git 分支 + commit 把它们一个个修掉。

不要一次性全改完再提交——那样你就学不到"一次提交只表达一个变化"了。
一次修一个，每次单独提交。
"""


def add_todo(todos, title):
    """添加一条任务。

    [BUG 1] 这里没有去重。
    预期：如果 title 已经存在，不要重复添加，并返回 False。
    现在：无脑 append，所以 main.py 里会出现两条一模一样的任务。
    """
    for todo in todos:
        if todo["title"] == title:
            return False
    todos.append({"id": len(todos) + 1, "title": title, "completed": False})
    return True


def list_todos(todos):
    """打印所有任务。

    [BUG 2] 打印状态时，完成显示成了 [ ]，未完成显示成了 [x]，反了。
    """
    if not todos:
        print("  （还没有任务）")
        return

    for todo in todos:
        mark = "[x]" if todo["completed"] else "[ ]"
        print(f"  {todo['id']}. {mark} {todo['title']}")


def complete_todo(todos, todo_id):
    """把指定 id 的任务标记为完成。

    [BUG 3] 参数名叫 todo_id，但循环里写的是 todo["id"] == id，
    用的是 Python 内置函数 id，所以永远匹配不上，函数永远返回 False。
    """
    for todo in todos:
        if todo["id"] == id:
            todo["completed"] = True
            return True
    return False


def count_completed(todos):
    """统计已完成的任务数。这个函数是对的，留作对照。"""
    return sum(1 for todo in todos if todo["completed"])
