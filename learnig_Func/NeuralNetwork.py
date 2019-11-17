import pickle as pick
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class NN:
    def __init__(self):
        self.weights=[]
        self.biases=[]
        self.activaes=[]
        self.losses=[]
        self.opts=[]
        self.x=[]
        self.y=[]
        self.step=np.zeros(100)

    def relu(self,x,w,b):
        """
        :param x: type tensor 入力のtensor
        :param w: type tensor 重みのtensor
        :param b: type tensor biasのtensor
        :return: type tensor  relu　name scope の設定
        """
        i = 0
        name = "relu" + str(self.step[i])
        with tf.name_scope(name):
            relu = tf.nn.relu(tf.matmul(x, w) + b)
            self.activaes.append(relu)
        self.step[i] += 1
        return relu

    def sigmoid(self,x,w,b):
        """
        :param x: type tensor 入力のtensor
        :param w: type tensor 重みのtensor
        :param b: type tensor biasのtensor
        :return: type tensor sigmoid  name scope の設定
        """
        i=1
        name="sigmoid"+str(self.step[i])
        with tf.name_scope(name):
            sigmoid = tf.nn.sigmoid(tf.matmul(x, w) + b)
            self.activaes.append(sigmoid)
        self.step[i]+=1
        return sigmoid

    def softmax(self,x,w,b):
        """
        :param x: type tensor 入力のtensor
        :param w: type tensor 重みのtensor
        :param b: type tensor biasのtensor
        :return: type tensor softmax  name scope の設定
        """
        i = 2
        name = "softmax" + str(self.step[i])
        with tf.name_scope(name):
            softmax = tf.nn.softmax(tf.matmul(x, w) + b)
            self.activaes.append(softmax)
        self.step[i] += 1
        return softmax

    def tanh(self,x,w,b):
        """
        :param x: type tensor 入力のtensor
        :param w: type tensor 重みのtensor
        :param b: type tensor biasのtensor
        :return: type tensor tanh  name scope の設定
        """
        i = 3
        name = "tanh" + str(self.step[i])
        with tf.name_scope(name):
            tanh = tf.nn.tanh(tf.matmul(x, w) + b)
            self.activaes.append(tanh)
        self.step[i] += 1
        return tanh

    def weight(self,dim,min=0,max=1,norm=False):
        """
        :param dim: type list　重みの次元　
        :return: type tensor 重みのtensor
        :todo : 重みのname scope を設定して重みを返す
        """
        i = 4
        name = "weight" + str(self.step[i])
        with tf.name_scope(name):
            if norm:
                w=tf.Variable(tf.truncated_normal(dim))
            else:
                w = tf.Variable(tf.random_uniform(dim, minval=min, maxval=max))

            self.weights.append(w)
        self.step[i] += 1
        return w

    def bias(self,dim,min=0,max=1,zeros=False):
        """
        :param dim: type list　biasの次元　
        :return: type tensor biasのtensor
        :todo : biasのname scope を設定してbiasを返す
        """
        i = 5
        name = "bias" + str(self.step[i])
        with tf.name_scope(name):
            if zeros:
                b= tf.Variable(tf.zeros(dim))
            else:
                b = tf.Variable(tf.random_uniform(dim, minval=min, maxval=max))

            self.biases.append(b)
        self.step[i] += 1
        return b

    def mape(self,x,label):
        """
        :param x: 　　推測データ
        :param label: 正解データ
        :return: type tensor loss
        :todo : MAPE=100/n*sum(abs((x-label)/label))
        """
        i = 6
        name = "mape" + str(self.step[i])
        with tf.name_scope(name):
            loss=tf.reduce_mean(tf.abs(tf.divide(tf.subtract(x,label),label)))
            self.losses.append(loss)
        self.step[i] += 1
        return loss

    def logloss(self,x,label):
        """
        :param x: 　　推測データ
        :param label: 正解データ
        :return: type tensor loss
        :todo : logloss=1/n*sum(label*x)
        """
        i = 7
        name = "logloss" + str(self.step[i])
        with tf.name_scope(name):
            loss =tf.losses.log_loss(label,x)
            self.losses.append(loss)
        self.step[i] += 1
        return loss

    def mse(self,x,label):
        """
        :param x: 　　推測データ
        :param label: 正解データ
        :return: type tensor loss
        :todo : 二乗平均誤差=1/n*sum((lx-label)**2)
        """
        i = 8
        name = "mse" + str(self.step[i])
        with tf.name_scope(name):
            loss =tf.reduce_mean(tf.square(tf.subtract(x,label)))
            self.losses.append(loss)
        self.step[i] += 1
        return loss



    def adam(self,loss,rate=1e-3):
        """
        :param loss:type tensor loss
        :return: type tensor Adam Optimizer
        """
        i = 9
        name = "adam" + str(self.step[i])
        with tf.name_scope(name):
            opt=tf.train.AdamOptimizer(rate).minimize(loss)
            self.opts.append(opt)
        self.step[i] += 1
        return opt

    def placeholder(self,name):
        """
        :param name: type str　name scope
        :return: type tensor placeholser
        :todo : placeholserのname scope を設定してplaceholderを返す
        """

        with tf.name_scope(name):
            x=tf.placeholder(tf.float32)
            self.x.append(x)

        return x

    def matmul(self,x,w,b):
        """
        :param x: type tensor 入力のtensor
        :param w: type tensor 重みのtensor
        :param b: type tensor biasのtensor
        :return: type tensor  relu　name scope の設定
        """
        i = 10
        name = "matmul" + str(self.step[i])
        with tf.name_scope(name):
            matmul= tf.matmul(x, w) + b
            self.activaes.append(matmul)
        self.step[i] += 1
        return matmul

    def sse(self,x,label):
        """
        :param x: 　　推測データ
        :param label: 正解データ
        :return: type tensor loss
        :todo : 二乗誤差和=sum((lx-label)**2)
        """
        i = 11
        name = "mse" + str(self.step[i])
        with tf.name_scope(name):
            loss =tf.reduce_sum(tf.square(x-label))
            self.losses.append(loss)
        self.step[i] += 1
        return loss


