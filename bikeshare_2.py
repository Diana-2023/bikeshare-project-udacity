import time

import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city from the list (chicago, new york city, washington): ').lower()
    while city not in CITY_DATA:
        print("Entered city is invalid. Please, choose from 'chicago', 'new york city', or 'washington'.")
        city = input('Enter the city: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Enter the month from the list (all, january, february, ..., june): ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Entered month is invalid. Please enter a valid month ('january', 'february', 'march', 'april', 'may', 'june') or 'all'.")
        month = input('Enter the month: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week from the list (all, monday, tuesday, ..., sunday): ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("Entered day is invalid. Please enter a valid day of the week ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') or 'all'.")
        day = input('Enter the day of the week: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data from the relevant CSV file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert 'Start Time' and 'End Time' columns to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month from 'Start Time' into a new column named 'journey_month'
    df['journey_month'] = df['Start Time'].dt.month

    # filter by month if a specific month is selected
    if month != 'all':
        # identify the corresponding integer for the chosen month
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        chosen_month = months_list.index(month) + 1

        # filter the DataFrame to include only the chosen month
        df = df[df['journey_month'] == chosen_month]

    # extract day of the week from 'Start Time' into a new column named 'journey_day_of_week'
    df['journey_day_of_week'] = df['Start Time'].dt.day_name()

    # filter by day of the week if a specific day is chosen
    if day != 'all':
        # filter the DataFrame to include only the chosen day
        df = df[df['journey_day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['journey_month'].mode()[0]
    print("The most common month is: {}".format(common_month))

    # display the most common day of week
    common_day_of_week = df['journey_day_of_week'].mode()[0]
    print("The most common day of the week is: {}".format(common_day_of_week))

    # display the most common start hour
    df['journey_hour'] = df['Start Time'].dt.hour
    common_start_hour = df['journey_hour'].mode()[0]
    print("The most common start hour is: {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combination of start station and end station trip is:")
    print(most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration_hours = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours is: {:.2f}".format(total_duration_hours))

    # display mean travel time
    mean_duration_hours = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time in hours is: {:.2f}".format(mean_duration_hours))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types)

    # check if 'Gender' column exists before trying to compute statistics on it
    if 'Gender' in df.columns:
        # display counts of gender
        user_gender = df['Gender'].value_counts()
        print("Counts of user genders:")
        print(user_gender)
    else:
        print("Gender information is not available for this dataset.")

    # check if 'Birth Year' column exists before trying to compute statistics on it
    if 'Birth Year' in df.columns:
        # display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print("\nThe earliest year of birth is:", earliest_year_of_birth,
              ",the most recent year of birth is:", most_recent_year_of_birth,
              "the most common year of birth is: ", most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # add the option to display raw data
        raw_data_option = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()

        # validate user input for raw data display
        while raw_data_option not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            raw_data_option = input('Enter yes or no: ').lower()

        row_index = 0

        while raw_data_option == 'yes':
            print(df.iloc[row_index: row_index + 5])
            row_index += 5

            raw_data_option = input('\nWould you like to see the next 5 lines of raw data? Enter yes or no.\n').lower()

            if raw_data_option != 'yes':
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
