-- 고양이와 개는 몇 마리 있을까 (GROUP BY)
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count 
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
-----------------------------------------------------------------------
-- 루시와 엘라 찾기 (String, Date)
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
-----------------------------------------------------------------------
-- 최솟값 구하기 (SUM, MAX, MIN)
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
---------------------------------------------------------------------------------
-- 동명 동물 수 찾기 (GROUP BY)
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL -- NULL값이 아닌 것들만
GROUP BY NAME
HAVING COUNT > 1 -- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 것이므로
ORDER BY NAME;
---------------------------------------------------------------------------------
-- 이름에 el이 들어가는 동물 찾기 (String, Date)
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;
-----------------------------------------------
-- 동물 수 구하기 (SUM, MAX, MIN)
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS
-----------------------------------------------
-- 입양 시각 구하기(1) (GROUP BY)
SELECT HOUR(DATETIME) HOUR,
COUNT(HOUR(DATETIME)) COUNT FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR;
-----------------------------------------------------------------------
-- NULL 처리하기 (IS NULL)
SELECT ANIMAL_TYPE, IF(NAME IS NULL, "No name", NAME), SEX_UPON_INTAKE
FROM ANIMAL_INS;
-----------------------------------------------------------------------
-- 중성화 여부 파악하기 문제는 블로그에 따로 정리할 예정 (String, Date)
-----------------------------------------------------------------------
-- 중복 제거하기 (SUM, MAX, MIN)
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS;
--------------------------------------------------------------
-- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') 날짜 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
--------------------------------------------------------------
