import pandas as pd
from pathlib import Path

def cargar_datos_cora_original(ruta_data_cora: str | Path):
    """
    Carga el dataset Cora original desde sus archivos crudos
    (cora.content y cora.cites), pensado para EDA y análisis de grafo.
    
    Args:
        ruta_data_cora (str | Path): Ruta a la carpeta data/cora.
        
    Returns:
        paper_ids (pd.Series): IDs de los artículos.
        features (pd.DataFrame): Características textuales binarias.
        labels (pd.Series): Etiquetas de clase.
        df_nodes (pd.DataFrame): DataFrame limpio para EDA.
        cora_cites (pd.DataFrame): Aristas de citación.
    """
    ruta = Path(ruta_data_cora)
    path_cora_content = ruta / "cora.content"
    path_cora_cites = ruta / "cora.cites"

    if not path_cora_content.exists() or not path_cora_cites.exists():
        raise FileNotFoundError(
            "No se encontraron cora.content y/o cora.cites en la carpeta indicada."
        )

    cora_content = pd.read_csv(path_cora_content, sep="\t", header=None)

    paper_ids = cora_content.iloc[:, 0].astype(str)
    features = cora_content.iloc[:, 1:-1]
    labels = cora_content.iloc[:, -1]

    df_nodes = pd.DataFrame({"paper_id": paper_ids, "label": labels})

    cora_cites = pd.read_csv(
        path_cora_cites,
        sep="\t",
        header=None,
        names=["cited_paper_id", "citing_paper_id"],
    )
    cora_cites["cited_paper_id"] = cora_cites["cited_paper_id"].astype(str)
    cora_cites["citing_paper_id"] = cora_cites["citing_paper_id"].astype(str)

    return paper_ids, features, labels, df_nodes, cora_cites


def cargar_datos_cora_enriquecido(ruta_csv: str | Path):
    """
    Carga y prepara el dataset enriquecido de Cora desde el CSV consolidado
    (incluye features topologicas y comunitarias).

    Args:
        ruta_csv (str | Path): Ruta directa al archivo cora_features_completas.csv.

    Returns:
        X (pd.DataFrame): Matriz de características listas para entrenar.
        y (pd.Series): Etiquetas de las clases.
    """
    ruta = Path(ruta_csv)
    df = pd.read_csv(ruta)
    
    # 2. Enviar el ID del artículo al índice para no entrenar con él
    if "paper_id" in df.columns:
        df = df.set_index("paper_id")

    # 3. Identificar y separar la variable objetivo (y)
    posibles_label = ["class_label", "label", "target", "y"]
    label_col = next((col for col in posibles_label if col in df.columns), None)
    
    if label_col is None:
        raise ValueError(
            f"El archivo no contiene una columna de etiqueta reconocida. Se buscó: {posibles_label}"
        )

    y = df[label_col].copy()
    X = df.drop(columns=[label_col])
    
    # 4. Asegurar que la Bolsa de Palabras sea estrictamente numérica entera
    #    (Esto previene definitivamente el error de Scikit-Learn 'ufunc isnan')
    word_cols = [c for c in X.columns if str(c).startswith("word_")]
    X[word_cols] = X[word_cols].astype(int)
    
    return X, y


def cargar_datos_cora(ruta: str | Path):
    """
    Función de compatibilidad.

    - Si recibe una carpeta, delega en cargar_datos_cora_original.
    - Si recibe un archivo, delega en cargar_datos_cora_enriquecido.
    """
    path = Path(ruta)
    if path.is_dir():
        return cargar_datos_cora_original(path)
    return cargar_datos_cora_enriquecido(path)