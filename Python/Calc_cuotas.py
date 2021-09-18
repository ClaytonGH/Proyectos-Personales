def compra_producto(valor_producto: int, nro_cuotas: int)->dict:
    diccionario = {}
    if nro_cuotas >= 1 and nro_cuotas <= 18:
        t = valor_producto * 0.15
        y = (valor_producto - t)
        if nro_cuotas >= 1 and nro_cuotas <= 6:
            x = (y * 0.10) / nro_cuotas
            x2 = y / nro_cuotas
            xf1 = x + x2
        elif nro_cuotas >= 7 and nro_cuotas <= 12:
            x = (y * 0.12) / nro_cuotas
            x2 = y / nro_cuotas
            xf1 = x + x2
        elif nro_cuotas >= 13 and nro_cuotas <= 18:
            x = (y * 0.15) / nro_cuotas
            x2 = y / nro_cuotas
            xf = x + x2
            xf1 = round(xf, 1)
        fa = xf1 * nro_cuotas + t
        diccionario ['valor_producto'] = valor_producto
        diccionario ['cuota_inicial'] = int(t)
        diccionario ['nro_cuotas'] = int(nro_cuotas)
        diccionario ['valor_cuota'] = int(xf1)
        diccionario ['valor_final_producto'] = int(fa)
        return diccionario
    else:
        return diccionario

print(compra_producto(6390000, 14))
