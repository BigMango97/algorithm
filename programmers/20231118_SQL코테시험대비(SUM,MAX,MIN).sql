-- 가격이 제일 비싼 식품의 정보 출력하기
-- Level 2 17,423명 완료
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM (SELECT * FROM FOOD_PRODUCT ORDER BY PRICE DESC)
WHERE ROWNUM = 1
 
-- 가장 비싼 상품 구하기
-- Level 1 18,085명 완료
SELECT MAX_PRICE
FROM (SELECT MAX(PRICE) AS MAX_PRICE
     FROM PRODUCT)

-- 최댓값 구하기
-- Level 1 62,646명 완료
SELECT DATETIME AS 시간
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME DESC)
WHERE ROWNUM = 1
 
-- 최솟값 구하기
-- Level 2 61,446명 완료
SELECT DATETIME AS 시간
FROM (SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME ASC)
WHERE ROWNUM = 1
 
-- 동물 수 구하기
-- Level 2 60,377명 완료
SELECT COUNT(*) AS count
FROM ANIMAL_INS

-- 중복 제거하기
-- Level 2 59,057명 완료
SELECT count(DISTINCT NAME) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL