import time
import pandas as pd
import numpy as np
import calendar
from datetime import datetime

CITY_DATA = { 'chicago': '/Users/EdgardoDumas/Desktop/udacity/Bikeshare-Project/chicago.csv',
              'new york city': '/Users/EdgardoDumas/Desktop/udacity/Bikeshare-Project/new_york_city.csv',
              'washington': '/Users/EdgardoDumas/Desktop/udacity/Bikeshare-Project/washington.csv' }

cityChoice = ['chicago', 'new york city', 'washington']
monthChoice = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
dayChoice = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like data from Chicago, New York City or Washington? ").lower()
        if city not in cityChoice:
            print("Not an appropiate response")
        elif city in cityChoice:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("From which month would you like data from? ")
        if month not in monthChoice:
            print("Not an appropiate response")
        elif month in monthChoice:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("From which day would you like data from? ")
        if day not in dayChoice:
            print("Not an appropiate response")
        elif day in dayChoice:
            break

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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'All':
        month = monthChoice.index(month)
        df = df[df['Month'] == month]

    if day!= 'All':
        df =df[df['Day_of_Week'] == day]

    return(df)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].value_counts().idxmax()
    print("The most common month is: ", calendar.month_name[common_month])

    # TO DO: display the most common day of week
    common_day = df['Day_of_Week'].value_counts().idxmax()
    print("The most common day is: ", common_day)

    # TO DO: display the most common start hour
    common_hour = df['Hour'].value_counts().idxmax()
    common_hour = datetime.strptime(str(common_hour), "%H")
    print("The most common hour is: ", common_hour.strftime("%I:%M %p"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination is: {}, {}".format(most_frequent_combination[0], most_frequent_combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types are:\n", user_types)

    if 'Gender' in df.columns:
        user_stats_gender(df)
    else:
        print('\nNo gender statistics')
    if 'Birth Year' in df.columns:
        user_stats_birth(df)
    else:
        print('No birth year statis')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display counts of gender
def user_stats_gender(df):
    gender_stats = df['Gender'].value_counts()
    print("\nThe gender counts are:\n", gender_stats)

    # TO DO: Display earliest, most recent, and most common year of birth
def user_stats_birth(df):
    birth_year = df['Birth Year']
    earliest_birth = birth_year.min()
    print("\nThe earliest birth year is: ", earliest_birth)
    most_recent_birthyear = birth_year.max()
    print("The most recent birth year is: ", most_recent_birthyear)
    most_common_birthyear = birth_year.value_counts().idxmax()
    print("The most common birth year is: ", most_common_birthyear)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Yes or No?")
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[:5])
        start_loc += 5
        view_display = input("Do you wish to continue?").lower()
        if view_display == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
