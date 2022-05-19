"""
The program is trying to take students grades from a text file called "Final.txt".
It will display the number of grades, the average grade, and the percentage of grades that are above the average grade
We will use three different functions to obtain the three different grades. 
"""

"""
main()
infile = open(file, 'r') = Open file to read data from the file
for line in infile = To access the lines of the file
[line.rstrip() for line in infile] = Creates a list of strings where each item of the list of the file minus its newline character
grades = [line.rstrip()]

grades[i] = int(grades[i]), to convert the list into integers
To get average grade = sum(grades) / len (grades)

To obtain grades that are above average, if the grade is above average grade then increment counter by 1

To get percentage of grades above average, number of grades that are above average divided by total of grades in the file
then *100 to get the percent of grades above average

Print and display the three values
Print total number of grades
Print average grade
Print percentage of grades that are above average
"""


infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades [i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0 
for grade in grades:
    if grade > average:
        num += 1

print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))
