import time
import pandas as pd

CITY_DATA = { 'ch': 'Data//chicago.csv',
              'ne': 'Data//new_york_city.csv',
              'wa': 'Data//washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        i = str(input('Please choose the first two letters from the required city[Chicago, New York City, Washington]:\n')).lower()
        if i in ('ch', 'ne', 'wa'):
            city = i
            break
        print("invalid city, please try again")
     
    while True:     
            e = str(input('please choose month you want to filter by or "all" for all months (just first 6 months):\n')).lower()
            if e in ('all','january', 'february', 'march', 'april', 'may', 'june'):
                month = e
                break
            print("invalid month, please try again.")
            
    while True:     
            o = str(input('please choose day you want to filter by or "all" for all days:\n')).lower()
            if o in ('all','sunday', 'monday', 'tuesday', 'wednesday', 'thuresday', 'friday' , 'saturday'):
                day = o
                break
            print("invalid day, please try again")        

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
        
    return df

def showing_data(df):
    """asking user to showing first 5 rows of data"""
    q = 0 
    qeustion = str(input("would you want to view first 5 rows from data ? \"yes\" or \"no\"\n")).lower()
    
    while True :
                if qeustion == "yes" :
                    print("the first 5 rows :\n",df[q:q+5])
                    qeustion = str(input("would you want to view next 5 rows from data ? \"yes\" or \"no\"\n")).lower()
                    q += 5
                elif qeustion == "no" :
                    break
                print("invalid choice, please try again.")
    
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)


    popular_day= df['day_of_week'].mode()[0]
    print('Most Popular day:', popular_day)


    popular_hour = df['hour'].mode()[0]
    print('Most Popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start = df['Start Station'].mode()[0]
    print('Most common start station:', popular_start)
    
    popular_end = df['End Station'].mode()[0]
    print('Most common end station:', popular_end)
    
    popular_combination = (df['Start Station']  + "-" +  df['End Station']).mode()[0]
    print('Most common comnination of stations:', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    
    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['hour'].sum()
    print('Total time:', total_time )


    time_average = df['hour'].mean()
    print('Time average:', time_average)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("user types is\n" , user_types)

    if 'Gender' in df:
        Gender_types = df['Gender'].value_counts()
        print("user gender is\n" , Gender_types)

    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
        print("earliest" , earliest)
        print("recent" , recent)
        print("most_common" , most_common)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        showing_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter "yes" if you want.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    