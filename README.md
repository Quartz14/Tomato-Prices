# Tomato-Prices
Analysis of tomato prices in Karnataka from 2016 to 2018/4

The tomato_app file is the web page made from flask. It uses the HTML files in templates.
Templates can be found in the templates branch

Price of Tomato Karnataka(2016-2018).csv file contains the raw data obtained from Kaggle URL: https://www.kaggle.com/vinayreddy4034/vegetablepricetomato

The modified data is stored in monthly_tomato.csv file  

Tomato2 is a python notebook containing the data exploration, analysis and visualizations, to identify trends in data

monthly_tomato notebook contains the machine learning part of code

monthly_gbr_model3 is the pickled machine learning model obtained from monthly_tomato notebook

monthly_tomato_app file is a flask app that uses the pickled model to predict the prices.

The Templates branch contains 2 html files:
    1) monthly_tomato_home - Home page that takes in user inputs Month, Market Area, Average Tonnes per month for that market
    2) tomato_result - Displays the predicted values
    
Requirements contains the python libraries required to run the pogram

