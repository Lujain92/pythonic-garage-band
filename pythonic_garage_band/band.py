from abc import ABC,abstractmethod


class Band:
    '''
    A class that contain an list for all instruments(gitar,drums,bass)
    '''
    instances=[]
    solos=[]
    def __init__(self,name,members=[]):
        self.name=name
        self.members=members
        Band.instances.append(self)
    def __len__(self):
        return    
    def __str__(self):
        return(f"this is the band {self.name}")
    def __repr__(self):
        return(f"formal band {self.name}")
    def play_solos(self):
        for member in self.members:
            Band.solos.append(member.play_solo())
        return Band.solos
    @classmethod    
    def to_list(cls):
        return Band.instances


class Musician(ABC):
    '''
    A parent class for Guitarist, Bassist, and Drummer.also it is an abstract has
    2 method that should the childs have it
    '''
    def __init__(self,name):
        self.name=name
    @abstractmethod    
    def get_instrument(self):
        pass
    @abstractmethod
    def play_solo(self):
        pass
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
    
class Guitarist(Musician):
    '''
    A child class from Musician that has 2 method that must have it from parent  
    '''
    def __init__(self,name):
        super().__init__(name)
    def get_instrument(self):
        return("guitar")
    def play_solo(self):
        return("face melting guitar solo")


class Bassist(Musician):
    '''
    A child class from Musician that has 2 method that must have it from parent  
    '''
    def __init__(self,name):
        super().__init__(name)
    def get_instrument(self):
        return("bass")
    def play_solo(self):
        return("bom bom buh bom")
class Drummer(Musician):
    '''
    A child class from Musician that has 2 method that must have it from parent  
    '''
    def __init__(self,name):
        super().__init__(name)
    def get_instrument(self):
        return("drums")
    def play_solo(self):
        return("rattle boom crash")   
