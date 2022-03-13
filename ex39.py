Provinces = {
        'Gauteng' : 'GP',
        'Free State' : 'FS',
        'Limpopo' : 'L',
        'Western Cape' : 'WP',
        'Northern Cape' : 'NP'
}

Cities = {
        'WP' : 'Cape Town',
        'GP' : 'Johannesburg',
        'L' : 'Polokwane'
}

Cities['NP']= 'Kimberly'
Cities['FS']= 'Bloofontien'

print('_' * 10)
print("Gauteng has: ", Cities['GP'])
print("Western Cape has: ", Cities['WP'])

print('_' * 10)
print("Gauteng's abbreviation is: ", Provinces['Gauteng'])
print("Limpopos abbreviation is: ", Provinces['Limpopo'])

print('_' * 10)
print("Northen Cape has:", Cities[Provinces['Northern Cape']])

print('_' * 10)
for Province, abbrev in list(Provinces.items()):
    print(f"{Province} is abbreviated as {abbrev}")

print('_' * 10)
for abbrev, City in list(Cities.items()):
    print(f"{abbrev} has the city {City}")

print('_' * 10)
for Province, abbrev in list(Provinces.items()):
    print(f"{Province} is abbreviated as {abbrev}")
    print(f"And has the cities:{Cities[abbrev]}")

print('_' * 10)
Province = Provinces.get('Durban')

if not Provinces:
    print("Sorry, no Durban.")

city = Cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")
