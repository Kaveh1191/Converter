Unit_In = input("Enter Input Unit: ").lower()
Unit_Ou = input("Enter Output Unit: ").lower()
Value = float(input("Enter Value: "))

LengthConvertFactor = {
    ('meter', 'kilometer'): 0.001,
    ('kilometer', 'meter'): 1000,
    ('meter', 'mile'): 1.609344,
    ('mile', 'meter'): 1609.344,
    ('meter', 'feet'): 3.28,
    ('feet', 'meter'): 0.328,
    ('meter', 'inch'): 39.370079,
    ('inch', 'meter'): 0.0254,
    ('kilometer', 'mile'): 0.6213,
    ('mile', 'kilometer'): 1.6093,
    ('kilometer', 'feet'): 3280.839,
    ('feet', 'kilometer'): 0.00030,
    ('kilometer', 'inch'): 39370.078,
    ('inch', 'kilometer'): 0.0000254,
    ('mile', 'feet'): 5280,
    ('feet', 'mile'): 0.000189,
    ('mile', 'inch'): 63360,
    ('inch', 'mile'): 0.000015,
    ('feet', 'inch'): 12,
    ('inch', 'feet'): 0.0833,
    ('gram', 'kilogram'): 0.001,
    ('kilogram', 'gram'): 1000,
    ('gram', 'pound'): 0.00220,
    ('pound', 'gram'): 453.59,
    ('kilogram', 'pound'): 2.2046,
    ('pound', 'kilogram'): 0.45359
}

TempConvertFactor = {
    ('cel', 'far'): 33.8,
    ('far', 'cel'): -17.22,
    ('cel', 'kel'): 274.15,
    ('kel', 'cel'): -272.15,
    ('far', 'kel'): 255.9277,
    ('kel', 'far'): -457.87
}
def LengthConvert(Value, Unit_in, Unit_ou):
    if (Unit_in, Unit_ou) in LengthConvertFactor:
        return LengthConvertFactor[(Unit_in, Unit_ou)] * Value
def TempConvert(Value, Unit_in, Unit_ou):
    if (Unit_in, Unit_ou) in TempConvertFactor:
        return TempConvertFactor[(Unit_in, Unit_ou)] * Value

result = None
if (Unit_In, Unit_Ou) in LengthConvertFactor:
    result = LengthConvert(Value, Unit_In, Unit_Ou)
elif (Unit_In, Unit_Ou) in TempConvertFactor:
    result = TempConvert(Value, Unit_In, Unit_Ou)
else:
    print("Conversion not supported for the given units.")

if result is not None:
    print(f'{Value} {Unit_In.capitalize()} = {result} {Unit_Ou.capitalize()}')
else:
    print("Invalid conversion.")
