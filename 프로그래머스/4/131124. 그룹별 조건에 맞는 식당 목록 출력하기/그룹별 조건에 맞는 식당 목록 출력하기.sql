SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, TO_CHAR(RR.REVIEW_DATE,'YYYY-MM-DD') REVIEW_DATE
FROM MEMBER_PROFILE MP INNER JOIN REST_REVIEW RR ON (MP.MEMBER_ID = RR.MEMBER_ID)
WHERE MP.MEMBER_ID IN (     -- 리뷰를 가장 많이 작성한 회원ID 구하기                   
                            SELECT MEMBER_ID
                            FROM (
                                    -- 리뷰 개수로 순위 매기기
                                    SELECT MEMBER_ID, 
                                           RANK() OVER (ORDER BY COUNT(REVIEW_ID) DESC) RANK
                                    FROM REST_REVIEW
                                    GROUP BY MEMBER_ID
                                 ) 
                            WHERE RANK = 1
                        )
ORDER BY 3 ASC, 2 ASC