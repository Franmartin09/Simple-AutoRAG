import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import numpy as np
import os
import matplotlib.cm as cm
from utils.model import get_embedding
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os

def plot_embeddings_3d(data: list[dict], output_path="plots/arxiv_embeddings.png", method="pca", user_input: str = None):
    """
    Visualiza los embeddings en 3D reduciendo dimensionalidad con PCA.
    Cada punto tiene un color distinto y aparece su título en la leyenda (debajo).
    Si se proporciona `user_input`, se añade como punto negro con etiqueta 'User Question'.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    embeddings = np.array([entry["embedding"] for entry in data])
    titles = [entry["title"] for entry in data]

    if user_input:
        user_emb = get_embedding(user_input)
        all_embeddings = np.vstack([embeddings, user_emb])
    else:
        all_embeddings = embeddings

    # Reducción de dimensionalidad
    reducer = PCA(n_components=3)
    reduced = reducer.fit_transform(all_embeddings)

    # Crear figura
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Colores únicos para cada entry
    cmap = cm.get_cmap('tab20', len(data))
    colors = [cmap(i) for i in range(len(data))]

    handles = []

    # Graficar entradas normales
    for i, (x, y, z) in enumerate(reduced[:len(data)]):
        sc = ax.scatter(x, y, z, color=colors[i], s=50, edgecolors='k', label=titles[i])
        handles.append(sc)

    # Si hay user_input, graficar como punto negro
    if user_input:
        user_coord = reduced[-1]
        user_scatter = ax.scatter(
            user_coord[0], user_coord[1], user_coord[2],
            color='black', s=80, marker='X', edgecolors='white', label='User Question'
        )
        handles.append(user_scatter)
        titles.append("User Question")

    # Ejes
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")

    # Título
    plt.suptitle("3D Embedding Visualization (PCA)", fontsize=16)

    # Leyenda
    fig.legend(handles=handles, labels=titles,
               loc='lower center', bbox_to_anchor=(0.5, -0.12),
               fontsize=8, ncol=3, frameon=True)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()



def generate_wordcloud_from_data(data: list[dict], output_path="output/wordcloud.png", field="title"):
    """
    Genera una nube de palabras a partir de los textos del campo especificado ('summary' o 'title').
    
    :param data: Lista de entradas con los textos
    :param output_path: Ruta donde guardar la imagen
    :param field: Campo de texto a usar ('summary' o 'title')
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Concatenar todos los textos
    combined_text = " ".join(entry.get(field, "") for entry in data)

    # Eliminar palabras vacías en inglés
    stopwords = set(STOPWORDS)

    # Crear nube de palabras
    wordcloud = WordCloud(
        width=1600,
        height=800,
        background_color="white",
        stopwords=stopwords,
        colormap="viridis",
        max_words=200
    ).generate(combined_text)

    # Mostrar y guardar imagen
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
