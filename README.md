# Demographic Data Analysis

## Overview
This project analyzes demographic data using Pandas to provide insights into various aspects such as race distribution, 
education levels, work hours, and income. The analysis includes calculating the average age of men, the percentage of 
people with Bachelor's degrees, and the percentage of people earning more than 50K based on their education level.

## Folder Structure
The project is organized into the following directories:

```
demographic-data-analysis/
├── data/
│   ├── adult_data.csv
├── scripts/
│   ├── analysis.py
├── results/
│   ├── analysis_results.txt
├── figures/
│   ├── race_distribution.png
│   ├── education_income.png
├── docs/
│   ├── data-description.md
│   ├── methodology.md
│   ├── results.md
├── requirements.txt
├── README.md
```

### Description of Directories
- **data/**: This directory contains the dataset file.
  - `adult_data.csv`: The dataset used for the analysis.
- **scripts/**: This directory contains the script for data analysis.
  - `demographics_analysis.py`: The main script that performs the demographic data analysis.
- **results/**: This directory contains the results of the analysis.
  - `analysis_results.txt`: A text file with the results of the demographic analysis.
- **figures/**: This directory contains the generated plots and visualizations.
  - `race_distribution.png`: Plot of race distribution.
  - `education_income.png`: Plot of education vs income.
- **docs/**: This directory contains documentation files.
  - `data-description.md`: Detailed description of the dataset.
  - `methodology.md`: Methodology of the analysis.
  - `results.md`: Results of the analysis.
- **requirements.txt**: This file contains the necessary Python libraries for the project.
- **README.md**: The readme file for the project.

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd demographic-data-analysis
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Place the dataset**:
   Ensure the dataset `adult_data.csv` is located in the `data` directory.

## Usage
To run the analysis, use the following command:

```bash
python scripts/demographics_analysis.py
```

## Conclusion
This analysis offers valuable insights into demographic factors influencing income. It highlights the importance of 
education and work hours in determining income levels and provides a comprehensive view of demographic distributions.

## Future Work
- Extend the analysis to include more demographic factors.
- Explore the impact of additional variables such as marital status and occupation type on income.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with any improvements or additional features.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
The conversation continues on [**Kaggle**](https://www.kaggle.com/code/mrowurakwarteng/demographic-data-analysis)

