SELECT TO_CHAR(SALES_DATE,'YYYY') YEAR, 
       TO_NUMBER(TO_CHAR(SALES_DATE,'MM')) MONTH, 
       COUNT(DISTINCT USER_ID) PUCHASED_USERS, 
       ROUND(COUNT(DISTINCT USER_ID) / ( 
                                -- 2021년에 가입한 총 회원수
                                SELECT COUNT(USER_ID) 
                                FROM USER_INFO 
                                WHERE TO_CHAR(JOINED,'YYYY') = '2021'
                              ),1) PUCHASED_RATIO          
FROM ONLINE_SALE
WHERE USER_ID IN (
                    -- 2021년에 가입한 회원ID
                    SELECT USER_ID
                    FROM USER_INFO
                    WHERE TO_CHAR(JOINED,'YYYY') = '2021'
                )
GROUP BY TO_CHAR(SALES_DATE,'YYYY'), TO_CHAR(SALES_DATE,'MM')
ORDER BY 1, 2 