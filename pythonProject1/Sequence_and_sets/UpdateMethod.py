

country_codes = {"Nigeria": 'NGA', "South Africa": 'SA', "Ghana":'GH', "Tanzania": 'TZN'}
country_codes.update({"Cote D'ivoire": "CDV"})
print(country_codes)

country_codes2 = {value: key for key, value in country_codes.items()}
print(country_codes2)

print({number: number**3 for number in range(1, 11)})

