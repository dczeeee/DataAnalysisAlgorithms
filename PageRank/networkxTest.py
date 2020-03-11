import networkx as nx

# 创建有向图
G = nx.DiGraph()
# 创建边
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
for edge in edges:
    G.add_edge(edge[0], edge[1])
# pagerank
pagerank_list = nx.pagerank(G, alpha=1)
print("pagerank值是：", pagerank_list)

