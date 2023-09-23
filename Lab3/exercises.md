# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:

   - MObject is a concrete class. This is because the class can be instantiated and is not defined with the ABC keyword as a parameter. An abstract class in Python imports the ABC module and creates abstract classes with (ABC) in the class parameter. If you try to instantiate these ABC abstract class and if they have an @abstractmethod decorator you will raise a type error.

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?

   - This method is called when the instance is going to be destroyed. It is also known as a destructor. If a base class has a **del** method, this method is called to ensure proper deletion of the base class part of the instance. This method is essentially performs actions that ensure it is later properly removed from memory.

3. What class does Texture inherit from?

   - Texture is inheriting from the Image class. We know this because the Texture class has the Image class as a parameter. This means that we can instantiate the Texture class and use the inherited constructor from the parent class which is Image. We also inherit the methods from the Image class meaning that we can call them in the Texture class.

4. What methods and attributes does the Texture class inherit from 'Image'?

   - Inherited Attributes:
     m_width
     m_height
     m_colorChannels
     m_Pixels
   - Inherited Methods:
     `__init__`(constructor)
     getWidth
     getHeight
     getPixelColorR
     getPixels
     setPixelsToRandomValue

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!

   - Saying that a texture is-a image does not make much sense. However, saying that an image has-a texture makes much more sense. This is because an image can have many different components to it with texture being one of them, so making it a composition makes a lot of sense.

6. I did not declare a constructor for Texture. Does Python automatically create constructors for us?

   - Although you did not declare a constructor in texture, you have inherited from Image. This means that we inherit the constructor from the parent Image class. In the case, the parents constructor is being used.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

- The first time the logger is constructed, it will print out:
  - `Logger created exactly once`
- If the logger is already initialized, it will print: - `logger already created`
  Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
  Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

- Singletons in Python are not thread safe. Python does not have a built in locking mechanism. Multiple threads could also concurrently call the singleton instance, so we could potentially have multiple instances. To make it thread safe, a lock would have to be added which could slow down the application.
