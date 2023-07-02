# EXPLAINABILITY FRAMEWORK FOR MOVIELENS GRAPH

[Project Overview](#project-overview) | [Installation](#installation) | [Data Description](#data-description) |  [Model Architecture](#model-architecture) | [Explainability Techniques](#explainability-techniques) | [Contribution](#contribution)

## Project Overview

This project focuses on enhancing the explainability of Graph Neural Networks (GNNs) for link prediction using a heterogeneous graph. The approach involves training a GNN model on the MovieLens dataset, utilizing the GNN explainer technique to provide insights into individual link predictions, and employing a surrogate model for validation. The results demonstrate improved interpretability and trust in the GNN's predictions, contributing to the field of explainable GNNs and facilitating better decision-making in link prediction tasks.

## Installation

1. [Install Pytorch](https://pytorch.org/get-started/locally/) 
2. Install Pytorch_geometric from master branch
```bash
pip install git+https://github.com/pyg-team/pytorch_geometric.git
```
3. [Install Pytorch_geometric](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html)


## Data Description
We are using MovieLens dataset consisted of movie ratings, which we represented as a heterogeneous graph. It includes diverse information, including movie ratings, user profiles, genre details, and movie metadata.

The dataset have 610 unique users and a movie features with 20 columns, encompassing genres like Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Sci-Fi, Thriller.

The statistics of the dataset is shown below:

| Data  | Graphs  |
|-------|--------|
| Number of nodes | 10,334  |  
| Number of edges | 100,836  |   


## Model Architecture
## Explainability Techniques
## Contribution
