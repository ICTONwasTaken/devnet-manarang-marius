"""
Module 2 — Lesson 4: Functions
Student: Manarang, Marius L.
Date: 09/24/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Functions are essentially reusable code that
you create so you don't have to constantly
copy and paste long stretches of code.
They are flexible and makes the code easier
to read and manage. And they aren't too
hard to understand when you get the hang of
it.

============================================
KEY VOCABULARY
============================================
- def: 
Short for "define", this keyword is how all functions
start, and it's how Python will know when something is
a function.

Essentially, telling Python that: "I am going to be
defining a function now!"

- function_name(parameter):
After telling Python that, you will need to actually
define it. And it requires a specific format to be valid.

First, is the name. This is how you will be calling the
function in your code. So whenever you want to use the
function, you use this name.
You are telling Python that: "Whenever I say this, I
want to play this function!"

Next, is the parameter, which are inside the parenthesis. 
This does not need to filled, you only use it when you 
want to pass certain variables inside. Like if you wanted 
to specifically use "Width" and "length".
When you create the function, what you put into the
parameter will serve as 'template variables' for your
purposes. And when you call it, the variables you
put will be assigned to the template variables until
the function ends.

The names you add when making the parameter don't actually 
matter, they are only for user convinience — You are free to 
put "dwadaw" if you want, as long as you think it can be
easily understood and typed — rather, it is the placement
of the variables that helps denote what variable will
be assigned  to what template variable.

In short, you tell Python: "Use the variables here in place
of anything inside those parenthesis!"

- parameter: str / int / float / bool / list / tuple / dict:
These are used if you want a specific data-type to be inside.
If the wrong data-type is inside, it will output an error.
This is used because you obviously don't want a string in
place of an int, or a list in place of a dictionary.

Telling python: "I ONLY want this type of variable to be 
used, nothing else!"

- return:
This keyword allows the function to send out something
once it's done. Incredibly useful for when you, say
have a function that does math, and you want it to give
you those results.
You need this because functions can't nromally alter 
variables outside (without being global). So the 
numbers you calculate disappear, unless you return it.

Telling Python: "After this function is done, give
me this thing."

- global:
As mentioned earlier, this keyword allows functions
to affect select variables outside of its range.

Telling Python: "Hey, I want to alter these
variables here, and I don't want these changes
to disappear after this function ends."

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
number1 = 0
number2 = 0

def example(this: int, that: int):
  global number2
  answer = this + that
  
  number2 = answer + 10
  return answer
  
print("Number 1:",number1)
print("Number 2:",number2)  

number1 = example(10, 20)

print("")
print("New Number 1:",number1)
print("New Number 2:",number2)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
