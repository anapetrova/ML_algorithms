import numpy as np
import math
from collections import Counter
import random

class KNearestNeighbor:
	def __init__(self, k, feat, label):
		self.train_feat = feat
		self.train_label = label
		self.k = k
	def predict(self, feat_vector):
		distances = np.apply_along_axis(lambda row:np.linalg.norm(row - feat_vector,ord=1), 1, self.train_feat)
		dist_tuples = []
		#create label-distance tuples
		for i in xrange(0, len(distances)):
			dist_tuples.append((self.train_label[i][0], distances[i]))
		#sort tuples by distance, select first k tuples, unzip tuple (leaves only label),		
		#count num of occurences for each label
		labels = Counter(zip(*(sorted(dist_tuples, key=(lambda x: x[1]))[0:self.k]))[0])
		#out of the most common labels, select a random one (for even k)
		return random.choice(labels.most_common(1))[0]


def readFromFile(filename):
	with open(filename, "r") as samples:
		feat_vectors = samples.readlines()
		num_feats = len(feat_vectors[0].strip().split(' '))
		feat_arr = np.empty([len(feat_vectors), num_feats - 1], dtype=int)
		label_arr = np.empty([len(feat_vectors), 1], dtype=int)
		i = 0
		for feat in feat_vectors:
			feat = map(int, filter(str.isdigit, feat.strip().split(' ')))
			feat_arr[i] = feat[0:-1]
			label_arr[i] = feat[-1]
			i += 1
		return feat_arr, label_arr


if __name__ == '__main__':
	train_feat, train_label = readFromFile('hw2train.txt')
	val_feat, val_label = readFromFile('hw2validate.txt')
	test_feat, test_label = readFromFile('hw2test.txt')
	
	#part a - test different k-values
	for k in [1, 3, 5, 11, 16, 21]:
		classifier = KNearestNeighbor(k, train_feat, train_label)
		train_error = 0.0
		val_error = 0.0
		test_error = 0.0
		#predict train data
		for (feat, label) in zip(train_feat, train_label):
			if(label[0] != classifier.predict(feat)):
				train_error += 1.0
		train_error /= len(train_label)
		#predict validation data
		for (feat, label) in zip(val_feat, val_label):
			if(label[0] != classifier.predict(feat)):
				val_error += 1.0
		val_error /= len(val_label)
		#predict test data
		for (feat, label) in zip(test_feat, test_label):
			if(label[0] != classifier.predict(feat)):
				test_error += 1.0
		test_error /= len(test_label)
		print 'k = ' + str(k)
		print 'Train Error: ' + str(train_error)
		print 'Validation Error: ' + str(val_error)
		print 'Test Error: ' + str(test_error)
		print '----------------------------------'
	
	#part b - calculate confusion matrix
	confusion_matrix = np.zeros([10, 10], dtype=float)
	classifier = KNearestNeighbor(3, train_feat, train_label)
	for (feat, label) in zip(test_feat, test_label):
		confusion_matrix[label[0]][classifier.predict(feat)] += 1
	for i in xrange(0, 10):
		confusion_matrix[i] /= np.sum(confusion_matrix[i])
	print confusion_matrix

'''
OUTPUT

k = 1
Train Error: 0.0
Validation Error: 0.13
Test Error: 0.113333333333
----------------------------------
k = 3
Train Error: 0.07
Validation Error: 0.156666666667
Test Error: 0.13
----------------------------------
k = 5
Train Error: 0.098
Validation Error: 0.15
Test Error: 0.103333333333
----------------------------------
k = 11
Train Error: 0.139
Validation Error: 0.196666666667
Test Error: 0.156666666667
----------------------------------
k = 16
Train Error: 0.16
Validation Error: 0.203333333333
Test Error: 0.16
----------------------------------
k = 21
Train Error: 0.182
Validation Error: 0.22
Test Error: 0.19
----------------------------------

[[ 0.89285714  0.          0.          0.          0.          0.          0.10714286  0.          0.          0.        ]
 [ 0.          1. **A**    0.          0.          0.          0.          0.          0.          0.          0.        ]
 [ 0.05263158  0.10526316  0.76315789  0.          0.          0.          0.          0.02631579  0.05263158  0.        ]
 [ 0.06666667  0.1         0.          0.7  **B**  0.          0.          0.          0.          0.06666667  0.06666667]
 [ 0.          0.          0.          0.          0.92857143  0.          0.          0.          0.          0.07142857]
 [ 0.          0.          0.          0.03846154  0.          0.84615385  0.          0.03846154  0.03846154  0.03846154]
 [ 0.          0.05405405  0.02702703  0.          0.          0.          0.91891892  0.          0.          0.        ]
 [ 0.          0.          0.          0.          0.          0.          0.          0.9         0.          0.1       ]
 [ 0.          0.03571429  0.          0.          0.          0.          0.03571429  0.03571429  0.89285714  0.        ]
 [ 0.          0.          0.          0.          0.111 **C** 0.          0.          0.          0.          0.88888889]]
'''
