# BikeShare-Data-Analysis
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

To complete this project, the following software was required :
- Python 3, NumPy, and pandas
- A text editor, like Atom.
- A terminal application

The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

Statistics Computed:

#1 Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of the day

#2 Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end

#3 Trip duration
- total travel time
- average travel time

#4 User info
- counts of each user type
- counts of each gender
- earliest, most recent, most common year of birth
