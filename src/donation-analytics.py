# -*- coding: utf-8 -*-
"""
Haixu, 2/7/2018
Data engineer challenge, insight

Last edit: 2/10/2018 19:17 EST
"""
# =============================================================================
# Package numpy is used to calculate the percentile
# =============================================================================
import numpy as np

# =============================================================================
# Package sys is used to take the environment argument as input
# =============================================================================
import sys

# =============================================================================
# Package os is used to remove the dummy file generated in the process
# =============================================================================
import os

# =============================================================================
# The code takes two inputs file names and one output file name:
# 1. "itcont.txt", sys.argv[1]
# 2. "percentile.txt", sys.argv[2]
# 3. "repeat_donors.txt", sys.argv[3]
# =============================================================================

if len(sys.argv)<=1:
    print "error, no files indicated!"
    exit

# =============================================================================
# First step, clean up the data, discard the useless information. 
# Save the revised data into the file itcont_short.txt.
# The variables I keep include:
#   1. CMT_ID
#   2. Name
#   3. Zip_code
#   4. Transaction_DT
#   5. Transaction_AMT
# Only the data with an "Empty" Other_ID will be recorded.
# =============================================================================

f=open(sys.argv[1],'r')
f_cat=open("itcont_short.txt","a")
for line in f:
    if line !="\n":
        x = line.split("|")
        if x[15]=="" and x[0]!="" and x[7]!="" and len(x[10])>=5 and\
        len(x[13])==8 and x[14]!="":
            f_cat.write(x[0]+"|"+x[7]+"|"+x[10]+"|"+x[13]+"|"+x[14]+"\n")
f.close()
f_cat.close()
# =============================================================================


# =============================================================================
# Second step, read the input of the percentile
# =============================================================================

f=open(sys.argv[2],'r')
x=f.readline()
f.close()
perc=int(x.rstrip())
# =============================================================================

# =============================================================================
# 
# =============================================================================

f_cat=open("itcont_short.txt","r")
f_repeat=open(sys.argv[3],"a")
#f_repeat=open("repeat_donors.txt","a")

# =============================================================================
# d_rec is an effort to take care the issue of data listed out of order...
# if the later data happens to be a data from previous year, it will not be
# considered as a repeat donor.
# =============================================================================
d_rec={}  #all the records, streame through the name and zip code. 
#A dictionary with key: name+zip_code, value: year
data_point={""} #A set registers the combination of CMT-ID, zip code and year
d={} #a dictionary stores the data of the information to generate outputs
label=""
line=""
date=""
output=""
year=0
for line in f_cat: #stream through all the data in the short version file
    x = line.split("|")
    ID=x[1]+x[2][:5] # Name + first 5 digits of the zip code
    date=x[3]
    year=int(date)%10000 # four digits of year
    if ID in d_rec: #test whether the donor is a repeat donor
        if year >= min(d_rec[ID]):#make sure the data is in order
            label=x[0]+"|"+x[2][:5]+"|"+str(year) # label contains CMT_ID, zip_code and year
            if label in data_point: #test whether this receiver has been donated before
                d[label].append(int(x[4].rstrip()))#register the donate amount
                output=label+"|"+\
                str(np.percentile(d[label],perc,interpolation="nearest"))+\
                "|"+str(sum(d[label]))+"|"+str(len(d[label]))
                f_repeat.write(output+"\n")
            else:
                output=label+"|"+x[4].rstrip()+"|"+x[4].rstrip()+"|"+"1"
                d.update({label:[int(x[4].rstrip())]})
                f_repeat.write(output+"\n")
                data_point.update([label])
        else:
            d_rec[ID].append(year) # update the year of donation if this is out of order
    else:
        d_rec.update({ID: [year]}) # register this first time donor info

f_cat.close()
f_repeat.close()
del d,x, data_point,date, label, line, output, perc, year, d_rec #delete the variables in memory
os.remove("itcont_short.txt") # remove the short version data file

