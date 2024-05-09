-- 코드를 입력하세요
SELECT USER_ID
     , NICKNAME
     , CITY || ' ' || STREET_ADDRESS1 || ' ' || STREET_ADDRESS2 AS "전체주소"
     , SUBSTR(TLNO, 1, 3) || '-' || SUBSTR(TLNO, 4, 4) || '-' || SUBSTR(TLNO, 8) AS "전화번호"
FROM USED_GOODS_USER 
WHERE USER_ID IN (
                    SELECT WRITER_ID 
                    FROM USED_GOODS_BOARD
                    GROUP BY WRITER_ID
                    HAVING COUNT(BOARD_ID) >= 3
                 )
ORDER BY USER_ID DESC
