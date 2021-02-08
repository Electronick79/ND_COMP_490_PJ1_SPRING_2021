from tokenize import Name

import Student as Student
import city as city
import self as self

class Universities(object):
    pass


Universities.py:


class university1:

    def __init__( self,School.Name, School.city, 2018.Student.size, 2017.Student.size,2017.earnings.3_yrs_after_completion,2016.repayment.3_yr_repayment):

    self.School.Name = School.Name

    self.School.city = School.city

    self.2018.Student.size = 2018.Student.size

    self.2017.Student.size = 2017.Student.size

    self.2017.earnings.3_yrs_after_completion = 2017.earnings.3_yrs_after_completion

    self.2016.repayment.3_yr_repayment= 2016.repayment.3_yr_repayment



    def setSchool_Name(self,School.Name):
        self.School.Name = School.Name

    def set2017_Student_size(self, 2017.Student.size)
        self.2017.Student.size = 2017.Student.size

    def set2018_Student_size(self, 2018.Student.size)
        self.2018.Student.size = 2018.Student.size

    def setType(self,School.city):
        self.School.city = School.city

    def set2017_earnings_3_yrs(self, 2017.earnings.3_yrs_after_completion):
        self.2017.earnings.3_yrs_after_completion = 2017.earnings.3_yrs_after_completion

    def set2016_repayment_3_yr(self,2016.repayment.3_yr_repayment ):
        self.2016.repayment.3_yr_repayment = 2016.repayment.3_yr_repayment

    def getSchool_Name(self):
        return self.School.Name

    def get2018_Student_size():
        return self.2018.Student.size

    def getType(self):
        return self.School.city


    def get2017_earnings_3_yrs(self,2017.earnings.3_yrs_after_completion):
        return self, 2017.earnings.3_yrs_after_completion


    def get2017_Student_size():
    return self, 2017.Student.size

    def getHrs(self):
        return self.earnings.3_yrs_after_completion

    def calculatePay(self, repayment.3_yr_repayment):
        regularpay = (repayment.3_yr_repayment* 36)

        Totalpay = regularpay

        return Totalpay



main()University2.py:
class University2:
    def __init__(self,School.Name, School.city, School.Name, 2017.Student.size,2017.earnings.3,2016.repayment.3_yr_repaym):
        self.School.Name = School.Name
        self.School.city = School.city
        self.2017.Student.size = 2017.Student.size
        self.2017.earnings.3_yrs = 2017.earnings.3_yrs
        self.2016.repayment.3_yr_repaym = 2016.repayment.3_yr_repaym

    def setSchool_Name(self, School.Name):
        self.Name = School.Name
    def setSchool_city(self,School.city ):
        self.School.city = School.city
    def setSa2016_repayment_3_yr_repaym(self, 2016.repayment.3_yr_repaym):
        self.2016.repayment.3_yr_repaym = 2016.repayment.3_yr_repaym
    def set2017_Student_size(2017.Student.size):
        self.2017.Student.size = 2017.Student.size
    def self2017_earnings_3_yrs(2017.earnings.3_yrs):
        self.2017.earnings.3_yrs = 2017.earnings.3_yrs

    def getSchool_Name(self):
        return self.School.Name

    def getSchool_city(self):
        return self.School.city

    def getSa2016_repayment_3_yr_repaym(self):
        return self.2016.repayment.3_yr_repaym

    def get2017_Student_size(self):
       return self.2017.Student.size

    def get2017_studet_earninig_3_Yrs(self)
        return self.2017.earning.3_Yrs

    def calculateYrly(self):
        self.earning
        return Yrlypay


Yarly.py:
from Universities1 import*
from University2 import*
def ReadName():
    while True:
        School.Name=input("Please enter the Universities name: ")
        if(School.Name.isalpha()==False):
            print("The name you have entered is invalid!!!")
            continue
        else:
            return School.Name
def UniversitiesType():
    while True:
        Emtype=input("Please enter the universities1 type (sup for university2 and emp for Universities1): ")
        if(Emtype.lower()!="sup" and Emtype.lower()!="emp"):
            print("The type of the employee is invalid!!!")
            continue
        else:
            return Emtype
def Printdetails(School.Name,School.city,x,pay):
    print ("Employee details")
    print("Name: ",Name)

    if(Emptype.lower()=="emp"):
        print("Type: Universities1")
        print("Yearly earning: ",x)
    else:
        print("Type: University2")
        print("Yearly earning: ",x)
    print("Yearly pay: ",pay)
def main():
    while True:
        Name=ReadName()
        Emptype=univerties1Type()
        if(Emptype.lower()=="emp"):
            obj1 = Universities1(self,School.Name, School.city, School.Name, 2017.Student.size,2017.earnings.3,2016.repayment.3_yr_repaym)
            Hrsworked=obj1.getHrs()
            pay=obj1.calculatePay(30)
            Printdetails(self,School.Name, School.city, School.Name, 2017.Student.size,2017.earnings.3,2016.repayment.3_yr_repaym )
        else:
            obj2 = Supervisor(Name,Emptype,500000)
            salary=obj2.getSalary()
            pay=obj2.calculatePay()
            Printdetails(self,School.Name, School.city, School.Name, 2017.Student.size,2017.earnings.3,2016.repayment.3_yr_repaym)
        choice=input("Do you want to add more Universities?(y or n)")
        if(choice=="n"):
            return
main()

