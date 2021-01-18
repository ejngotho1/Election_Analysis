# data we need to retrieve
# 1. total number of votes cast
# 2. list of candidates
# 3. % of votes each candidate got
# 4. total number of votes eaach candidate got
# 5. winner of election

#%%
# determine the time right now
# import datetime model
import datetime
# use "now()" attribute to get present time
now = datetime.datetime.now()
# print time now
print("The time is ", now)
# %%
# same code written as

import datetime as dt
now = dt.datetime.now()
print("The time now is ", now)
# %%
# we want to read data from a file
# assign a variable for the file to load
file_to_load = "Resources/election_results.csv"
# lets open and read the file to read
with open(file_to_load) as election_data:
    print(election_data)
# %%
import csv
import os
# assign a variable for file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# open and read election file
with open(file_to_load) as election_data:
    print(election_data)
# %%
# we now want to open file and write to dir

# create a variable to direct/indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")
# lets use "with" to open as a txt file
outfile = open(file_to_save, "w")
# write data to this file
outfile.write("Hello World")
# close file
outfile.close()


# %%

# create a variable to direct/indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")
# lets use "with" to open as a txt file
with open(file_to_save, "w") as txt_file:
# write data to file
    txt_file.write("Hello Colorado! It is and amazing day!\n")
    txt_file.write("--------------------------------------\n")
# write more data into the file   
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")
# %%
# NOW WE WANT TO READ THE ELECTION FILE

# add dependencies
import csv
import os
# assign a variable to load file from path (this time an Unknown path)
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open election results and read file
with open(file_to_load) as election_data:
# read file object with reader function
    file_to_read = csv.reader(election_data)
# lets skip headers
    headers = next(file_to_read)        
# lets print each row in the csv file
    for row in file_to_read:
        print(row)    
# %%
# DETERMINING TOTAL NUMBER OF VOTES

# add dependencies
import csv
import os
# assign a variable to load file from path (this time an Unknown path)
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Lets initialize total vote COUNTER
total_votes = 0
# lets declare a new list
candidate_options = []
# open election results and read file
with open(file_to_load) as election_data:
# read file object with reader function
    file_to_read = csv.reader(election_data)
# lets read headers
    headers = next(file_to_read)        
# lets print each row in the csv file
    for row in file_to_read:
        # Adding to vote counter
        total_votes += 1
# lets print  candidate name from each row
        candidate_name = row[2]    
# lets check if candidate name has been added - unique candidate name 
        if candidate_name not in candidate_options:        
#  add candidate name to the candidate_options list if not in list
            candidate_options.append(candidate_name)           
# print total votes
print(candidate_options)  
# %%
