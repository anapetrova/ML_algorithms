import numpy as np

class Perceptron:
	def __init__(self, train_data):
		self.train_data = train_data
		self.mistake_list = {}

	
	def build_kernel(self, num_iter, substr_size):  #total runs through data
		for n in range(0, num_iter):
			for data, label in self.train_data.iteritems():
				#sum of y_i * K(x_i, x) 
				total_sum = 0
				for data_i, label_i in self.mistake_list.iteritems():
					#all substrings of size substr_size
					total_sum += label_i * self.num_substrings(data_i, data, substr_size)
				if total_sum * label <= 0:
					self.mistake_list[data] = label	
					
		
	def predict_kernel(self, x, substr_size):
		total_sum = 0
		for data, label in self.mistake_list.iteritems():
			total_sum += self.num_substrings(data, x, substr_size) * label
		if total_sum == 0:
			return total_sum
		return (total_sum / abs(total_sum))

	#K(s, t)
	def num_substrings(self, s, t, p):
		substr_found = set()
		for i in range(1, len(s) - p + 1):
			v = s[i:(i + p - 1)]
			if v in t and v not in substr_found:
				substr_found.add(v)
		return len(substr_found)
		


def readFromFile(filename):
	with open(filename, "r") as samples:
		feat_vectors = samples.readlines()
		feat_dict = {}
		for feat in feat_vectors:
			feat_str, useless, feat_label = feat.split(" ")			
			feat_dict[feat_str] = int(feat_label)
		return feat_dict		

if __name__ == "__main__":
	train_feat = readFromFile('hw5train.txt')
	test_feat = readFromFile('hw5test.txt')
	perceptron = Perceptron(train_feat)

	test_num = float(len(test_feat))
	train_num = float(len(train_feat))
	for p in range(3, 5):
		test_error = 0.0
		perceptron.build_kernel(1, p)

		train_error = 0.0
		for train_vec, label in train_feat.iteritems():
			if(label != perceptron.predict_kernel(train_vec, p)):
				train_error += 1.0
		print "String Kernel Perceptron with p = " + str(p) + ", Train error: " + str(train_error/train_num)

		for test_vec, label in test_feat.iteritems():
			if(label != perceptron.predict_kernel(test_vec, p)):
				test_error += 1.0
		print "String Kernel Perceptron with p = " + str(p) + ", Test error: " + str(test_error/test_num)

