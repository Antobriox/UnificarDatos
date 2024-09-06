def unify_data(mysql_data_vino12, mysql_data_vino34, mysql_data_vino5):
    unified_data = []
    
    # Función auxiliar para verificar si un registro ya existe en la lista unificada
    def record_exists(nombre_vino, color, porcentaje_alchol, año):
        for record in unified_data:
            if (record["nombre_vino"] == nombre_vino and
                record["color"] == color and
                record["porcentaje_alchol"] == porcentaje_alchol and
                record["año"] == año):
                return True
        return False

    # Unificamos los datos de vino12 con los de vino5 usando nombre_vino como clave
    for vino12_row in mysql_data_vino12:
        nombre_vino_vino12 = vino12_row[0]
        color = vino12_row[1]

        for vino5_row in mysql_data_vino5:
            nombre_vino_vino5 = vino5_row[0]
            porcentaje_alchol = vino5_row[1]

            if nombre_vino_vino12 == nombre_vino_vino5:
                if not record_exists(nombre_vino_vino12, color, porcentaje_alchol, None):
                    unified_data.append({
                        "nombre_vino": nombre_vino_vino12,
                        "color": color,
                        "porcentaje_alchol": porcentaje_alchol,
                        "año": None  
                    })

    # Unificamos con los datos de vino34 usando porcentaje_alchol como clave
    for vino34_row in mysql_data_vino34:
        porcentaje_alchol = vino34_row[0]
        año = vino34_row[1]

        for unified_row in unified_data:
            if unified_row["porcentaje_alchol"] == porcentaje_alchol:
                unified_row["año"] = año

    return unified_data
