from sqlalchemy import Table, Column, Integer, String, Float, Boolean
from database import Base


class Planning(Base):
    __tablename__ = 'Planning'

    id = Column(Integer, primary_key=True, index=True)
    originalId = Column(String)
    talentId = Column(String)
    talentName = Column(String)
    talentGrade = Column(String)
    bookingGrade = Column(String)
    operatingUnit = Column(String)
    officeCity = Column(String)
    officePostalCode = Column(String)
    jobManagerName = Column(String)
    jobManagerId = Column(String)
    totalHours = Column(Float)
    startDate = Column(String)
    endDate = Column(String)
    clientName = Column(String)
    clientId = Column(String)
    industry = Column(String)
    isUnassigned = Column(String)
    requiredSkillsName = Column(String)
    requiredSkillsCategory = Column(String)
    optionalSkillsName = Column(String)
    optionalSkillsCategory = Column(String)