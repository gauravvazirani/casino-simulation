import math

class  IntegerStatistics(list):
    """
    An extension of the built in list data structure that stores 
    at hand mehtods to calculate the mean and standard deviation of the elements
    """
    def mean(self):
        """
        :return: (decimal) mean of the list elements
        """
        return sum(self)/len(self)

    def stdev(self):
        """
        :return: (decimal) standard deviation of the list elements
        """
        m = self.mean()
        return math.sqrt(sum((x-m)**2 for x in self)/(len(self)-1))
        