-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD,AGE,IFNULL(TLNO,'NONE') AS TLNO
FROM PATIENT
WHERE AGE<=12 AND GEND_CD='W'
ORDER BY AGE DESC,PT_NAME;