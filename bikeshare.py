import time
import pandas as pd
import numpy as np

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
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    city = ''
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? \n')
        if city.lower() not in ('chicago','new york city','washington'):
            print('invalid city')
        else:
            break
            
    month = ''
    while True:
        month = input('Which month? (all, january, february, march, april, may, june) \n')
        if month.lower() not in ('all, january, february, march, april, may, june'):
            print('invalid month')
        else:
            break
                      
    day = ''
    while True:
        day = input('Which day? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) \n')
        if day.lower() not in ('all, monday, tuesday, wednesday, thursday, friday, saturday, sunday'):
            print('invalid day')
        else:
            break
        
    print('-'*40)
  
    return city,month,day

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
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    
    common_month = df['month'].mode()[0]
    print('Month: ',common_month)

    #display the most common day of week
    
    common_day = df['day'].mode()[0]
    print('Day of Week: ',common_day)

    #display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour: ',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ',start_station)    

    #display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ',end_station)

    #display most frequent combination of start station and end station trip
    df["Start & End"] = df['Start Station'].astype(str) + ' & ' + df['End Station']
    combined_stations = df['Start & End'].mode()[0]
    print('Most frequent combination of start station and end station:\n',combined_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ',total_travel_time)

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Counts of user types: ',count_user_type)

    #Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('Counts of gender: ',gender_count)

    #Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].sort_values().iloc[0]
    most_recent_birth = df['Birth Year'].sort_values(ascending=False).iloc[0]
    common_birth = df['Birth Year'].mode()[0]
    print('The earliest year of birth: ',earliest_birth)
    print('The most recent year of birth: ',most_recent_birth)
    print('The most common year of birth: ',common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
    main()

