import networkx as nx
import matplotlib.pyplot as plt

# 1. Inisialisasi Graf Tak Berarah
G = nx.Graph()

# 2. Menambahkan Simpul beserta Nilai Heuristik h(n)
nodes_data = {
    "Batavia": 0, "Jacatraweg": 1.3, "Molenvliet": 1.2, "Pintoe Besi": 2.5,
    "Rijswijk": 2.8, "Harmoni": 3.0, "Sawah Besar": 3.5, "Senen": 4.2,
    "Koningsplein": 4.5, "Tanah Abang": 5.0, "Kramat": 5.5, "Menteng": 6.5,
    "Matramanweg": 8.0, "Mr.Cornelis": 10.5, "Asemka": 1.5, "Djembatan Lima": 3.0,
    "Tamarindelaan": 5.5
}

# Mapping warna spesifik dari gambar diagram Anda (Hex Codes)
node_colors_map = {
    "Batavia": "#E13A3E",       # Merah Tua
    "Jacatraweg": "#0C9444",    # Hijau Tua
    "Asemka": "#7EC242",        # Hijau Muda
    "Djembatan Lima": "#F7941E",# Oranye terang
    "Molenvliet": "#1B75BC",    # Biru Utama
    "Harmoni": "#662D91",       # Ungu
    "Rijswijk": "#BE1E2D",      # Merah Cerah
    "Sawah Besar": "#F58220",   # Oranye Halus
    "Pintoe Besi": "#00A651",   # Hijau Daun
    "Senen": "#F9A058",         # Oranye Muda Pastel
    "Koningsplein": "#2E3192",  # Biru Gelap
    "Menteng": "#27AAE1",       # Biru Langit
    "Tanah Abang": "#A04196",   # Ungu Magenta
    "Tamarindelaan": "#8C6239", # Cokelat
    "Kramat": "#92278F",        # Ungu Tua
    "Matramanweg": "#ED1C24",   # Merah Cabai
    "Mr.Cornelis": "#C1272D"    # Merah Gelap Marun
}

for node, h_val in nodes_data.items():
    G.add_node(node, heuristic=h_val, color=node_colors_map.get(node, "#999999"))

# 3. Menambahkan Lintasan Sisi (Edges)
edges_data = [
    ("Djembatan Lima", "Asemka", 1.3, 5),
    ("Asemka", "Molenvliet", 1.2, 5),
    ("Asemka", "Jacatraweg", 1.3, 5),       
    ("Batavia", "Molenvliet", 1.2, 5),      
    ("Jacatraweg", "Pintoe Besi", 2.0, 9),   
    ("Molenvliet", "Sawah Besar", 1.6, 5),
    ("Molenvliet", "Harmoni", 1.5, 6),
    ("Sawah Besar", "Pintoe Besi", 1.5, 4),
    ("Harmoni", "Rijswijk", 0.8, 3),
    ("Harmoni", "Koningsplein", 1.0, 4),
    ("Harmoni", "Tanah Abang", 2.5, 12),
    ("Pintoe Besi", "Senen", 2.4, 9),
    ("Rijswijk", "Senen", 2.0, 10),
    ("Senen", "Kramat", 1.2, 5),
    ("Koningsplein", "Menteng", 1.8, 8),
    ("Menteng", "Kramat", 1.5, 7),           
    ("Menteng", "Tamarindelaan", 1.2, 3),    
    ("Tanah Abang", "Tamarindelaan", 1.5, 7),
    ("Kramat", "Matramanweg", 1.5, 13),
    ("Matramanweg", "Mr.Cornelis", 3.0, 20)
]

for u, v, km, gulden in edges_data:
    if G.has_node(u) and G.has_node(v):
        G.add_edge(u, v, distance=km, cost=gulden)

# 4. Tata Letak Koordinat Posisi Layout (Skala Diperluas Biar Rapi)
pos = {
    "Batavia": (0.0, 5.0),
    "Asemka": (-2.0, 4.3),
    "Djembatan Lima": (-4.5, 4.3),
    "Jacatraweg": (2.0, 4.3),
    "Molenvliet": (-1.0, 3.2),
    "Pintoe Besi": (3.5, 2.3),
    "Sawah Besar": (1.2, 2.7),
    "Harmoni": (-2.0, 1.8),
    "Rijswijk": (0.0, 1.8),
    "Senen": (3.5, 0.8),
    "Koningsplein": (-1.0, 0.5),
    "Menteng": (1.2, 0.3),
    "Tanah Abang": (-3.5, -0.5),
    "Tamarindelaan": (-1.0, -0.8),
    "Kramat": (3.5, -0.8),
    "Matramanweg": (4.5, -2.5),
    "Mr.Cornelis": (5.5, -5.0)
}

# Membuat Offset Posisi Teks (Digeser sedikit ke atas/samping node)
pos_labels = {}
for node, (x, y) in pos.items():
    if node in ["Batavia", "Sawah Besar", "Asemka"]:
        pos_labels[node] = (x, y + 0.35)  # Geser ke Atas
    elif node in ["Pintoe Besi", "Senen", "Kramat", "Matramanweg", "Mr.Cornelis", "Jacatraweg"]:
        pos_labels[node] = (x + 0.65, y)  # Geser ke Samping Kanan
    elif node in ["Djembatan Lima", "Tanah Abang", "Harmoni"]:
        pos_labels[node] = (x - 0.75, y)  # Geser ke Samping Kiri
    else:
        pos_labels[node] = (x, y - 0.40)  # Geser ke Bawah

# 5. Eksekusi Render Gambar
plt.figure(figsize=(14, 11), facecolor="white")
plt.title("Visualisasi Graf Jaringan Trem Batavia 1934", fontsize=15, fontweight='bold', pad=25)

# Gambar Garis Penghubung (Edges)
nx.draw_networkx_edges(G, pos, width=2.5, edge_color='#A6A6A6', alpha=0.85)

# Gambar Lingkaran Stasiun (Nodes) Satuan per Warna
for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos, 
        nodelist=[node], 
        node_color=G.nodes[node]['color'], 
        node_size=550, 
        edgecolors='black', 
        linewidths=1.2
    )

# Gambar Label Nama & Nilai h(n) di Luar Node menggunakan pos_labels
node_labels = {node: f"{node}\n(h={G.nodes[node]['heuristic']})" for node in G.nodes()}
nx.draw_networkx_labels(G, pos_labels, labels=node_labels, font_size=8.5, font_weight='bold', font_family='sans-serif')

# Gambar Atribut Bobot Jalur (Jarak km & Biaya G)
edge_labels = {(u, v): f"{d['distance']} km\n{d['cost']} G" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7.5, font_color='#8C1D1D', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1))

# Konfigurasi Akhir Canvas
plt.axis('off')
plt.xlim(-6.0, 7.5)  # Beri ruang tambahan untuk teks samping kanan/kiri
plt.ylim(-5.5, 6.0)
plt.tight_layout()

# Menyimpan Gambar Beresolusi Tinggi
plt.savefig("graf_trem_batavia_1934.png", format="PNG", dpi=300, bbox_inches='tight')
print("[SUCCESS] Graf revisi warna dan tata letak teks berhasil diperbarui!")
plt.show()

