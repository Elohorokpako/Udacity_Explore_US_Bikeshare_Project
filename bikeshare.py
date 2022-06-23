import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
accepted_months=('all', 'jan', 'feb', 'march', 'april', 'may', 'june')
accepted_days=('all', 'monday', 'tuesday', 'wednesday', 'thurdsay', 'friday', 'saturday', 'sunday')
try:
    def get_filters():
        print('Hello! Let\'s explore some US bikeshare data!')
        while True:
            city=input('Which city would you like to see? \nChicago, New York City or Washington: ').lower()
            if city in CITY_DATA:
                break
            else:
                print('Please select the right city: Chicago, New York City or Washington')
        while True:
            month=input('''Would you like to filter the data by month? \n {}\n 
                        Enter your preferred months or type 'all' if you do 
                        not want to filter the data '''.format(accepted_months)).lower()
            if month in accepted_months:
                break
            else:
                print('Please enter the right month from {}'.format(accepted_months))

        while True:
            day=input('''Would you like to filter the data by a day of the week?\n{}\n 
            Type all if you do not want to filter the data: '''.format(accepted_days)).lower()
            if day in accepted_days:
                break
            else:
                print('Please enter the right day in the format {}'.format(accepted_days))

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
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday
    # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['jan', 'feb', 'march', 'april', 'may', 'june']
            month = months.index(month)+1

        # filter by month to create the new dataframe
            df = df[df['month']==month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            day=days.index(day)+1
            df = df[df['day_of_week']==day]

        return df

    def time_stats(df):
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        answers=('January','February','March','April','May','June')
        number=df['month'].mode()[0]
        print('The most common month is {}'.format(answers[number-1]))

        # TO DO: display the most common day of week
        days_of_the_week=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        answer=df['day_of_week'].mode()[0]
        print('The most common day of the week is {}'.format(days_of_the_week[answer-1]))

        # TO DO: display the most common start hour
        df['Hour']=df['Start Time'].dt.hour
        hour=df['Hour'].mode()[0]
        if int(hour)<12:
            print('The most common start hour is {}{}'.format(hour,'.00 AM'))
        elif int(hour)==12:
            print('The most common start hour is {}{}'.format(hour,'.00 NOON'))
        elif int(hour)>12:
            print('The most common start hour is {}{}'.format(hour-12,'.00 PM'))
        else:
            print('The most common start hour is {}{}'.format(hour,'.00'))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        print('The most commonly used start station is {}'.format(df['Start Station'].mode()[0]))

        # TO DO: display most commonly used end station
        print('The most commonly used end station is {}'.format(df['End Station'].mode()[0]))

        # TO DO: display most frequent combination of start station and end station trip
        print('The most frequent combination of start and end station trip is {}'.format(df[['Start Station','End Station']].mode()))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        print('The total travel time is {}'.format(df['Trip Duration'].sum()))

        # TO DO: display mean travel time
        print('The mean travel time is {}'.format(df['Trip Duration'].mean()))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    def user_stats(df):
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types

        print('The count of the user types is {}'.format(df['User Type'].value_counts()))
        # TO DO: Display counts of gender
        if 'Gender' in df.columns:
            print('The count by gender is {}'.format(df['Gender'].value_counts()))
        # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            print('''The earliest year of birth is {} \nThe most Recent Year of birth is {} \nThe most common year of birth is {}
            '''.format(df['Birth Year'].min(),df['Birth Year'].max(), df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

        while True:
            prompt=input('Would you like to see five rows of the raw data? ').lower()
            if prompt=='yes':
                print(df.loc[0:4,:])
                break
            elif prompt=='no':
                loop='break'
                break
            else:
                print('Please Enter yes or no')
        if prompt=='yes':
            m=5
            n=10
            while True:
                prompt=input('Would you like to see another five rows of the raw data? ').lower()
                if prompt=='yes':
                    print(df.iloc[m:n,:])
                    m+=5
                    n+=5
                elif prompt=='no':
                    break
                else:
                    print('Please select yes or no')

    def main():
        while True:
            city, month, day = get_filters()
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
except:
    print('Error occured, Rerun the program if you wish to continue!!')

