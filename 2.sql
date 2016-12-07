SELECT Country.Name, bRCountry.bRate FROM Country
INNER JOIN
(
	SELECT LiteracyRate.CountryCode AS bCountryCode, LiteracyRate.Rate AS bRate, MAX(LiteracyRate.Year) FROM LiteracyRate
	GROUP BY LiteracyRate.CountryCode
 	ORDER BY LiteracyRate.Rate DESC
 	LIMIT 1
) bRCountry
ON Country.Code = bRCountry.bCountryCode;
