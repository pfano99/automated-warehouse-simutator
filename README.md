# automated-warehouse-simutator
simple automated warehouse simulation using pygame

### Blob (Robot)
we have a robots that moves around the grid, this robots can be assigned a mission to do which is to deliver packages from the storage section to the delivery section.
if the robot does not have a mission it will go an pack at the packing session and a robot that is assigned a mission will go to pick up the package and delivers it. A robot is caying a package will be indicated by a green circle thing. 

### Missions
missions are randomly generated.

### Grid
we have multiple grid colors each color represent different section.
1. Red on the top row: This is a storage area where a robot(blob) gets packages.
2. Green on the bottom row: This is a delivery area, where a robot(blob) delivers a package to.
3. Dark blue column: This is just a barriers/walls that robot(blob) cannot walk through.
4. Dark purple on the first and last column: this is a packing area, a robot(blob) or blob parks here if don't have any missions/(packages to deliver)   

https://user-images.githubusercontent.com/53374350/227920780-792af129-d30f-415a-ab65-69b695752b90.mp4

