select C.company_code, C.founder,
        count(distinct LM.lead_manager_code),
        count(distinct SM.senior_manager_code),
        count(distinct M.manager_code),
        count(distinct E.employee_code)
from company C, lead_manager LM, senior_manager SM, manager M, employee E 
where C.company_code = LM.company_code and
        LM.lead_manager_code = SM.lead_manager_code and
        SM.senior_manager_code = M.senior_manager_code and
        M.manager_code = E.manager_code 
group by C.company_code, C.founder 
order by C.company_code 