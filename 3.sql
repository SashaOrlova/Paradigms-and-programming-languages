select City.Name from City
inner join Capital on City.Id = Capital.CityId
inner join Country on Capital.CountryCode = Country.Code
where Country.Name = "Malaysia";
