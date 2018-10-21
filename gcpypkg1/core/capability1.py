"""
Base core capability of this package
"""
from __future__ import division, absolute_import, print_function

class NN_Model(object):
  """
  Class of neural network to train using the training data
  After training, the model need to be validated using test data.

  # Return
  --------
    A 'model' object. This is a single hidden layer model.

  # Parameters
  ------------
    X_train : array of training data (inputs)
        NumPy array [N, 784] of float.
    Y_train : array of labels
        NumPy array [N, 1] of float.
    epoch : integer
        Number of epoch to train the model.
    batch_size : integer or 'None'
        Number of samples per gradient update.
        If unspecified, `batch_size` will default to 32.

  # Raises
    RuntimeError: If the model was never compiled.
    ValueError: In case of mismatch between the provided input data
      and what the model expects.

  # See Also
  ----------
    CNN_Model, RNN_Model

  # Examples
  ----------
    >>> model = NN_Model((X_train, Y_train), 100, 50)

  """

  model = None

  def __init__(self, X_train, Y_train, epoch, batch_size):
    self.model = None
    print('__init__ capability1 NN_Model...')
    return self.model

  def train(self):
    if self.model is None:
      raise RuntimeError('Model has not bee created')
    model = None  # TODO

  def validate(self):
    if self.model is None:
      raise RuntimeError('Model has not bee created')


