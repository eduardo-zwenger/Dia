# Day of the Week Validator (QA & Logic Testing)

A Python script designed to determine the day of the week based on numerical input (1-7). This project serves as an excellent sandbox for practicing **Boundary Value Analysis (BVA)** and preparing structural logic for automated **Unit Testing** in Python.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Concepts:** Conditional logic, input handling, and validation.

## 📋 QA Test Strategy & Boundary Values

In software testing, inputs around the edges of acceptable ranges often cause defects. This project maps those exact scenarios:

### 1. Equivalence Partitioning (EP)
*   **Valid Partition:** Integers from `1` to `7` (Expected: Monday through Sunday).
*   **Invalid Partition Low:** Numbers `< 1` (Expected: Error message / Out of range handling).
*   **Invalid Partition High:** Numbers `> 7` (Expected: Error message / Out of range handling).

### 2. Robustness & Data Validation (Negative Testing)
*   **String Inputs:** Passing letters or symbols (e.g., `"Monday"`, `@#$`) instead of an integer.
*   **Float Inputs:** Passing decimal numbers (e.g., `3.5`).

## 🚀 Automation Roadmap
* [ ] Implement automated unit tests using Python's native `unittest` framework to validate all 7 correct outputs.
* [ ] Add automated assertions to check how the script handles out-of-range exceptions and invalid data types.
