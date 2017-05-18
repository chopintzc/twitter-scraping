# **Twitter-scraping**

## **Summary of the project:**

This is the Project for my Natural Language Processing class, written in Python.
It can crawl tweets via twitter api. We scraped more than 10,000 tweets which contain emoticons
Those tweets are labeled as positive or negative based on the contained emoticons. We then train a few
ML classifiers using the labeled training data. The trained classifiers are tested with testing data to
verify the performance of classifiers.
We tried a couple of ML classifiers such as linear SVM, Multinomial Naive Bayes, Bernoulli Naive Bayes,
Ridge, and Perceptron classifiers. 

## **Requirement**

This program requires Python 2.7, python-twitter 3.2.1, and scikit-learn 0.18

## **Features**
* scraped more than 10,000 tweets using twitter api
* all the scraped tweets are labeled as positive or negative based on the contained emoticon
* ML classifiers are trained using the labeled training data and their performance are verified using testing data
* We test linear SVM, multinomial Naive Bayes, Bernoulli Naive Bayes, Ridge and Perceptron classifiers