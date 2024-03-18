SELECT FLAVOR
FROM 
    (
        -- 상반기 아이스크림 총 주문량 + 7월 아이스크림 총 주문량
        SELECT FH.FLAVOR, FH.TOTAL_ORDER + J.J_TOTAL
        FROM FIRST_HALF FH INNER JOIN 
            (   
                -- 7월 아이스크림 총 주문량
                SELECT FLAVOR, SUM(TOTAL_ORDER) J_TOTAL
                FROM JULY
                GROUP BY FLAVOR
            ) J ON (FH.FLAVOR = J.FLAVOR)
        ORDER BY 2 DESC
    ) 
WHERE ROWNUM <= 3

