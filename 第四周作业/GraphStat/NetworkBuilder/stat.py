## -*- coding: utf-8 -*-

#import graph
import networkx as nx
import numpy as np
import csv
import matplotlib.pyplot as plt 	
#计算节点数
def get_node_number(G):
    G.order()
    return G.number_of_nodes()
#计算边数
def get_edge_number(G):
    G.size()
    return G.number_of_edges()
#计算网络中的平均度
def cal_average_dgree(G):
    sum_dgree=0
    num=0
    for i in G.degree:
        sum_dgree += i[1]
        num+=1
    return sum_dgree/num
#计算网络的度分布
def cal_dgree_distribution(G):
    num=G.number_of_nodes()
    dgree_dic={}
    for i in G.degree:
        if i[1] in dgree_dic:
            dgree_dic[i[1]]+=1
        else:
            dgree_dic[i[1]]=1
    for key in dgree_dic:
        dgree_dic[key]=dgree_dic[key]/num
    return dgree_dic

#计算 views 属性的分布
def cal_views_distribution(dic):
    dic_shuxing={}
    for key in dic:
        if dic[key][0] in dic_shuxing:
            dic_shuxing[dic[key][0]]+=1
        else:
            dic_shuxing[dic[key][0]]=1
    for key in dic_shuxing:
        dic_shuxing[key]=dic_shuxing[key]/len(dic)
    return dic_shuxing
#计算 mature 属性的分布
def cal_mature_distribution(dic):
    dic_shuxing={}
    for key in dic:
        if dic[key][1] in dic_shuxing:
            dic_shuxing[dic[key][1]]+=1
        else:
            dic_shuxing[dic[key][1]]=1
    for key in dic_shuxing:
        dic_shuxing[key]=dic_shuxing[key]/len(dic)
    return dic_shuxing 
#计算 life_time 属性的分布
def cal_life_time_distribution(dic):
    dic_shuxing={}
    for key in dic:
        if dic[key][2] in dic_shuxing:
            dic_shuxing[dic[key][2]]+=1
        else:
            dic_shuxing[dic[key][2]]=1
    for key in dic_shuxing:
        dic_shuxing[key]=dic_shuxing[key]/len(dic)
    return dic_shuxing 
#计算 affiliate 属性的分布
def cal_affiliate_distribution(dic):
    dic_shuxing={}
    for key in dic:
        if dic[key][7] in dic_shuxing:
            dic_shuxing[dic[key][7]]+=1
        else:
            dic_shuxing[dic[key][7]]=1
    for key in dic_shuxing:
        dic_shuxing[key]=dic_shuxing[key]/len(dic)
    return dic_shuxing 


#    
#dic=node.init_node(r'C:\Users\lenovo 13pro\Desktop\ceshi.csv')
#G=graph.init_graph(dic,r'C:\Users\lenovo 13pro\Desktop\hu.csv')
#c=cal_dgree_distribution(G)
#plot_ego(G,2)
