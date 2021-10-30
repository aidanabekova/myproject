data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i[0] == "0":
        codes.append(i)
    else:
        designations.append(i)
print(designations)
print(codes)
operators = dict(zip(designations, codes))
print(operators)
operators.pop("Katel")
del operators["Fonex"]
print(operators)
operators["O!"] = {"0705", "0700", "0500"}
operators["Megacom"] = {"0550", "0999", "0555"}
operators["Beeline"] = {"0770", "0222", "0777"}
print(operators)

for key, value in operators.items():
    print(key, "-", value)