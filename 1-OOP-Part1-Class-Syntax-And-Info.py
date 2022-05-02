# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Constructor Of The Objcet
# [02] Class Instantiate Means Create Instance Of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword Class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You craete object from class
# [09] __init__ Method is Initialize The Date for the object
# [10] Any method with two underscore in the start and end called Dunder or Magic Method
# [11] Self Refer to the current Instnace created from class and must be first parameter
# [12] self can be name anything
# [13] in python you don't need to call new() keyword to creat object
# -------------------------------------------------------------------------------------
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