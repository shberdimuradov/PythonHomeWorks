import math, json, csv, os

class Vector:
    def __init__(self, *c): self.c = tuple(c)
    def __str__(self): return f"Vector{self.c}"
    def __check(self, o):
        if not isinstance(o, Vector) or len(self.c)!=len(o.c): raise ValueError
    def __add__(self, o): self.__check(o); return Vector(*[a+b for a,b in zip(self.c,o.c)])
    def __sub__(self, o): self.__check(o); return Vector(*[a-b for a,b in zip(self.c,o.c)])
    def __mul__(self, o): return sum(a*b for a,b in zip(self.c,o.c)) if isinstance(o,Vector) else Vector(*[a*o for a in self.c])
    __rmul__=__mul__
    def magnitude(self): return math.sqrt(sum(x*x for x in self.c))
    def normalize(self): m=self.magnitude(); return Vector(*[x/m for x in self.c]) if m else Vector(*self.c)

class Employee:
    def __init__(self,id,name,pos,sal): self.id,self.name,self.pos,self.sal = id,name,pos,sal
    def __str__(self): return f"{self.id}, {self.name}, {self.pos}, {self.sal}"

class EmployeeManager:
    def __init__(self,f='employees.txt'): self.f=f
    def _read(self):
        if not os.path.exists(self.f): return []
        with open(self.f) as f: return [Employee(*line.strip().split(', ')) for line in f]
    def _write(self,emps):
        with open(self.f,'w') as f: [f.write(f"{e}\n") for e in emps]
    def add(self,e):
        emps=self._read()
        if any(x.id==e.id for x in emps): return
        with open(self.f,'a') as f: f.write(f"{e}\n")
    def view(self): return self._read()
    def find(self,id): return next((e for e in self._read() if e.id==id),None)
    def update(self,id,**kw):
        emps=self._read()
        for e in emps:
            if e.id==id:
                for k,v in kw.items(): setattr(e,k,v)
        self._write(emps)
    def delete(self,id): self._write([e for e in self._read() if e.id!=id])
    def menu(self):
        while True:
            print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
            c=input("Choice:")
            if c=='1': self.add(Employee(input(),input(),input(),input()))
            elif c=='2': [print(e) for e in self.view()]
            elif c=='3': print(self.find(input()))
            elif c=='4': self.update(input(),**{i: input() for i in['name','pos','sal']})
            elif c=='5': self.delete(input())
            elif c=='6': break

class Task:
    def __init__(self,id,title,desc,due='',status='Pending'):
        self.id,self.title,self.desc,self.due,self.status = id,title,desc,due,status
    def __str__(self): return f"{self.id}, {self.title}, {self.desc}, {self.due}, {self.status}"
    def to_dict(self): return self.__dict__

class Storage:
    def save(self,tasks): pass
    def load(self): return []

class JSONStorage(Storage):
    def __init__(self,f='tasks.json'): self.f=f
    def save(self,t): json.dump([x.to_dict() for x in t],open(self.f,'w'))
    def load(self): return [Task(**d) for d in json.load(open(self.f))] if os.path.exists(self.f) else []

class CSVStorage(Storage):
    def __init__(self,f='tasks.csv'): self.f=f
    def save(self,t):
        with open(self.f,'w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=t[0].to_dict().keys()); w.writeheader(); w.writerows(x.to_dict() for x in t)
    def load(self): return [Task(**r) for r in csv.DictReader(open(self.f))] if os.path.exists(self.f) else []

class TaskManager:
    def __init__(self,s): self.s=s; self.tasks=s.load()
    def add(self,t): self.tasks.append(t)
    def view(self): return self.tasks
    def update(self,id,**kw):
        for t in self.tasks:
            if t.id==id:
                for k,v in kw.items(): setattr(t,k,v)
    def delete(self,id): self.tasks=[t for t in self.tasks if t.id!=id]
    def filter(self,st): return [t for t in self.tasks if t.status==st]
    def save(self): self.s.save(self.tasks)

if __name__=='__main__':
    print("Select:1.Employee 2.To-Do 3.Vector Demo")
    m=input()
    if m=='1': EmployeeManager().menu()
    elif m=='2':
        fmt=input("json/csv:")
        s=JSONStorage() if fmt=='json' else CSVStorage()
        tm=TaskManager(s)
        while True:
            print("1.Add 2.View 3.Update 4.Delete 5.Filter 6.Save 7.Exit")
            c=input("Choice:")
            if c=='1': tm.add(Task(input(),input(),input(),input(),input()))
            elif c=='2': [print(t) for t in tm.view()]
            elif c=='3': tm.update(input(),**{i:input() for i in['title','desc','due','status']})
            elif c=='4': tm.delete(input())
            elif c=='5': [print(t) for t in tm.filter(input())]
            elif c=='6': tm.save()
            elif c=='7': tm.save(); break
    else:
        v1=Vector(1,2,3); v2=Vector(4,5,6)
        print(v1+v2, v2-v1, v1*v2, 3*v1, v1.magnitude(), v1.normalize())
