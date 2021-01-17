#%%
print("Hello World")

# %%
counties = ["Arapahoe", "Denver", "Jefferson"]

# %%
print(counties)
# %%
type(counties)
# %%
my_turple = ()

# %%
my_turple = ("Arapahoe","Denver","Jefferson")
# %%
type(my_turple)
# %%
len(my_turple)
# %%
my_turple[2]
# %%
my_turple[1:1]
# %%
my_turple[:2]
# %%
my_turple[1:2]
# %%
my_turple[:-1]
# %%
my_dictionary = {}
# %%
my_counties = {}
# %%
my_counties["Arapahoe"] = 422829
# %%
my_counties["Denver"] = 463353
# %%
my_counties['Jefferson'] = 432438
# %%
type(my_counties)
# %%
print(my_counties)
# %%
my_counties.items()
# %%
my_counties.keys()
# %%
my_counties.values
# %%
my_counties.__dict.values
# %%
my_counties_dict.values()
# %%
my_counties.values()
# %%
my_counties.get("Denver")
# %%
my_counties.get('Denver')
# %%
my_counties.get["Denver"]
# %%
my_counties["Arapahoe"]

# %%
my_counties.get("Arapahoe")
# %%
my_counties.items

# %%
voting_data = {}
# %%
voting_data.append({"county":"Arapaho","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
# %%
for county in voting_data:
    print(county)

# %%
counties = ["Arapahoe","Denver","Jefferson"]
# %%
print(counties)
# %%
if counties[1] == 'Denver':
    print(counties[1])
# %%
print(counties[0])
# %%
if counties[3] != 'Jefferson':
    print(counties[2])

#%%
temperature = int(input("What is the outside temperature? "))    
# %%
temperature = int(input("What is the outside temperature? ")) 

if temperature > 80:
    print("Turn on AC.")
else:
    print("Open the windows. ")    
  
# %%
score = int(input("Wwhat is your score? "))
#determine grade
if score > 90:
    print('Your grade is A. ')
else:
    if score > 80:
        print("Your grade is B. ")
    else:
        if score > 70:
            print("Your grade is C. ")    
        else:
            if score > 60:
                print("Your grade is D? ")
            else:
                print("Your grade is F. ")            

# %%
# What is your score
 score = int(input("what is your test score? "))
#find the grade
if score > 90:
    print("your score is A")
elif score > 80:
    print("your score is B") 
elif score > 70:
    print("your score is C")
elif score > 60:
    print("your score is D")
else:
    print("your score is F")                

# %%
print("counties")
# %%
print(counties)
# %%
counties = ["Arapahoe","Denver","Jefferson"]
# %%
if "Arapahoe" not in counties:
    print("True")
else:
    print("False")    
 
# %%
print(counties)
# %%
if "El paso" in counties:
    print("El Paso is in list counties")
else:
    print("El paso is not in list of counties")  
# %%
x = 5
y = 5
if x == 3 or y == 5:
    print("True")
else:
    print("False")    
# %%
if x == 3 and y == 5:
    print("True")
else:
    print("False") 
# %%
x = 0
while x <= 5:
    print(x)
    x = x+1
# %%
for county in counties:
    print(county)
# %%
numbers = [0,1,2,3,4,5]
for num in numbers:
    print(num)
# %%
for nums in numbers:
    print(nums)
# %%
for num in range(6):
    print(num)
# %%
for num in range(5):
    print(num)
# %%
for i in range(len(counties)):
    print(counties[i])
# %%
county_turple = ["Arapahoe","Denver","Jefferson"]

for i in range(len(county_turple)):
    print(county_turple[i])
# %%
county_turple = ["Arapahoe","Denver","Jefferson"]

for i in len(county_turple):
    print(county_turple[i])
# %%
print(my_dictionary)
# %%
my_dictionary = {"Arapahoe": 422829,"Denver":463353,"Jefferson":432438}
# %%
print(my_dictionary)
# %%
for county in my_dictionary:
    print(county)
# %%
for j in my_dictionary.keys():
    print(j)
# %%
for j in my_dictionary.values():
    print(j)
# %%
for key, value in my_dictionary.items():
    print(key,value)
# %%
voting_data = [{"county":"Arapaho","registered_voters":422829},
               {"county":"Denver","registered_voters":463353},
               {"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)               
# %%
for i in range(len(voting_data)):
    print(voting_data[i])
# %%
for county_dict in voting_data:
    print(county_dict)
# %%
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# %%
for county_dict in voting_data:
    print(county_dict.values())
# %%
for value in county_dict:
    print(county_dict['registered_voters'])
# %%
for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)
# %%
for county_dict in voting_data:
    print(county_dict['registered_voters'])
# %%
for county_dict in voting_data:
    print(county_dict['county'])
# %%
total_votes = 422829 + 463353 + 432438
# %%
a = 422829
b = 463353
c = 432438
# %%
total_votes = a+b+c
#%%
Arapahoe_votes = 422829
#%%
print(Arapahoe_votes)

# %%
print(total_votes)
# %%
Arapahoe_votes = int(input("How many votes are in Arapahoe?"))
total_votes = int(input("What is total votes in three counties?"))
Arapahoe_percentage_votes = (Arapahoe_votes / total_votes)*100
print("Arapahoe has " + str(Arapahoe_percentage_votes) + "% of the total votes.")
# %%
print(Arapahoe_percentage_votes)
# %%
Arapahoe_votes = int(input("How many votes are in Arapahoe?"))
total_votes = int(input("What is total votes in three counties?"))

# %%
Arapahoe_percentage_votes = (Arapahoe_votes / total_votes)*100
# %%
print(Arapahoe_percentage_votes)
# %%
counties_dict = {"Arapahoe": 422829, "Denver":463353,"Jefferson":432438}

# %%
for county, registered_voters in counties_dict.items():
    print(county + " county has " + str(registered_voters) + " registered voters.")

# %%
counties_dict = {"Arapahoe": 422829, "Denver":463353,"Jefferson":432438}
for county, registered_voters in counties_dict.items():
    print(county + " county has " + str(registered_voters) + " registered voters.")

# %%
for county, registered_voters in counties_dict.items():
    print(f"{county} county has {registered_voters} registered voters.")
# %%
candidate_votes = int(input("How many votes did candidate get."))
total_vote = int(input("what was the total vote?."))
message_to_candidate = (
    f"You received {candidate_votes} votes."
    f"The total number of votes was {total_vote}."
    f"You received {candidate_votes / total_vote *100}% of total votes." )

print(message_to_candidate)    
# %%
counties_dict = {"Arapahoe": 422829, "Denver":463353,"Jefferson":432438}
for county, registered_voters in counties_dict.items():
    print(county + " county has " + str(registered_voters) + " registered voters.")

# %%
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, 
                 {"county":"Denver", "registered_voters": 463353}, 
                 {"county":"Jefferson", "registered_voters": 432438}]
# %%
print(registered_voters)
# %%
counties_dict = {"Arapahoe": 422829, "Denver":463353,"Jefferson":432438}
for county, registered_voters in counties_dict.items():
    print(county + " county has " + str(registered_voters) + " registered voters.")

# %%
