import numpy as np

np.set_printoptions(precision=3, linewidth=160, suppress=True)

class Perceptron:
	def __init__(self, train_data):
		self.train_data = train_data
		self.w_list = {}
		self.w = None
	
	def build_basic(self, num_iter):  #total runs through data
		self.w = np.zeros(len(self.train_data[0][0]))
		for i in range(0, num_iter):
			for data, label in self.train_data:
				if label[0] * self.w.dot(data) <= 0:
					self.w = self.w + label*data

	def build_voted(self, num_iter):
		m = 1
		c_m = 1
		curr_w = np.zeros(len(self.train_data[0][0]))

		for i in range(0, num_iter):
			for data, label in self.train_data:
				if label[0] * curr_w.dot(data) <= 0:
					if (curr_w != np.zeros(len(self.train_data))):
						self.w_list[c_m] = curr_w
					curr_w = curr_w + label*data
					m += 1
					c_m = 1
				else:
					c_m += 1
		
	def predict_basic(self, x):
		return np.sign(self.w.dot(x))

	def predict_average(self, x):
		return np.sign(sum([(c*w).dot(x) for (c, w) in self.w_list.iteritems()]))

	def predict_voted(self, x):		
		return np.sign(sum([c*np.sign(w.dot(x)) for (c, w) in self.w_list.iteritems()]))
		

def readFromFile(filename, l=None):
	with open(filename, "r") as samples:
		feat_vectors = samples.readlines()
		num_feats = len(feat_vectors[0].strip().split(' '))
		feat_arr = np.empty([len(feat_vectors), num_feats - 1], dtype=int)
		label_arr = np.empty([len(feat_vectors), 1], dtype=int)
		i = 0
		for feat in feat_vectors:
			feat = map(int, filter(str.isdigit, feat.strip().split(' ')))
			feat_arr[i] = feat[0:-1]
			if l != None:
				if(feat[-1] == l):
					label_arr[i] = 1
				else:
					label_arr[i] = -1
			else:
				label_arr[i] = feat[-1]
			i += 1
		return zip(feat_arr, label_arr)


if __name__ == "__main__":
	#part a
	train_feat = readFromFile('hw4atrain.txt', 6)
	test_feat = readFromFile('hw4atest.txt', 6)
	perceptron = Perceptron(train_feat)
	test_num = float(len(test_feat))
	train_num = float(len(train_feat))
	for i in range(1, 4):
		test_error = 0.0
		perceptron.build_basic(i)

		train_error = 0.0
		for train_vec, label in train_feat:
			if(label[0] != perceptron.predict_basic(train_vec)):
				train_error += 1.0
		print "Num passes: " + str(i) + ", Basic Perceptron, Train error: " + str(train_error/train_num)

		for test_vec, label in test_feat:
			if(label[0] != perceptron.predict_basic(test_vec)):
				test_error += 1.0
		print "Num passes: " + str(i) + ", Basic Perceptron, Test error: " + str(test_error/test_num)

		test_error = 0.0
		perceptron.build_voted(i)
	
		train_error = 0.0
		for train_vec, label in train_feat:
			if(label[0] != perceptron.predict_voted(train_vec)):
				train_error += 1.0
		print "Num passes: " + str(i) + ", Voted Perceptron, Train error: " + str(train_error/train_num)


		for test_vec, label in test_feat:
			if(label[0] != perceptron.predict_voted(test_vec)):
				test_error += 1.0
		print "Num passes: " + str(i) + ", Voted Perceptron, Test error: " + str(test_error/test_num)

		train_error = 0.0
		for train_vec, label in train_feat:
			if(label[0] != perceptron.predict_average(train_vec)):
				train_error += 1.0
		print "Num passes: " + str(i) + ", Average Perceptron, Train error: " + str(train_error/train_num)


		test_error = 0.0
		for test_vec, label in test_feat:
			if(label[0] != perceptron.predict_average(test_vec)):
				test_error += 1.0
		print "Num passes: " + str(i) + ", Average Perceptron, Test error: " + str(test_error/test_num)

	#part b
	c_list = []
	for i in range(0, 10):
		train_feat = readFromFile('hw4btrain.txt', i)
		p = Perceptron(train_feat)
		p.build_basic(1)
		c_list.append(p)

	confusion_matrix = np.zeros([11, 10], dtype=float)

	test_feat = readFromFile('hw4btest.txt')

	for feat, label in test_feat:
		i_list = []
		for i in range(0, 10):
			if c_list[i].predict_basic(feat) == 1:
				i_list.append(i)
		if len(i_list) != 1:
			confusion_matrix[10][label[0]] += 1
		else:
			confusion_matrix[i_list[0]][label[0]] += 1

	for i in xrange(0, 11):
		confusion_matrix[i] /= np.sum(confusion_matrix[i])
	print confusion_matrix

'''
OUTPUT

Num passes: 1, Basic Perceptron, Train error: 0.01
Num passes: 1, Basic Perceptron, Test error: 0.02
Num passes: 1, Voted Perceptron, Train error: 0.016
Num passes: 1, Voted Perceptron, Test error: 0.014
Num passes: 1, Average Perceptron, Train error: 0.012
Num passes: 1, Average Perceptron, Test error: 0.01
Num passes: 2, Basic Perceptron, Train error: 0.008
Num passes: 2, Basic Perceptron, Test error: 0.01
Num passes: 2, Voted Perceptron, Train error: 0.006
Num passes: 2, Voted Perceptron, Test error: 0.012
Num passes: 2, Average Perceptron, Train error: 0.008
Num passes: 2, Average Perceptron, Test error: 0.01
Num passes: 3, Basic Perceptron, Train error: 0.008
Num passes: 3, Basic Perceptron, Test error: 0.014
Num passes: 3, Voted Perceptron, Train error: 0.003
Num passes: 3, Voted Perceptron, Test error: 0.008
Num passes: 3, Average Perceptron, Train error: 0.002
Num passes: 3, Average Perceptron, Test error: 0.01

[[ 0.987  0.     0.     0.     0.     0.     0.013  0.     0.     0.   ]
 [ 0.     0.964  0.036  0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.922  0.031  0.016  0.     0.016  0.     0.     0.016]
 [ 0.     0.     0.021  0.938  0.     0.021  0.     0.021  0.     0.   ]
 [ 0.     0.     0.021  0.     0.957  0.021  0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     1.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.02   0.98   0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.033  0.     0.     0.967  0.     0.   ]
 [ 0.016  0.008  0.048  0.056  0.024  0.113  0.081  0.008  0.629  0.016]
 [ 0.     0.     0.     0.     0.074  0.012  0.012  0.037  0.012  0.852]
 [ 0.047  0.166  0.081  0.126  0.104  0.109  0.107  0.118  0.033  0.109]]

'''
