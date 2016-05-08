import tensorflow as tf
from tensorflow.contrib import skflow

# based on: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/skflow/text_classification.py

class GPUClassifier:
    EMBEDDING_SIZE = 50
    N_CLASSES = 10
    MAX_DOCUMENT_LENGTH = 133
    SPLIT_STEP = 10000

    def __init__(self, n_classes=10, split_step=10000, train_steps=1000, learning_rate=0.01):
        GPUClassifier.N_CLASSES = n_classes
        GPUClassifier.SPLIT_STEP = split_step
        self.classifier = skflow.TensorFlowEstimator(model_fn=self.rnn_model, n_classes=GPUClassifier.N_CLASSES,
                                                     steps=train_steps, optimizer='Adam', learning_rate=learning_rate,
                                                     continue_training=True)

    @staticmethod
    def rnn_model(X, y):
        """Recurrent neural network model to predict from sequence of words
        to a class."""
        # Convert indexes of words into embeddings.
        # This creates embeddings matrix of [n_words, EMBEDDING_SIZE] and then
        # maps word indexes of the sequence into [batch_size, sequence_length,
        # EMBEDDING_SIZE].
        word_vectors = skflow.ops.categorical_variable(X, n_classes=GPUClassifier.N_CLASSES,
                                                       embedding_size=GPUClassifier.EMBEDDING_SIZE, name='words')
        # Split into list of embedding per word, while removing doc length dim.
        # word_list results to be a list of tensors [batch_size, EMBEDDING_SIZE].
        word_list = skflow.ops.split_squeeze(1, GPUClassifier.MAX_DOCUMENT_LENGTH, word_vectors)
        # Create a Gated Recurrent Unit cell with hidden size of EMBEDDING_SIZE.
        cell = tf.nn.rnn_cell.GRUCell(GPUClassifier.EMBEDDING_SIZE)
        # Create an unrolled Recurrent Neural Networks to length of
        # max_document_length and passes word_list as inputs for each unit.
        _, encoding = tf.nn.rnn(cell, word_list, dtype=tf.float32)
        # Given encoding of RNN, take encoding of last step (e.g hidden size of the
        # neural network of last step) and pass it as features for logistic
        # regression over output classes.
        return skflow.models.logistic_regression(encoding, y)

    def fit(self, X, y):
        GPUClassifier.MAX_DOCUMENT_LENGTH = X.shape[1]
        for i in range(0, X.shape[0], GPUClassifier.SPLIT_STEP):
            if X.shape[0] - i > GPUClassifier.SPLIT_STEP:
                j = i + GPUClassifier.SPLIT_STEP - 1
            else:
                j = X.shape[0]
            self.classifier.partial_fit(X[i:j].toarray(), y[i:j])
        return self.classifier

    def predict(self, thing):
        thing = thing.toarray()
        return self.classifier.predict(thing)

    def save_classifier(self, file_location):
        return self.classifier.save(file_location)

    def load_classifier(self, file_location):
        self.classifier = skflow.TensorFlowEstimator.restore(file_location)
