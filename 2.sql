select Name from Country 
where Code in (select CountryCode from LiteracyRate
	where Rate in (select max(Rate) from (
		select max(Year), Rate from LiteracyRate
			group by CountryCode)));
