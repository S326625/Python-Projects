# -*- coding: utf-8 -*-
"""
 By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Neela Rajesh
# Section:      213
# Assignment:   Lab 11-1: barcode_checker
# Date:         11/5/23

"""

fileName = input("Enter the name of the file: ")
barcodesFile = open(fileName)
lines = barcodesFile.read()

lines_list = lines.split("\n")
validFile = open("valid_barcodes.txt", "w")
count = 0


for i in range(len(lines_list)):
    current_line = lines_list[i]
    sum_first = 0
    sum_second = 0
    if len(current_line) == 13:
        for j in range(0, 11, 2):
            sum_first += int(current_line[j])
    
        for k in range(1, 12, 2):
            sum_second += int(current_line[k])
        
        sec_group_change = sum_second * 3
        first_group_added = sec_group_change + sum_first
        first_group_added_str = str(first_group_added)
        last_dig = 10 - int(first_group_added_str[len(first_group_added_str) - 1])
        
        if last_dig == int(current_line[len(current_line) - 1]):
            count += 1
            validFile.write(current_line)
            validFile.write("\n")


validFile.close()
print("There are", count, "valid barcodes")

#Comment
