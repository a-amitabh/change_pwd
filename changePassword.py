import pwd_validator

def verifyPassword():
    return True

def changePassword(oldPassword, newPassword):
    if verifyPassword():
        val = pwd_validator.PasswordValidator(oldPassword, newPassword)
        print(val.validate_all())
        if val.validated is False:
            #print("Password not changed")
            return False
        else:
            #print("Password changed successfully")
            return True
    else:
        #print("entered pwd is incorrect")
        return False
