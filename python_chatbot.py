import datetime
import string
import sys
import time

name=input('Please enter your name :')

presenthour=datetime.datetime.now().hour

if 5<=presenthour<12:
    print('Good Morning '+name+' !' )
elif 12<=presenthour<17:
    print('Good Afternoon',name,'!')
elif 17<=presenthour<21:
    print('Good Night',name,'!')

print('Welcome to your study buddy! how can I help you?')

responses = {
    # ==========================================
    # 1. GREETINGS & CHITCHAT
    # ==========================================
    (
        "hello", "hi", "hey", "hello there", "hi there", "yo", "greetings"
    ): "Hello! I am your Python study buddy. How can I help you learn Python today?",

    (
        "how are you", "how are you doing", "how's it going", "are you doing well"
    ): "I'm doing fantastic! Ready to parse some Python concepts. What are we studying today?",

    (
        "who are you", "what are you", "what is your name", "tell me about yourself"
    ): "I am your interactive Python Tutor Bot! Ask me any Python question, from basic variables to advanced OOP.",

    # ==========================================
    # 2. PYTHON BASICS & SYNTAX
    # ==========================================
    (
        "what is python", "explain python", "why use python", "what is python language"
    ): "Python is a high-level, interpreted, general-purpose programming language. It is famous for its simple, readable syntax (which looks a lot like English) and its massive ecosystem for web development, data science, and AI.",

    (
        "what is a print statement", "what is print", "how to print", "how do you use print", "explain print statement"
    ): "The print() function outputs text or data to the console. Example:\nprint('Hello, World!')\nYou can also print multiple items: print('Age:', 25)",

    (
        "what is a variable", "what is variable", "how to define a variable", "explain variables", "what are variables"
    ): "A variable is a named storage location in your computer's memory that holds a value. In Python, you don't need to declare its type. Example:\nx = 10\nname = 'Alice'",

    (
        "what are the basic data types", "what are data types", "explain data types", "python data types"
    ): "Python's standard basic data types are:\n1. Integer (int): Whole numbers like 10, -5\n2. Float (float): Decimal numbers like 3.14, 0.0\n3. String (str): Text enclosed in quotes like 'hello'\n4. Boolean (bool): True or False.",

    (
        "what is type casting", "how to change data types", "what is type conversion", "explain typecasting"
    ): "Type casting is converting a variable from one data type to another. For example:\n- int('5') converts the string '5' to integer 5.\n- float(10) converts integer 10 to 10.0.\n- str(123) converts number 123 to string '123'.",

    # ==========================================
    # 3. CONTROL FLOW & LOOPS
    # ==========================================
    (
        "what is an if statement", "how to use if else", "explain conditional statements", "what is elif"
    ): "Conditional statements run different code depending on whether a condition is True or False. Example:\nif score >= 90:\n    print('A')\nelif score >= 80:\n    print('B')\nelse:\n    print('C')",

    (
        "what is a for loop", "how do for loops work", "explain for loop", "how to loop through a list"
    ): "A 'for loop' is used to iterate over a sequence (like a list, tuple, string, or range). Example:\nfor item in [1, 2, 3]:\n    print(item)",

    (
        "what is a while loop", "how do while loops work", "explain while loop", "when to use while loop"
    ): "A 'while loop' repeatedly runs a block of code as long as a specific condition remains True. Example:\ncount = 0\nwhile count < 3:\n    print(count)\n    count += 1",

    (
        "what is break and continue", "what does break do", "what does continue do", "difference between break and continue"
    ): "- 'break' immediately stops and exits the current loop.\n- 'continue' skips the rest of the code in the current iteration and jumps straight to the next loop cycle.",

    # ==========================================
    # 4. DATA STRUCTURES (COLLECTIONS)
    # ==========================================
    (
        "what is a list", "what is list", "explain lists", "what are lists", "how to make a list"
    ): "A list is an ordered, changeable (mutable) collection of items written inside square brackets []. Example:\nmy_list = ['apple', 'banana', 10, True]",

    (
        "what is a tuple", "what is tuple", "explain tuples", "what are tuples", "difference between list and tuple"
    ): "A tuple is an ordered, unchangeable (immutable) collection written inside parentheses (). Because they are immutable, they are faster than lists. Example:\nmy_tuple = (1, 2, 3)",

    (
        "what is a set", "what is set", "explain sets", "what are sets", "how do sets work"
    ): "A set is an unordered, unindexed collection of unique elements written inside curly braces {}. Sets automatically filter out duplicate items. Example:\nmy_set = {1, 2, 2, 3}  # results in {1, 2, 3}",

    (
        "what is a dictionary", "what is dict", "explain dictionaries", "what are dictionaries", "how to use a dict"
    ): "A dictionary is a collection of key-value pairs stored inside curly braces {}. It allows you to quickly look up a value using its unique key. Example:\nuser = {'name': 'Alice', 'role': 'Admin'}",

    # ==========================================
    # 5. FUNCTIONS & SCOPE
    # ==========================================
    (
        "what is a function", "what is function", "what are functions", "how to define a function", "explain functions"
    ): "A function is a reusable block of code that only executes when it is called. Define it with 'def'. Example:\ndef greet(name):\n    return f'Hello {name}'",

    (
        "what is a lambda function", "what are lambdas", "explain lambda", "what is an anonymous function"
    ): "A lambda function is a small, one-line anonymous function defined without a name using the 'lambda' keyword. Example:\nadd_five = lambda x: x + 5\nprint(add_five(10))  # Outputs 15",

    (
        "what are args and kwargs", "what is *args", "what is **kwargs", "explain args and kwargs"
    ): "- *args allows a function to accept any number of positional arguments (passed as a tuple).\n- **kwargs allows a function to accept any number of keyword arguments (passed as a dictionary).",

    # ==========================================
    # 6. FILE HANDLING
    # ==========================================
    (
        "what is file handling", "how to open a file", "explain file handling", "how to read and write files in python"
    ): "File handling allows you to read, write, and manipulate external files. Always use the 'with' statement (context manager) to automatically close files when done. Example:\nwith open('file.txt', 'r') as file:\n    content = file.read()",

    (
        "how to write to a file", "how to write a file", "how to append to a file", "difference between w and a modes"
    ): "- Use mode 'w' to write to a file (this overwrites existing content).\n- Use mode 'a' to append content to the end of an existing file.\nExample:\nwith open('notes.txt', 'a') as f:\n    f.write('\\nNew Line Added!')",

    # ==========================================
    # 7. EXCEPTION & ERROR HANDLING
    # ==========================================
    (
        "how do you handle exceptions", "what is exception handling", "explain try except", "what is try except", "how to handle errors"
    ): "Exception handling prevents your program from crashing when an error occurs by using 'try' and 'except' blocks. Example:\ntry:\n    num = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')",

    (
        "what is finally block", "what does try except finally do", "explain try except finally", "what is finally in python"
    ): "The 'finally' block in a try-except statement will always run, regardless of whether an exception was raised or caught. It is used for cleanup tasks like closing database connections.",

    # ==========================================
    # 8. OBJECT-ORIENTED PROGRAMMING (OOP)
    # ==========================================
    (
        "what is oop", "what is object oriented programming", "explain oop concepts", "what is class and object"
    ): "OOP stands for Object-Oriented Programming. It is a programming style that models real-world things using:\n- Classes: The blueprints (templates).\n- Objects: The actual items built from those blueprints.",

    (
        "what is a class", "what is class", "how to create a class", "explain classes"
    ): "A class is a blueprint for creating objects. It defines the state (attributes) and behavior (methods) that its objects will have. Example:\nclass Dog:\n    def __init__(self, name):\n        self.name = name",

    (
        "what is init method", "what is the constructor", "what does __init__ do", "explain constructor in python"
    ): "The __init__ method is the constructor of a Python class. It runs automatically when you create a new object of that class, initializing its starting attributes.",

    (
        "what is inheritance", "explain inheritance", "how does inheritance work in python", "what is a parent and child class"
    ): "Inheritance allows a child class to inherit attributes and methods from a parent class, promoting code reuse. Example:\nclass Animal:\n    pass\nclass Dog(Animal): # Dog inherits from Animal\n    pass",

    (
        "what is polymorphism", "explain polymorphism", "how does polymorphism work"
    ): "Polymorphism means 'many forms'. It allows different classes to have methods with the same name but different behaviors. For example, both a Dog class and a Cat class can have a speak() method, but Dog barks while Cat meows.",

    (
        "what is encapsulation", "explain encapsulation", "how to hide variables in python", "what are private attributes"
    ): "Encapsulation is hiding the internal details of an object and restricting direct access to its data. In Python, you make an attribute private by prefixing its name with double underscores, like self.__secret_key.",

    (
        "what is abstraction", "explain abstraction", "what are abstract classes"
    ): "Abstraction hides complex implementation details and only shows the essential features to the user. This is achieved in Python using the 'abc' module and declaring abstract methods that must be defined by child classes.",

    # ==========================================
    # 9. ADVANCED CONCEPTS & DECORATORS
    # ==========================================
    (
        "what is a decorator", "explain decorators", "how do decorators work", "what is @ in python"
    ): "A decorator is a function that takes another function as an argument, extends its behavior without modifying the original code, and returns a new function. It is written using the '@' symbol above a function definition.",

    (
        "what is a generator", "explain generators", "what does yield do", "difference between return and yield"
    ): "A generator is a special function that yields values one at a time using 'yield' instead of returning all at once. It saves computer memory because it generates data on the fly rather than keeping it all in memory.",

    (
        "what is list comprehension", "explain list comprehensions", "how to write list comprehension"
    ): "List comprehension offers a shorter, cleaner syntax to create a new list from an existing sequence. Example:\nsquares = [x**2 for x in range(5)]  # yields [0, 1, 4, 9, 16]",

    # ==========================================
    # 10. MODULES & PACKAGES
    # ==========================================
    (
        "what is a module", "what is module", "explain modules", "what are modules", "how to import a module"
    ): "A module is a single Python file (.py) containing code (functions, classes, variables) that you can import and use in other files. Example: import math.",

    (
        "what is a package", "what is package", "explain packages", "difference between module and package"
    ): "A package is a collection of modules organized in folders. For a folder to be treated as a Python package, it traditionally contains an empty __init__.py file."
}


def professional_print(text, delay=0.005):
    """Prints text with a subtle, professional typewriter effect for UI polish."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ==========================================
# INITIALIZE METRICS & START LOOP
# ==========================================
# This line MUST go right here before the loop starts so it doesn't reset to 0 every time you type!
questions_answered_count = 0 

print("=" * 60)
print("   PYTHON STUDY BUDDY V2.5 - ARCHITECTURE ACTIVE")
print("=" * 60)
print("System: Ready. Type your query or 'exit' to terminate session.\n")

while True:
    # 1. Capture user input safely
    try:
        raw_input = input("\nYou: ")
    except (KeyboardInterrupt, EOFError):
        print("\n\nSession interrupted safely.")
        break

    # 2. Sanitize input (Lowercase, strip whitespace, remove punctuation like ?)
    clean_input = raw_input.strip().lower()
    clean_input = clean_input.translate(str.maketrans('', '', string.punctuation))

    # 3. Evaluate exit conditions & display final analytics summary
    if clean_input in ["exit", "quit", "bye", "goodbye", "good bye"]:
        print("-" * 60)
        professional_print("System: Compiling session analytics...")
        time.sleep(0.4) 
        
        # The counter displays your total final score right here!
        summary_msg = (
            f"\n[SESSION COMPLETE]\n"
            f"You successfully reviewed {questions_answered_count} technical concepts during this session. "
            f"Your commitment to mastering these Python fundamentals demonstrates excellent progress. "
            f"Keep up the rigorous study habit. Terminal connection closed. Goodbye!"
        )
        professional_print(summary_msg)
        print("-" * 60)
        break

    # 4. Skip empty inputs gracefully
    if not clean_input:
        continue

    # 5. Search the knowledge base
    found_match = False
    print("\n" + "-" * 40)  # Visual boundary for the bot's response
    
    for questions_tuple, answer in responses.items():
        # Check if the cleaned input matches any variation in the dictionary keys
        if clean_input in questions_tuple:
            professional_print(f"Bot: {answer}")
            found_match = True
            questions_answered_count += 1  # <--- It adds 1 to your counter here!
            break
            
    # 6. Professional fallback framework if no match is found
    if not found_match:
       
        fallback_msg = (
        "Bot: I don't have an answer for that question specific topic yet. "
        "However, I can help you with the following core Python concepts:\n\n"
        "• Variables and Data Types\n"
        "• Control Flow (If statements, Loops)\n"
        "• Functions and Modules\n"
        "• Lists, Dictionaries, and Tuples\n"
        "• Error Handling (Try/Except)\n\n"
        "Please try asking a question about one of these topics!\n\n"
        "If you are asking about those topics try a different way"
)
        professional_print(fallback_msg)
        
        print("-" * 40)
                      