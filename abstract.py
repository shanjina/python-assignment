from abc import ABC , abstractmethod
class shape(ABC):
   @abstractmethod
   def area():
      return 0
   def display(self):
      print("This is concrete method")
      
