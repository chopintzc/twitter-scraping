'''
Created on Feb 2, 2017

@author: Zhongchao
'''

from sklearn.svm.classes import *
from sklearn.linear_model import *
from sklearn.model_selection import *
from sklearn.naive_bayes import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import metrics
import pandas as pd




def __getVectorizer(ngram_range=(1, 1), stop_words=None, lowercase=False, max_df=1.0, min_df=1, max_features=None, binary=False, sublinear_tf=True, vocabulary=None):
    vectorizer = TfidfVectorizer(sublinear_tf=sublinear_tf, max_df=max_df, min_df=min_df, lowercase=lowercase, \
                                 ngram_range=ngram_range, stop_words=stop_words, max_features=max_features, binary=binary, vocabulary=vocabulary)  # ,stop_words='english')
    return vectorizer



def __CLF(data,target,clf):
    scores = cross_val_score(clf, data, target, cv=10)
    predicted = cross_val_predict(clf, data, target, cv=10)

    accuracy = metrics.accuracy_score(target, predicted)
    precision = metrics.precision_score(target, predicted, pos_label='positive')
    f1 = metrics.f1_score(target, predicted, pos_label='positive')
    recall = metrics.recall_score(target, predicted, pos_label='positive')

    return [scores,accuracy,precision,f1,recall]
    # print 'accuracy score for each cv(NB): ', scores
    # print 'average accuracy score:(NB) ', accuracy

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '%s' % float(height))

def draw_bar(labels,quants,name):
    width = 0.4
    ind = np.linspace(0.5,5.5,6)
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    # Bar Plot
    rect = ax.bar(ind-width/2,quants,width,color='blue')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('Classification Method')
    ax.set_ylabel('accuracy')
    # title
    ax.set_title('%s of 5 Classification Method'%name, bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    autolabel(rect)
    # plt.show()
    plt.savefig("visualization/%s.jpg"%name)
    plt.close()

if __name__ == '__main__':
    df = pd.read_csv('stemmed-data.csv', header=0, names=['emoticon', 'text', 'label'])
    text = [s[0] for s in df.as_matrix(['text']).tolist()]
    target = [s[0] for s in df.as_matrix(['label']).tolist()]


    vectorizer = __getVectorizer(max_df=1.00, min_df=1, vocabulary=None, binary=False)
    data = vectorizer.fit_transform(text)

    #define 5 classificaiton methods
    clf = [LinearSVC(),SVC(kernel='rbf'),MultinomialNB(),BernoulliNB(),RidgeClassifier(),Perceptron(n_iter=50)]#
    


    clf_name = ['Linear SVC','Radial kernel SVC','Multinomial NB','Bernoulli NB','Ridge Classifier','Perceptron'] #
    (Acc,Pre,Rec,F) =([],[],[],[])
    for i in range(len(clf)):
        [scores, accuracy, precision, f1, Recall] = __CLF(data,target,clf[i])
        Acc.append(round(accuracy,3))
        Pre.append(round(precision, 3))
        Rec.append(round(Recall, 3))
        F.append(round(f1, 3))
        print '%s:\n  accuracy score for each cv :%s'%(clf_name[i], scores)
        print '  average accuracy score : ', accuracy
        print '  average precision score: ', precision
        print '  average f1 score: ', f1
        print '  average recall score: %s\n'%Recall,"-"*100,"\n"
        plt.figure(i)
        plt.xlabel(u'cv')
        plt.ylabel(u'accuracy')
        plt.title(u'Accuracy Score of %s'%clf_name[i],bbox={'facecolor':'0.8', 'pad':5})
        rect = plt.bar(left=range(0,10,1), height=[round(a,3) for a in scores], width=0.35,color="green")
        # plt.plot(range(0,10,1),accuracy)
        autolabel(rect)
        plt.savefig("visualization/%s.jpg"%clf_name[i])
        plt.close()
    draw_bar(clf_name,Acc,"Accuracy")
    draw_bar(clf_name, Pre,"Precision")
    draw_bar(clf_name, F, "Fmeasure")
    draw_bar(clf_name, Rec, "Recall")