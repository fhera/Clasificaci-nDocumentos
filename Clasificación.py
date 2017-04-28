import pandas
import numpy
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors


class Clasificacion():
    def __init__(self,documento):
        self.documento = documento


    def __str__(self):
        return "La clasificación del documento con nombre {} es del tipo {}.".format(self.documento, self.tipo)

c = 