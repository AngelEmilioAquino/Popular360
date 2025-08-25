from db import database
from datetime import datetime

# Guarda tasas de moneda
async def save_exchange_rates(data):
    monedas = data.get("monedas", {}).get("moneda", [])
    fecha_str = data.get("monedas", {}).get("fechaConsulta")
    
    if not monedas or not fecha_str:
        print("No hay datos de monedas para guardar:", data)
        return

    # Convertir fecha
    fecha_str = fecha_str.replace(" - ", " ")
    fecha_consulta = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")

    for m in monedas:
        query = """
            INSERT INTO tasas_moneda (descripcion, compra, venta, fecha_consulta)
            VALUES (:descripcion, :compra, :venta, :fecha_consulta)
        """
        await database.execute(query, values={
            "descripcion": m.get("descripcion"),
            "compra": m.get("compra"),
            "venta": m.get("venta"),
            "fecha_consulta": fecha_consulta
        })


# Guarda tasas de interés
async def save_interest_rates(data):
    tasas = data.get("tasasint", {})
    if not tasas:
        print("No hay 'tasasint' en la respuesta:", data)
        return

    tasas_prestamos = tasas.get("tasaprestamos", {})
    tasas_certificados = tasas.get("tasacertificados", {})

    fecha_str = data.get("fechaConsulta")
    if not fecha_str:
        fecha_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")  # fallback
    fecha_consulta = datetime.strptime(fecha_str, "%Y-%m-%d-%H:%M:%S")

    for producto, tasa in {**tasas_prestamos, **tasas_certificados}.items():
        query = """
            INSERT INTO tasas_interes (producto, tasa, fecha_consulta)
            VALUES (:producto, :tasa, :fecha_consulta)
        """
        await database.execute(query, values={
            "producto": producto,
            "tasa": tasa,
            "fecha_consulta": fecha_consulta
        })
