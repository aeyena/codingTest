-- 코드를 입력하세요
SELECT CAR_ID
  FROM CAR_RENTAL_COMPANY_CAR 
  WHERE CAR_TYPE = '세단'
    AND CAR_ID IN (
                    -- 10월에 대여를 시작한 CAR_ID
                    SELECT DISTINCT CAR_ID
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                    WHERE TO_CHAR(START_DATE,'MM') = '10'
                  )
ORDER BY 1 DESC