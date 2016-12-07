select Name, Rate from Country, LiteracyRate
where Country.Code in (select CountryCode from LiteracyRate
	where Rate in (select max(Rate) from (
		select max(Year), Rate from LiteracyRate
			group by CountryCode)))and
			(Rate in (select max(Rate) from (
				select max(Year), Rate from LiteracyRate
					group by CountryCode)));
