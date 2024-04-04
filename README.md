# Project Title
Video Game Sales Analysis

## Short Description
This project analyzes video game sales data to determine if there's a difference in average global sales before and after the year 2005. It also labels records as 'pre-2005' or 'post-2005' based on the release year.

## Getting Started
These guidelines will assist you in obtaining a copy of the code for development and testing on your local machine. Refer to the deployment section for instructions on how to deploy the project on a live system.

## Prerequisites
- Python 3
- pandas
- sqlalchemy
- pymysql

## Installing
- Clone the repository to your local machine.
- Install the required dependencies using pip:

pip install pandas sqlalchemy pymysql


## Running the Tests
To run the analysis, execute the provided Python script in your preferred environment. Ensure that you have configured the database connection properly.

## Breakdown of Tests
- The script first establishes a connection to the MySQL database.
- It then creates a new column in the dataset to label records as 'pre-2005' or 'post-2005' based on the release year.
- Next, it calculates the average global sales for the periods before and after 2005.
- Finally, it prints the results of the analysis.

## Deployment
This project can be further developed into a web application or integrated into a larger data analysis pipeline for decision-making purposes.

## Author
Kostubh Kumar

## License
This project is licensed under the CC0 1.0 Universal license.

## Acknowledgement
Special thanks to Professor Omar Al-Trad for his guidance
