# Reporte de Análisis de Vehículos - Pandas

`Rafael Arevalo Machine Learning pandas, NC 0031`

## 1. DataFrame Convertido

```text
       Marca   Modelo  Anio
0     Toyota  Corolla  2020
1       Ford    Focus  2019
2      Honda    Civic  2021
3     Nissan   Sentra  2018
4  Chevrolet    Spark  2022
5      Mazda        3  2020
```

## 2.1 Primeras Filas (head)

```text
    Marca   Modelo  Anio
0  Toyota  Corolla  2020
1    Ford    Focus  2019
```

## 2.2 Últimas Filas (tail)

```text
       Marca Modelo  Anio
4  Chevrolet  Spark  2022
5      Mazda      3  2020
```

## 2.3 Dimensiones (Filas, Columnas)

```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna

```text
Marca       str
Modelo      str
Anio      int64
dtype: object
```

## 2.5 Información General (info)

```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Marca   6 non-null      str  
 1   Modelo  6 non-null      str  
 2   Anio    6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la columna Anio

```text
count       6.000000
mean     2020.000000
std         1.414214
min      2018.000000
25%      2019.250000
50%      2020.000000
75%      2020.750000
max      2022.000000
Name: Anio, dtype: float64
```

## 4. Orden Ascendente por Anio

```text
       Marca   Modelo  Anio
3     Nissan   Sentra  2018
1       Ford    Focus  2019
0     Toyota  Corolla  2020
5      Mazda        3  2020
2      Honda    Civic  2021
4  Chevrolet    Spark  2022
```

## 5. Orden Descendente por Anio

```text
       Marca   Modelo  Anio
4  Chevrolet    Spark  2022
2      Honda    Civic  2021
5      Mazda        3  2020
0     Toyota  Corolla  2020
1       Ford    Focus  2019
3     Nissan   Sentra  2018
```

`Rafael Arevalo Machine Learning pandas, NC 0031`