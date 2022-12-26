import json
import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
# query = "create table if not exists Planning (id INT primary key NOT NULL,originalId VARCHAR(100) NOT NULL,talentId VARCHAR(100),talentName VARCHAR(100),talentGrade VARCHAR(100), bookingGrade VARCHAR(100),operatingUnit VARCHAR(100) NOT NULL,officeCity VARCHAR(100), officePostalCode VARCHAR(100) NOT NULL, jobManagerId VARCHAR(100), totalHours FLOAT NOT NULL, startDate VARCHAR(100) NOT NULL, endDate VARCHAR(100) NOT NULL, clientName VARCHAR(100), clientId VARCHAR(100) NOT NULL, industry VARCHAR(100), isUnassigned varchar(100) DEFAULT 'false', optionalSkills VARCHAR(255), optionalSkills VARCHAR(255);"
cursor.execute("create table if not exists Planning (id INT primary key NOT NULL,originalId VARCHAR(100) NOT NULL,talentId VARCHAR(100),talentName VARCHAR(100),talentGrade VARCHAR(100), bookingGrade VARCHAR(100),operatingUnit VARCHAR(100) NOT NULL,officeCity VARCHAR(100), officePostalCode VARCHAR(100) NOT NULL, jobManagerName VARCHAR(100), jobManagerId VARCHAR(100), totalHours FLOAT NOT NULL, startDate VARCHAR(100) NOT NULL, endDate VARCHAR(100) NOT NULL, clientName VARCHAR(100), clientId VARCHAR(100) NOT NULL, industry VARCHAR(100), isUnassigned varchar(100) DEFAULT 'false', requiredSkillsName VARCHAR(255), requiredSkillsCategory VARCHAR(255), optionalSkillsName VARCHAR(255), optionalSkillsCategory VARCHAR(255))")
planning_json = json.load(open('planning.json'))
columns = ['id','originalId','talentId','talentName','talentGrade','bookingGrade','operatingUnit','officeCity','officePostalCode','jobManagerName','jobManagerId','totalHours','startDate','endDate','clientName','clientId','industry','isUnassigned','requiredSkillsName','requiredSkillsCategory','optionalSkillsName','optionalSkillsCategory']
print(len(columns))
for planning in planning_json:
    skill_lst = planning.get('requiredSkills')
    required_skills_names_lst = []
    required_skills_cat_lst = []
    for skills in skill_lst:
        lst = list(skills.values())
        # print(lst)
        required_skill_name = lst[0]
        required_skill_cat = lst[1]
        required_skills_names_lst.append(required_skill_name)
        required_skills_cat_lst.append(required_skill_cat)
    required_skills_name_str = ",".join( required_skills_names_lst )
    required_skills_cat_str = ",".join( required_skills_cat_lst )
    # print(required_skills_name_str)
    # print(required_skills_cat_str)
    skill_lst = planning.get('optionalSkills')
    optional_skills_names_lst = []
    optional_skills_cat_lst = []
    for skills in skill_lst:
        lst = list(skills.values())
        # print(lst)
        optional_skill_name = lst[0]
        optional_skill_cat = lst[1]
        optional_skills_names_lst.append(optional_skill_name)
        optional_skills_cat_lst.append(optional_skill_cat)
    optional_skills_name_str = ",".join( optional_skills_names_lst )
    optional_skills_cat_str = ",".join( optional_skills_cat_lst )
    # print(optional_skills_name_str)
    # print(optional_skills_cat_str)
    planning.pop('requiredSkills', None)
    planning.pop('optionalSkills', None)
    planning['requiredSkillsName'] = required_skills_name_str
    planning['requiredSkillsCategory'] = required_skills_cat_str
    planning['optionalSkillsName'] = optional_skills_name_str
    planning['optionalSkillsCategory'] = optional_skills_cat_str
    # print(planning)
    # print(skill_names)
    keys= tuple(planning[c] for c in columns)
    print(keys)
    cursor.execute('insert into Planning values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',keys)
    print(f'{planning["id"]} data inserted Succefully')

connection.commit()
connection.close()