import unittest
import changePassword

class TestPwdChange(unittest.TestCase):

    """Tests to validate minimum alphanumeric char limit of 18"""
    def test_AlphaNum(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "ABCDXYZabcdxyz@123"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ@1234"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ@1234A"))

    """Tests to validate permissible spec char list"""
    def test_SpecChar(self):
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ!@#$1234"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ#$&*1234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ+#_1234"))

    """Tests to validate min char limit for alphabet, number and spec char"""
    def test_MinCharReq(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzabcdxyz@12341234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "ABCDXYZABCDXYZ@12341234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "ABCDXYZabcdxyz@EFGH"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "ABCDXYZabcdxyz1234"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "ABCDEFGHIJKLMNOPp1@"))

    """Tests to validate limitation of at most 4 duplicates of a char"""
    def test_duplicateCharLimit(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdaaaaABCDXYZ!@#$1234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcd2222ABCDXYZ!@#$1234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyz@@ABCD@@XYZ!@#$1234"))
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdAAAAABCDXYZ!@#$1234"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdAAABCDXYZ###$111234"))

    """Test to validate limitation on number of spec chars"""
    def test_SpecCharLimit(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ@#!@@1234"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "abcdxyzABCDXYZ@#!@1234"))

    """Tests to validate limit on percentage of chars in password which are numbers """
    def test_numCountLimit(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "1234567891ABCDabcd@"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "123456789AABCDabcd@"))

    """Test to validate that password with greater than 80% simmilarity are not allowed"""
    def test_PwdDissimilarity(self):
        self.assertFalse(changePassword.changePassword("ABCDXYZabcdxyz@123123", "12CDXYZabcdxyz@123AB"))
        self.assertTrue(changePassword.changePassword("ABCDXYZabcdxyz@123123", "12CDXYZabcdxyz@12AB"))


if __name__ ==  '__main__':
    unittest.main()