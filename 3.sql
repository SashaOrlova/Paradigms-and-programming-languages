select Name from City
where id in (select CityId from Capital 
	where CountryCode in (select Code from Country
		where Name in ('Malaysia')));
