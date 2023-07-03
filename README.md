# EXPLAINABILITY FRAMEWORK FOR MOVIELENS GRAPH

[Project Overview](#project-overview) | [Installation](#installation) | [Execution](#execution) | [Data Description](#data-description) |  [Model Architecture](#model-architecture) | [Explainability Techniques](#explainability-techniques) | [Contribution](#contribution)

## Project Overview

This project focuses on enhancing the explainability of Graph Neural Networks (GNNs) for link prediction using a heterogeneous graph. The approach involves training a GNN model on the MovieLens dataset, utilizing the GNN explainer technique to provide insights into individual link predictions, and employing a surrogate model for validation. The results demonstrate improved interpretability and trust in the GNN's predictions, contributing to the field of explainable GNNs and facilitating better decision-making in link prediction tasks.

## Installation

1.First : [Install Pytorch](https://pytorch.org/get-started/locally/) 

2.Second: Install Pytorch_geometric from master branch
```bash
pip install git+https://github.com/pyg-team/pytorch_geometric.git
```
3.Third: [Install Pytorch_geometric](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html)

4.Fourth: Install Python dependencies from the requirements.txt file.
```bash
pip install -r requirements.txt
```
If you encounter any **ERROR** or the code is **NOT EXECUTABLE**. Please refer to this [Link](https://colab.research.google.com/drive/19gCLvZi77ih5hTSAjUbHISmX-I9fi12m?usp=sharing)

## Execution 
For execution of the project 
1. First execute : **Main.ipynb**
2. Secondly, execute : **Tabular form.ipynb**

## Data Description
If you install the project manually, you do not need to download the dataset 
We are using MovieLens dataset consisted of movie ratings, which we represented as a heterogeneous graph. It includes diverse information, including movie ratings, user profiles, genre details, and movie metadata.

The dataset have 610 unique users and a movie features with 20 columns, encompassing genres like Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Sci-Fi, Thriller.

The statistics of the dataset is shown below:

| Data  | Graphs  |
|-------|--------|
| Number of nodes | 10,334  |  
| Number of edges | 100,836  |   


## Model Architecture

The model architecture used in this project consists of a Graph Neural Network (GNN) for link prediction in a heterogeneous graph. 
The GNN encoder utilizes SAGEConv layers to aggregate information from neighboring nodes and learn node representations. 
The model employs a GNN explainer technique to provide explanations for individual link predictions. 
Additionally, a surrogate model (Random Forest) is used to compare and validate the explanations provided by the GNN explainer. 
This architecture enhances the interpretability and transparency of the GNN model.

## Explainability Techniques

In order to enhance the explainability of the Graph Neural Network (GNN) model for link prediction, two techniques were employed: 

### 1.GNN explainer
The GNN explainer technique attributed importance scores to nodes and edges, providing insights into the decision-making process of the GNN model at an individual edge level. This technique helped identify influential features and their relationships within the graph.

### 2.Using Random Forest for Explaination.
Using Random Forest was employed to validate and compare the explanations provided by the GNN explainer. The combination of these techniques facilitated a comprehensive understanding of the factors driving the predictions of the GNN model, enhancing its interpretability and transparency.

## Contribution

Amal and Aryman, played vital roles in the project's success. Amal excelled in meticulous data preprocessing and data analysis, ensuring the dataset's quality and engineering informative features. Meanwhile, Aryman focused on model development and training, demonstrating a deep understanding of GNNs and effectively utilizing the PyTorch and PyTorch Geometric libraries.
