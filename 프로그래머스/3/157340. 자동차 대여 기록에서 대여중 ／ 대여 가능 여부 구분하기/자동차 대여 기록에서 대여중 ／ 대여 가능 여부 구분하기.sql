select A.car_id, 
      case when A.car_id in B.car_id then '대여중'
      else '대여 가능' end as AVAILABILITY
from 
    -- car_id 중복제거한 테이블
    ( 
      select distinct car_id 
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) A left outer join 
    -- 2022-10-16에 대여중이었던 car_id 추출
    (
      select car_id
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
      where to_char(start_date,'yyyy-mm-dd') <= '2022-10-16'
      and to_char(end_date,'yyyy-mm-dd') >= '2022-10-16'
      group by car_id
    ) B on (A.car_id = B.car_id)
order by car_id desc
