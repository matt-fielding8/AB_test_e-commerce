# E-commerce A/B-Test Analysis

A/B tests are commonly used in industry to test changes on a web page by exposing a control group to the old webpage and a treatment group to the new web page. The level of user engagement can be measured by a selected metric, in this case we use conversion rate.

## Description
An e-commerce company has developed a new web page in order to try and increase purchases (conversions) made through their site. They have run an AB experiment and collected data regarding the number of conversions for a control group and a treatment group. The objective of this project is to assess the data and help the company understand if they should implement this new page, keep the old page, or run the experiment longer to make their decision.

We will then implement logistic regression algorithms in order to predict the probability of a individual users purchasing products from their site.

## Data Overview
The datasets for this project are provided by **Udacity** in association with their **Data Analyst Nanodegree** programme. They have been generated to represent example AB experiment results from an e-commerce website. There are 2 raw csv files:

  * `ab_test.csv` - contains information regarding the group (control or treatment), landing page (old or new), timestamp of visit and conversion.
  * `countries.csv` - contains information regarding the country of origin of each user.
  * `ab_test_clean.csv` - the product of merging and cleaning `ab_test.csv` and `countries.csv`. The cleaning process is documented in [AB_Test](http://localhost:8888/notebooks/AB_Test/notebooks/AB_Test.ipynb).

## Notebooks
[AB_Test.ipynb](http://localhost:8888/notebooks/AB_Test/notebooks/AB_Test.ipynb) - documents end to end analysis of the test results and the steps taken to clean the data.
