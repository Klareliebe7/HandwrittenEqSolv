# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:36:31 2020

@author: zqd-d
"""

with open('C:\\Users\\zqd-d\\Desktop\\groundtruth_train\\all_groundtruth_train_no_root.tsv','r')as f:
           lines = f.readlines()
           lines_sorted= sorted(lines)
           lines_without_n = set(lines_sorted)
           #print(lines_without_n)
           for line in lines_without_n:
               if line.split():
                   with open("C:\\Users\\zqd-d\\Desktop\\groundtruth_train\\all_to_split.tsv","a") as fnew:
                       fnew.writelines(line)
                       
                       #10986 lines in fnew