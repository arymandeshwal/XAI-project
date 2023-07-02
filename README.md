# EXPLAINABILITY FRAMEWORK FOR MOVIELENS GRAPH

[Installation](#installation) | [Dataset](#dataset) | [Description](#description) |  [PyG Example](https://github.com/rusty1s/pytorch_geometric/blob/master/examples/upfd.py)  | [DGL Example](https://github.com/dmlc/dgl/blob/master/python/dgl/data/fakenews.py)   | [Benchmark](https://paperswithcode.com/dataset/upfd) | [Intro Video](https://youtu.be/QAIVFr24FrA) | [How to Contribute](#how-to-contribute)

This project focuses on enhancing the explainability of Graph Neural Networks (GNNs) in the context of link prediction using a heterogeneous graph. GNNs have proven effective in various applications, including link prediction tasks. The objective of this study is to develop an interpretable GNN model that provides explanations for individual edges in the graph.


## Installation

1. [Install Pytorch](https://pytorch.org/get-started/locally/) 
2. Install Pytorch_geometric from master branch
```bash
pip install git+https://github.com/pyg-team/pytorch_geometric.git
```
3. [Install Pytorch_geometric](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html)


## Dataset
We are using MovieLens dataset consisted of movie ratings, which we represented as a heterogeneous graph. It includes diverse information, including movie ratings, user profiles, genre details, and movie metadata.

The dataset have 610 unique users and a movie features with 20 columns, encompassing genres like Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Sci-Fi, Thriller.

The statistics of the dataset is shown below:

| Data  | Graphs  |
|-------|--------|
| Number of nodes | 10,334  |  
| Number of edges | 100,836  |   


## Description




## How to Contribute
