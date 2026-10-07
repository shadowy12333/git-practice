# -*- coding: utf-8 -*-
"""任务清单小程序的入口。

Task7 练习用。这个项目本身很简单，重点不是它，而是学会用 Git 管住它。
"""

from todos import add_todo, list_todos, complete_todo


def main():
    todos = []

    print("=== 我的任务清单 ===")

    add_todo(todos, "学会 git init")
    add_todo(todos, "学会写 .gitignore")
    add_todo(todos, "学会看 git diff")
    add_todo(todos, "学会建分支提交")
    add_todo(todos, "学会用 Codex/Claude Code 改代码后再自己 review diff")

    # 故意重复添加一条，看看会发生什么
    add_todo(todos, "学会看 git diff")

    print(f"\n一共 {len(todos)} 条任务：")
    list_todos(todos)

    print("\n把第 2 条标记为完成：")
    complete_todo(todos, 2)
    list_todos(todos)


if __name__ == "__main__":
    main()
