import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imsave

def plot_val_values(plotname, name1, val1, name2, val2):
	fig = plt.figure()
	ax = fig.gca()
	ax.plot(np.arange(len(val1)), val1, linewidth = 5, color = '#2A6EA6', label = name1)
	ax.plot(np.arange(len(val2)), val2, linewidth = 5, color = '#FFA933', label = name2)
	ax.legend(loc = "upper right")
	ax.set_xlabel('Epoch', fontsize = 20)
	ax.set_ylabel('Values', fontsize = 20)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.suptitle(plotname, fontsize = 24, fontweight = 'bold')
	plt.show()

def plot_val_errors(plotname, names, err):
	fig = plt.figure()
	n = len(err)
	# plt.title("CNN vs FCNN")
	for i in xrange(n):
		ax = fig.add_subplot(n, 1, i + 1)
		# ax = fig.add_subplot(n, 1, i + 1)
		e1 = err[i][0]
		e2 = err[i][1]
		ax.plot(np.arange(len(e1)), e1, linewidth = 5, color = '#FFA933', label = names[i][0])
		ax.plot(np.arange(len(e2)), e2, linewidth = 5, color = '#2A6EA6', label = names[i][1])
		ax.legend(loc = "upper right")
		ax.set_xlabel('Epoch', fontsize = 20)
		ax.set_ylabel('Err', fontsize = 20)

		for tick in ax.xaxis.get_major_ticks():
			tick.label.set_fontsize(18)
		for tick in ax.yaxis.get_major_ticks():
			tick.label.set_fontsize(18)

	plt.suptitle(plotname, fontsize = 24, fontweight = 'bold')
	plt.show()

def plot_val_errors2(plotname, s):
	fig = plt.figure()
	# plt.title("CNN vs FCNN")
	cnt = 0
	c1 = '#FFA933'
	c2 = '#2A6EA6'
	l1 = 'Train'
	l2 = 'Val'
	last = -1
	for j in xrange(len(s)):
		if s[j] == '[':
			if cnt % 2 == 0:
				ax = fig.add_subplot(2, 1, cnt / 2 + 1)
			for i in xrange(j, len(s)):
				if s[i] == ']':
					ss = s[j : i + 1]
					a = np.array(eval(ss))
					if cnt % 2 == 0:
						c = c1
						l = l1
					else:
						c = c2
						l = l2
					ax.plot(np.arange(a.shape[0]), a, linewidth = 5, color = c, label = s[last + 1 : j - 3])
					xmin = np.argmin(a)
					ymin = np.min(a)
					ax.annotate('{}'.format(ymin), xy = (xmin, ymin), xytext = (xmin + 0.3, ymin * 0.99), color = c)
					last = i
					break

			if cnt % 2 == 1:
				ax.legend(loc = "upper right")
				ax.set_xlabel('Epoch', fontsize = 20)
				ax.set_ylabel('Err', fontsize = 20)
				for tick in ax.xaxis.get_major_ticks():
					tick.label.set_fontsize(18)
				for tick in ax.yaxis.get_major_ticks():
					tick.label.set_fontsize(18)
			cnt = cnt + 1

	plt.suptitle(plotname, fontsize = 24, fontweight = 'bold')
	plt.show()


with open('seaquest_dqn_valid.txt', 'r') as f:
	a = f.readlines()

with open('seaquest_double_valid.txt', 'r') as f:
	b = f.readlines()

for i in xrange(len(a)):
	a[i] = a[i][:-1]

for i in xrange(len(b)):
	b[i] = b[i][:-1]

dqn_valid = np.asarray(a)
double_valid = np.asarray(b)
print dqn_valid.shape
print double_valid.shape
plot_val_values("Validation values", 'Q-learning', dqn_valid, 'Double Q-learning', double_valid)