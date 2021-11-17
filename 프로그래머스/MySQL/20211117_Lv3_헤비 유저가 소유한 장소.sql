-- 코드를 입력하세요
SELECT ID, NAME, HOST_ID FROM PLACES
WHERE HOST_ID IN -- IN : 서브쿼리의 결과에 존재하는 임의의 값과 동일한 조건을 의미한다.
    (
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING count(HOST_ID) > 1  -- HAVING 절은 집계함수를 가지고 조건비교를 할 때 사용한다. GROUP BY절과 함께 사용.
    )
ORDER BY ID; -- ID 순으로 조회해야 하므로
