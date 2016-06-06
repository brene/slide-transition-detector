from abc import ABCMeta, abstractmethod


class Source(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def contents(self):
        pass


class ListSource(Source):
    def __init__(self, list):
        self.list = list

    def contents(self):
        return self.list

    def __len__(self):
        return len(self.contents())


class AnalyzerSource(Source):
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def contents(self):
        for content in self.analyzer.analyze():
            yield content

    def __len__(self):
        return 10000000000000000