class Contact():
  def __init__(self,name,number,email):
    self.name = name
    self.number = number
    self.email = email
  def __repr__(self):
    return "Name: " + self.name + "\n" + "\tNumber: " + self.number + "\n" + "\tEmail: " + self.email + "\n"
  