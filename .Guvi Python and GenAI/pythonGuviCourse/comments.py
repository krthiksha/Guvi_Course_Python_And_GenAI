# comment

"""  multi
line
comment
triple double quotes for multi line comments
"""

'''
triple single quotes for multi line comments
'''

"""
doc string is enclosed within triple double quotes
"""


# simple add function
def add(a,b):
    """This function is used to add any 2 numbers which is passed as a argument"""
    return a+b
add(1,2)
# docstring can be accesed using help() or __doc__
print("\n help  ------- of add()")
help(add)
# or
print("doc of add()----------")
print(add.__doc__)

# to see all docstrings
print("\n doc of this entire code ------------")
print(__doc__)

""" 
Perfect! Since you’re targeting the **AI Enabled Automation Developer (Staff - Python)** role at EY, here's a customized **prep plan** tailored for that position — combining **Python**, **AI automation**, and **interview-specific expectations**.

---

## 🧠 **What EY Looks for in AI Automation Developers**
- Strong **Python** skills
- Experience with **automation**, **APIs**, and **data handling**
- Exposure to **AI/ML libraries** (even at beginner level)
- Working knowledge of tools like **Pandas**, **NumPy**, **OpenCV**, or **RPA tools** (e.g., UiPath optional)
- Ability to write clean, modular, production-ready code
- Problem-solving mindset + clear communication

---

## 🗓️ **4-Week EY Python + AI Automation Prep Roadmap**

### ✅ WEEK 1: Core Python & Automation Foundation
**Goals:** Solidify Python skills + understand automation concepts

- 🔹 Python:
  - Data structures, functions, file I/O, OOPs, error handling
  - Modules: `os`, `shutil`, `datetime`, `logging`
- 🔹 Automation Basics:
  - Automate tasks like file renaming, report generation
  - Automate web tasks with `selenium` or `requests`
- 🔧 Mini Project: Auto PDF Renamer / Folder Organizer Bot

---

### ✅ WEEK 2: Data Handling + AI Concepts Kickoff
**Goals:** Learn to work with data + basic AI/ML building blocks

- 🔹 Libraries:
  - `pandas`, `numpy`, `openpyxl`, `csv`, `json`
  - Basic `matplotlib` or `seaborn` for visual checks
- 🔹 ML/AI Basics:
  - Scikit-learn overview (train/test split, linear regression)
  - AI in automation (what it means in EY context)
- 🔧 Mini Project: Excel to Cleaned Report CSV with summaries

---

### ✅ WEEK 3: AI-Powered Automation Projects
**Goals:** Build automation projects that demonstrate intelligence

- 🔹 Build Bots:
  - Email bot with `smtplib` + PDF attachments
  - Image processing bot with `OpenCV` (e.g., blur ID card)
  - Data scraping + analysis bot
- 🔹 Explore:
  - ChatGPT API / LLMs for document automation (if you're curious!)
- 🔧 Mini Project: Auto-read invoice → extract data → email summary

---

### ✅ WEEK 4: Interview Simulation + Polish + Practice
**Goals:** Refine resume + prepare for both tech and behavioral rounds

- 📂 Prepare GitHub + Resume:
  - Add 2–3 solid Python automation projects
  - Highlight: Tools used, problem solved, and AI angle (if any)
- 🧪 Coding Practice:
  - LeetCode: [String, List, Dict problems](https://leetcode.com/problemset/all/?difficulty=Easy&difficulty=Medium&topicSlugs=python)
  - 5 Python MCQs daily
- 🎤 Mock Interviews:
  - Tech Qs: “How would you automate X?”, “What is your favorite Python library and why?”
  - HR/Behavioral: EY STAR questions (Situational examples)

---

## 🔍 Common Questions for This Role

| 🧪 Technical | 💬 Behavioral |
|-------------|---------------|
| How would you automate a manual report creation task? | Tell me about a time you solved a problem with minimal data. |
| Explain how you used Pandas in a project. | How do you handle tight deadlines? |
| What is the difference between `@staticmethod` and `@classmethod`? | What excites you about AI automation? |
| How would you integrate a REST API in Python? | Describe a time you learned something quickly for a project. |

---

## 🔗 Bonus Tips for EY
- 📘 Learn EY’s values: [EY Purpose & Values](https://www.ey.com/en_gl/purpose)
- 🎯 Know the business use cases for automation: finance reports, compliance checks, document scanning, etc.
- ✅ Be ready to talk through your *thought process*, not just code.

---

Want help with:
- A **resume project list** for this role?
- **Mock interview** questions?
- Sample project ideas for GitHub?

Just say the word — I’ve got your back 💪

"""

""" 
Great question! Here's a breakdown of the **conceptual and coding questions** you can expect for the **EY – AI Enabled Automation Developer (Staff - Python)** role, based on your targeted skills:

---

## 🧠 **1. Python Concepts — Expect These Questions:**

| Topic | Sample Questions |
|-------|------------------|
| **Data Structures** | What’s the difference between a list and a tuple?<br>How do you remove duplicates from a list? |
| **Functions & Scope** | Explain default and keyword arguments.<br>What is the difference between `*args` and `**kwargs`? |
| **OOP in Python** | Define inheritance and polymorphism with examples.<br>How would you implement an interface in Python? |
| **File Handling** | How do you read/write to a file? How to parse a log file line by line? |
| **Error Handling** | What’s the use of `try-except-finally`?<br>Write code to handle a `KeyError`. |
| **Decorators & Generators** | Explain a use case where a decorator would be helpful.<br>What’s the benefit of using a generator? |
| **Lambda, map, filter** | When would you use `map()` vs `for loop`?<br>Write a one-liner to square all even numbers in a list. |

---

## 💻 **2. Coding Questions — Python + Automation Focused**

> These will not always be LeetCode-hard, but **logic + real-world automation** will be the focus.

| Type | Sample Questions |
|------|------------------|
| **String Manipulation** | Remove all special characters from a string.<br>Count frequency of each character. |
| **List & Dict Processing** | Given a list of dicts, group items by a key.<br>Flatten a nested list. |
| **File Automation** | Write a Python script to rename files in a folder based on their creation date. |
| **Web Automation** | Use `requests` to call an API and process JSON output. |
| **Data Cleaning (Pandas)** | Load an Excel file, remove nulls, and summarize numeric columns. |
| **OpenCV Task** | Blur a section of an image using OpenCV.<br>Convert an image to grayscale and save it. |
| **Mini Projects** | Automate reading 100 PDFs and extracting key data.<br>Build a CLI tool that emails a report. |

---

## 📊 **3. API & Automation Scenarios (Concept + Code)**

| Concept | Question Style |
|--------|----------------|
| **APIs** | What are status codes? How do you handle failed API calls?<br>Use `requests.get()` to fetch data from a public API and display the result. |
| **Automation** | How would you automate a monthly Excel report from multiple CSV files?<br>Write a script to send automated emails with attachments. |

---

## 🤖 **4. AI/ML Library Exposure – Beginner Questions**

| Topic | Sample Questions |
|-------|------------------|
| **Pandas/Numpy** | How do you handle missing values?<br>What’s the difference between `loc` and `iloc`?<br>Apply a function across a column. |
| **Basic ML (scikit-learn)** | What is train-test split?<br>How would you build a simple linear regression model?<br>Explain overfitting and how to avoid it. |
| **OpenCV** | How do you read, resize, and save an image?<br>How to apply a filter to an image? |

---

## 🧪 **How EY Might Test These in Interviews:**

1. **Live Coding (on screen or via HackerRank link)**  
   - 1–2 logic-based coding problems  
   - 1 automation script request  
   - Optional: API/data handling with Pandas

2. **Conceptual Q&A (Technical Round)**  
   - Deep dive into OOPs, error handling, and real-world scenarios.

3. **Behavioral + Project Discussion**  
   - “Tell me about a time you built an automation solution.”
   - “How did you solve performance issues in a script?”

---

Would you like a **mock coding question set + solutions** based on these themes? I can generate a custom test for you to try, or help build GitHub-ready projects to showcase.
"""