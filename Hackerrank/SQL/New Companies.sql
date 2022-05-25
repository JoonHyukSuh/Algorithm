select C.company_code, C.founder,
        count(distinct LM.lead_manager_code),
        count(distinct SM.senior_manager_code),
        count(distinct M.manager_code),
        count(distinct E.employee_code)
from company C
left join lead_manager LM on c