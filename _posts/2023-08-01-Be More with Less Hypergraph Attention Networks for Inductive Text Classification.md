---
layout: post
title: "[parer review] Be More with Less: Hypergraph Attention Networks for Inductive Text Classification"
author: 2022Gwang-jae
icon: star-o
tags: [paper review]
---
## 1. Indtoduction

문서 분류(text classification)에 GNN을 사용하면 성능은 좋으나, 두 가지의 한계점이 있다.
1) Expressive Power. GNN은 두 노드 간의 관계에만 초점을 맞추고 다중관계에 대해서는 다루지 않기 때문에 real-world를 표현하는데 한계가 있음.
2) Computational Consumption. 메모리 사용량의 과부하 때문에 transductive 학습을 하는데, 문서가 입력될때마다 학습을 해야하기 때문에 비효율적이다(transductive 학습은 그래프 내부에서 노드를 비워놓고, 노드를 찾는 학습 방법이다.)

따라서, 표현력도 상승시키면서 계산 효율성이 높은 모델이 필요하며 이를 hyperedge 개념으로 해결하고자한다.

## 3. Methodology

### - hyperedge
본 논문에서는 hyperedge라는 개념을 사용하여, 하나의 edge에 여러 노드가 포함될 수 있도록 하였다. 그 표현방식은 두가지 인데,
1) sequential hyperedges. 문서를 문장으로 나누어서, **그 문장에 포함하는 단어들을 모두 연결한다**
2) semantic hyperedge. LDA를 사용하여 문서를 토픽화 시키고 **top K 단어를 hyperedge로 간주한다.**
   

### - Attention Networks
학습 시 두가지 방식으로 학습을 하게 되는데,
1) node-level attention. 특정 hyperedge에 있는 모든 노드가 동등하게 기여하는 것이 아니기에 노드의 중요성을 강조하려고 attention mechanism을 사용한다**(이를 통해 가장 기여도가 높은 노드가 표현될 듯?)**
2) edge-level attention. 다음 레이어에서 노드를 학습하기 위한 hyperedge를 학습하기 위해 사용한다 **(노드 v에 대한 hyperedge의 기여도를 나타내는듯?)**

## 4. Experiments

의미있는 결과를 말하자면,
semantic보다는 sequential hyperedge가 더 중요한 역할을 한다. 
*w/o attention은 dual attention 대신 convolution으로 대체
**w/o sequential, w/o semantic은 각각 sequential, semantic hyperedge를 제외
![image](/img/news/230717_img1.png)

### - case study

Text-level GNN과 비교했을때 더 표현력이 좋다는 것을 알 수 있다(클래스 23개)

![image](/img/news/230717_img2.png)

실제 문장에다가 하이라이팅을 한 것으로,
처음 3개 문장은 sequential hyperedge, 마지막 문장은 semantic hyperedge를 나타낸다(파란색으로 구분).
주황색은 노드를 의미하며 가중치가 높을수록 진한색을 띈다.

![image](/img/news/230717_img3.png)


## discussion

본 논문의 코드를 살펴봐야하겠지만, sequential 혹은 semantic hyperedge를 구성요건 계층화에 맞춰서 학습을 해보려고 한다.