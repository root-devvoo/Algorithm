-- 상위 n개 레코드 (Level 1)
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
-----------------------------------------------
-- 최댓값 구하기 (Level 1)
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
-----------------------------------------------
-- 모든 레코드 조회하기 (Level 1)
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
-----------------------------------------------
-- 이름이 없는 동물의 아이디
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL;
-----------------------------------------------
-- 이름이 있는 동물의 아이디
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
------------------------------------------------------------------------
-- NULL 처리하기
SELECT ANIMAL_TYPE, IF(NAME IS NULL, "No name", NAME), SEX_UPON_INTAKE
FROM ANIMAL_INS;
------------------------------------------------------------------------
-- 없어진 기록 찾기
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS INS RIGHT JOIN ANIMAL_OUTS OUTS
/* 
RIGHT OUTER JOIN은 오른쪽 테이블을 기준으로 
JOIN 조건이 일치하는 값들과 일치하지 않는 값을 출력한다. 
일치하는 값이 없다면 NULL을 리턴하여 채워준다.
*/
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID 
WHERE INS.ANIMAL_ID IS NULL;
