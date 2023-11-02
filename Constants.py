import pandas as pd
import os
import tensorflow as tf


MAX_FEATURES = 100000
sequence_length = 1500
batch_size = 32
seed = 1000
AUTOTUNE = tf.data.AUTOTUNE
VOCAB_SIZE = 1000

train = pd.read_csv("data/jigsaw-toxic-comment-classification/train.csv")
test = pd.read_csv("data/jigsaw-toxic-comment-classification/test.csv")
test_labels = pd.read_csv("data/jigsaw-toxic-comment-classification/test_labels.csv")
submissn = pd.read_csv("data/jigsaw-toxic-comment-classification/sample_submission.csv")

data_directory = os.path.join("data/jigsaw-toxic-comment-classification")