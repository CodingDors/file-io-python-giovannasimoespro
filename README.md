### README for File I/O Operations Exercise

---

# 📁 File I/O Operations in Python

Welcome, students! 🚀 This exercise is designed to deepen your understanding of file I/O operations with Python.

## 🎯 Objectives

- Implement and understand file I/O operations in Python.
- Develop functions to manage and manipulate files.
- Validate function implementations through testing and debugging.

## 🔍 Overview

Your working file is `fileio.py`, which contains partial implementations of 10 functions, each designed to perform a unique file operation.

In addition, `fileio.py` contains a `run_example_operations()` function, which provides example usage of each file operation function and outputs log messages to explain the expected behaviors of the respective operations. 

After implementing each function, uncomment the corresponding file in run_example() so that you can 
verify your implementation works as you expect.

## ✅ Tasks

### 1️⃣ Understand the distribution code

While working in `fileio.py`:
- Read the documentation (docstrings) of each function to understand what you need to implement.
- Run the following in the terminal:

````bash
python fileio.py
````

You should see a file being created on the sidebar. If you open it up you will see that
a string was written to it. This is to help you understand how to use run_example_operations()

- Also run before starting on the terminal

````bash
pytest
````

You should run this after completing each function to verify that it was correctly implemented. Once
all tests pass you can submit your code for review.

### 2️⃣ Debugging with VSCode

Should your functions exhibit unexpected behaviors or issues:
- Place breakpoints in your code within VSCode.
- Use the VSCode debugger to navigate through your code, inspect variables, and diagnose potential issues.
- Modify your code as needed, guided by your findings during debugging.
- [Debugger Tutorial](https://www.youtube.com/watch?v=7qZBwhSlfOo&t=7s)

### 3️⃣ Implementing the function

Implement each function in the TODO. Do the following steps:

- Add your implementation
- Uncomment corresponding section on run_example_operations() and Run `python file.io` to make
sure it works as you intenteded.
- Run `pytest` to make sure it passsed the tests

### 4️⃣ Committing and Pushing Changes using VSCode Codespaces

Once all the tests have completed:

1. **Stage Changes**: 
   - View your changes in the Source Control view.
   - Click on the `+` (plus) sign next to the files you wish to stage.
2. **Commit Changes**: 
   - Enter a descriptive commit message.
   - Press `Ctrl + Enter` (or `Cmd + Enter` on macOS) to commit the changes.
3. **Push Changes**: 
   - Click on the ellipsis `...` in the Source Control view.
   - Select **Push**.
4. **Verify you code has passed**: 

## 📘 Resources

- **File I/O in Python**: Review foundational knowledge with Python’s [file I/O documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

## 🤔 Need Help?

- **Clarifications**: Don’t hesitate to ask for clarifications regarding the functionality of the on Discord.
- **Debugging**: If you’re grappling with bugs or issues, seek help! Debugging is key to learning.
- **Answer**: We have a file called answer.py. Only look at it if you are stuck for some time (30 min+)

