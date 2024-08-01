"""
This is a simple program that uses Pandas to analyze demographic data.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(filepath):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The dataset is empty.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The data file is empty or not properly formatted.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def analyze_demographics(df):
    """Perform demographic analysis on the dataset."""
    results = {}

    try:
        # Number of people of each race
        results['race_count'] = df['race'].value_counts()

        # Average age of men
        results['avg_men_age'] = df[df['sex'] == 'Male']['age'].mean()

        # Percentage of people with Bachelor's degree
        results['BS_degree'] = round(((df['education'] == 'Bachelors').mean() * 100), 2)

        # Percentage of people with advanced education making more than 50K
        advanced_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
        results['advanced_edu_gt_50k'] = round(((advanced_edu['salary'] == '>50K').mean() * 100), 2)

        # Percentage of people without advanced education making more than 50K
        results['without_advanced_edu_gt_50k'] = 100 - results['advanced_edu_gt_50k']

        # Minimum hours a person works
        results['min_work_hours'] = df['hours-per-week'].min()

        # Percentage of people who work minimum hours and earn more than 50K
        min_workers = df[df['hours-per-week'] == results['min_work_hours']]
        results['people_min_hours'] = round(((min_workers['salary'] == '>50K').mean() * 100), 2)

        # Country with the highest percentage of people making more than 50K
        rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
        country_percentage = ((rich_country / df['native-country'].value_counts()) * 100).idxmax()
        results['rich_country'] = country_percentage

        # Most popular occupation in India for those earning more than 50K
        rich_indian_job = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        results['rich_indian_job'] = rich_indian_job['occupation'].value_counts().idxmax()

    except KeyError as e:
        raise KeyError(f"Missing expected column: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during analysis: {e}")

    return results


def save_results(results, filepath):
    """Save the analysis results to a text file."""
    try:
        with open(filepath, 'w') as file:
            for key, value in results.items():
                file.write(f"{key}: {value}\n\n")
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving results: {e}")


def plot_race_distribution(df, filepath):
    """Plot race distribution and save the figure."""
    try:
        race_count = df['race'].value_counts()
        race_count.plot(kind='bar', color='skyblue')
        plt.xlabel('Race')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right', va='top')
        plt.title('Race Distribution')
        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting race distribution: {e}")


def plot_education_income(df, filepath):
    """Plot education vs income and save the figure."""
    try:
        education_income = df[df['salary'] == '>50K']['education'].value_counts()
        education_income.plot(kind='bar', color='green')
        plt.xlabel('Education')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right', va='top')
        plt.title('Education Level of Those Earning >50K')
        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting education vs income: {e}")


def main():
    # Load the dataset
    filepath = '../data/adult_data.csv'
    try:
        df = load_data(filepath)
    except Exception as e:
        print(e)
        return

    # Perform demographic analysis
    try:
        results = analyze_demographics(df)
    except Exception as e:
        print(e)
        return

    # Save results to a text file
    try:
        save_results(results, '../results/analysis_results.txt')
    except Exception as e:
        print(e)

    # Print results
    for key, value in results.items():
        print(f"{key}: {value}")

    # Plot race distribution
    try:
        plot_race_distribution(df, '../figures/race_distribution.png')
    except Exception as e:
        print(e)

    # Plot education vs income
    try:
        plot_education_income(df, '../figures/education_income.png')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
