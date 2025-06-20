import pandas as pd
from django.db import transaction
from insumos.models import Insumo, Categoria
from proveedor.models import Proveedor
from establecimiento.models import Campo, Lote
from compras.models import Compra, CompraDetalle
from Ordenes.models import Ordenes, OrdenesDetalle, OrdenesLote

def run():
    # Cargar el archivo Excel con todas las hojas
    # file_path = r"C:\Proyectos\Mascota\datos.xlsx"  # La r evita problemas con las barras invertidas
    
    file_path = r"/home/joaquin/Documentos/Proyectos/Mascota/datos.xlsx"  # La r evita problemas con las barras invertidas
    
    try:
        # Carga todas las pestañas
        sheets = pd.read_excel(file_path, sheet_name=None)
        
        # --- Cargar Categorías ---
        print("Procesando categorias...")
        df_categoria = sheets["Categoria"]  # Pestaña llamada "Categoria"
        categorias_a_crear = []
        categorias_existentes = {c.nombre: c for c in Categoria.objects.all()}  # Cachear existentes
        
        for _, row in df_categoria.iterrows():  # El _ es para que ignore el indice
            if row["nombre"] not in categorias_existentes:
                categorias_a_crear.append(Categoria(nombre=row["nombre"]))
        
        if categorias_a_crear:
            Categoria.objects.bulk_create(categorias_a_crear)
        
        print(f"[OK] {len(categorias_a_crear)} Categorias nuevas cargadas.")
        
        # --- Cargar Proveedores ---
        print("Procesando proveedores...")
        df_proveedor = sheets["Proveedor"]  
        
        proveedores_a_crear = []
        proveedores_existentes = {p.nombre: p for p in Proveedor.objects.all()}
        
        for _, row in df_proveedor.iterrows():
            if row["nombre"] not in proveedores_existentes:
                proveedores_a_crear.append(Proveedor(nombre=row["nombre"],cuit=row["cuit"]))
        
        if proveedores_a_crear:
            Proveedor.objects.bulk_create(proveedores_a_crear)
        
        print(f"[OK] {len(proveedores_a_crear)} Proveedores nuevos cargados.")
        
        # --- Cargar Campos ---
        print("Procesando campos...")
        df_campo = sheets["Campos"]  
        
        campos_a_crear = []
        campos_existentes = {p.nombre: p for p in Campo.objects.all()}
        
        for _, row in df_campo.iterrows():
            if row["nombre"] not in campos_existentes:
                campos_a_crear.append(Campo(nombre=row["nombre"],localidad=row["localidad"]))
        
        if campos_a_crear:
            Campo.objects.bulk_create(campos_a_crear)
        
        print(f"[OK] {len(campos_a_crear)} campos nuevos cargados.")

        # --- Cargar Lotes ---
        print("Procesando lotes...")
        df_lote = sheets["Lotes"]  
        
        lotes_a_crear = []
        lotes_existentes = {p.nombre: p for p in Lote.objects.all()}
        campos_existentes = {p.nombre: p for p in Campo.objects.all()}
        for _, row in df_lote.iterrows():
            if row["nombre"] not in lotes_existentes:
                # car = campos_existentes.get("La Esmeralda")
                # print(car.nombre)
                campo_nombre = str(row["campo"])  
                campo = campos_existentes.get(campo_nombre)
                lotes_a_crear.append(Lote(nombre=row["nombre"],superficie=row["superficie"],campo=campo))
        
        if lotes_a_crear:
            Lote.objects.bulk_create(lotes_a_crear)
        
        print(f"[OK] {len(lotes_a_crear)} lotes nuevos cargados.")

        # --- Cargar Insumos ---
        print("Procesando insumos...")
        df_insumo = sheets["Insumos"]
        
        # Refrescar FK después de cargar categorías y proveedores
        categorias_existentes = {c.nombre: c for c in Categoria.objects.all()}
        proveedores_existentes = {p.nombre: p for p in Proveedor.objects.all()}
        insumos_existentes = {i.nombre: i for i in Insumo.objects.all()}
        
        insumos_a_crear = []
        errores = 0
        
        def clean_text(text):
            """Limpia caracteres Unicode problemáticos"""
            if not isinstance(text, str):
                return text
                
            # Reemplazar caracteres surrogate con un espacio
            clean_text = ""
            for char in text:
                try:
                    # Si el carácter puede ser codificado en ASCII, mantenlo
                    char.encode('ascii')
                    clean_text += char
                except UnicodeEncodeError:
                    # Si no, sustitúyelo por un espacio
                    clean_text += ' '
            
            return clean_text
        
        for index, row in df_insumo.iterrows():
            if row["nombre"] not in insumos_existentes:
                try:
                    # Limpiar los textos
                    nombre = clean_text(str(row["nombre"]))
                    codigo = clean_text(str(row["codigo"])) if isinstance(row["codigo"], str) else row["codigo"]
                    unidad_medida = clean_text(str(row["unidad_medida"]))
                    cat_nombre = clean_text(str(row["categoria"]))
                    prov_nombre = clean_text(str(row["proveedor"]))
                    
                    # Buscar categoría y proveedor
                    categoria = categorias_existentes.get(cat_nombre)
                    proveedor = proveedores_existentes.get(prov_nombre)
                    
                    if categoria and proveedor:
                        insumos_a_crear.append(Insumo(
                            codigo=codigo,
                            nombre=nombre,
                            unidad_medida=unidad_medida,
                            cantidad=row["cantidad"],
                            proveedor=proveedor,
                            categoria=categoria
                        ))
                    else:
                        print(f"[AVISO] No se encontro categoria o proveedor para: {nombre}")
                        errores += 1
                except Exception as e:
                    print(f"[ERROR] En fila {index+2}: {str(e)}")
                    errores += 1
        
        # Cargar insumos en una sola transacción
        with transaction.atomic():
            if insumos_a_crear:
                Insumo.objects.bulk_create(insumos_a_crear)
        
        print(f"[OK] {len(insumos_a_crear)} Insumos nuevos cargados.")
        if errores > 0:
            print(f"[AVISO] Se encontraron {errores} problemas durante la importacion.")

        # --- Cargar Compras ---
        print("Procesando compras...")
        df_compra = sheets["Compras"]  
        
        compras_a_crear = []
        compras_existentes = {p.id: p for p in Compra.objects.all()}

        for _, row in df_compra.iterrows():
            
            if row["indice"] not in compras_existentes:

                compras_a_crear.append(Compra(
                    fecha=row["fecha"],
                    ciclo=row["ciclo"],
                    empresa=row["empresa"]
                    )
                )
        
        if compras_a_crear:
            Compra.objects.bulk_create(compras_a_crear)
        
        print(f"[OK] {len(compras_a_crear)} compras nuevos cargados.")

        # --- Cargar Ordenes ---
        print("Procesando ordenes...")
        df_ordenes = sheets["Ordenes"]  
        
        ordenes_a_crear = []
        ordenes_existentes = {p.id: p for p in Ordenes.objects.all()}

        for _, row in df_ordenes.iterrows():
            
            if row["indice"] not in ordenes_existentes:

                ordenes_a_crear.append(Ordenes(
                    fecha=row["fecha"]
                    )
                )
        
        if ordenes_a_crear:
            Ordenes.objects.bulk_create(ordenes_a_crear)
        
        print(f"[OK] {len(ordenes_a_crear)} ordenes nuevas cargados.")

        # --- Cargar Ordenes Detalle  ---
        print("Procesando ordenesDetalle...")
        df_ordenes = sheets["Ordenes_Detalle"]  
        
        ordenes_detalle_a_crear = []
        ordenes_detalle_existentes = {p.id: p for p in OrdenesDetalle.objects.all()}

        ordenes_existentes = {p.id: p for p in Ordenes.objects.all()}
        insumos_existentes = {p.id: p for p in Insumo.objects.all()}
        
        for _, row in df_ordenes.iterrows():
            
            if row["indice"] not in ordenes_detalle_existentes:
                insumo_id = int(str(row["insumo_id"]))
                insumo = insumos_existentes.get(insumo_id)
                
                orden_id = int(str(row["orden_id"]))
                orden = ordenes_existentes.get(orden_id)
                
                ordenes_detalle_a_crear.append(OrdenesDetalle(
                    orden=orden,
                    insumo=insumo,
                    cantidad=row["cantidad"]
                    )
                )
        
        if ordenes_detalle_a_crear:
            OrdenesDetalle.objects.bulk_create(ordenes_detalle_a_crear)
        
        print(f"[OK] {len(ordenes_detalle_a_crear)} ordenes detalle nuevas cargados.")


        # --- Cargar Ordenes Lote  ---
        print("Procesando ordenesLote...")
        df_lote = sheets["Ordenes_Lote"]  
        
        ordenes_lote_a_crear = []
        ordenes_lote_existentes = {p.id: p for p in OrdenesLote.objects.all()}

        ordenes_existentes = {p.id: p for p in Ordenes.objects.all()}
        lotes_existentes = {p.id: p for p in Lote.objects.all()}

        for _, row in df_lote.iterrows():
            
            if row["indice"] not in ordenes_lote_existentes:
                lote_id = int(str(row["lote_id"]))
                lote = lotes_existentes.get(lote_id)
                
                orden_id = int(str(row["orden_id"]))
                orden = ordenes_existentes.get(orden_id)
                
                ordenes_lote_a_crear.append(OrdenesLote(
                    orden=orden,
                    lote=lote
                    )
                )
        
        if ordenes_lote_a_crear:
            OrdenesLote.objects.bulk_create(ordenes_lote_a_crear)
        
        print(f"[OK] {len(ordenes_lote_a_crear)} ordenes lote nuevas cargados.")



        # --- Cargar ComprasDetalle ---
        print("Procesando comprasDetalle...")
        df_compra = sheets["Compras_Detalle"]  
        
        comprasDetalle_a_crear = []
        comprasDetalle_existentes = {p.id: p for p in CompraDetalle.objects.all()}
        compras_existentes = {p.id: p for p in Compra.objects.all()}
        insumos_existentes = {p.nombre: p for p in Insumo.objects.all()}
        
        for _, row in df_compra.iterrows():
            
            if row["indice"] not in comprasDetalle_existentes:
                insumo_id = str(row["descripcion"])
                insumo = insumos_existentes.get(insumo_id)
                compra_id = row["id_compra"]
                compra = compras_existentes.get(compra_id)
                comprasDetalle_a_crear.append(CompraDetalle(
                    compra=compra,
                    insumo=insumo,
                    precio=row["precio"],
                    cantidad=row["cantidad"]
                    )
                )
        
        if comprasDetalle_a_crear:
            CompraDetalle.objects.bulk_create(comprasDetalle_a_crear)
        
        print(f"[OK] {len(comprasDetalle_a_crear)} comprasDetalle nuevos cargados.")
        
    except Exception as e:
        print(f"[ERROR] Error general: {str(e)}")


