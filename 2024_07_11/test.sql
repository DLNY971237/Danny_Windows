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
----------------------------------

SELECT sna as 站點, total as 總車輛數, rent_bikes as 可借, return_bikes as 可還, mday as 時間, act as 狀態
FROM youbike
WHERE (updatetime, sna) IN (
	SELECT MAX(updatetime),sna
	FROM youbike
	WHERE sarea = '大同區'
	GROUP BY sna
)

