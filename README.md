## Overview
This project analyzes bike share data for various cities. It allows users to explore patterns and statistics related to bike share usage. The primary focus is on three major cities in the United States: Chicago, New York City, and Washington.

### Bike Share Data
The data used for analysis is provided by Motivate, a bike share system provider for major U.S. cities. The datasets contain randomly selected data for the first six months of 2017 for all three cities. The core columns include:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City datasets also include additional columns:
- Gender
- Birth Year

### Statistics Computed
The analysis covers a range of descriptive statistics to uncover bike share usage patterns. The computed statistics include:
- Popular times of travel: most common month, most common day of the week, most common hour of the day.
- Popular stations and trips: most common start station, most common end station, most common trip from start to end.
- Trip duration: total travel time, average travel time.
- User information: counts of each user type, counts of each gender (available for NYC and Chicago), earliest, most recent, most common year of birth (available for NYC and Chicago).

### The Files
To perform this analysis, a Python script (bikeshare.py) is provided in this repository. Additionally, you will need the following dataset files:
- chicago.csv
- new_york_city.csv
- washington.csv

### Requirements
- Python 3.x
- Pandas library

### Installation
1. Clone the repository to your local machine.
    ```bash
    git clone git@github.com:Diana-2023/bikeshare-project-udacity.git
    ```
2. Move your bikeshare.py and data files into your local repository.
3. Run the script by entering the city, month, and day to analyze specific data.

### License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

### Acknowledgements
- Udacity Programming for Data Science Nanodegree program


