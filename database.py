from sqlalchemy import create_engine#this is used to create a engine
from sqlalchemy.orm import declarative_base,sessionmaker
# declarative_base:this is to recognize classes as tables
#sessionmaker is used to create the sessions
db_url='sqlite:///./EmployeeManagement.db'
#./ is used to create a Database in current working directory
engine=create_engine(db_url)
#now lets take a step for tables
Base=declarative_base()
#creating sessions
SessionLocal=sessionmaker(bind=engine)