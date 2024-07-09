'''
    This is a simple program that uses Pandas to analyse demographic data
'''

import pandas as pd

df = pd.read_csv('adult_data.csv')

#   number of people of each race
race_count = df['race'].value_counts()

#   average age of men
avg_men_age = df[df['sex'] == 'Male']['age'].mean()

#   percentage of people with Bachelor's degree
BS_degree = round(((df['education'] == 'Bachelors').mean() * 100), 2)

#   percentage of people with advanced education making more than 50K
advanced_edu_gt_50k = round(((df[df['education'].isin(['Bachelor', 'Masters', 'Doctorate'])]['salary'] == '>50K').mean() * 100), 2)

#   percentage of people without advanced education making more than 50K
without_advanced_edu_gt_50k = 100 - advanced_edu_gt_50k

#   min hours a person works
min_work_hours = df['hours-per-week'].min()

#   percentage of people who work min works and earns more than 50K
people_min_hours = round(((df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100), 2)

#   country with the highest percentage of people making more than 50K
rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
rich_country_percentage = ((rich_country/(df['native-country'].value_counts())) * 100).idxmax()

#   most popular occupation in india who makes more than 50K
rich_indian_job = df[df['native-country']=='India'][df['salary']=='>50K']['occupation'].value_counts().idxmax()


