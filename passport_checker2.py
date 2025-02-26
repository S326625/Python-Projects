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
# Assignment:   Lab 11-2: passport_checker2
# Date:         11/3/23

"""
#Comment 

fileName = input("Enter the name of the file: ")
passportFile = open(fileName)
lines = passportFile.read()

lines_list = lines.split("\n\n")
validFile = open("valid_passports2.txt", "w")
count = 0


for i in range(len(lines_list)):
    line_str = lines_list[i]
    if 'byr' in lines_list[i]:
        if (int(line_str[(line_str.index('byr') + 4):(line_str.index('byr') + 8)]) >= 1920) and (int(line_str[(line_str.index('byr') + 4):(line_str.index('byr') + 8)]) <= 2007):
            if 'iyr' in lines_list[i]:
                if (int(line_str[(line_str.index('iyr') + 4):(line_str.index('iyr') + 8)]) >= 2013) and (int(line_str[(line_str.index('iyr') + 4):(line_str.index('iyr') + 8)]) <= 2023):
                    if 'eyr' in lines_list[i]:
                        if (int(line_str[(line_str.index('eyr') + 4):(line_str.index('eyr') + 8)]) >= 2023) and (int(line_str[(line_str.index('eyr') + 4):(line_str.index('eyr') + 8)]) <= 2033):
                            if 'hgt' in lines_list[i]:
                                line_str_list = line_str.split("\n")
                                str_new = " ".join(line_str_list)
                                new_line_list = str_new.split(" ")
                                hgt = ""
                                hgt_num = ""
                                hgt_unit = ""
                                valid = False

                                for k in range(len(new_line_list)):
                                    if 'hgt' in new_line_list[k]:
                                        hgt += new_line_list[k]
                                        hgt_unit += hgt[len(hgt) - 2 : len(hgt)]
                                        break
                                    
                                for l in range(len(hgt)):
                                    if hgt[l].isdigit():
                                        hgt_num += hgt[l]

                                if hgt_unit == "cm":
                                    if (int(hgt_num) >= 150) and (int(hgt_num) <= 193):
                                        valid = True

                                elif hgt_unit == "in":
                                    if (int(hgt_num) >= 59) and (int(hgt_num) <= 76):
                                        valid = True

                                if valid:
                                    if 'hcl' in lines_list[i]:                                  
                                        line_str_list2 = line_str.split("\n")
                                        str_new2 = " ".join(line_str_list2)
                                        new_line_list2 = str_new2.split(" ")
                                        hcl = ""
                                        hcl_code = ""
                                        valid2 = False

                                        for m in range(len(new_line_list2)):
                                            if 'hcl' in new_line_list2[m]:
                                                hcl += new_line_list2[m]
                                                hcl_code += hcl[hcl.index(':') + 1 : len(hcl)]
                                                break

                                        if len(hcl_code) == 7:
                                            if hcl_code[0] == '#':
                                                for n in range(1, len(hcl_code)):
                                                    if hcl_code[n].isdigit():
                                                        if (int(hcl_code[n]) >= 0) and (int(hcl_code[n]) <= 9):
                                                            valid2 = True
                                                            continue
                                                        else:
                                                            valid2 = False
                                                            break
                                                        
                                                    elif hcl_code[n] in ['a', 'b', 'c', 'd', 'e', 'f']:
                                                        valid2 = True
                                                        continue
              
                                                    else:
                                                        valid2 = False
                                                        break
                                        if valid2:
                                            if 'pid' in lines_list[i]:
                                                line_str_list3 = line_str.split("\n")
                                                str_new3 = " ".join(line_str_list3)
                                                new_line_list3 = str_new3.split(" ")
                                                pid = ""
                                                pid_num = ""
                                                pid_list = []
                                                valid3 = False
                                                isDigit = False
                                                
                                                for o in range(len(new_line_list3)):
                                                    if 'pid' in new_line_list3[o]:
                                                        pid += new_line_list3[o]
                                                        pid_list = pid.split(":")
                                                        break
                                                
                                                pid_num += pid_list[1]
                                                
                                                for p in range(len(pid_num)):
                                                    if pid_num[p].isdigit():
                                                        isDigit = True
                                                    else:
                                                        isDigit = False
                                                
                                                if len(pid_num) == 9:
                                                    if isDigit:
                                                        if 'cid' in lines_list[i]:
                                                            line_str_list4 = line_str.split("\n")
                                                            str_new4 = " ".join(line_str_list4)
                                                            new_line_list4 = str_new4.split(" ")
                                                            cid = ""
                                                            cid_num = ""                              
                                                            cid_list = []
                                                            valid4 = False
                                                            isDigit2 = False
                                                            hasLeading = False
                                                            lengthCount = 0
                                                            
                                                            for q in range(len(new_line_list4)):
                                                                if 'cid' in new_line_list4[q]:
                                                                    cid += new_line_list4[q]
                                                                    cid_list = cid.split(":")
                                                                    break
                                                            
                                                            cid_num += cid_list[1]
                                                            
                                                            for r in range(len(cid_num)):
                                                                if cid_num[r].isdigit():
                                                                    isDigit2 = True
                                                                else:
                                                                    isDigit2 = False 
                                                            
                                                            if cid_num.startswith('0'):
                                                                for s in range(1, len(cid_num)):
                                                                    if cid_num[s] == '0':
                                                                        hasLeading = True
                                                                        continue
                                                                    else:
                                                                        lengthCount += 1
                                                            
                                                            else:
                                                                lengthCount = len(cid_num)
                                                            
                                                            if lengthCount == 3:
                                                                if isDigit2:
                                                                    count += 1
                                                                    newline_list = lines_list[i].split("\n")
                                                                    for j in range(len(newline_list)):
                                                                        validFile.write(newline_list[j])
                                                                        validFile.write("\n")
                                                                    validFile.write("\n")
                                                        
                                                    

validFile.close()
print("There are", count, "valid passports")