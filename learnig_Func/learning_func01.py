import pickle as pick
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from NeuralNetwork import NN
from time import sleep



class Model(NN):
    def __init__(self):
        super().__init__()
        self.sess=tf.InteractiveSession()


        self.histry=[]


    def create_model(self,hidden,output_size,data_size):
        """
        :param hidden: type list 隠れ層のパーセプトロンの数
        :param output_size: type int 出力の次元
        :param data_size: type int データのサイズ
        :return: None
        :todo : モデルを組み立てる
        """
        x=self.placeholder("x")
        label=self.placeholder("label")

        x_ = tf.reshape(x, [-1,data_size ])

        n1=self.sigmoid(x_,self.weight([data_size,hidden[0]]),self.bias([hidden[0]]))
        n2=self.sigmoid(n1,self.weight([hidden[0],hidden[1]]),self.bias([hidden[1]]))
        n3=self.relu(n2,self.weight([hidden[1],hidden[2]]),self.bias([hidden[2]]))
        n4=self.relu(n3,self.weight([hidden[2],hidden[3]]),self.bias([hidden[3]]))

        out=self.matmul(n4,self.weight([hidden[3],output_size]),self.bias([output_size]))
        loss=self.sse(out,label)

        opt=self.adam(loss)

        self.x=x
        self.label=label
        self.out=out
        self.loss=loss
        self.opt=opt

        self.sess.run(tf.global_variables_initializer())

    def train_model(self,x,label):
        """
        :param x: 入力
        :param label: 　正解データ
        :return: None
        :todo : モデルの学習
        """
        train_opt=self.sess.run(self.opt,feed_dict={self.x:x,self.label:label})
        return train_opt


    def predict(self,x):
        """
        :param x: 入力
        :return: predict
        :todo : predictの計算
        """
        out=self.sess.run(self.out,feed_dict={self.x:x})
        return out

    def get_loss(self,x,label):
        """
        :param x: 入力
        :param label: 　正解データ
        :return: loss
        :todo : loss の計算
        """
        loss=self.sess.run(self.loss,feed_dict={self.x:x,self.label:label})
        return loss

    def save_model(self,path):
        """
        :param path: graph を保存する場所
        :return: None
        :todo : graph保存する
        """
        self.saver = tf.train.Saver()
        self.saver.save(self.sess,path)

def func(x):

    return np.sin(x)+1+0.5*np.cos(x)+0.2*np.sin(x)+ np.random.randn(x.size)/3




Epoch=1000000
hidden=[5,5,10,5]
dim=1

model=Model()
model.create_model(hidden,dim,dim)

fig, ax = plt.subplots(1, 1)
x_ =np.arange(0,6,0.02)# np.arange(-np.pi, np.pi, 0.001)
y_ =func(x_)
dataset = np.vstack((x_, y_))
idx = np.random.choice(300,120)     # ランダムに作成したデータから一部を選択
idx.sort()
dataset_mini = dataset[0: , idx]
x =np.reshape(x_,[-1,1])# dataset_mini[0].reshape(120,1)
y =np.reshape(y_,[-1,1]) #dataset_mini[1].reshape(120,1)
p=model.predict(x)
ax.plot(x, y,color=(0,0,1))
lines,=ax.plot(x,p,color=(1,0,0))

#sleep(10)

for i in range(Epoch):
    model.train_model(x, y)

    if i % 100 == 0:
        print("Epoch : ", i)
        p = model.predict(x)
        lines.set_data(x, y)
        lines.set_data(x, p)



        loss = model.get_loss(x, y)
        print("------------------------------------------------------")
        print("loss : ", loss)
        print("------------------------------------------------------")

        ax.set_ylim((np.min([y.min(), p.min()]), np.max([y.max(), p.max()])))
        plt.pause(.01)








