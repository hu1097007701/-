## -*- coding: utf-8 -*-
#graph.py
#def init_graph()（可以考虑用 networkx 中的 Graph 等。）
#构建网络
#def save_graph(graph):
#序列化图信息
#def load_graph(file): 将网络加载至内存

import networkx as nx
import matplotlib.pyplot as plt 		
import pandas as pd

def init_graph(dic,filename):
    G=nx.Graph() 
    G.add_nodes_from(list(dic.keys()))#添加节点
    
    f2 = pd.read_csv(filename,encoding='UTF-8')
    num1=list(f2['numeric_id_1'])
    num2=list(f2['numeric_id_2'])
    num=[]
    for i in range(len(num1)):
        num.append((num1[i],num2[i]))#将边提取成元组存入列表

    G.add_edges_from(num)#添加边
    return G

def save_graph(graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph,pos,with_labels = True,node_color = 'pink',node_size = 200)#绘制图像
    plt.savefig('gragh.svg', dpi=None)#储存图像
#    plt.show()


#dic=node.init_node(r'C:\Users\lenovo 13pro\Desktop\ceshi.csv')
#graph=init_graph(dic,r'C:\Users\lenovo 13pro\Desktop\hu.csv')
#save_graph(graph)