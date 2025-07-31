
propietarios = {}
vehicle_d = {}
key = True
print("-------Bienvenido al program de boutique-------")
while key:
    ops = input("\nSeleccione una opción:\n1. Agregar productos\n2. Ver productos\n3. Buscar producto\n4. Total de inventario\n5. Productos por categoría\n6. Salir")
    match ops:
        case "1":
            try:
                start_prod = int(input("Cuántos propietarios hay: "))
                for new_product in range(start_prod):
                    nit_validation = False
                    #Validación de NIT
                    while not nit_validation:
                        nit = input("Coloque el NIT del propietario: ")
                        if nit in propietarios:
                            print("Ese código ya existe...")
                        else:
                            nit_validation = True
                    p_name = input("Coloque su nombre completo: ")
                    p_number = input("Coloque su número de teléfono: ")
                    v_namba = int(input("Coloque cuántos vehiculos posee: "))


                    propietarios[nit] = {
                        "nombre":p_name,
                        "numero": p_number,
                        "v_details": 0
                    }
                    for new_vehicle in range(v_namba):
                        v_plate = input("Coloque la placa del carro: ")
                        v_brand = input("Coloque la marca del vehpiculo: ")
                        v_type = input("Coloque el tipo de vehpiculo: ")
                        v_year = input("Coloque el año del vehículo: ")
                        tax = None
                        tax_ver = input("Ya pagó el impuesto? Y/N")
                        if tax_ver.lower() == "y":
                            tax = True
                        elif tax_ver.lower() == "n":
                            tax = False
                        propietarios[nit]["v_details"][v_plate] = {
                            "year": v_year,
                            "brand": v_brand,
                            "type": v_type,
                            "tax": tax
                        }
            except ValueError:
                print("Eso no es un número")
        case "2":
            # Display de propietarios
            print("Estos son los productos registrados: ")
            for nits, item in propietarios.items():
                print(f"Código: {nits}\nNombre: {item["nombre"]}\nNumero: {item["numero"]}\n\n")
                print("Autos:\n")
                for auto, details in item["v_details"].items():
                    print(f"Placa: {auto}\nAño: {details["year"]}\nMarca: {details["brand"]}\nTipo: {details["type"]}\nImpuesto: {details["tax"]}")