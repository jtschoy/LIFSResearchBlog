---
layout: post
title: "Paper Review: Event Extraction for Criminal Legal Text"
author: 2023jinheon
icon: star-o
tags: [research, paper, event extraction]
---

## Introduction

The paper discusses the growing accessibility of legal documents and related judicial data to the public, as well as the potential for leveraging this data for intelligent legal services and judgment assistance. It highlights the challenges posed by the vague and ambiguous language often used in legal documents, which makes applying event extraction technology to legal text difficult. To address this issue, the paper proposes a comprehensive event extraction approach that focuses on larceny cases in Chinese legal text.

Furthermore, it emphasizes the significance of document disclosure for the legal institution, the public, and society, and explores the potential application of big data technology in the legal field.

## Related Work

The paper reviews related research on the application of event extraction technology across various domains, such as news articles, biomedical literature, and social media. It underscores the specific challenges encountered when applying event extraction technology to legal text due to the intricacies and ambiguity of legal language. The paper also highlights the importance of event extraction in the legal domain, as it can aid legal professionals in evaluating and judging cases.

The proposed event extraction approach for larceny cases in Chinese legal text encompasses data acquisition and annotation, deep learning model training, testing, and adjustment, as well as visualizing the extraction results. it also acknowledges the significance of document disclosure and the potential of big data technology in the legal realm.

## Approach

The approach presented in the paper focuses on a comprehensive event extraction method for larceny cases in Chinese legal text. The process involves data acquisition and annotation, training deep learning models, testing and fine-tuning, and visualizing the extracted events. The event extraction task for larceny cases is divided into two steps: jointly extracting trigger words and arguments, and assigning event argument roles.

The first step utilizes BERT to obtain Chinese character vectors and employs the BiLSTM-CRF model for extraction. In the second step, additional features are combined with the results from the first step and fed into the CRF model to further improve extraction accuracy.

The paper demonstrates the extracted event information in a time series format to achieve litigation visualization. This involves formatting Chinese time expressions, sorting the event information chronologically, and developing a web application to display the event timeline.

## Experiments

The paper conducts experiments to evaluate the proposed event extraction approach for larceny cases in Chinese legal text, using the CAIL 2018 dataset and criminal case texts from news websites. Performance evaluation is based on precision, recall, and F1-score metrics, comparing the proposed approach with other state-of-the-art event extraction methods.

The results show that the proposed approach outperforms other methods in terms of precision, recall, and F1-score. The paper also validates the effectiveness of the proposed approach in visualizing extracted event information in a time series format.

## Conclusion

In conclusion, the paper establishes the effectiveness of the proposed event extraction approach for larceny cases in Chinese legal text, surpassing other state-of-the-art methods in performance. The approach demonstrates accurate extraction of event information from unstructured and narrative-rich Chinese legal text, and successfully visualizes the extracted events in a time series format.

The paper also identifies and addresses the issue of imbalanced label distribution in the dataset, proposing a solution inspired by the two-labeling model. Finally, the paper suggests that the proposed approach can be extended to other types of legal text, thereby enhancing the efficiency and accuracy of legal work.