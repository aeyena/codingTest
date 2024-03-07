select to_number(to_char(start_date,'MM')) month, car_id, count(history_id) records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in 
(select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between to_date('20220801','YYYY-MM-DD') and to_date('20221031','YYYY-MM-DD')
having count(car_id) >= 5
group by car_id)
and start_date between to_date('20220801','YYYY-MM-DD') and to_date('20221031','YYYY-MM-DD')
group by to_char(start_date,'MM'), car_id
order by to_char(start_date,'MM'), car_id desc