# -*- coding:utf-8 -*-
# 用 PageRank 挖掘希拉里邮件中的重要任务关系

import networkx as nx
import pandas as pd
from _collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

emails = pd.read_csv('./input/Emails.csv')
persons_file = pd.read_csv('./input/Persons.csv')
aliases_file = pd.read_csv('./input/Aliases.csv')

# 人名
persons = dict()
for index, row in persons_file.iterrows():
    persons[row['Id']] = row['Name']

# 别名
aliases = dict()
for index, row in aliases_file.iterrows():
    aliases[row['Alias']] = row['PersonId']


# 对别名进行转换
def unify_name(name):
    # 统一小写
    name = str(name).lower()
    # 去掉，和@后的内容
    name = name.replace(',', '').split('@')[0]
    # 别名转换
    if name in aliases.keys():
        return persons[aliases[name]]
    return name


# 画网络图
def show_graph(graph, layout='spring_layout'):
    # 使用 Spring Layout 布局，类似中心放射状
    if layout == 'circular_layout':
        positions = nx.circular_layout(graph)
    else:
        positions = nx.spring_layout(graph)
    # 设置网络图中的节点大小，大小与 pagerank 值相关，因为 pagerank 值很小所以需要 *20000
    nodesize = [x['pagerank'] * 20000 for v, x in graph.nodes(data=True)]
    # 设置网络图中的边长度
    edgesize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
    # 绘制节点
    nx.draw_networkx_nodes(graph, positions, node_size=nodesize, alpha=0.4)
    # 绘制边
    nx.draw_networkx_edges(graph, positions, edge_size=edgesize, alpha=0.2)
    # 绘制节点的 label
    nx.draw_networkx_labels(graph, positions, font_size=10)
    # 输出希拉里邮件中的所有人物关系图
    plt.show()


emails['MetadataTo'] = emails['MetadataTo'].apply(unify_name)
emails['MetadataFrom'] = emails['MetadataFrom'].apply(unify_name)

# 设置边的权重等于发邮件的次数
edges_weights_temp = defaultdict(list)
for row in zip(emails.MetadataFrom, emails.MetadataTo, emails.RawText):
    temp = (row[0], row[1])
    if temp not in edges_weights_temp:
        edges_weights_temp[temp] = 1
    else:
        edges_weights_temp[temp] = edges_weights_temp[temp] + 1

# 转化格式 (from, to), weight => from, to, weight
edges_weights = [(key[0], key[1], value) for key, value in edges_weights_temp.items()]
# 创建一个有向图
graph = nx.DiGraph()
# 设置有向图中的路径及权重 (from, to, weight)
graph.add_weighted_edges_from(edges_weights)
# 计算每个节点（人）的 PR 值，并作为节点的 pagerank 属性
pagerank = nx.pagerank(graph)

# 将 pagerank 数值作为节点的属性
nx.set_node_attributes(graph, name='pagerank', values=pagerank)
# 画网络图
show_graph(graph)

# 将完整的图谱进行精简
# 设置 PR 值的阈值，筛选大于阈值的重要核心节点
pagerank_threshold = 0.005
# 复制一份计算好的网络图
small_graph = graph.copy()
# 剪掉 PR 值小于 pagerank_threshold 的节点
for n, p_rank in graph.nodes(data=True):
    if p_rank['pagerank'] < pagerank_threshold:
        small_graph.remove_node(n)
# 画网络图,采用circular_layout布局让筛选出来的点组成一个圆
show_graph(small_graph, 'circular_layout')

