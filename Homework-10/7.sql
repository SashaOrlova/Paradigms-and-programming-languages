SELECT Country.Name FROM Country
LEFT JOIN City ON Country.Code = City.CountryCode
GROUP BY Country.Code
HAVING (SUM(City.Population) <= 0.5 * Country.Population) or (count(city.name) = 0 and country.population > 0)
ORDER BY Country.Name;
