# Problem Statement
There are N different models of mobiles manufactured at a mobile manufacturing unit. Each
mobile must go through 2 major phases: ‘parts manufacturing’ and ‘assembling’. Obviously,
‘parts manufacturing’ must happen before “assembling’. The time for ‘parts manufacturing’
and ‘assembling’ (pmi and ai for ith mobile) for every mobile may be different. If we have only
1 unit for ‘parts manufacturing’ and 1 unit for ‘assembling’, how should we produce n mobiles
in a suitable order such that the total production time is minimized?

## Requirement
1. Write a Greedy Algorithm to select the mobile ‘parts manufacturing’ and ‘assembling’ in such a way that total production time is minimized.
2. Analyse the time complexity of your algorithm.
3. Implement the above problem statement using Python.

## Input
For example, now there are 6 different Mobiles in total. Time for each mobile ‘parts
manufacturing’ and ‘assembling’ are given as shown:
|Mobile i|pmi (Minutes)|ai(Minutes)|
|1|5|7|
|2|1|2|
|3|8|2|
|4|5|4|
|5|pm5|a5|
|6|pm6|a6|
