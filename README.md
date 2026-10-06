# Employee Management System

A console-based Employee Management System built using Python and Object-Oriented Programming concepts. The project allows users to create and manage Employees, Managers, and Developers.

The main purpose of this project is to practice important OOP concepts such as classes, objects, inheritance, encapsulation, constructors, getters, setters, and the `super()` method.

## Overview

The system contains three classes:

- `Employee`
- `Manager`
- `Developer`

`Manager` and `Developer` are child classes of the `Employee` class.

All employees have common information such as:

- Name
- Age
- Employee ID
- Salary

Managers also have a Department, while Developers have a list of Programming Languages.

## Employee IDs

Each employee has a unique alphanumeric ID.

Examples:

- Developer: `D123`
- Manager: `M234`
- Employee: `E456`

An ID can only be used once in the entire system. If an ID already exists, it cannot be assigned to another Employee, Manager, or Developer.

For example, if `D123` is already registered, another employee cannot use `D123`.

## Features

- Create multiple Developers
- Create multiple Employees
- Create multiple Managers
- Store multiple employee objects
- Display employee details using their ID
- Prevent duplicate employee IDs
- Store Developer programming languages
- Store Manager departments
- Keep Employee ID and Salary as private attributes
- Access private data using a getter method
- Modify private data using setter methods
- Use inheritance between Employee, Manager, and Developer
- Use `super()` to initialize inherited Employee data
- Interactive menu-based console interface

## OOP Concepts Used

### Classes and Objects

The project uses classes to define the structure and behavior of different employee types.

The `Employee` class acts as the parent class, while `Manager` and `Developer` inherit from it.

Objects are created from these classes when the user chooses an option from the menu.

### Inheritance

`Manager` and `Developer` inherit from `Employee`.

This allows both child classes to use the common properties and methods of the Employee class without rewriting the same functionality.

The class relationship is:

    Employee
       |
    ----------
    |        |
    Manager  Developer

### `super()` Method

The `super()` method is used inside the child classes to call the constructor of the parent class.

The following statement:

    super().__init__(ID, name, age, salary)

calls the `__init__()` method of the `Employee` class.

This allows `Manager` and `Developer` to initialize the common Employee information first and then add their own specific information.

### Encapsulation

Employee ID and Salary are intentionally kept private using double underscores.

The private attributes are:

    self.__employee_id
    self.__salary

These attributes are not directly accessed from the child classes. Instead, the getter method is used to access them.

This demonstrates encapsulation in Python.

### Getter

The `getter()` method provides controlled access to the private Employee ID and Salary.

    def getter(self):
        return self.__employee_id, self.__salary

The child classes use this method when they need to access the private data inherited from `Employee`.

### Setter

Setter methods are included to modify or add values related to the private attributes.

For example:

    def salary_setter(self, newSalary):
        self.__salary.append(newSalary)

Another setter is provided for Employee IDs.

### Constructor

The `__init__()` method is used to initialize an object when it is created.

The Employee constructor initializes:

- Employee ID
- Name
- Age
- Salary

The child classes call this constructor through `super()`.

## Employee Class

The `Employee` class is the parent class and contains the common employee information.

It stores:

- ID
- Name
- Age
- Salary
- Private Employee ID data
- Private Salary data
- Stored names
- Stored ages

The `Emp_data()` method prepares the data for storing and displaying employee information.

## Manager Class

The `Manager` class inherits from `Employee`.

In addition to the common Employee information, it stores the Manager's department.

Example:

    Name: Ahmed
    Age: 35
    Manager ID: M234
    Salary: $75000
    Department: Development

## Developer Class

The `Developer` class also inherits from `Employee`.

In addition to the common Employee information, it stores the programming languages provided by the user.

Languages are entered as comma-separated values.

Example input:

    Python,C,JavaScript

The languages are then split and stored as a set.

Example:

    {'Python', 'C', 'JavaScript'}

## Multiple Object Storage

The program is designed to store multiple objects of each type.

Three separate lists are used:

    devs = []
    emps = []
    mans = []

Developers are stored in `devs`, Employees are stored in `emps`, and Managers are stored in `mans`.

For example, the system can store:

    devs
    ├── Developer D101
    ├── Developer D102
    └── Developer D103

    emps
    ├── Employee E201
    ├── Employee E202
    └── Employee E203

    mans
    ├── Manager M301
    └── Manager M302

This allows multiple objects of the same class to exist at the same time.

## Unique ID Validation

A common set is used to keep track of all IDs that have already been assigned.

    all_ids = set()

Before creating a new employee, the entered ID is checked against this set.

If the ID already exists, the program displays an error message and does not create the new object.

This validation works across all three employee types.

For example:

    Developer -> D123
    Employee  -> D123  X
    Manager   -> D123  X

But different IDs are allowed:

    Developer -> D123
    Employee  -> E123
    Manager   -> M123

## Displaying Details

The program allows the user to search for a particular employee using their ID.

For example:

    Enter Developer ID to check: D123

The program searches through the stored Developer objects and displays the details of the matching object.

The same process is used for Employees and Managers.

## Menu

When the program starts, the following menu is displayed:

    --- Python OOP Project: Employee Management System ---

    Choose an operation:
    1. Create a Developer
    2. Create an Employee
    3. Create a Manager
    4. Show Details
    5. Exit

The user can select an option by entering the corresponding number.

### Option 1: Create a Developer

The program asks for:

- Name
- Age
- Developer ID
- Salary
- Programming Languages

The Developer object is then created and stored in the Developer list.

### Option 2: Create an Employee

The program asks for:

- Name
- Age
- Employee ID
- Salary

The Employee object is then created and stored in the Employee list.

### Option 3: Create a Manager

The program asks for:

- Name
- Age
- Manager ID
- Salary
- Department

The Manager object is then created and stored in the Manager list.

### Option 4: Show Details

The user first selects the employee type and then enters the corresponding ID.

The program searches the stored objects and displays the matching employee's details.

### Option 5: Exit

The program exits the Employee Management System.

## Example Employee IDs

    Developers:
    D101
    D102
    D103

    Employees:
    E201
    E202
    E203

    Managers:
    M301
    M302
    M303

All IDs must be unique.

## Requirements

- Python 3.10 or newer
- No external libraries are required

The project uses Python's `match-case` statement, which requires Python 3.10 or newer.

## How to Run

Save the program as a Python file, for example:

    employee_management.py

Open a terminal in the project directory and run:

    python employee_management.py

## Project Structure

    Employee Management System
    |
    |-- Employee
    |   |-- ID
    |   |-- Name
    |   |-- Age
    |   |-- Salary
    |
    |-- Manager
    |   |-- Employee Information
    |   |-- Department
    |
    |-- Developer
    |   |-- Employee Information
    |   |-- Languages
    |
    |-- Unique ID Validation
    |-- Multiple Object Storage
    |-- Getter and Setter Methods
    |-- Display System
    |-- Menu System

## Conclusion

This project is a practical implementation of Python Object-Oriented Programming. It demonstrates how a parent class can provide common functionality to multiple child classes through inheritance.

It also demonstrates encapsulation through private attributes, controlled access through getters and setters, constructor inheritance using `super()`, and the management of multiple objects using lists.

The project can be further extended with features such as updating employee information, deleting employees, searching across all employee types, saving data to a file, and adding a graphical user interface.
