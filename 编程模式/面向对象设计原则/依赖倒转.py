from abc import ABC,abstractmethod

class IFileHandler(ABC):
    @abstractmethod
    def open(self,filename):
        pass

class TextProcessor:
    def __init__(self,file_handler:IFileHandler):
        self.file_handler = file_handler

    def open_file(self,filename):
        self.file_handler.open(filename)

class LocalFileHandler(IFileHandler):
    def open(self,filename):
        print(f'open {filename},use local file handler')


class CloudFileHandler(IFileHandler):
    def open(self,filename):
        print(f'open {filename},use cloud file handler')

text_processer = TextProcessor(LocalFileHandler())
text_processer.open_file('test.txt')

text_processer = TextProcessor(CloudFileHandler())
text_processer.open_file('test.txt')
