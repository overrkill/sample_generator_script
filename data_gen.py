#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : data_gen.py
# Author            : Abhishek Kale  <https://github.com/overrkill>
# Date              : 25.04.2021
# Last Modified Date: 25.04.2021
# Last Modified By  : Abhishek Kale  <https://github.com/overrkill>

import csv
import sys 
import random as r

#issues and their priotrity by public 
issue_priority = {"road":8,"education":8 ,"electricity": 4 ,"internet": 6 ,"employment":9,"poverty":8} 

#generate a sample 
def generate_sample():
    return [ r.randint(0,10) for x in range(len(issue_priority.keys())) ]
    # return [r.randint(0,10),r.randint(0,10),r.randint(0,10),r.randint(0,10),r.randint(0,10),r.randint(0,10),]
    # return {"road":r.randint(1,10),"education":r.randint(1,10) ,"electricity":r.randint(1,10),"internet":r.randint(1,10),"employment":r.randint(1,10),"poverty":r.randint(1,10) }


#calculate a candidates with certain agenda to get votes 
#from a voter with given expectations
def calc_win_per(sample):
   expectations = issue_priority.values()
   how_much_expectaions = len(expectations)
   expected_sum = sum(expectations)
   sample_sum = sum(sample)
   score = round((sample_sum/expected_sum)*1000) + r.randint(-50,50)
   score = score - (score - 950) + r.randint(-50,50) if score > 950  else score + r.randint(-50,50)
   # print("{} {} {}".format(sample_sum,expected_sum,score))
   return score
   # for i in range(how_much_expectaions):
       # if sample[i]-expectations[i] == 0 :
        # elif sample[i]-expectations[i] > 0 :
        # else:

if __name__ == "__main__":
    ip_size = 1000
    file_name = "samples.csv"
    if(len(sys.argv)>2):
        ip_size = int(sys.argv[1])
        file_name = sys.argv[2] 
    # print(generate_sample())
    with open( file_name  , "w") as csv_file : 
        csv_writer = csv.writer(csv_file ,delimiter=",",quoting=csv.QUOTE_MINIMAL ,)
        head =[]
        for i in issue_priority.keys():
            head.append(i)
        head.append("votes")
        csv_writer.writerow(head)
        for i in range(ip_size ):
            entry = generate_sample();
            entry.append( calc_win_per(entry) )
            csv_writer.writerow(entry)

