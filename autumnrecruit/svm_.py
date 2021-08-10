# coding: utf-8
import numpy as np
from sklearn import svm

np.random.seed(0) # 使用相同的seed()值，则每次生成的随即数都相同
# 创建可线性分类的数据集与结果集
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20,2) + [2, 2]]
Y = [0] * 20 + [1] * 20

# 构造 SVM 模型
clf = svm.SVC(kernel='linear')
clf.fit(X, Y) # 训练 
w = clf.coef_[0]
a = -w[0] / w[1] # 斜率
xx = np.linspace(-5, 5) # 在区间[-5, 5] 中产生连续的值，用于画线
yy = a * xx - (clf.intercept_[0]) / w[1]
b = clf.support_vectors_[0] # 第一个分类的支持向量
yy_down = a * xx + (b[1] - a * b[0])

b = clf.support_vectors_[-1] # 第二个分类中的支持向量
yy_up = a * xx + (b[1] - a * b[0])

import pylab as pl

pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')
pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
           s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()