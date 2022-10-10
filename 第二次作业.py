# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:03:50 2022

@author: lenovo 13pro
"""

import jieba
import re  
import matplotlib.pyplot as plt  
import numpy as np 

#去掉重复词条
def delete_same(filename):
    a=0
    file_in = open(filename,'r',encoding='utf-8')   
    file_out=open('C:\\Users\\lenovo 13pro\\Desktop\\delete_same.txt','a',encoding='utf-8')

    lines_seen = set()
    for i in range(10000):
        w = file_in.readline()
        if w not in lines_seen:	#如果从源文档中读取的内容不在目标文档中则写入，否则跳过，实现去除重复功能
             a += 1
             file_out.write(w)
             lines_seen.add(w)
    file_out.close()         
    file_in.close()
    print("delet_same success\n")
    

#加入jieba自定义字典
def add_dic(filename):
    jieba.load_userdict(filename)


#清洗评论 去除噪声
def clean_word(filename):   
    file_in = open(filename,'r',encoding='utf-8')    
    for i in range(1000):
        text = file_in.readline()
        if '分享图片' in text:
           continue
        text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
        text = re.sub(r"\[\S+\]", "", text)      # 去除表情符号
        text = re.sub(r"【\S+\】", "", text)      # 去除【】内容
        text = re.sub(r"\S+\.0","",text)     #去除用户id
        URL= re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',re.IGNORECASE)
        text = re.sub(URL, "", text)       # 去除网址
        text = text.replace("我在:", "")       # 去除无意义的词语
        text = text.replace("我在这里:","") # 去除无意义的词语
        text = re.sub(r"\s+", " ", text) # 合并空格

        file_out= open('C:\\Users\\lenovo 13pro\\Desktop\\cleanword.txt','a',encoding='utf-8')
        file_out.write(text+'\n')
    print("clean_word success\n")

#将情绪词语导入字典
def emo_to_dic(filename,dic):
    file = open(filename,'r',encoding='utf-8')
    dic.append([line.strip() for line in file.readlines()])
    file.close()
    return dic

#构造闭包 确定评论情绪 并获取时间地点
def emodic(filename):
    #将五种情绪词加入情绪字典   
    edic=[]
    edic=emo_to_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\anger.txt",edic)
    edic=emo_to_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\disgust.txt",edic)
    edic=emo_to_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\fear.txt",edic)
    edic=emo_to_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\joy.txt",edic)
    edic=emo_to_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\sadness.txt",edic)

    def splitword():  
        nonlocal edic
        emotion_list,time_list,address_list=[],[],[]
        with open(filename,'r',encoding='utf-8') as f:
            txt = f.readlines()
            for line in txt:
                sline = line.strip().split(' ')
                address = ''.join(sline[0:2])#获取地址
                time=sline[-6:-2]#获取时间
                sentence = ''.join(sline[2:-6])#获取评论语句
                #对每条语句进行情绪词统计
                emotion_dict = {'anger':0,'disgust':0,'fear':0,'joy':0,'sadness':0}
                splitword = jieba.lcut(sentence)
                for word in splitword:
                    if word in edic[0]:
                        emotion_dict['anger'] +=1
                    elif word in edic[1]:
                        emotion_dict['disgust'] +=1
                    elif word in edic[2]:
                        emotion_dict['fear'] +=1
                    elif word in edic[3]:
                        emotion_dict['joy'] +=1
                    elif word in edic[4]:
                        emotion_dict['sadness'] +=1
                       
                if max(emotion_dict.values())==0:#定义没有情绪的情况
                    emotion = 'no'
                else:
                    emotion = max(emotion_dict,key=emotion_dict.get)#选取最大值情绪作为该语句情绪 
                emotion_list.append(emotion)#储存语句情绪
                time_list.append(time)
                address_list.append(eval(address))
        print('splitword success')
        return emotion_list,time_list,address_list
    return splitword

#讨论不同时间情绪比例的变化趋势
def plot_time(emotion,time,emotion_list,time_list):
    if time == "month":
        month_dict={'Jan':0,'Feb':0,'Mar':0,'Apr':0,'May':0,'Jun':0,'Jul':0,'Aug':0,'Sep':0,'Oct':0,'Nov':0,'Dec':0}#建立月度情绪字典
        for i in range(len(time_list)):
            if emotion_list[i] == emotion:
                month_dict[time_list[i][1]] += 1; #各个月份该种情绪的数量                    
        x=list(month_dict.keys())
        y=list(month_dict.values())
        plt.plot(x,y)#绘制图像
        
    elif time == "week":
        week_dict={'Mon':0,'Tus':0,'Wed':0,'Ths':0,'Fri':0,'Sat':0,'Sun':0}
        for i in range(len(time_list)):
            if emotion_list[i] == emotion:
                week_dict[time_list[i][0]] += 1;                     
        x=list(week_dict.keys())
        y=list(week_dict.values())
        plt.plot(x,y)
      
    elif time == "hour":
        hour_dict={'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0}
        for i in range(len(time_list)):
            if emotion_list[i] == emotion:
                hour_dict[time_list[i][3][0:2]] += 1;                     
        x=list(hour_dict.keys())
        y=list(hour_dict.values())
        plt.plot(x,y)
        plt.show()
    
    else:
        print("Error input")
    
#讨论情绪的空间分布 r为半径
def emo_space(emotion_list,address_list,r):
    emo_dict={'sadness':0,'joy':0,'fear':0,'disgust':0,'anger':0}
    
    address_x,address_y=[],[]#分别位置获得横纵坐标的参数
    for i in range(len(address_list)):
        if(address_list[i][1]<117):
            address_x.append(address_list[i][0])
            address_y.append(address_list[i][1])
    center_x= np.mean(address_x)#取均值作为中心坐标
    center_y= np.mean(address_y)
    
    for i in range(len(address_x)):
        if emotion_list[i]!='no':
            dis=np.sqrt(np.square(center_x-address_x[i])+np.square(center_y-address_y[i]))#计算情绪与中心坐标之间的距离
            if dis <= r:
                emo_dict[emotion_list[i]] += 1
    
    x=list(emo_dict.values())
    y=list(emo_dict.keys())
    plt.pie(x,labels=y,autopct = '%3.2f%%')#绘制饼图反应情绪所占比例
    plt.show()

#定义主函数
def main():
    #将五种情绪词加入jieba自定义字典   
    add_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\anger.txt")
    add_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\disgust.txt")
    add_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\fear.txt")
    add_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\joy.txt")
    add_dic("C:\\Users\\lenovo 13pro\\Desktop\\emotion_lexicon\\sadness.txt")
    
    #去掉重复词条
    delete_same('C:\\Users\\lenovo 13pro\\Desktop\\weibo.txt')
        
    #清洗评论 去除噪声
    clean_word('C:\\Users\\lenovo 13pro\\Desktop\\delete_same.txt')
    
    #构造闭包 确定评论情绪
    f = emodic('C:\\Users\\lenovo 13pro\\Desktop\\cleanword.txt')
    emotion_list,time_list,address_list = f()
    
    #讨论不同时间情绪比例的变化趋势
    emotion = input('please enter the emotion:')
    time = input('please enter the time:')
    plot_time(emotion,time,emotion_list,time_list)
    
    #讨论情绪的空间分布    
    emo_space(emotion_list,address_list,0.11)


##调用主函数
#if __name__ == '__main__':
#    main()