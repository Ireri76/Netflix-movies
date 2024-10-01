README file

PYTHON

The original dataset load in preparation for this project is named ‘netflix_data.csv’. Seven separate files were developed to ensure the codes are efficient, optimized, and easier to maintain as changes can be made targeting only a particular file. This project was run using the Jupyter lab platform and thus to ensure that the codes run well in other Python environments, the .ipynb files were converted to .py files.
The following order was adopted to create all the separate files used in this project:

1.	data_preparation.py: The code loads the original raw data (netflix_data.csv) file into the program.
2.	data_cleaning.py: The code is used to clean the raw data and the clean data under a new file named ‘netflix_show_movies.csv’
3.	data_evaluation.py: The code evaluates the cleaned data to ensure it is clean and ready for analysis.
4.	data_exploration.py: The code explores the cleaned data for initial analysis, patterns and insights.
5.	data_visualization.py: The code is used to visualize and evaluate the cleaned dataset.
6.	data_analysis.py: The code performs the basic chi-square test and it generates the chi statistics and the p-values.
7.	main.py: The code runs the entire process from the first file to the last file, which includes: loading, cleaning, evaluating, exploring, visualizing and the chi-square test.

NB://
1.	To ensure prevention from any accidental deletion of the snippets, run the file named ‘RUN Code.ipybn’. This file has the snippet code %run main.py which will run the entire process effectively.
2. 	The original csv file was not zip and thus, it was not necessary to add a snippet in the code to unzip it.
3. 	Ensure all the seven files and the original dataset are in the same folder.

R Graphs
1.	The same graphs that were generated using using Python, have been generated again using R  and its associated packages. 
2.	The only major difference is that the graphs in Python are side by side, while those in R are generated separately.
3	Ensure that you change the path that I have used to import and load the dataset to your our path. And maybe, you can create a relative path for the same purpose but ensure all the files are in the same folder.
