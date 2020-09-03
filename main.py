# Author: ShangYuan Lim szl6038@psu.edu

a = 4
a_minus = 3.67
b_plus = 3.33
b = 3
b_minus = 2.67
c_plus = 2.33
c = 2.0
d = 1.0
f = 0

Course1grade = input("Enter your course 1 letter grade: ")

Course1credit = input("Enter your course 1 credit: ")

if Course1grade=="A":
  GP1 = float(a)
  GPC1 = (a*float(Course1credit))
elif Course1grade=="A-":
  GP1 = float(a_minus)
  GPC1 = (a_minus*float(Course1credit))
elif Course1grade=="B+":
  GP1 = float(b_plus)
  GPC1 = (b_plus*float(Course1credit))
elif Course1grade=="B":
  GP1 = float(b)
  GPC1 = (b*float(Course1credit))
elif Course1grade=="B-":
  GP1 = float(b_minus)
  GPC1 = (b_minus*float(Course1credit))
elif Course1grade=="C+":
  GP1 = float(c_plus)
  GPC1 = (c_plus*float(Course1credit))
elif Course1grade=="C":
  GP1 = float(c)
  GPC1 = (c*float(Course1credit))
elif Course1grade=="D":
  GP1 = float(d)
  GPC1 = (d*float(Course1credit))
else:
  GP1 = float(f)
  GPC1 = float(f)

print("Grade point for course 1 is: " + str(GP1))

Course2grade = input("Enter your course 2 letter grade: ")

Course2credit = input("Enter your course 2 credit: ")

if Course2grade=="A":
  GP2 = float(a)
  GPC2 = (a*float(Course2credit))
elif Course2grade=="A-":
  GP2 = float(a_minus)
  GPC2 = (a_minus*float(Course2credit))
elif Course2grade=="B+":
  GP2 = float(b_plus)
  GPC2 = (b_plus*float(Course2credit))
elif Course2grade=="B":
  GP2 = float(b)
  GPC2 = (b*float(Course2credit))
elif Course2grade=="B-":
  GP2 = float(b_minus)
  GPC2 = (b_minus*float(Course2credit))
elif Course2grade=="C+":
  GP2 = float(c_plus)
  GPC2 = (c_plus*float(Course2credit))
elif Course2grade=="C":
  GP2 = float(c)
  GPC2 = (c*float(Course2credit))
elif Course2grade=="D":
  GP2 = float(d)
  GPC2 = (d*float(Course2credit))
else:
  GP2 = float(f)
  GPC2 = float(f)

print("Grade point for course 2 is: " + str(GP2))

Course3grade = input("Enter your course 3 letter grade: ")

Course3credit = input("Enter your course 3 credit: ")

if Course3grade=="A":
  GP3 = float(a)
  GPC3 = (a*float(Course3credit))
elif Course3grade=="A-":
  GP3 = float(a_minus)
  GPC3 = (a_minus*float(Course3credit))
elif Course3grade=="B+":
  GP3 = float(b_plus)
  GPC3 = (b_plus*float(Course3credit))
elif Course3grade=="B":
  GP3 = float(b)
  GPC3 = (b*float(Course3credit))
elif Course3grade=="B-":
  GP3 = float(b_minus)
  GPC3 = (b_minus*float(Course3credit))
elif Course3grade=="C+":
  GP3 = float(c_plus)
  GPC3 = (c_plus*float(Course3credit))
elif Course3grade=="C":
  GP3 = float(c)
  GPC3 = (c*float(Course3credit))
elif Course3grade=="D":
  GP3 = float(d)
  GPC3 = (d*float(Course3credit))
else:
  GP3 = float(f)
  GPC3 = float(f)

print("Grade point for course 3 is: " + str(GP3))

TGPC = (GPC1+GPC2+GPC3)

TC = (float(Course1credit)+float(Course2credit)+float(Course3credit))

GPA = (TGPC/TC)

print("Your GPA is: " + str(GPA))


