from fastapi import FastAPI, Depends, Path, status, Response, Query
from typing import List, Optional
from fastapi_pagination import Page, add_pagination, paginate
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc

app = FastAPI() 

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# NOTE: Pagination, Sorting, Searching/Filtering is included in this API. 
@app.get("/all-data", response_model=Page[schemas.Planning])
def all_data(*,response: Response, db : Session = Depends(get_db), search: Optional[str] = Query(None, description="Search the talent name of the item you want you'd like to view"), sort: Optional[str] = Query(None, enum=["id", "originalId", "talentId", "talentName", "talentGrade", "bookingGrade", "operatingUnit", "officeCity", "officePostalCode", "jobManagerName", "jobManagerId", "totalHours", "startDate", "endDate", "clientName", "clientId", "industry", "isUnassigned"]), sort_dir: Optional[str]= Query(None, description="Select sorting direction e.g 'asc' or 'desc' (default asc)", enum=["asc", "desc"])):
    if search:
        planning_data =  db.query(models.Planning).filter(models.Planning.talentName.contains(search))
        if sort:
            planning_data = planning_data.order_by(sort).all()
        elif sort and sort_dir == "desc":
            planning_data = planning_data.order_by(desc(sort)).all()
        else:
            planning_data = planning_data.all()
    else:
        planning_data = db.query(models.Planning)
        if sort:
            planning_data = planning_data.order_by(sort).all()
        elif sort and sort_dir == "desc":
            planning_data = planning_data.order_by(desc(sort)).all()
        else:
            planning_data = planning_data.all()

    if not planning_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        
    for planning in planning_data:
        required_skills_lst = []
        required_skills_name_lst = []
        required_skills_cat_lst = []
        optional_skills_lst = []
        optional_skills_name_lst = []
        optional_skills_cat_lst = []
        
        if len(planning.requiredSkillsName.split(",")) >= 1 and planning.requiredSkillsName.split(",")[0] != '':
            required_skills_name_lst = planning.requiredSkillsName.split(",")
            required_skills_cat_lst = planning.requiredSkillsCategory.split(",")
        for n, c in zip(required_skills_name_lst, required_skills_cat_lst):
            # print(n,c)
            required_skills_lst.append({"name": n,"category": c})
        planning.requiredSkills = required_skills_lst
        if len(planning.optionalSkillsName.split(",")) >= 1 and planning.optionalSkillsName.split(",")[0] != '':
            optional_skills_name_lst = planning.optionalSkillsName.split(",")
            optional_skills_cat_lst = planning.optionalSkillsCategory.split(",")
        for n, c in zip(optional_skills_name_lst, optional_skills_cat_lst):
            # print(n,c)
            optional_skills_lst.append({"name": n,"category": c})
        planning.optionalSkills = optional_skills_lst
        del planning.requiredSkillsName
        del planning.requiredSkillsCategory
        del planning.optionalSkillsName
        del planning.optionalSkillsCategory

    return paginate(planning_data)

@app.get("/get-data-by-originalId/{originalId}", response_model = List[schemas.Planning])
def get_data_by_originalId(*,originalId: str = Path(description="The original ID of the item you want you'd like to view"),response: Response,db : Session = Depends(get_db)):
    planning_data = db.query(models.Planning).filter(models.Planning.originalId == originalId).all()
    if not planning_data:
        response.status_code = status.HTTP_404_NOT_FOUND
    for planning in planning_data:
        required_skills_lst = []
        required_skills_name_lst = []
        required_skills_cat_lst = []
        optional_skills_lst = []
        optional_skills_name_lst = []
        optional_skills_cat_lst = []
        if len(planning.requiredSkillsName.split(",")) >= 1 and planning.requiredSkillsName.split(",")[0] != '':
            required_skills_name_lst = planning.requiredSkillsName.split(",")
            required_skills_cat_lst = planning.requiredSkillsCategory.split(",")
        for n, c in zip(required_skills_name_lst, required_skills_cat_lst):
            # print(n,c)
            required_skills_lst.append({"name": n,"category": c})
        planning.requiredSkills = required_skills_lst
        if len(planning.optionalSkillsName.split(",")) >= 1 and planning.optionalSkillsName.split(",")[0] != '':
            optional_skills_name_lst = planning.optionalSkillsName.split(",")
            optional_skills_cat_lst = planning.optionalSkillsCategory.split(",")
        for n, c in zip(optional_skills_name_lst, optional_skills_cat_lst):
            # print(n,c)
            optional_skills_lst.append({"name": n,"category": c})
        planning.optionalSkills = optional_skills_lst
        del planning.requiredSkillsName
        del planning.requiredSkillsCategory
        del planning.optionalSkillsName
        del planning.optionalSkillsCategory

    return planning_data

@app.get("/get-data-by-operatingUnit/{operatingUnit}",response_model = List[schemas.Planning])
def get_data_by_operatingUnit(*,operatingUnit: str = Path(description="The opearting unit of the item you want you'd like to view"), response: Response,db : Session = Depends(get_db)):
    planning_data = db.query(models.Planning).filter(models.Planning.operatingUnit == operatingUnit).all()
    if not planning_data:
        response.status_code = status.HTTP_404_NOT_FOUND
    for planning in planning_data:
        required_skills_lst = []
        required_skills_name_lst = []
        required_skills_cat_lst = []
        optional_skills_lst = []
        optional_skills_name_lst = []
        optional_skills_cat_lst = []
        if len(planning.requiredSkillsName.split(",")) >= 1 and planning.requiredSkillsName.split(",")[0] != '':
            required_skills_name_lst = planning.requiredSkillsName.split(",")
            required_skills_cat_lst = planning.requiredSkillsCategory.split(",")
        for n, c in zip(required_skills_name_lst, required_skills_cat_lst):
            # print(n,c)
            required_skills_lst.append({"name": n,"category": c})
        planning.requiredSkills = required_skills_lst
        if len(planning.optionalSkillsName.split(",")) >= 1 and planning.optionalSkillsName.split(",")[0] != '':
            optional_skills_name_lst = planning.optionalSkillsName.split(",")
            optional_skills_cat_lst = planning.optionalSkillsCategory.split(",")
        for n, c in zip(optional_skills_name_lst, optional_skills_cat_lst):
            # print(n,c)
            optional_skills_lst.append({"name": n,"category": c})
        planning.optionalSkills = optional_skills_lst
        del planning.requiredSkillsName
        del planning.requiredSkillsCategory
        del planning.optionalSkillsName
        del planning.optionalSkillsCategory

    return planning_data

@app.get("/get-data-by-officePostalCode/{officePostalCode}", response_model = List[schemas.Planning])
def get_data_by_officePostalCode(*,officePostalCode: str = Path(description="The Office Postal Code of the item you want you'd like to view"), response: Response,db : Session = Depends(get_db)):
    planning_data = db.query(models.Planning).filter(models.Planning.officePostalCode == str(officePostalCode)).all()
    if not planning_data:
        response.status_code = status.HTTP_404_NOT_FOUND

    for planning in planning_data:
        required_skills_lst = []
        required_skills_name_lst = []
        required_skills_cat_lst = []
        optional_skills_lst = []
        optional_skills_name_lst = []
        optional_skills_cat_lst = []
        if len(planning.requiredSkillsName.split(",")) >= 1 and planning.requiredSkillsName.split(",")[0] != '':
            required_skills_name_lst = planning.requiredSkillsName.split(",")
            required_skills_cat_lst = planning.requiredSkillsCategory.split(",")
        for n, c in zip(required_skills_name_lst, required_skills_cat_lst):
            # print(n,c)
            required_skills_lst.append({"name": n,"category": c})
        planning.requiredSkills = required_skills_lst
        if len(planning.optionalSkillsName.split(",")) >= 1 and planning.optionalSkillsName.split(",")[0] != '':
            optional_skills_name_lst = planning.optionalSkillsName.split(",")
            optional_skills_cat_lst = planning.optionalSkillsCategory.split(",")
        for n, c in zip(optional_skills_name_lst, optional_skills_cat_lst):
            # print(n,c)
            optional_skills_lst.append({"name": n,"category": c})
        planning.optionalSkills = optional_skills_lst
        del planning.requiredSkillsName
        del planning.requiredSkillsCategory
        del planning.optionalSkillsName
        del planning.optionalSkillsCategory

    return planning_data

@app.get("/get-data-by-clientId/{clientId}", response_model = List[schemas.Planning])
def get_data_by_clientId(*,clientId: str = Path(description="The Client ID of the item you want you'd like to view"),response: Response,db : Session = Depends(get_db)):
    planning_data = db.query(models.Planning).filter(models.Planning.clientId == str(clientId)).all()
    if not planning_data:
        response.status_code = status.HTTP_404_NOT_FOUND
    for planning in planning_data:
        required_skills_lst = []
        required_skills_name_lst = []
        required_skills_cat_lst = []
        optional_skills_lst = []
        optional_skills_name_lst = []
        optional_skills_cat_lst = []
        if len(planning.requiredSkillsName.split(",")) >= 1 and planning.requiredSkillsName.split(",")[0] != '':
            required_skills_name_lst = planning.requiredSkillsName.split(",")
            required_skills_cat_lst = planning.requiredSkillsCategory.split(",")
        for n, c in zip(required_skills_name_lst, required_skills_cat_lst):
            # print(n,c)
            required_skills_lst.append({"name": n,"category": c})
        planning.requiredSkills = required_skills_lst
        if len(planning.optionalSkillsName.split(",")) >= 1 and planning.optionalSkillsName.split(",")[0] != '':
            optional_skills_name_lst = planning.optionalSkillsName.split(",")
            optional_skills_cat_lst = planning.optionalSkillsCategory.split(",")
        for n, c in zip(optional_skills_name_lst, optional_skills_cat_lst):
            # print(n,c)
            optional_skills_lst.append({"name": n,"category": c})
        planning.optionalSkills = optional_skills_lst
        del planning.requiredSkillsName
        del planning.requiredSkillsCategory
        del planning.optionalSkillsName
        del planning.optionalSkillsCategory

    return planning_data

add_pagination(app)


