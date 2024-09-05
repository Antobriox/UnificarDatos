def unify_data(mysql_data_vino12, mysql_data_vino34, mysql_data_vino5):
    unified_data = []
    
    # Primero unificamos los datos de vino12 con los de vino5 usando nombre_vino como clave
    for vino12_row in mysql_data_vino12:
        nombre_vino_vino12 = vino12_row[0]
        color = vino12_row[1]

        for vino5_row in mysql_data_vino5:
            nombre_vino_vino5 = vino5_row[0]
            porcentaje_alchol = vino5_row[1]

            if nombre_vino_vino12 == nombre_vino_vino5:
                unified_data.append({
                    "nombre_vino": nombre_vino_vino12,
                    "color": color,
                    "porcentaje_alchol": porcentaje_alchol,
                    "ano": None  # Año se llenará después
                })

    # Ahora unificamos con los datos de vino34 usando porcentaje_alchol como clave
    for vino34_row in mysql_data_vino34:
        porcentaje_alchol = vino34_row[0]
        ano = vino34_row[1]

        for unified_row in unified_data:
            if unified_row["porcentaje_alchol"] == porcentaje_alchol:
                unified_row["ano"] = ano

    return unified_data
