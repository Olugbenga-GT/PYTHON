# practising a dictionary
country_codes = {"Nigeria": 'NGA', "South Africa": 'SA', "Ghana":'GH', "Tanzania": 'TZN'}

if country_codes:
    print(f'there are {len(country_codes)} countries')
else: print(f'Country codes is empty')

for country, code in country_codes.items():
    print(f'{country} has {code} as it\'s code')

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
print(roman_numerals)

roman_numerals['V'] = 75
print(roman_numerals)

roman_numerals['L'] = 50
roman_numerals['V'] = 5
print(roman_numerals)

print('V' in roman_numerals)
print('V' not in roman_numerals)

for country in sorted(country_codes.keys()):
    print(country)


