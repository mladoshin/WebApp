class User():
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
    def check_email(self, email):
        isValid = False
        if("@" in email):
            isValid = True
        
        return isValid
    def check_password(self, password):
        isValid = False
        u = 0
        l = 0
        d = 0
        for character in password:
            if(character.isupper()):
                u += 1
            
            if(character.islower()):
                l += 1

            if(character.isdigit()):
                d += 1

        if(u*l*d != 0) and (len(password)>=6 and len(password)<=12):
            isValid = True

        return isValid

user1 = User("Max", "Ladoshin", "ml@gmail.ru", "Asd124")
print(user1.check_email(user1.email))
print(user1.check_password(user1.password))