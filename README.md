# 练习仓库说明

这是你在 Task7 里要亲手变成 Git 仓库的练习项目。

## 这个项目是什么

一个很小的命令行程序，故意留了几处**故意写坏**的地方，让你在 `git diff` 里能看出真实的修改。

```
练习仓库/
  main.py         程序入口
  todos.py        任务逻辑
  notes.txt       随手记的笔记
  config.ini      配置（里面有一个假的密码，用来练 .gitignore）
  README.md       说明
```

## 你的任务

1. 在这个文件夹里 `git init`
2. **先写 `.gitignore`**（讲义里有模板），把 `config.ini` 和 `__pycache__/` 排除掉
3. 把项目提交成第一个 commit
4. 然后修 `todos.py` 里标了 `[BUG]` 的地方，用分支 + commit 的方式修
5. 最后 `git log --oneline` 看你的历史

## 为什么要先写 .gitignore

因为 `config.ini` 里有密码。如果你先 `git add .` 再写 `.gitignore`，
密码就已经进了 Git 历史 —— 这是新手最常见的真实事故之一。

讲义里第七节专门讲这个，并且我写了脚本让你在**安全环境**里亲眼看到泄露长什么样（`演示-密钥泄露.py`）。

## 先跑一下这个项目

```powershell
py main.py
```

它应该能跑，但有一处行为是错的。你能不能自己看出来是哪一处？
（提示：`todos.py` 里那个函数名带 `[BUG]` 注释的）
