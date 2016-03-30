import numpy as np
import math
from scipy.stats import itemfreq


class DTNode:
	def __init__(self, parent=None):
		self.split_dim = None
		self.split_threshold = None
		self.label = None
		self.parent = None
		self.num_data = 0
		self.children = []

	def build(self, train_data, dim_used=[]):
		self.num_data = len(train_data)
		feat_vectors, labels = zip(*train_data)
		#Check for purity
		if (len(np.unique(np.asarray(labels))) == 1 or dim_used == len(feat_vectors[0])):
			self.label = labels[0]
			return
		#calculate total entropy
		freq_counts = itemfreq(labels)
		num_labels = len(freq_counts)
		H = -sum([freq[1]/self.num_data * math.log(freq[1]/self.num_data, 2) for freq in freq_counts])
		max_ig = 0
		#calculate conditional entropy for each dimension
		for dim in range(0, len(feat_vectors[0])):
			if dim in dim_used:
				continue
			#find thresholds
			temp =  np.sort(np.unique(np.array(feat_vectors)[:,dim]))
			thresholds = np.zeros([len(temp) - 1, 1], dtype=float)
			for i in range(0, len(temp) - 1):
				thresholds[i] = (temp[i] + temp[i + 1])/2

			#find entropy for each threshold
			for threshold in thresholds:
				#find probability table
				probability_table = np.zeros([2, num_labels])
				for feat_vector, label in zip(feat_vectors, labels):
					if feat_vector[dim] > threshold:
						probability_table[0][int(label)-1] += 1				
					else:
						probability_table[1][int(label)-1] += 1
				total_sum = np.sum(probability_table[0] + np.sum(probability_table[1]))
				probability_table[0] /= total_sum
				probability_table[1] /= total_sum
				cond_entropy = 0
				#Calculate conditional entropy -- sum(p(x,y)log(p(x)/p(x,y)))
				for i in range (0, 2):
					for j in range (0, num_labels):
						p_x_y = probability_table[i][j]
						p_x = np.sum(probability_table[i])
						if p_x_y != 0:
							cond_entropy += p_x_y * math.log(p_x/p_x_y, 2)
				#Find IG
				IG = H - cond_entropy
				if IG > max_ig:
					max_ig = IG
					self.split_dim = dim
					self.split_threshold = threshold
		
		#no branch
		left_data = []
		#yes branch
		right_data = []
		for feat_vector, label in zip(feat_vectors, labels):
			if feat_vector[self.split_dim] > self.split_threshold:
				right_data.append([feat_vector, label])
			else:
				left_data.append([feat_vector, label])
	
		left_node = DTNode(self)
		right_node = DTNode(self)
		self.children.append(left_node)
		self.children.append(right_node)
		dim_used.append(self.split_dim)
		left_node.build(left_data, dim_used)
		right_node.build(right_data, dim_used)


	def predict(self, data):
		if self.label != None:
			return self.label
		elif data[self.dim_split] > self.split_threshold:
			return self.children[1].predict(data)
		else:
			return self.children[0].predict(data)
			
		

	def str_repr(self, level=0): 
		string_rep = ""
		if self.label == None:
			string_rep += "Splitting Rule: " + str(self.split_dim) + "<" + str(self.split_threshold)
		else:
			string_rep += "Label: " + str(self.label)
		ret = "\t"*level + string_rep + "; Num data: " + str(self.num_data) +"\n"
		for child in self.children:
			ret += child.str_repr(level+1)
		return ret
		

		

def readFromFile(filename):
	with open(filename, "r") as samples:
		feat_vectors = samples.readlines()
		num_feats = len(feat_vectors[0].strip().split(' '))
		#change these to regular lists
		feat_arr = np.empty([len(feat_vectors), num_feats - 1], dtype=float)
		label_arr = np.empty([len(feat_vectors), 1], dtype=float)
		i = 0
		for feat in feat_vectors:
			feat = map(float, filter(lambda x : is_float(x) , feat.strip().split(' ')))
			feat_arr[i] = feat[0:-1]
			label_arr[i] = feat[-1]
			i += 1
		return zip(feat_arr, label_arr)   #this doesn't work

def is_float(x):
	try:
		float(x)
		return True
	except ValueError:
		return False


if __name__ == '__main__':
	train_data = readFromFile("hw3train.txt")
	decision_tree = DTNode()
	decision_tree.build(train_data)
	print decision_tree.str_repr()
	
	test_data = readFromFile("hw3test.txt")
	test_error = 0
	for feat_vector, label in test_data.iteritems():
		if decision_tree.predict(feat_vector) != label:
			test_error += 1
	
	test_error /= len(test_data)

	print "\nTest Error: " + str(test_error)
