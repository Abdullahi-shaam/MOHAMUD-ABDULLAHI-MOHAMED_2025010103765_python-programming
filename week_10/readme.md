# Week 10: HR Salary Calculator System

## Project Overview
A modular Python program developed for the HR department to automate employee salary calculations, including gross pay, statutory deductions (EPF & SOCSO), overtime pay, and tenure rewards.

## Project Structure
* `main.py`: Coordinates the main workflow of the program.
* `employee.py`: Handles collecting employee input data.
* `salary.py`: Calculates gross salary, EPF (11%), SOCSO (0.5%), overtime, loyalty bonus, and net salary.
* `report.py`: Displays the formatted salary summary report.

## Features
* Calculates EPF deduction at 11%.
* Calculates SOCSO deduction at 0.5%.
* Supports overtime pay calculation at RM25/hour.
* Incorporates a loyalty bonus for employees with over 3 years of service.

## How to Run
Execute the main program from your terminal:
```bash
python main.py