import tensorflow as tf
import tensorflow.keras as keras

"""
Progress bar for displaying various process progress
"""
class ProgressBar:

    def __init__(self, length: int, message: str):
        self.length = length
        self.bar = '-'*length
        self.message = message
        self.frac = 0

    def update(self, frac: float):
        self.frac = 1 if frac > 1 else frac
        whole = int(self.frac * self.length)
        self.bar = '#'*whole + '-'*(self.length - whole)

    def display(self, suffix:str = ''):
        delim = '' if self.frac != 1.0 else '\n'
        print(f'\r{self.message}[{self.bar}] {suffix}', end=delim)

    def update_display(self, frac: float, suffix:str=''):
        self.update(frac)
        self.display(suffix)

"""
AUC for a single class to compile in each model (WIP, may not use at all)
"""
class MulticlassAUC_angry (keras.metrics.AUC):

    def __init__ (self, t_label, **kwargs):
        super().__init__(**kwargs)
        self.t_label = t_label

    def update_state (self, t_true, t_pred, **kwargs):
        t_true = tf.math.equal(t_true, self.t_label)
        t_true = tf.squeeze(t_true)

        t_pred = t_pred[..., self.t_label]
        
        super().update_state(t_true, t_pred, **kwargs)