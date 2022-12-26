from pydantic import BaseModel
from typing import Optional, Union
from typing import List

my_datatype = Union[dict,bool,str,int,list,List]

class Planning(BaseModel):
    id : int
    originalId : my_datatype
    talentId : my_datatype
    talentName : my_datatype
    talentGrade : my_datatype
    bookingGrade : my_datatype
    operatingUnit : my_datatype
    officeCity : my_datatype
    officePostalCode : my_datatype
    jobManagerName : my_datatype
    jobManagerId : my_datatype
    totalHours : my_datatype
    startDate : my_datatype
    endDate : my_datatype
    clientName : my_datatype
    clientId : my_datatype
    industry : my_datatype
    isUnassigned : my_datatype
    requiredSkills : list
    optionalSkills : list

    class Config:
        orm_mode = True