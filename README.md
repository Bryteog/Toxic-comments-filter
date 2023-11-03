### Overview

Created a toxic comments filter, which detects and classifies comments as one or a combination of the following classes; toxic, severe_toxic, obscene, threat, insult and identity_hate. The dataset is obtained from the Toxic Comments challenge on [kaggle](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). The data directory contains a train file, with comments and associated labels, a test file with comments only a test_labels file with comment labels only and a sample submission file, all in csv format. Data analysis is done with the Pandas library.


#### Model
Text vectorisation is done to remove punctuation signs and assign embeddings to text with the Keras library.
The data is divided into three parts, training testing and validating sets. A bidirectional LSTM is used along with some dense layers. The last layer has 6 units with sigmoid activation as some of the comments can belong to more than one class.

The model is saved and later used in building a Gradio app which can be accessed [at](http://127.0.0.1:7860).
