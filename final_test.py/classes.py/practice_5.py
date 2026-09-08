# Create Employee and Manager classes, where Manager inherits from Employee and adds a team list
# plus an add_team_member() method.
class Employee :
    pass
    
class Manager(Employee):
    def __init__(self,teamlist):
        self.teamlist = teamlist

    def add_team_member(self,member) :
        self.teamlist.append(member)
        return self.teamlist

emp = Employee()
man = Manager(["Ali","Zara","Maria"])
print(man.add_team_member("Ria"))