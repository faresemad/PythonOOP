# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -------------------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes and Methods On the same object
# Instance Methods Can Access the Class Itself
# -------------------------------------------------------------------------------

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
print(mone.getFullInfo())2