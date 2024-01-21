import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan','feb','mar','apr','may','jun']
week_days = {"mon":'Monday', "tue":"Tuesday", "wed":"Wednesday", "thu":"Thursday", "fri":"Friday","sat":"Saturday", "sun":"Sunday"}

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
    while True:
        try:
            city = input("Please enter the city you want to analyze! (chicago - new york city - washington)\n").lower().strip()
            CITY_DATA[city]
            print("\n")
            break
        except KeyError:
            print("\nPlease enter a valid city name ...\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please enter name of month you want to analyze in short form \nex: jan, feb, mar, .. jun   *you can type all ...\n").lower().strip()
            if month != 'all':
                month = months.index(month) + 1
            print("\n")
            break
        except ValueError:
            print('\nPlease write the month name in apperviated letters ex: jan, feb .. jun \n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Please enter the week day you want to analyze in short form \nex: sat, sun    *you can type all ...\n").lower().strip()
            if day != 'all':
                day = week_days[day]
            print("\n")
            break
        except ValueError:
            print('\nPlease write the week day name in apperviated letters ex: sat, sun, mon, tue, wed, thu, fri\n')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    if month != 'all':
        df = df[df.month == month]

    if day != 'all':
        df = df[df.day == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is ',months[df['month'].mode()[0]-1].title())

    # display the most common day of week
    print('The most common day of week is',df['day'].mode()[0])

    # display the most common start hour
    print('The most common start hour is',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is from ",(df['Start Station']+" to "+df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is", round((df['End Time'] - df['Start Time']).dt.total_seconds().sum()/3600,2),'hours.' )

    # display mean travel time
    print("Mean travel time is", round((df['End Time'] - df['Start Time']).dt.total_seconds().mean()/3600,2),'hours.' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The count of user types is .. \n',df['User Type'].value_counts(),'\n')

    # Display counts of gender

    try:
        print('The count of users gender is ..\n',df['Gender'].value_counts(),'\n')
    except :
        print('This city has no data about gender \n')



    # Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth is ..\n',int(df['Birth Year'].min()),'\n')
        print('The most recent year of birth is ..\n',int(df['Birth Year'].max()),'\n')
        print('The most common year of birth is ..\n',int(df['Birth Year'].mode()[0]),'\n')

    except :
        print('This city has no data about birth year of users')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    indx = 0
    while True :
        print('\nPrinting 5 rows...\n')
        print(df[indx:indx+5])
        indx+=5

        display = input('\nDo you want to see 5 more rows of data? Enter yes or no.\n')
        if display.lower() != 'yes':
            break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        if input('\nDo you want to see the first 5 rows of data? Enter yes or no.\n').lower() == 'yes':
            display_data(df)

        if input('\nWould you like to restart? Enter yes or no.\n').lower() != 'yes':
            break


if __name__ == "__main__":
	main()
