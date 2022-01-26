Election Analysis

## Project Overview
Colorado Board of Elections employees, Seth and Tom, have made the following requests to conduct a final election audit of a congressional election. 
1. Calculate the total number of votes casted. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidates received. 
4. Calculate the percentage of votes each candidate received. 
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest turnout of voters. 

### Resources
* Data Source: election_results.csv
* Software: Python 3.9.7, Visual Studio Code 1.63.2 (Universal)

## Election-Audit Results
The analysis results of the election consists of the follow:
* There were a total of 369,711 votes casted in the congressional election.
* There were three (3) counties that were part of the congressional election. The county names, percentage of votes, and total vote counts per county are as follow:
  1. Jefferson County had 10.5% of the votes with 38,855 votes casted.
  2. Denver County had 82.8% of the votes with 306,055 votes casted. 
  3. Arapahoe County had only 6.7% of the votes with 24,801 votes casted. 
* The county with the largest county vote turnout is Denver with 82.8% of the total votes with 306,055 votes.
* There were three (3) candidates. The candidates were: 
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
* The candidate results were: 
  1. Charles Casper Stockham received 23.0% of the votes which totaled up to be 85,213 votes.
  2. Diana DeGette received 73.8% of the votes which totaled up to be 272,892 votes.
  3. Raymon Anthony Doane received 3.1% of the votes which totaled up to be 11,606 votes. 
* The winner is Diana DeGette who received 73.8% of the votes which totaled up to be 272,892 out of 369,711. 

![Election Results](https://user-images.githubusercontent.com/96089187/151122704-3d59f062-65f0-4da8-81da-f054f9e5c8c0.png)

## Election-Audit Summary
Prepared for Election Commission
Prepared by Data Analyst Yang
The purpose of this proposal is for the Election Commission to adopt this script as the sample script to analyze future election results. This script will need little modifications. Please see the following steps on what the script will do -
1. Importing the CSV file with election results into Python or a Python interpreter like VS Code and use python code to build a path. What you would have to do differently is ensure the proper CSV file is uploaded. 

![Import file](https://user-images.githubusercontent.com/96089187/151111832-6aa7c037-da52-4f8e-ab11-da202982ae52.png)

2. Read the "header row" to know what position (or column) you will be analyzing. In this case, if we are looking at county data, the position in the row is 1 and the position for the candidates is 2.  

![Header row](https://user-images.githubusercontent.com/96089187/151124714-d6f0c4f5-774a-44d2-b974-e8d690a9f9a9.png)

3. Used repetition statements and conditional statements with logical operators, and print statements to print out the data we're looking for. In our exercise together, we worked on creating the candidates election results. We used very similar codes to obtain the names of the county by conducting a for loop. What you can do differently is modify variable names to not get confused by them.

![County names](https://user-images.githubusercontent.com/96089187/151124821-7e07a383-addf-4354-a0f7-253c4621e5d9.png)

![County info](https://user-images.githubusercontent.com/96089187/151125499-60d61b32-c816-4bfb-b2ae-ffe0156b6854.png)

4. Sample for loops and if statements scripts we previously did together to Obtain the candidates election results. 

![Candidate names](https://user-images.githubusercontent.com/96089187/151112092-f2c4eef2-7786-48df-9ff4-f3e2ab2ec250.png)

![Candidate vote count](https://user-images.githubusercontent.com/96089187/151112183-16e3ffda-90c1-414f-9602-f9deeae1de4c.png)

5. Get the percentage of the votes for each candidates and counties. 

![Vote Percentages](https://user-images.githubusercontent.com/96089187/151112274-a177fa9f-5553-4a2b-b43f-9cde2a7267c6.png)

![County Percentages](https://user-images.githubusercontent.com/96089187/151125817-742a7403-c066-4e77-8547-4632a516de75.png)

6. Lastly, write the Election Results into a text file. 
![Write to txt file1](https://user-images.githubusercontent.com/96089187/151112413-237767fb-75af-4de3-84fb-61007911a1fa.png)
![Write to txt file2](https://user-images.githubusercontent.com/96089187/151112423-c03db7a8-32fb-464b-bb26-983103089c2a.png)
![County results in txt file](https://user-images.githubusercontent.com/96089187/151125946-36ee8c2d-2582-44fe-8bbc-8de0082331b0.png)

If you go with this script, your election commission will save time from having to build a new code to get the same results. You just need to modify it depending on the election results you're looking for. 
