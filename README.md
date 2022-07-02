# Using Python To Count Votes in the 1st Congressional District of Colorado

## Introduction

Federal Elections in the United States of America generates a lot of data that needs to be tabulated. It is important that any person that votes, according to the State's laws, has their ballot tallied to provide legitimacy to the U.S. Government. The U.S. adheres to a Democratic Republic system of Government. It is where the populace votes for representatives, these representatives are then the ones who decide public policy. The rational behind a Democratic Republic is by giving citizens a choice when electing leaders, in turn, these leaders will prioritize the will of the people and make laws to better the live's of the citizens. Hence, it behooves vote counters to be accurate and count every vote as it decides how the nation is managed for the good of the people. 

The U.S. has a very large population, estimated at 330 million in 2020 according to the U.S. Census. Not everyone votes but the majority of people do. It would be very resource intensive to count individual votes by hand. To expedite the electoral process, having standardized voting forms called ballots, ballot counting machines and software that quickly sums up and compares the votes for each candidate is common. 

A U.S. congressional precinct in Colarado has inquired about using a computer script to count votes quickly and to print out the results coincedentally. The hope is, that not only will the computer script achieve these objectives but then the script can be used for other Federal elections in Colorado. The election race the script will be first tested on is Colorado's 1st Congressional District that includes the counties of Arapahoe, Jefferson and Denver. This is an urban congressional district and the data provided is from 2018.  


## Results

The computer script used to tabulate all 369,711 votes in the 1st Congressional Distric was written in Python 3.7.6 and compiled with Visual Studio Code. The attributes of focus were the votes per county and the voter per candidate.

- Denver County was decidedly larger than Jefferson and Araphoe. Denver County has 82.8% of the vote from 306,055 ballots counted
- Jefferson and Arapahoe are comparable with Jefferson representing 10.5 % of the vote with 38,855 ballots cast and Arapahoe containing 6.7% of the vote with 24,801 ballots cast.
-  Incumbent Democrate, Diana Degette, was number one in voting for the Congressional District obtaining 73.8% of the vote with a count of 272,892   
-  Republican Challenger Charles Casper Stockham was second in voting with 23.0% of the vount with a count of 85,213
-  Third place in vote count went to Libertarian Raymon Anthony Doane with 3.1% of the vote, a count of 11,606.   


## Summary

According to the ballots casted and recorded, Dianna Degette is the clear winner and should be Colorado's 1st District Representative. As the current script is written it achieves it's goal of being adaptable and able to use in other elections as long as a similarily formatted CSV is provided. The script does not contain any hardcoded numbers or names but instead uses python lists and dictionaries to obtain and record candidates as well as variables that increment to obtain counts and are used later for percentages. 

What the script is lacking is a breakdown of which county favored which candidate. The First Congressional District is urban but Denver County, in particular, is a heavily populated city. Whichever candidate this county favores is likely to win. A second addition to the code that would be helpful given extra data is the percentage of votes to registered voters. This statistic provides an indicator of enthusiams for the electoral race at hand and Governmental system. It can also be an indicator of where elected officials need to campaign and spark enthusiasm to dissillusioned voters. If a county has a poor turnout with regard to voting from registered voters, is a significant proportion of the districts population and it favored the non-winning candidate, this is seen as a swing area. Voting tends to follow a regional pattern with urban centers voting democrate and rural areas favoring Republicans. Usually counties are small enough in area that the region is predominantly rural or urban. Thus, the sample that voted likely represents the larger populace and having more of the, underrepresented, county vote could swing an election.        
