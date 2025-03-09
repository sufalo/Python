a = input("Wprowadź daną: ")

if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
    data_type = "int"
elif a.lower() in ["true", "false"]:
    data_type = "bool"
else:
    try:
        float(a)
        data_type = "float"
    except ValueError:
        data_type = "str"

print(f"Podana wartość jest typu: {data_type}")
