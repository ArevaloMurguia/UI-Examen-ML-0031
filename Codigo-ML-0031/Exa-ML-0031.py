
import sys
import os
import io
import importlib.util
import pandas as pd

# Nombre del alumno
encabezado_pie = "Rafael Arevalo Machine Learning pandas, NC 0031"
print(encabezado_pie)

# 1. Localizar e importar el diccionario
carpeta_proyecto = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ruta_diccionario = os.path.join(
    carpeta_proyecto,
    "Datos-De-Entrada-ML-0031",
    "Dicc_0031.py"
)

if not os.path.isfile(ruta_diccionario):
    raise FileNotFoundError(
        f"No se encontró el archivo: {ruta_diccionario}\n"
        "Revisa el nombre de la carpeta y del archivo."
    )

spec = importlib.util.spec_from_file_location(
    "Dicc_0031", ruta_diccionario
)

Dicc_0031 = importlib.util.module_from_spec(spec)
sys.modules["Dicc_0031"] = Dicc_0031
spec.loader.exec_module(Dicc_0031)

# 2. Preparar el reporte Markdown
contenido_md = [
    "# Reporte de Análisis de Vehículos - Pandas",
    "",
    f"`{encabezado_pie}`",
    ""
]

def registrar(titulo, contenido):
    """Muestra los resultados y los guarda en el reporte."""
    print(f"\n--- {titulo} ---")
    print(contenido)

    contenido_md.append(f"## {titulo}\n")
    contenido_md.append("```text")
    contenido_md.append(str(contenido))
    contenido_md.append("```\n")

# 3. Convertir el diccionario a DataFrame
df = pd.DataFrame(Dicc_0031.datos_vehiculos)
registrar("1. DataFrame Convertido", df)

# 4. Información estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# 5. Información general
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 6. Estadísticas de la columna Anio
registrar(
    "3. Estadísticas Generales de la columna Anio",
    df["Anio"].describe()
)

# 7. Ordenar ascendentemente por año
df_asc_anio = df.sort_values(
    by="Anio", ascending=True
)
registrar("4. Orden Ascendente por Anio", df_asc_anio)

# 8. Ordenar descendentemente por año
df_desc_anio = df.sort_values(
    by="Anio", ascending=False
)
registrar("5. Orden Descendente por Anio", df_desc_anio)

# 9. Crear la carpeta de resultados
carpeta_resultados = os.path.join(
    carpeta_proyecto, "Resultados-0031"
)
os.makedirs(carpeta_resultados, exist_ok=True)

# 10. Guardar el reporte
ruta_archivo_md = os.path.join(
    carpeta_resultados, "Resultados-ML-0031.md"
)

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(contenido_md))

print("\n[ÉXITO] Archivo generado correctamente:")
print(ruta_archivo_md)
print(encabezado_pie)

print("Rafael Arevalo Machine Learning pandas, NC 0031")

