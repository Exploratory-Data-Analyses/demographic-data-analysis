# Methodology

The analysis process consists of the following steps:

## Data Loading
1. **Load Data**: Load the dataset from the CSV file using `pandas.read_csv()`.
2. **Error Handling**: Implement error handling to manage missing files, empty datasets, or improperly formatted data.

## Data Analysis
1. **Race Count**: Calculate the number of people of each race using `value_counts()`.
2. **Average Age of Men**: Compute the average age of men using `mean()`.
3. **Percentage of Bachelor's Degree Holders**: Calculate the percentage of people with a Bachelor's degree.
4. **Percentage with Advanced Education Earning >50K**: Calculate the percentage of people with advanced education (Bachelor's, Master's, Doctorate) earning more than 50K.
5. **Percentage without Advanced Education Earning >50K**: Calculate the percentage of people without advanced education earning more than 50K.
6. **Minimum Work Hours**: Determine the minimum number of hours worked per week.
7. **Percentage of People Working Minimum Hours and Earning >50K**: Calculate the percentage of people working minimum hours and earning more than 50K.
8. **Country with Highest Percentage of People Earning >50K**: Identify the country with the highest percentage of individuals earning more than 50K.
9. **Most Popular Occupation in India for >50K Earners**: Identify the most common occupation among individuals in India earning more than 50K.

## Data Visualization
1. **Race Distribution**: Plot the race distribution using a bar chart.
2. **Education vs Income**: Plot the distribution of education levels among individuals earning more than 50K using a bar chart.
