-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, 
        DATE_FORMAT(OUT_DATE,'%Y-%m-%d') as OUT_DATE,
        CASE 
            WHEN OUT_DATE <= DATE('20220501') 
            THEN '출고완료'
            WHEN OUT_DATE IS NULL
            THEN '출고미정'
            ELSE '출고대기'
        END 출고여부
FROM FOOD_ORDER
ORDER BY 1