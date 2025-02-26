# -*- coding: utf-8 -*-
"""
Team header:

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Neela Rajesh
#               Emily Haddad
#               Gabi Eguizabal
#               Jojo Owens
# Section:      213
# Assignment:   Lab 11-1: passport_checker
# Date:         11/3/23

"""
#Comment 

fileName = input("Enter the name of the file: ")
passportFile = open(fileName)
lines = passportFile.read()

lines_list = lines.split("\n\n")
validFile = open("valid_passports.txt", "w")

count = 0


for i in range(len(lines_list)):
    if 'byr' in lines_list[i]:
        if 'iyr' in lines_list[i]:
            if 'eyr' in lines_list[i]:
                if 'hgt' in lines_list[i]:
                    if 'hcl' in lines_list[i]:
                        if 'pid' in lines_list[i]:
                            if 'cid' in lines_list[i]:
                                count += 1
                                newline_list = lines_list[i].split("\n")
                                for j in range(len(newline_list)):
                                    validFile.write(newline_list[j])
                                    validFile.write("\n")
                                validFile.write("\n")
    
                    

validFile.close()
print("There are", count, "valid passports")