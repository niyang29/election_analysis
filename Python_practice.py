counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties:
    #print(county)
#for i in range(len(counties)):
    #print(counties[i])
#Results
#Arapahoe
#Denver
#Jefferson

# for voters in counties_dict.values():
    # print(voters)

# for county in counties_dict:
    # print(counties_dict[county])

#for county in counties_dict:
    #print(counties_dict.get(county))
#Results 
#422829
#463353
#432438

#for county, voters in counties_dict.items():
    #print(county, voters)
#Results
#Arapahoe 422829
#Denver 463353
#Jefferson 432438

#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voter ")

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")
 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)

#for i in range(len(voting_data)):
    #print(voting_data[i]['county'])

#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#How would you retrieve the number of registered voters from each dictionary?
#for county_dict in voting_data:
     #print(county_dict['registered_voters'])

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f"You received {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    #f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

#candidate_votes = 3345
#total_votes = 23123
#message_to_candidate = (
    #f"You received {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    #f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)
 
#candidate_votes = 3345
#total_votes = 23123
#message_to_candidate = (
    #f"You received {candidate_votes:,} number of votes. "
    #f"The total number of votes in the election was {total_votes:,}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

for county, voters in counties_dict.items():
    print(f"{county:,} county has {voters:,} registered voters.")
    

