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
