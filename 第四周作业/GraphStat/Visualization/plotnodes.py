## -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
def plot_nodes_attr(dic,shuxing):
    if shuxing == 'views':
        plt.rcParams['font.sans-serif'] = ['SimHei'] #解决图表中中文显示问题
        plt.xlabel('views')
        plt.ylabel('分布')
        plt.title('views的分布')
        x=dic.keys()
        y=dic.values()
        plt.bar(x,y)
        plt.show()
    elif shuxing == 'mature':
        plt.rcParams['font.sans-serif'] = ['SimHei'] #解决图表中中文显示问题
        plt.xlabel('mature')
        plt.ylabel('分布')
        plt.title('mature的分布')
        x=dic.keys()
        y=dic.values()
        plt.bar(x,y)
        plt.show()
    elif shuxing == 'life_time':
        plt.rcParams['font.sans-serif'] = ['SimHei'] #解决图表中中文显示问题
        plt.xlabel('life_time')
        plt.ylabel('分布')
        plt.title('life_time的分布')
        x=dic.keys()
        y=dic.values()
        plt.bar(x,y)
        plt.show()     
    elif shuxing == 'affiliate':
        plt.rcParams['font.sans-serif'] = ['SimHei'] #解决图表中中文显示问题
        plt.xlabel('affiliate')
        plt.ylabel('分布')
        plt.title('affiliate的分布')
        x=dic.keys()
        y=dic.values()
        plt.bar(x,y)
        plt.show() 
    else:
        print('Error input')