import pandas as pd
from django.db import transaction
from insumos.models import Insumo, Categoria
from proveedor.models import Proveedor

# Cargar el archivo Excel con todas las hojas
file_path = "C:\Proyectos\Mascota\datos.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)  # Carga todas las pestañas

# --- Cargar Categorías ---
print("hola")
df_categoria = sheets[2]  # Pestaña número 2
print("---------------")
print(f"soy el print... {df_categoria}")

categorias_a_crear = []
categorias_existentes = {c.nombre: c for c in Categoria.objects.all()}  # Cachear existentes

for _, row in df_categoria.iterrows(): # El _ es para que ignore el indice
    if row["nombre"] not in categorias_existentes:
        categorias_a_crear.append(Categoria(nombre=row["nombre"]))

if categorias_a_crear:
    Categoria.objects.bulk_create(categorias_a_crear)

print(f"✅ {len(categorias_a_crear)} Categorías nuevas cargadas.")

# # --- Cargar Proveedores ---
# df_proveedor = sheets[3]  # Pestaña número 3

# proveedores_a_crear = []
# proveedores_existentes = {p.nombre: p for p in Proveedor.objects.all()}

# for _, row in df_proveedor.iterrows():
#     if row["nombre"] not in proveedores_existentes:
#         proveedores_a_crear.append(Proveedor(nombre=row["nombre"]))

# if proveedores_a_crear:
#     Proveedor.objects.bulk_create(proveedores_a_crear)

# print(f"✅ {len(proveedores_a_crear)} Proveedores nuevos cargados.")

# # --- Cargar Insumos ---
# df_insumo = sheets[1]  # Pestaña número 1

# df_insumo = df_insumo.rename(columns={
#     "codigo": "codigo",
#     "nombre": "nombre",
#     "unidad_medida": "unidad_medida",
#     "cantidad": "cantidad",
#     "proveedor": "proveedor",
#     "categoria": "categoria",
# })

# # Refrescar FK después de cargar categorías y proveedores
# categorias_existentes = {c.nombre: c for c in Categoria.objects.all()}
# proveedores_existentes = {p.nombre: p for p in Proveedor.objects.all()}

# insumos_a_crear = []

# for _, row in df_insumo.iterrows():
#     categoria = categorias_existentes.get(row["categoria"])
#     proveedor = proveedores_existentes.get(row["proveedor"])

#     if categoria and proveedor:
#         insumos_a_crear.append(Insumo(
#             codigo=row["codigo"],
#             nombre=row["nombre"],
#             unidad_medida=row["unidad_medida"],
#             cantidad=row["cantidad"],
#             proveedor=proveedor,
#             categoria=categoria
#         ))
#     else:
#         print(f"⚠️ No se encontró la categoría o proveedor para el insumo: {row['nombre']}")

# # Cargar insumos en una sola transacción
# with transaction.atomic():
#     if insumos_a_crear:
#         Insumo.objects.bulk_create(insumos_a_crear)

# print(f"✅ {len(insumos_a_crear)} Insumos nuevos cargados.")
