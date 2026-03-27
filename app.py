import streamlit as st
import pandas as pd

st.title("Mi Primera Tabla de Datos")

# 1. Creamos los datos (como un diccionario)
datos = {
    "Emprendimiento": ["Logística IA", "Robótica Senior", "Reciclaje Litio", "Streaming B2B"],
    "Origen": ["China", "China", "Chile", "China"],
    "Inversión (USD)": [500000, 750000, 300000, 450000],
    "Estado": ["Activo", "En Pausa", "Planificación", "Activo"]
}

# 2. Convertimos los datos en un DataFrame (Tabla) de Pandas
df = pd.DataFrame(datos)

# 3. Mostramos la tabla en Streamlit
st.subheader("Lista de Proyectos 2026")
st.table(df) # Esta es una tabla estática y bonita

# 4. Mostramos una tabla interactiva
st.subheader("Tabla Interactiva (puedes ordenar las columnas)")
st.dataframe(df)  
# Filtro interactivo
opcion_estado = st.selectbox("Filtrar por Estado:", df["Estado"].unique())
tabla_filtrada = df[df["Estado"] == opcion_estado]

st.write(f"Viendo proyectos en estado: {opcion_estado}")
st.dataframe(tabla_filtrada)

# 2. Agregar el Gráfico de Barras
st.subheader("Visualización: Inversión por Proyecto")

# Aquí le decimos: usa la columna 'Emprendimiento' para el eje X 
# y 'Inversión (USD)' para el eje Y
st.bar_chart(data=df, x="Emprendimiento", y="Inversión (USD)")

# 3. Un extra: Gráfico de Áreas (si quieres ver tendencia o volumen)
st.subheader("Vista de Volumen")
st.area_chart(data=df, x="Emprendimiento", y="Inversión (USD)")

# agregamos etiquetas de datos a los gráficos
import matplotlib.pyplot as plt
st.subheader("Gráfico de Barras con Etiquetas")
fig, ax = plt.subplots()
ax.bar(df["Emprendimiento"], df["Inversión (USD)"], color='skyblue')
ax.set_xlabel("Emprendimiento")
ax.set_ylabel("Inversión (USD)")
st.pyplot(fig)


