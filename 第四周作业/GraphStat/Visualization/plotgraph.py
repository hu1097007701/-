## -*- coding: utf-8 -*-
#绘制节点的局部网络（找一些度大小合适的节点尝试。）
import networkx as nx
import matplotlib.pyplot as plt 
#度的分布图
def plotdgree_distribution(dgree_dic):
    figure = plt.figure()    
    plt.rcParams['font.sans-serif'] = ['SimHei'] #解决图表中中文显示问题
    plt.xlabel('度')
    plt.ylabel('分布')
    plt.title('度的分布')
    x=dgree_dic.keys()
    y=dgree_dic.values()
    plt.bar(x,y)
#    plt.hist(list(G.degree),color='pink',bins=100)
    plt.show()  
    
    

#l=list(G.degree[1])