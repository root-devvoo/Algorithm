-- 상위 n개 레코드
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
-----------------------------------------------
-- 최댓값 구하기
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
-----------------------------------------------
-- 최솟값 구하기
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
-----------------------------------------------
-- 동물 수 구하기
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS
-----------------------------------------------
-- 중복 제거하기
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS;
-----------------------------------------------
-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count 
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
-----------------------------------------------
-- 동명 동물 수 찾기
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL -- NULL값이 아닌 것들만...
GROUP BY NAME
HAVING COUNT > 1 -- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 것이므로
ORDER BY NAME;
-----------------------------------------------
-- 모든 레코드 조회하기
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
