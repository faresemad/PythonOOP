# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -------------------------------------------------------------
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
print(mtwo.getFullInfo())
