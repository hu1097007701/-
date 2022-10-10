import pandas as pd
def init_node(filename):
    f1=pd.read_csv(filename,encoding='UTF-8')
    keys=list(f1['numeric_id'])
    value=zip(f1['views'],f1['mature'],f1['life_time'],f1['created_at'],f1['updated_at'],f1['dead_account'],f1['language'],f1['affiliate'])
    dic=dict(zip(keys,value))
    return dic

def get_views(node,dic):
    return dic[node][0]

def get_mature(node,dic):
    return dic[node][1]

def get_life_time(node,dic):
    return dic[node][2]

def get_created_at(node,dic):
    return dic[node][3]

def get_updated_at(node,dic):
    return dic[node][4]

def get_dead_account(node,dic):
    return dic[node][5]

def get_language(node,dic):
    return dic[node][6]

def get_affiliate(node,dic):
    return dic[node][7]

def print_node(node,dic):
    print('id:',node)
    print('views: {0[0]}\nmature: {0[1]}\nlife_time: {0[2]}\ncreated_at: {0[3]}\nupdated_at: {0[4]}\ndead_account: {0[5]}\nlanguage: {0[6]}\naffiliate: {0[7]}'.format(dic[node]))
       

#dic=init_node(r'C:\Users\lenovo 13pro\Desktop\ceshi_features.csv')
#print_node(1,dic)




    

