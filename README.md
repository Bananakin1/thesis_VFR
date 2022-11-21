<h1> MSc Thesis: Asset value prediction using Sentiment Analysis on social media </h1>

Universidad Nacional de Estudios a Distancia (UNED)
Student: Victor Fiz Real
September 2021

<h3> Thesis done originally in Spanish during the MSc in Big Data and Business Analytics of the UNED. This readme file contains a summary of the content commented translated 
to English, to ease the understanding for non-spanish speaker readers </h3>

<h2> Index </h2>

1. Scope
2. Tools used
3. Pipeline  
  3.1. Data mining  
  3.2. Preprocessing  
  3.3. EDA  
  3.4. Modelling

<h2> Scope </h2>

The main objective of the thesis is to be able to generate a pipeline able to:
  - Extract tweets using keywords considered relevant to the behaviour of the asset during a certain period of time
  - Perform a sentiment analysis over the data mined 
  - Extract the historical evolution of said asset
  - Elaborate an appropriate model able to predict the evolution of the asset with a decent accuracy
  
The practical case of the thesis was performed over the cryptocurrency Bitcoin during November of 2017, due to the vast amount of publications on social media 
and the popularity of the asset.

<h2> Tools used </h2>

Programming language: Python

Data mining: Twitter API, Bitstamp API

Data Handling: Pandas, PySpark

Data Processing: 
  Numerical: Numpy
  Text: Preprocessor
  Sentiment Analysis: Vader, textblob

Data visualization: Matplotlib, seaborn

Machine Learning: Sklearn, Keras, Elephas

<h2> Pipeline </h2>

<h3> Data mining </h3>

Hourly historical values of Bitcoin were extracted from Bitstamp, in this case any exchange platform allows to download the data easily.

The official Twitter API allowed to download the tweets that included the keyword "bitcoin". The free version of the API worked at a very slow rate, and despite the potential
of the tool, the time limitations of the project restricted the amount of data collected. During the span of one month (~700h) over 2.5 million tweets (including retweets) 
were collected and analyzed.

<h3> Preprocessing </h3>

The tweet dataset preprocessing follows the next algorithm:
  - Drop all the metadata related to the tweet, keeping only the text and the date.
  - Text cleaning: link, emoji, symbol and mention removal. Hasthag words are kept.
  - Sentiment analysis: assing values for the compound sentiment.
  
The Bitcoin historical value dates are adapted to match the sentiment timestamp.

<h3> EDA </h3>

Polarity and subjetivity analysis and visualization of the tweets excluding the retweets.

<h3> Modelling </h3>

The features considered are the sentiment scores obtained in the previous steps. The target is the price of the Bitcoin.

To model the time series since the amount of features used is reduced, the dataset is phased temporally to increase the weight of the short term measures over the longer ones.
Initially a Linear Regression model is implemented, to compare with the LSTM applied afterwards, which is the best model to apply on temporal series.
