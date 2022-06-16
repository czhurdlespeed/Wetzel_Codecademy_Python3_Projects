class School:

  def __init__(self,name, level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def getName(self):
    return self.name
  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents
  def setNumberOfStudents(self,number):
    self.numberOfStudents = number
    
  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students".format(level=self.level,name=self.name,numberOfStudents=self.numberOfStudents)

class PrimarySchool(School):
  def __init__(self,name, numberOfStudents, pickupPolicy):
    super().__init__(name,'primary',numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def getPickupPolicy(self):
    return self.pickupPolicy
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup policy is {pickupPolicy}".format(pickupPolicy= self.pickupPolicy)

myprimary= PrimarySchool("Riverside",400,"by parents only")
print(myprimary.getPickupPolicy())
print(myprimary)

class HighSchool(School):
  def __init__(self,name,numberOfStudnets, sportsTeams):
    super().__init__(name,'high',numberOfStudnets) 
    self.sportsTeams = sportsTeams
  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    school_repr=super().__repr__()
    return school_repr + " offers athletics such as {sports}".format(sports= ', '.join(self.sportsTeams))
  
myHighschool=HighSchool("Riverside", 400, ["Track","Baseball","Basketball"])
print(myHighschool.getSportsTeams())
print(myHighschool)
