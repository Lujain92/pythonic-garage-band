class Band:
    instances=[]
    def __init__(self,name,members=[]):
        self.name=name
        self.members=members
        Band.instances.append(self)
    def __len__(self):
        return    
    def play_solos(self):
        return(["face melting guitar solo","bom bom buh bom","rattle boom crash"])
    @staticmethod    
    def to_list():
        return Band.instances
class Musician:
    def __init__(self,name):
        self.name=name
    
class Guitarist(Musician,Band):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return(f"My name is {self.name} and I play guitar")
    def __repr__(self):
        return(f"Guitarist instance. Name = {self.name}")
    def get_instrument(self):
        return("guitar")
    def play_solo(self):
        return(self.play_solos()[0])


class Bassist(Musician,Band):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return(f"My name is {self.name} and I play bass")
    def __repr__(self):
        return(f"Bassist instance. Name = {self.name}")
    def get_instrument(self):
        return("bass")
    def play_solo(self):
        return(self.play_solos()[1])
class Drummer(Musician,Band):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return(f"My name is {self.name} and I play drums")
    def __repr__(self):
        return(f"Drummer instance. Name = {self.name}")
    def get_instrument(self):
        return("drums")
    def play_solo(self):
        return(self.play_solos()[2])   
