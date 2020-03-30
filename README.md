# Data Science Practicum I, II

A repository for the Regis University Data Science Cloud Project to prepare documentations for Regis University students in Data Science and Data Engineering classes.

# Description of the Project

   This project is an ongoing process of multiple steps in a small group of graduate students and a professor. The environment of the project is CloudStack, where a few instances (Virtual machines) created to work on. The goal of the project is to create documentation in Cloud Project Regis University GitHub page for all the data science related students at Regis University to use in their classes. 
   I am working with 2 databases PostgreSQL and MongoDB to test how Virtual Machines on CloudStack behave to analize the process and in the future to make decisions what hardware to use. I use Yelp dataset which was downloaded from https://www.yelp.com/dataset to test those two databases. Using these datasets, I create tables and import data into them in Linux on Ubuntu 18.04 Virtual Machine on CloudStack. After all data stored in the tables, I am working with standard queries performed in Python so I could run multi-processing, test loading to identify how many students could run queries in those databases at the same time. 
   I am trying to represent performance under 1 set of configuration parameters for VM/server, network by analyzing CPU cores, CPU clock speed and RAM Size. Additionally, during this project we are trying to collect data that will be used to help determine hardware specifications on new equipment by load testing on created virtual machine on CloudStack. Besides hardware we need to estimate how much RAM a computer or cluster of computers would need to support 2 or 3 Data Science classes of every student was using it simultaneously.


# Description of Data 

   We work with Yelp data set in this project that was downloaded from the website: https://www.yelp.com/dataset
This dataset is a subset of Yelp's businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. In the dataset there is information about businesses across 11 metropolitan areas in four countries.

# Project Process:
-	Install Global Protect and CloudStack environment 
-	Exploring CloudStack and creating/destroying instances 
-	Installing Ubuntu 18.04 and Windows 10 virtual machines 
-	Installing WinSCP and PuTTY 
-	Creating tin0,tin1,tin2 user with sudo privileges 
-	Converting yelp data fils from JSON to CSV/ moving files using WinSCP 
-	Installing PostgreSQL and MongoDB databases in Linux 
-	Creating tables in psql and importing data into the tables/ importing data into mongoDB
-	Data cleaning (file user.csv (5GB) to import into psql)
-	Creating instance from ISO and creating template (Ubuntu 18.04) in CloudStack 
-	Repeating PostgreSQL and MongoDB databases processes in CS VM for documentation
-	Moving files from local VM to CloudStack VM using private network with tin0 account using WinSCP and PuTTY
-	Document everything for future students` use in data science and data engineering classes at Regis University 


# Timeline of the Project 
   Week 1
1.	Write Proposal for Capstone Part 2
2.	Create documentation for what was done in Capstone Part 1 in PDF
3.	Create content in GitHub for Project Part 2, import all files to GitHub
4.	Write README.md on GitHub

   Week 2
1.	Finish documentation
2.	Learn about how to connect psql database in Python
3.	Solve configuration and nrtwork privacy issues
   
   Week 3
1.	Explore software for load-testing
2.	Explore multi-processing code examples 
3.	Connect yelpdb (psql database) in Python 
4.	Run 5 queries in Python using all the created tables in yelpdb (psql) 

