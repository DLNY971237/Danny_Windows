SELECT *
FROM youbike


SELECT *
FROM youbike
WHERE sarea IN ('大安區','士林區')

SELECT MAX(updatetime),sna
FROM youbike
GROUP BY sna

------儲存最新資料進SQL--------------
SELECT *
FROM youbike
WHERE (updatetime, sna) IN (
	SELECT MAX(updatetime),sna
	FROM youbike
	GROUP BY sna
)

