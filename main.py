from fastapi import FastAPI,Depends,Path
from typing import Optional
from database import Base,SessionLocal,engine
from sqlalchemy.orm import Session
import models
#creation of app
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
#creating a method for reading all employees
@app.get('/allEmp')
def read_all(db:Session=Depends(get_db)):
    user_list=db.query(models.Employee).all()
    return user_list
#printing a sepcific department
@app.get('/filtering/{dept}')
def filtering(dept:str=Path(description='Enter Employee Department'),db:Session=Depends(get_db)):
    user_list=db.query(models.Employee).filter(models.Employee.Department==dept).all()
    return user_list
#incrementing  salary for dept==HR by 5000
@app.put('/update')
def update(db: Session = Depends(get_db)):
    db.query(models.Employee)\
      .filter(models.Employee.Department == 'HR')\
      .update({
          models.Employee.salary: models.Employee.salary + 5000
      })
    db.commit()
    return {"message": "Updated Successfully"}
@app.delete('/delete/{sal}')
def delete(sal:int=Path(description='Enter a salary to delete the record'),db:Session=Depends(get_db)):
    db.query(models.Employee).filter(models.Employee.salary<sal).delete()
    db.commit()#it saves the changes
    return {"message": "Deleted Successfully"}
