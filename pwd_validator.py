import re

class PasswordValidator(object):
    """ A password validator, used to validate a password for
        specific characters, numbers, and special characters """

    validated = False

    def __init__(self, curr_password, new_password):
        self.curr_Password = curr_password
        self.new_Password = new_password

    def validate_alphanum_count(self):
        return len(re.sub(r'[^a-zA-Z0-9]', '', self.new_Password)) >= 18

    def validate_specChar_list(self):
        return re.subn(r'[^a-zA-Z0-9!@#$&*]', '', self.new_Password)[1] == 0

    def validate_upper_case(self):  # Check for upper case characters
        return re.search("[A-Z]", self.new_Password) is not None

    def validate_lower_case(self):  # Check for lower case characters
        return re.search("[a-z]", self.new_Password) is not None

    def validate_integers(self):  # Check for integers
        return re.search("[0-9]", self.new_Password) is not None

    def validate_spec_chars(self):  # Check for special characters
        return re.search("[!@#$&*]", self.new_Password) is not None

    def validate_max_duplicate(self):
        pwd = self.new_Password
        chars = set(pwd)
        for char in chars:
            if (pwd.count(char) >= 4):
                return False
            else:
                pass
        return True

    def validate_max_specChar(self):
        return len(re.sub(r'[^!@#$&*]', '', self.new_Password)) <= 4

    def validate_maxNumRatio(self):
        return len(re.sub(r'[^0-9]', '', self.new_Password)) < len(self.new_Password)/2

    def validate_pwd_similarity(self):
        width = int(len(self.curr_Password) * 0.8)
        for i in range(0, len(self.curr_Password) - width):
            if (self.curr_Password[i:i+width] in self.new_Password):
                return False
            else:
                pass
        return True


    def validate_all(self):
        """ Validate all criterias """
        alphanumCount = self.validate_alphanum_count()
        # print(alphanumCount)
        specChar = self.validate_specChar_list()
        upper = self.validate_upper_case()
        lower = self.validate_lower_case()
        digits = self.validate_integers()
        specs = self.validate_spec_chars()
        duplicates = self.validate_max_duplicate()
        #print(duplicates)
        MaxSpecChar = self.validate_max_specChar()
        MaxNumRatio = self.validate_maxNumRatio()
        Pwd_similarity = self.validate_pwd_similarity()

        if alphanumCount is False:
            return "Failed minimum alphanum count validation"
        elif specChar is False:
            return "Only !@#$&* are allowed as special char"
        elif upper is False:
            return "Failed uppercase validation. At least one upper case char is required (A - Z)"
        elif lower is False:
            return "Failed lower case validation. At least one lower case char is required (a - z)"
        elif digits is False:
            return "Failed integer validation. At least one integer is required (0 - 9)"
        elif specs is False:
            return "Failed special characters validation. At least one special char is required (! @ # $ & *)"
        elif duplicates is False:
            return "A char cannot occur more than 4 times"
        elif MaxSpecChar is False:
            return "No more than 4 special characters are allowed"
        elif MaxNumRatio is False:
            return " 50 % of password should not be a number"
        elif Pwd_similarity is False:
            return "New Password should be less than 80% similar to old password"
        else:
            self.validated = True
            return "Entered password is valid"

