# Visual Regression Test

This repository describes how to perform a visual regression test using Selenium in Python.

## How it Works

### Local Setup:

- The test visits a website, takes an initial screenshot (`baselnine_screenshot.png`).
- On subsequent executions, it checks if the baseline screenshot exists and takes another screenshot (`current_screenshot.png`).
- It compares `baselnine_screenshot.png` and `current_screenshot.png` using `ImageChops` and creates a `diff_screenshot.png` showing visual differences between both screenshots (`baselnine_screenshot.png` and `current_screenshot.png`).
- If the team accepts a new update, you can delete the baseline and run the test again for subsequent updates to repeat the process.

### Cloud Setup:

- The test takes a baseline screenshot using the LT SmartUI.
- You then take other non-baseline screenshots.
- Compare new screenshots with the baseline to monitor UI differences due to code updates.

```
regression_testing
├─ compare
│  └─ compare.py
├─ screenshot
│  └─ screenshots.py
├─ setup
│  └─ setup.py
└─ test_regression_demo.py

```
