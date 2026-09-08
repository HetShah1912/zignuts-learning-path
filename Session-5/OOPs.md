# Object-Oriented Programming (OOP)

## 1. What is OOP?

**OOP stands for Object-Oriented Programming.**

OOP is a programming approach where we organize a program around **objects**.

An object contains:

- **Properties** → data/state
- **Methods** → behavior/actions

For example, think about a `Student`.

A student has:

- name
- age
- course

And a student can:

- study
- attendClass
- displayDetails

Instead of keeping all of this information and functionality separately, OOP allows us to group them together inside an object.

### Why use OOP?

OOP helps us:

- Organize large programs
- Reuse code
- Reduce duplicate code
- Make code easier to maintain
- Represent real-world entities
- Create relationships between different types of objects

GFG describes JavaScript OOP around objects containing data/properties and behavior/methods, while W3Schools similarly describes Python and PHP OOP around classes and objects, reuse, and maintainability.

---

# 2. Classes and Objects

## What is a Class?

A **class is a blueprint/template** used to create objects.

Think about a building blueprint.

The blueprint itself isn't the actual building. It describes what the building should contain.

Similarly:

```text
Class
  ↓
Blueprint

Object
  ↓
Actual thing created from blueprint
```

For example:

```text
Class: Student

Properties:
- name
- age
- course

Methods:
- study()
- displayDetails()
```

From this class, we can create many students:

```text
student1
student2
student3
```

Each object can have different values.

---

## What is an Object?

An **object is an instance of a class**.

If `Student` is the class:

```javascript
const student1 = new Student();
```

then `student1` is an object of the `Student` class.

GFG describes a JavaScript class as a blueprint and an object as an instance of that class. W3Schools gives the same basic class/object distinction for Python and PHP.

---

## JavaScript

```javascript
class Student {
  display() {
    console.log("I am a student");
  }
}

const student1 = new Student();

student1.display();
```

### Explanation

```javascript
class Student
```

Creates a class named `Student`.

```javascript
display();
```

Creates a method.

```javascript
const student1 = new Student();
```

Creates an object from the `Student` class.

```javascript
student1.display();
```

Calls the method of that object.

### Output

```text
I am a student
```

---

## Python

```python
class Student:
    def display(self):
        print("I am a student")


student1 = Student()

student1.display()
```

Here:

```python
class Student:
```

creates the class.

```python
student1 = Student()
```

creates an object.

Python uses `self` to refer to the current object.

W3Schools describes a Python class as a blueprint for creating objects.

---

## PHP

```php
<?php

class Student
{
    public function display()
    {
        echo "I am a student";
    }
}

$student1 = new Student();

$student1->display();

?>
```

In PHP:

```php
new Student()
```

creates an object.

PHP uses `->` to access an object's properties and methods.

---

# 3. Constructor

A **constructor is a special method that runs automatically when an object is created.**

The main purpose of a constructor is to **initialize the object**.

For example, when creating a student object, we can immediately give it:

- name
- age
- course

Instead of doing:

```javascript
student.name = "Het";
student.age = 21;
student.course = "JavaScript";
```

we can pass the values when creating the object.

---

## JavaScript Constructor

JavaScript uses:

```javascript
constructor();
```

inside a class.

```javascript
class Student {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  display() {
    console.log(`Name: ${this.name}`);
    console.log(`Age: ${this.age}`);
  }
}

const student1 = new Student("Het", 21);

student1.display();
```

### Output

```text
Name: Het
Age: 21
```

### Important part

```javascript
constructor(name, age);
```

receives values.

```javascript
this.name = name;
this.age = age;
```

stores those values inside the object.

```javascript
new Student("Het", 21);
```

creates the object and automatically executes the constructor.

GFG specifically describes JavaScript's constructor as a special method that executes automatically when an object is created using `new`.

---

## Python Constructor

Python uses:

```python
__init__()
```

as the initializer/constructor method.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Het", 21)

student1.display()
```

### Output

```text
Name: Het
Age: 21
```

---

## PHP Constructor

PHP uses:

```php
__construct()
```

```php
<?php

class Student
{
    public $name;
    public $age;

    public function __construct($name, $age)
    {
        $this->name = $name;
        $this->age = $age;
    }

    public function display()
    {
        echo "Name: " . $this->name . "<br>";
        echo "Age: " . $this->age;
    }
}

$student1 = new Student("Het", 21);

$student1->display();

?>
```

PHP's OOP documentation explicitly includes `__construct()` as its constructor mechanism.

---

# 4. Destructor

A **destructor is a special method that is associated with the destruction/cleanup of an object.**

This concept is different from a constructor.

```text
Constructor
    ↓
Object is created

Destructor
    ↓
Object is destroyed/cleaned up
```

## JavaScript

JavaScript does **not** have a traditional class destructor.

So there is no JavaScript destructor example in this section.

---

## Python

Python provides:

```python
__del__()
```

which can be used as a finalizer associated with object destruction.

```python
class Student:
    def __init__(self, name):
        self.name = name
        print("Object created")

    def __del__(self):
        print("Object destroyed")


student1 = Student("Het")

del student1
```

### Output

```text
Object created
Object destroyed
```

The `del` statement removes the reference to the object. The timing of `__del__()` execution should not be treated as a general-purpose resource-management mechanism.

---

## PHP

PHP uses:

```php
__destruct()
```

```php
<?php

class Student
{
    public function __construct()
    {
        echo "Object created<br>";
    }

    public function __destruct()
    {
        echo "Object destroyed";
    }
}

$student1 = new Student();

?>
```

PHP's OOP curriculum explicitly includes `__destruct()` as its destructor mechanism.

---

# 5. Access Modifiers

**Access modifiers control who can access properties and methods of a class.**

The common access levels are:

```text
public
protected
private
```

They are mainly used for **encapsulation**.

---

# JavaScript

Modern JavaScript supports:

```javascript
public;
private;
```

JavaScript class fields are public by default, while a `#` prefix creates a private field.

```javascript
class Student {
  name = "Het";
  #age = 21;

  display() {
    console.log(this.name);
    console.log(this.#age);
  }
}

const student = new Student();

student.display();

console.log(student.name);

// console.log(student.#age); // Error
```

`name` is public.

`#age` is private and can only be accessed from inside the class.

GFG discusses encapsulation in JavaScript and the use of private fields (`#`) for hiding internal data.

---

# Python

Python uses naming conventions and name mangling for access control.

### Public

```python
class Student:
    def __init__(self):
        self.name = "Het"
```

### Protected convention

```python
class Student:
    def __init__(self):
        self._age = 21
```

A single `_` indicates that the member is intended for internal/protected use.

### Private

```python
class Student:
    def __init__(self):
        self.__age = 21
```

Double underscore triggers name mangling.

```python
student = Student()

# print(student.__age)  # Error
```

W3Schools explains Python's `_` protected convention and `__` private/name-mangled members.

---

# PHP

PHP has three explicit access modifiers:

### Public

Accessible from anywhere.

### Protected

Accessible inside the class and derived classes.

### Private

Accessible only inside the class where it is declared.

```php
<?php

class Student
{
    public $name = "Het";

    protected $course = "JavaScript";

    private $password = "12345";

    public function display()
    {
        echo $this->name;
        echo $this->course;
        echo $this->password;
    }
}

$student = new Student();

echo $student->name;

// echo $student->course;    // Error
// echo $student->password;  // Error

?>
```

W3Schools defines PHP's `public`, `protected`, and `private` visibility rules this way.

---

# 6. Inheritance

**Inheritance allows one class to acquire properties and methods from another class.**

The existing class is called the:

```text
Parent / Base class
```

The new class is called the:

```text
Child / Derived class
```

Example:

```text
Animal
   ↓
Dog
```

`Dog` can inherit functionality from `Animal`.

Inheritance is useful for **code reuse** and creating relationships between classes. GFG describes JavaScript inheritance using `extends`, including method overriding.

---

## JavaScript

```javascript
class Animal {
  eat() {
    console.log("Animal is eating");
  }
}

class Dog extends Animal {
  bark() {
    console.log("Dog is barking");
  }
}

const dog = new Dog();

dog.eat();
dog.bark();
```

### Output

```text
Animal is eating
Dog is barking
```

`Dog` inherits:

```javascript
eat();
```

from `Animal`.

### Method overriding

A child class can provide its own implementation of a parent method.

```javascript
class Animal {
  sound() {
    console.log("Animal makes a sound");
  }
}

class Dog extends Animal {
  sound() {
    console.log("Dog barks");
  }
}

const dog = new Dog();

dog.sound();
```

Output:

```text
Dog barks
```

---

## Python

```python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
```

Python's `Dog(Animal)` means `Dog` inherits from `Animal`.

---

## PHP

```php
<?php

class Animal
{
    public function eat()
    {
        echo "Animal is eating<br>";
    }
}

class Dog extends Animal
{
    public function bark()
    {
        echo "Dog is barking";
    }
}

$dog = new Dog();

$dog->eat();
$dog->bark();

?>
```

PHP uses the `extends` keyword for inheritance.

---

# 7. Constants

A **constant is a value that should not be changed after it has been defined.**

For example:

```text
PI = 3.14159
MAX_USERS = 100
COLLEGE_NAME = "ABC College"
```

---

## JavaScript

JavaScript uses `const` for variables that cannot be reassigned.

```javascript
const PI = 3.14159;

console.log(PI);

// PI = 4; // Error
```

Inside a class, JavaScript can also have static properties, but `const` itself is not a class-member declaration.

---

## Python

Python does not enforce a class constant with a dedicated `const` keyword.

A common convention is to use uppercase names:

```python
PI = 3.14159

print(PI)
```

or:

```python
class Math:
    PI = 3.14159

print(Math.PI)
```

The uppercase naming convention communicates that the value is intended to remain unchanged.

---

## PHP

PHP has a dedicated class constant using:

```php
const
```

```php
<?php

class Student
{
    const COLLEGE = "ABC College";
}

echo Student::COLLEGE;

?>
```

The value of a class constant cannot be changed after declaration. W3Schools documents class constants using `const` and access using `ClassName::CONSTANT`.

---

# 8. Abstract Classes

An **abstract class is a class designed to be inherited rather than directly instantiated.**

It is useful when multiple child classes should follow a common structure.

For example:

```text
Vehicle
   ↓
Car
Bike
Truck
```

All vehicles may need a `start()` method, but each type can implement it differently.

---

## JavaScript

JavaScript does not provide a dedicated `abstract class` keyword.

Therefore, no JavaScript implementation is included here.

---

## Python

Python provides abstract classes using the `abc` module.

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


square = Square(5)

print(square.area())
```

Output:

```text
25
```

The abstract class defines a required method:

```python
@abstractmethod
def area(self):
    pass
```

The child class must implement it.

W3Schools documents `ABC` and `abstractmethod` for creating abstract base classes.

---

## PHP

PHP has native abstract classes.

```php
<?php

abstract class Animal
{
    abstract public function sound();

    public function sleep()
    {
        echo "Animal is sleeping";
    }
}

class Dog extends Animal
{
    public function sound()
    {
        echo "Dog barks";
    }
}

$dog = new Dog();

$dog->sound();
$dog->sleep();

?>
```

The abstract class contains:

```php
abstract public function sound();
```

The child class must implement that method.

PHP's abstract-class rules are documented by W3Schools.

---

# 9. Interfaces

An **interface defines a contract that implementing classes must follow.**

An interface specifies what methods must exist, while the implementing class provides the implementation.

For example:

```text
Interface: Payment

Methods:
- pay()

        ↓

CreditCard
UPI
PayPal
```

Each payment class must provide `pay()`.

---

## JavaScript

JavaScript does not provide a native `interface` keyword.

Therefore, no JavaScript implementation is included here.

---

## Python

Python does not provide a dedicated `interface` keyword.

Therefore, no Python implementation is included here.

---

## PHP

PHP provides native interfaces.

```php
<?php

interface Payment
{
    public function pay();
}

class CreditCard implements Payment
{
    public function pay()
    {
        echo "Payment made using Credit Card";
    }
}

class UPI implements Payment
{
    public function pay()
    {
        echo "Payment made using UPI";
    }
}

$payment = new UPI();

$payment->pay();

?>
```

The interface says:

```php
public function pay();
```

Any class implementing `Payment` must provide the `pay()` method.

PHP uses:

```php
implements
```

to implement an interface. W3Schools states that interface methods must be implemented by classes that implement the interface.

---

# 10. Traits

A **trait is a mechanism for reusing methods across multiple classes.**

Instead of creating a parent-child relationship, a trait allows a class to include reusable functionality.

For example, suppose multiple classes need logging functionality:

```text
Student
Teacher
Admin

All need:

log()
```

A trait can contain the `log()` method.

---

## JavaScript

JavaScript does not have a native `trait` keyword.

Therefore, no JavaScript implementation is included here.

---

## Python

Python does not have a native `trait` keyword.

Therefore, no Python implementation is included here.

---

## PHP

PHP provides native traits.

```php
<?php

trait Logger
{
    public function log()
    {
        echo "Logging information...";
    }
}

class Student
{
    use Logger;
}

class Teacher
{
    use Logger;
}

$student = new Student();
$teacher = new Teacher();

$student->log();
$teacher->log();

?>
```

The trait:

```php
trait Logger
```

contains reusable functionality.

A class uses it with:

```php
use Logger;
```

Both `Student` and `Teacher` can now use `log()`.

W3Schools describes traits as a mechanism for reusing methods across multiple classes.

---

# 11. Static Methods and Properties

## What does Static mean?

Normally, a property or method belongs to an **object**.

Example:

```javascript
const student1 = new Student();
const student2 = new Student();
```

Each object can have its own instance data.

A **static member belongs to the class itself**, not to individual objects.

Think:

```text
Instance member
        ↓
Object

Static member
        ↓
Class
```

---

# JavaScript

JavaScript uses the `static` keyword.

### Static Method

```javascript
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(10, 20));
```

Output:

```text
30
```

Notice:

```javascript
MathUtils.add();
```

not:

```javascript
const math = new MathUtils();

math.add();
```

The method belongs to the class.

### Static Property

```javascript
class Student {
  static college = "ABC College";

  constructor(name) {
    this.name = name;
  }
}

const student1 = new Student("Het");
const student2 = new Student("Rahul");

console.log(Student.college);
```

Output:

```text
ABC College
```

The `college` property belongs to the class.

GFG describes JavaScript static methods and properties as members attached to the class rather than individual instances, accessed using the class name.

---

# Python

Python provides static methods using:

```python
@staticmethod
```

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(10, 20))
```

Output:

```text
30
```

The method can be called directly using the class.

Python also supports class-level attributes:

```python
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Het")
student2 = Student("Rahul")

print(Student.college)
print(student1.college)
print(student2.college)
```

Here `college` is defined on the class and can be accessed through the class.

---

# PHP

PHP uses the `static` keyword for both static methods and properties.

### Static Method

```php
<?php

class MathUtils
{
    public static function add($a, $b)
    {
        return $a + $b;
    }
}

echo MathUtils::add(10, 20);

?>
```

Output:

```text
30
```

Notice:

```php
MathUtils::add()
```

A PHP static method can be called without creating an object.

### Static Property

```php
<?php

class Student
{
    public static $college = "ABC College";
}

echo Student::$college;

?>
```

Output:

```text
ABC College
```

PHP accesses static properties using:

```php
ClassName::$property
```

W3Schools documents static properties as class-level properties that can be accessed without creating an instance.

---

# Quick Revision Table

| Concept           | JavaScript       | Python                   | PHP                          |
| ----------------- | ---------------- | ------------------------ | ---------------------------- |
| OOP               | ✅               | ✅                       | ✅                           |
| Classes & Objects | ✅               | ✅                       | ✅                           |
| Constructor       | `constructor()`  | `__init__()`             | `__construct()`              |
| Destructor        | —                | `__del__()`              | `__destruct()`               |
| Access Modifiers  | Public / Private | `_` / `__` conventions   | Public / Protected / Private |
| Inheritance       | `extends`        | Parentheses              | `extends`                    |
| Constants         | `const`          | Uppercase convention     | `const`                      |
| Abstract Classes  | —                | `ABC` + `abstractmethod` | `abstract`                   |
| Interfaces        | —                | —                        | `interface`                  |
| Traits            | —                | —                        | `trait`                      |
| Static Methods    | `static`         | `@staticmethod`          | `static`                     |
| Static Properties | `static`         | Class attributes         | `static`                     |

---

# Most Important Keywords to Remember

## JavaScript

```javascript
class
constructor
new
extends
super
static
this
#
```

## Python

```python
class
__init__
self
__del__
ABC
abstractmethod
@
```

## PHP

```php
class
__construct
__destruct
public
protected
private
extends
const
abstract
interface
implements
trait
use
static
```

---

# OOP Concepts in Simple Words

| Concept         | Simple Meaning                                           |
| --------------- | -------------------------------------------------------- |
| OOP             | Programming using objects                                |
| Class           | Blueprint for objects                                    |
| Object          | Actual instance of a class                               |
| Constructor     | Initializes an object                                    |
| Destructor      | Performs finalization associated with object destruction |
| Access Modifier | Controls access to class members                         |
| Inheritance     | Child gets functionality from parent                     |
| Constant        | Value intended not to change                             |
| Abstract Class  | Base class intended for inheritance                      |
| Interface       | Contract that implementing classes must follow           |
| Trait           | Reusable methods shared across classes                   |
| Static Method   | Method belonging to the class                            |
| Static Property | Property belonging to the class                          |

---

# A Simple Mental Model

Imagine a **Student Management System**.

```text
                 Student
                   |
          ┌────────┴────────┐
          |                 |
       Student 1          Student 2
          |                 |
        Het               Rahul
```

### Class

```text
Student
```

is the blueprint.

### Objects

```text
student1
student2
```

are actual students.

### Constructor

Sets:

```text
name
age
course
```

when the object is created.

### Access Modifiers

Control who can access:

```text
name
age
password
```

### Inheritance

Could create:

```text
Student
   ↓
CollegeStudent
```

### Abstract Class

Could define a common structure for:

```text
Student
Teacher
Staff
```

### Interface

Can define a required contract such as:

```text
Payment
   ↓
pay()
```

### Trait

Can provide reusable functionality such as:

```text
Logger
   ↓
log()
```

### Static Property

Could store information shared by the entire class:

```text
Student.totalStudents
```

### Static Method

Could perform a class-level operation:

```text
Student.getTotalStudents()
```

---

# Final Priority for Your Learning

Since **JavaScript is your first preference**, learn the concepts in this order:

```text
1. OOP basics
       ↓
2. Classes & Objects
       ↓
3. Constructor
       ↓
4. Access Modifiers
       ↓
5. Inheritance
       ↓
6. Constants
       ↓
7. Static Methods & Properties
       ↓
8. Abstract Classes
       ↓
9. Interfaces
       ↓
10. Traits
       ↓
11. Destructor
```

For your actual JavaScript learning, the first seven are especially important because they map directly to JavaScript's class system. The remaining topics are useful for understanding OOP across languages, particularly because your syllabus explicitly includes them.

## Reference Sources

- JavaScript: [GeeksforGeeks — Object-Oriented Programming in JavaScript](https://www.geeksforgeeks.org/javascript/introduction-object-oriented-programming-javascript/?utm_source=chatgpt.com)
- JavaScript Classes & Objects: [GeeksforGeeks — Classes and Objects in JavaScript](https://www.geeksforgeeks.org/javascript/classes-and-objects-in-javascript/?utm_source=chatgpt.com)
- JavaScript Inheritance: [GeeksforGeeks — JavaScript Inheritance](https://www.geeksforgeeks.org/javascript/javascript-inheritance/?utm_source=chatgpt.com)
- JavaScript Static Methods/Properties: [GeeksforGeeks — JavaScript Static Methods and Properties](https://www.geeksforgeeks.org/javascript/js-static-methods/?utm_source=chatgpt.com)
- Python: [W3Schools — Python OOP](https://www.w3schools.com/python/python_oop.asp?utm_source=chatgpt.com)
- Python Classes: [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp?utm_source=chatgpt.com)
- Python Encapsulation: [W3Schools — Python Encapsulation](https://www.w3schools.com/python/python_encapsulation.asp?utm_source=chatgpt.com)
- Python Abstract Base Classes: [W3Schools — Python abc Module](https://www.w3schools.com/python/ref_module_abc.asp?utm_source=chatgpt.com)
- PHP OOP: [W3Schools — PHP OOP](https://www.w3schools.com/php/php_oop_what_is.asp?utm_source=chatgpt.com)
- PHP OOP Topics: [W3Schools — PHP OOP Examples](https://www.w3schools.com/php/php_examples.asp?utm_source=chatgpt.com)
