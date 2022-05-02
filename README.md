# Python Object Oriented Programming (OOP)
<ht>
  
## Class Syntax and Info 
- [01] Class is The Blueprint Or Constructor Of The Objcet
- [02] Class Instantiate Means Create Instance Of A Class
- [03] Instance => Object Created From Class And Have Their Methods and Attributes
- [04] Class Defined With Keyword Class
- [05] Class Name Written With PascalCase [UpperCamelCase] Style
- [06] Class May Contains Methods and Attributes
- [07] When Creating Object Python Look For The Built In __init__ Method
- [08] \_\_init__ Method Called Every Time You craete object from class
- [09] \_\_init__ Method is Initialize The Date for the object
- [10] Any method with two underscore in the start and end called Dunder or Magic Method
- [11] Self Refer to the current Instnace created from class and must be first parameter
- [12] self can be name anything
- [13] in python you don't need to call new() keyword to creat object
```python
# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A CLass ]
#     Each Instance Is Separate Object 
#     def __init__(self , other_data):
#         Body Of Function
# -------------------------------------------------------------------------------------
class Member:
    def __init__(self) -> None:
        print("A New member has been added")

# Create Object From Class
member_one = Member()

# get all attributes on my class
print(dir(member_one))
```
## Instance Attributes and Methods
- Self: Point To Instance Created From Class
- Instance Attributes: Instance Attributes Defined Inside The Constructor
- [1] Instance Methods: Take Self Parameter Which Point Instance Created From Class
- [2] Instance Methods Can Have More Than One Parameter Like Any Function
- [3] Instance Methods Can Freely Access Attributes and Methods On the same object
- [4] Instance Methods Can Access the Class Itself
```python
class Member:
    # Hint Typing For Attribute => ( -> None )
    def __init__(self,firstName,middleName,lastName,gender) -> None: # Hint Typing
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.gender = gender


    def getFullName(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"

    def getNameWithTitle(self):
        if self.gender == "Male":
            return f"Hello Mr.{self.firstName}"
        elif self.gender == "Female":
            return f"Hello Miss.{self.firstName}"
        else:
            return f"Hello {self.firstName}"

    def getFullInfo(self):
        return f"{self.getNameWithTitle()} , Your Full Name Is {self.getFullName()}"

mone = Member("Fares" , "Emad" , "El-Sherbiny","Male")
# print(dir(mOne))
# print(mOne.firstName,mOne.middleName,mOne.lastName)

# print(mone.getFullName())
# print(mone.getNameWithTitle())
print(mone.getFullInfo())
```
## Class Attributes
- Class Attributes: Attributes Defined Outside The Constructor
```python
class Member:
    notAllowedNames = ["hell","shit","fuck","fucken"]
    def __init__(self,firstName,middleName,lastName,gender) -> None: # Hint Typing
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.gender = gender

    def getFullName(self):
        if (self.firstName) and (self.lastName) and (self.middleName) in Member.notAllowedNames:
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.firstName} {self.middleName} {self.lastName}"

    def getNameWithTitle(self):
        if self.gender == "Male":
            return f"Hello Mr.{self.firstName}"
        elif self.gender == "Female":
            return f"Hello Miss.{self.firstName}"
        else:
            return f"Hello {self.firstName}"

    def getFullInfo(self):
        return f"{self.getNameWithTitle()} , Your Full Name Is {self.getFullName()}"

mthree = Member("tomas","hasan","shalaby","Male")
print(mthree.getFullInfo())

mtwo = Member("tomas","fucken","shelby","Male")
print(mtwo.getFullInfo()) # here we will see in output "Name Not Allowed" cuz 'fucken' in notAllowedNames
```
