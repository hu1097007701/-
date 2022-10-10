# -*- coding: utf-8 -*-
from NetworkBuilder import *
from Visualization import *
#1.1. 实现函数 init_node()，从数据文件中加载所有节点及其属性；
dic=node.init_node(r'C:\Users\lenovo 13pro\Desktop\large_twitch_features.csv')
#1.2. 实现函数 print_node()，利用 format 函数或 f-string，输出某节点的属性
mature7=node.get_mature(7,dic)#（以第七个节点为例）
print("第7个节点的mature属性为：",mature7)
node.print_node(7,dic)
#2. 实现 graph.py 模块，实现图结构的序列化存储和加载。
G=graph.init_graph(dic,r'C:\Users\lenovo 13pro\Desktop\large_twitch_edges.csv')
#graph.save_graph(G)
#3. 实现 stat.py 模块，进行基础的统计分析
#3.1. 计算网络的节点数、边数、平均度等并返回
print("网络节点数：",stat.get_node_number(G))
print("网络边数：",stat.get_edge_number(G))
print("网络平均度：",stat.cal_average_dgree(G))
#3.2. 统计某个节点属性的分布(以affiliate为例)
affiliate_dic=stat.cal_affiliate_distribution(dic)
#绘制节点的属性分布，并提供结果的输出或文件保存（图片）
#度的分布图
dgree_dic=stat.cal_dgree_distribution(G)
plotgraph.plotdgree_distribution(dgree_dic)
#节点属性分布图(以affiliate为例)
plotnodes.plot_nodes_attr(affiliate_dic,'affiliate')