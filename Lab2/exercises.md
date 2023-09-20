# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping)
   and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL.
   Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing?

- A good example would be a function called 'pop' which only removes one element.
- A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

I think that the Python overall gives pretty good verbs to describe functions and member functions. For example, the dictionary has .clear() which removes all items and .keys() which returns all the keys. The list has .append(), .clear(), and .copy() which all accurately reflect what the function does.Python does a good job with these verbs which helps make it an easier and more intuitive language to use.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

In Python a dictionary is really a hashmap/hashtable. It stores key and value pairs which are accessed by their keys. A list is using a dynamic array as its data structure. Python is unique in that is uses dynamic arrays that do not need to be resized.

These two are different in the ways that they store data. A list stores the data in a contiguous chunk of memoery where as a hashmap will hash the the pairs into memory in different memory locations. These designs means that data can be added, searched, or removed with different speeds of the two. A hashmap is much faster as operations like searching for an element can be done in constant O(1) time where a list is done in linear O(n) time.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list does allow random access.This is because the data is stored in a contiguous block. This means that we can use the index to retrieve the desired data in O(1) time from the array.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.).
   What do you think are the pros/cons of a library that can work with any data type?

   The pros are that it makes the language easy to work with. You can easily implement these data structures without having to put to much work into checking for correct data types or having to define what type of data you are using in the first place. It also makes it easy to pass data through your program to other functions or methods.

   The cons are that with it being so easy to use any kind of data, it is easy to have type errors or data corruption. For example, string numbers could easily be mistaken for float or int numbers in python, because the data type is not explicitly stated. Time might have to be wasted processing data if it is not the desired type.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
   Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

   In the context of the requests API, I think that the function names convey the type of request being made pretty well. We have 7 main methods which are GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Requests.Request has up to 10 parametrs that can be included which can be confusing. With so many arguments it can be confusing as to what is most critical to use or not.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?

`**kwargs` stands for key word arguments. This allows us to enter a keyworded variable amount of arguments into a function. It being keyworded means that we provide a name to the variables passed in the function. They keywords are essentially having their word mapped to a value.

Strengths are that it is quite flexible and we can input different data types into the key words. We also have a refrence word that maps to the value.

Weaknesses are that it could be potentially hard to clean the keyword data if we have many different data types. Also there are a lot of different key words that could be entered which would not give much structure to our code.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text.
   Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

   By setting something to None and having that in the docs, then you know that parameter is optional. If there is an argument that we know we need, then we can set it to some predetermined value to minimize user error. So essentially None is helping us determine what is critical or not to the function.
