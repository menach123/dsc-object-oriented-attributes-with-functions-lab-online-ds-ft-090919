class School():
    
    def __init__(self, name, roster= {}):
        self.name = name
        self.roster = roster
    def add_student(self, name, grade):
        try:
            self.roster[str(grade)].append(name)
        except:
            self.roster.update({str(grade) : [name]})
    def grade(self, a):
        return self.roster[str(a)]
    def sort_roster(self):
        a = []
        for i in self.roster.keys():
            a.append(int(i))
            a = sorted(a)
        reorder = {}
        for i in a:
            
            reorder[str(i)] = (self.roster[str(i)])
        return reorder