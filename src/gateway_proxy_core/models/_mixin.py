class ModelNameStrTrainMixin:
    def __str__(self):
        return f"<{self.__class__.__name__}({self.pk}):{self.name}>"

    def __repr__(self):
        return self.__str__()