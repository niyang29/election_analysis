# election_analysis

## Project Overview
A Colorado Board of Elections employee has made the following requests to conduct a final election audit of a congressional election. 
1. Calculate the total number of votes casted. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidates received. 
4. Calculate the percentage of votes each candidate received. 
5. Determine the winner of the election based on popular vote. 

### Resources
* Data Source: election_results.csv
* Software: Python 3.9.7, Visual Studio Code 1.63.2 (Universal)

## Summary
The analysis results of the election consists of the follow:
* There were a total of 369,711 votes casted in the election.
* There were three (3) candidates. The candidates were: 
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
* The candidate results were: 
  1. Charles Casper Stockham received 23.0% of the votes which totaled up to be 85,213 votes.
  2. Diana DeGette received 73.8% of the votes which totaled up to be 272,892 votes.
  3. Raymon Anthony Doane received 3.1% of the votes which totaled up to be 11,606 votes. 
* The winner is Diana DeGette who received 73.8% of the votes which totaled up to be 272,892 out of 369,711. 
![Election Analysis](https://user-images.githubusercontent.com/96089187/151111680-c98a9f7f-5c6f-4653-8ef7-8bd27601aab4.png)

## Challenge Overview
The challenge consisted of the following steps -
1. Importing the election_results.csv into PyPoll.py. 
![Import file](https://user-images.githubusercontent.com/96089187/151111832-6aa7c037-da52-4f8e-ab11-da202982ae52.png)
2. Read the "header row" to know what data we're working with. 
![Header row](https://user-images.githubusercontent.com/96089187/151111999-9859cdb5-c28c-456e-94ca-2041b2f79ba9.png)
3. Obtain the names of all candidates by conducting a for loop.
![Candidate names](https://user-images.githubusercontent.com/96089187/151112092-f2c4eef2-7786-48df-9ff4-f3e2ab2ec250.png)
4. Conduct a for loop to attain the total vote count for the eleciton and for each candidate.
![Candidate vote count](https://user-images.githubusercontent.com/96089187/151112183-16e3ffda-90c1-414f-9602-f9deeae1de4c.png)
5. Get the percentage of the votes for each candidates. 
![Vote Percentages](https://user-images.githubusercontent.com/96089187/151112274-a177fa9f-5553-4a2b-b43f-9cde2a7267c6.png)
6. Lastly, write the Election Results, Winner, Vote Count and percentage into a text file. 
![Write to txt file1](https://user-images.githubusercontent.com/96089187/151112413-237767fb-75af-4de3-84fb-61007911a1fa.png)
![Write to txt file2](https://user-images.githubusercontent.com/96089187/151112423-c03db7a8-32fb-464b-bb26-983103089c2a.png)

## Challenge Summary
The challenge was to conduct a final election audit of a Colorado congressional election. 
