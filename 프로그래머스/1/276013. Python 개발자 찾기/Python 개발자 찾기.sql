select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPER_INFOS
where  SKILL_1 = 'Python' or SKILL_2 = 'Python' or SKILL_3 = 'Python'
ORDER BY ID ASC