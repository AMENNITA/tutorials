## Problem Statement
In an attendance monitoring system, the unique integer ID number of every employee is noted
whenever the employee swipes his card in the office. First time an employee enters into the office,
the attendance counter is set to 1. From then onwards, each time an employee leaves the office
premises for tea break or lunch break the counter is incremented, and incremented again when he
enters back. If the counter is odd on a day, it means the employee is in the office premises and if
the counter is even, it means he is out of the premises.
The organization uses this data to perform the following analytics:
1. How many employees came today?
2. Did a particular employee come today?
3. How often did an employee enter into the office?
4. Which employee moves out of office the greatest number of times?
5. Which employee ids within a range of IDs attended office, the attendance counter for them, and
whether they are inside or outside office?
Asks:
1. Implement the above problem statement in Python using BINARY TREE ADT.
2. Perform an analysis for the questions above and give the running time in terms of input
size: n.
The basic structure of the employee node will be:
