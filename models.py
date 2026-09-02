from database import Base,engine,SessionLocal
from sqlalchemy import Column,Integer,String
#these are necessary prequisites for model creation
class Employee(Base):
    __tablename__='Employee'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    Department=Column(String)
    salary=Column(Integer)
#now create all tables first
Base.metadata.create_all(engine)
session=SessionLocal()#creating a session object
#inserting data
e1=Employee(id=1,name='Alice',Department='IT',salary=50000)
e2=Employee(id=2,name='Bob',Department='HR',salary=40000)
e3=Employee(id=3,name='Carol',Department='IT',salary=60000)
e4=Employee(id=4,name='David',Department='Sales',salary=30000)
e5=Employee(id=5,name='Eva',Department='HR',salary=45000)
session.add_all([e1,e2,e3,e4,e5])#data addedto session
session.commit()