"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
path_0 = r'files\input\tbl0.tsv'
path_2 = r'files\input\tbl2.tsv'
df_0 = pd.read_csv(path_0, sep='\t', header=0)
df_2 = pd.read_csv(path_2, sep='\t', header=0)

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    df_final = df_0.join(df_2.set_index('c0'),on='c0')

    return df_final.groupby('c1').apply(lambda x: x['c5b'].sum())

print(pregunta_13())




