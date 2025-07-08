# vlan_checker.py

vlan = input("Ingrese el número de VLAN: ")

try:
    vlan_num = int(vlan)
    if 1 <= vlan_num <= 1005:
        print("La VLAN ingresada pertenece al rango NORMAL (1-1005).")
    elif 1006 <= vlan_num <= 4094:
        print("La VLAN ingresada pertenece al rango EXTENDIDO (1006-4094).")
    else:
        print("La VLAN ingresada no pertenece a un rango válido.")
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
