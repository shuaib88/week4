#gpa.py
#   Program to find student with highest GPA


#define class Student
#Get the file from the user
#Open the file for reading
#Set best to be the first student
#For each student s in the file
#    if s.gpa() > best.gpa()
#        set best to s
#print out information about best


class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours


def makeStudent(infoStr):
    #infoStr is a semicolon -seperated line: name hourse qpoints
    #returns a corresponding string object
    name, hours, qpoints = infoStr.split(";")


def main():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    #set best to the record for the first student in the file
    best = makeStudent(infile.readline())
##
##    #process subsequent lines of the file
##    for line in infile:
##        #turn the line into a student record
##        s = makeStudent(line)
##        # if this student is best so far, remember it
##        if s.gpa() > best.gpa():
##            best = s
##
##    infile.close()
##
##
##    # print information about the best student
##    print("The best student is:", best.getName())
##    print("hours:", best.getHours())
##    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
