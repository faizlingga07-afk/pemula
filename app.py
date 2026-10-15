import streamlit as st

# Judul Aplikasi
st.title("Aplikasi Interaktif Pertama")

# Input Teks dari User
nama = st.text_input("Masukkan nama kamu:")

# Tombol Aksi
if st.button("Sapa Saya"):
    if nama:
        st.success(f"Halo, {nama}! Selamat datang di aplikasi Streamlit.")
    else:
        st.warning("Silakan masukkan nama terlebih dahulu.")


# ==========================================
# 1. PERSIAPAN & MATPLOTLIB DASAR
# ==========================================
from IPython.display import HTML, display, Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px

# Menampilkan teks berjalan (Marquee)
display(HTML("""
<div class="marquee-text">
SEMOGA ANTRIAN BBM SEGERA BERAKHIR
</div>
"""))

# Contoh Grafik Dasar dengan Style
plt.style.use('classic')
x = np.linspace(0, 10, 100)
y = np.cos(x)
plt.plot(x, y)
plt.title("Contoh Grafik dengan Style")
plt.show()

# Grafik Simple
x = [1, 3, 7, 8, 12]
y = [3, 5, 9, 19, 12]
plt.plot(x, y)
plt.title("GRAFIK SIMPLE")
plt.xlabel('nilaiX')
plt.ylabel('NilaiY')
plt.show()

# Scatter Sederhana dengan Numpy Random
from numpy.random import rand
x, y = rand(2, 100)
plt.scatter(x, y)
plt.show()


# ==========================================
# 2. VISUALISASI DATASET 1 (PENJUALAN)
# ==========================================
url1 = "https://raw.githubusercontent.com/Alam-A99/DATAAKSI/refs/heads/main/dataset_fiskal_97_hipoFull.csv"
df = pd.read_csv(url1)
df['total'] = df[['jan', 'feb', 'mar', 'apr']].sum(axis=1)

# A. Bar Chart Penjualan (Matplotlib)
plt.figure(figsize=(8, 5))
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei']
penjualan = [150, 200, 180, 250, 125]
plt.barh(bulan, penjualan, color='blue')
plt.title('Penjualan per Bulan')
plt.xlabel('Jumlah')
plt.ylabel('Bulan')
for i, nilai in enumerate(penjualan):
    plt.text(nilai + 2, i, str(nilai), va='center', fontsize=14, color='red')
plt.show()

# B. Bar Chart Penjualan (Seaborn)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
df_sorted = df.sort_values('total', ascending=False)
sns.barplot(data=df_sorted, x='nama', y='total', palette='viridis')
plt.title('Total Penjualan per Orang', fontsize=12)
plt.xlabel('Nama Karyawan')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# C. Bar Chart + Garis Tren
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Juli']
penjualan = [150, 200, 180, 250, 125, 200, 130]
plt.figure(figsize=(8, 4))
sns.barplot(x=bulan, y=penjualan, palette='muted')
plt.plot(range(len(bulan)), penjualan, color='red', marker='o', linestyle='-', linewidth=2, label='Garis Tren')
plt.title('Penjualan per Bulan dengan Garis Tren', fontsize=12, fontweight='bold')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.legend()
plt.tight_layout()
plt.show()

# D. Pie Chart (Proporsi Penjualan)
plt.figure(figsize=(5, 5))
total_per_bulan = df[['jan', 'feb', 'mar', 'apr']].sum()
plt.pie(total_per_bulan, labels=total_per_bulan.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('muted'))
plt.title('Proporsi Penjualan per Bulan', fontsize=12)
plt.tight_layout()
plt.show()

# E. Stack Plot (Stacked Bar Chart)
plt.figure(figsize=(8, 5))
df.set_index('nama')[['jan', 'feb', 'mar', 'apr']].plot(kind='bar', stacked=True, colormap='Pastel1', ax=plt.gca())
plt.title('Komposisi Penjualan Bulanan per Orang (Stacked)', fontsize=12)
plt.xlabel('Nama Karyawan')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.legend(title='Bulan')
plt.tight_layout()
plt.show()

# F. Histogram (Distribusi Total Penjualan)
plt.figure(figsize=(6, 4))
sns.histplot(df['total'], bins=5, kde=True, color='teal')
plt.title('Distribusi Frekuensi Total Penjualan', fontsize=12)
plt.xlabel('Range Total Penjualan')
plt.ylabel('Jumlah Karyawan (Frekuensi)')
plt.tight_layout()
plt.show()

# G. Scatter Plot & Subplot
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('Dashboard Analisis Sederhana', fontsize=14, fontweight='bold')
sns.scatterplot(data=df, x='mar', y='apr', s=80, color='purple', ax=axes[0])
axes[0].set_title('Korelasi Maret vs April')
axes[0].set_xlabel('Maret')
axes[0].set_ylabel('April')
sns.histplot(df['total'], bins=10, kde=True, color='orange', ax=axes[1])
axes[1].set_title('Distribusi Total Penjualan')
axes[1].set_xlabel('Total')
axes[1].set_ylabel('Frekuensi')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# H. Fill Between & Fluktuasi
x_index = np.arange(len(df))
plt.figure(figsize=(8, 4))
plt.plot(x_index, df['jan'], marker='o', color='blue', label='Januari')
plt.plot(x_index, df['feb'], marker='s', color='orange', label='Februari')
plt.fill_between(x_index, df['jan'], df['feb'], color='gray', alpha=0.3, label='Selisih Jan-Feb')
plt.title('Fluktuasi Penjualan: Januari vs Februari (Fill Between)', fontsize=12)
plt.xlabel('Indeks Karyawan')
plt.ylabel('Jumlah Penjualan')
plt.xticks(x_index, df['nama'], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================
# 3. PLOTLY EXPRESS (Interaktif)
# ==========================================
df_plot = df.melt(id_vars='nama', value_vars=['jan', 'mar'], var_name='bulan', value_name='penjualan')
fig = px.line(
    df_plot, 
    x='nama', 
    y='penjualan', 
    color='bulan', 
    symbol='bulan', 
    symbol_sequence=['circle', 'triangle-up'], 
    color_discrete_sequence=['royalblue', 'crimson'], 
    markers=True, 
    title='<b>Perbandingan Penjualan: Januari vs Maret</b>', 
    labels={'penjualan': 'Jumlah Penjualan', 'nama': 'Nama Karyawan', 'bulan': 'Bulan'}
)
fig.update_layout(width=800, height=450, title_x=0.5, hovermode='x unified')
fig.show()


# ==========================================
# 4. VISUALISASI DATASET 2 (DATA FISKAL & SOSIAL)
# ==========================================
url2 = "https://raw.githubusercontent.com/Alam-A99/DATAAKSI/refs/heads/main/dataset_fiskal_97_hipoFull.csv"
df1 = pd.read_csv(url2)
df1.columns = df1.columns.str.strip()

# A. Distribusi Kemiskinan
sns.set_theme(style="whitegrid", font_scale=1.1, palette="muted")
plt.figure(figsize=(8, 4))
sns.histplot(data=df1, x='KEMISKINAN', bins=30, kde=True, color='coral')
plt.title('Distribusi Tingkat Kemiskinan di Seluruh Daerah', fontsize=12, fontweight='bold')
plt.xlabel('Tingkat Kemiskinan (%)')
plt.ylabel('Frekuensi (Jumlah Daerah)')
plt.tight_layout()
plt.show()

# B. Boxplot IPM
plt.figure(figsize=(6, 5))
sns.boxplot(data=df1, y='IPM', color='skyblue', width=0.4)
plt.title('Sebaran Indeks Pembangunan Manusia (IPM)', fontsize=12, fontweight='bold')
plt.ylabel('Nilai IPM (0-100)')
plt.tight_layout()
plt.show()

# C. Matriks Korelasi (Heatmap)
plt.figure(figsize=(10, 8))
kolom_korelasi = ['PAD', 'KEMISKINAN', 'IPM', 'bm_pendidikan', 'bm_kesehatan', 'PENGANGGURAN']
df_korelasi = df1[kolom_korelasi]
corr_matrix = df_korelasi.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, cbar_kws={"shrink": .8})
plt.title('Matriks Korelasi Variabel Fiskal & Sosial', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# D. Joint Plot (PAD vs Kemiskinan)
g = sns.jointplot(data=df1, x='PAD', y='KEMISKINAN', kind='reg', color='purple', height=6, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
g.fig.suptitle('Analisis Mendalam: PAD vs Tingkat Kemiskinan', y=1.02, fontsize=14, fontweight='bold')
plt.show()

# E. FacetGrid (Kategori PAD)
df1['Kategori_PAD'] = pd.qcut(df1['PAD'], q=3, labels=['Rendah', 'Sedang', 'Tinggi'])
sns.relplot(data=df1, x='bm_pendidikan', y='IPM', hue='Kategori_PAD', col='Kategori_PAD', kind='scatter', height=4, aspect=1.2, palette='Set2')
plt.subplots_adjust(top=0.85)
plt.suptitle('Hubungan Belanja Pendidikan dan IPM berdasarkan Kategori PAD', fontsize=14)
plt.show()


# ==========================================
# 5. DASHBOARD INTERAKTIF (IPYWIDGETS + PLOTLY)
# ==========================================
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from scipy import stats

df1['Tahun'] = df1['Tahun'].astype(str)
variabel_terikat = ['KEMISKINAN', 'PENGANGGURAN', 'KETIMPANGAN', 'IPM', 'PE']
variabel_bebas = [col for col in df1.columns if col not in variabel_terikat + ['Kota', 'Tahun', 'Kategori_PAD']]

# Widget Setup
widget_kota = widgets.SelectMultiple(
    options=sorted(df1['Kota'].unique().tolist()),
    value=[sorted(df1['Kota'].unique().tolist())[0]],
    description='Pilih Daerah:',
    rows=8,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

widget_x = widgets.SelectMultiple(
    options=variabel_bebas,
    value=[variabel_bebas[0], variabel_bebas[1]] if len(variabel_bebas) >= 2 else [variabel_bebas[0]],
    description='Variabel Bebas (X):',
    rows=6,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

widget_y = widgets.Dropdown(
    options=variabel_terikat,
    value='IPM',
    description='Variabel Terikat (Y):',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

def buat_dashboard_regresi(kota_list, var_x_list, var_y):
    if not kota_list:
        print("! Silakan pilih minimal satu daerah.")
        return
    if not var_x_list:
        print("! Silakan pilih minimal satu variabel bebas.")
        return

    var_x_list = list(var_x_list)
    n_x = len(var_x_list)
    df_filter = df1[df1['Kota'].isin(kota_list)].copy()

    regresi_results = []
    for var_x in var_x_list:
        x_data = df_filter[var_x].values
        y_data = df_filter[var_y].values
        mask = ~(np.isnan(x_data) | np.isnan(y_data))
        x_clean, y_clean = x_data[mask], y_data[mask]
        
        if len(x_clean) < 2:
            continue
            
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_clean, y_clean)
        r_squared = r_value ** 2
        
        if abs(r_value) >= 0.8: kekuatan = "Sangat Kuat"
        elif abs(r_value) >= 0.6: kekuatan = "Kuat"
        elif abs(r_value) >= 0.4: kekuatan = "Sedang"
        elif abs(r_value) >= 0.2: kekuatan = "Lemah"
        else: kekuatan = "Sangat Lemah"
            
        arah = "Positif (+)" if slope > 0 else "Negatif (-)"
        
        regresi_results.append({
            'variabel': var_x, 'slope': slope, 'intercept': intercept,
            'r_squared': r_squared, 'r_value': r_value, 'p_value': p_value,
            'kekuatan': kekuatan, 'arah': arah, 'x_clean': x_clean, 'y_clean': y_clean
        })

    if not regresi_results:
        print("! Tidak ada hasil regresi yang valid.")
        return

    fig = make_subplots(
        rows=2, cols=n_x + 1,
        specs=[
            [{"type": "xy"}] * n_x + [{"type": "table"}],
            [{"type": "xy", "colspan": n_x}] + [None] * (n_x - 1) + [{"type": "xy"}]
        ],
        subplot_titles=(
            [f"Regresi: {reg['variabel']} vs {var_y}" for reg in regresi_results] +
            [f"Ranking {var_y}", "Rata-rata per Daerah", "Tren Tahunan"]
        ),
        vertical_spacing=0.12, horizontal_spacing=0.08
    )

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    for idx, reg in enumerate(regresi_results):
        var_x = reg['variabel']
        color = colors[idx % len(colors)]
        
        for kota in kota_list:
            df_kota = df_filter[df_filter['Kota'] == kota]
            fig.add_trace(
                go.Scatter(x=df_kota[var_x], y=df_kota[var_y], mode='markers', name=kota,
                           marker=dict(size=9, opacity=0.7, color=color, line=dict(width=1, color='white')),
                           showlegend=(idx == 0)),
                row=1, col=idx + 1
            )
            
        x_line = np.array([reg['x_clean'].min(), reg['x_clean'].max()])
        y_line = reg['slope'] * x_line + reg['intercept']
        fig.add_trace(
            go.Scatter(x=x_line, y=y_line, mode='lines', name=f"{var_x} (R2={reg['r_squared']:.3f})",
                       line=dict(color='red', width=2, dash='dash'), showlegend=True),
            row=1, col=idx + 1
        )

        stats_text = (f"<b>R2:</b> {reg['r_squared']:.4f}<br>"
                      f"<b>Korelasi:</b> {reg['kekuatan']} {reg['arah']}<br>"
                      f"<b>p-value:</b> {reg['p_value']:.4f}")
        
        xref_val = "x domain" if idx == 0 else f"x{idx + 1} domain"
        yref_val = "y domain" if idx == 0 else f"y{idx + 1} domain"
        
        fig.add_annotation(
            text=stats_text, xref=xref_val, yref=yref_val, x=0.05, y=0.95,
            showarrow=False, bgcolor="rgba(255, 255, 255, 0.9)", bordercolor="gray",
            borderwidth=1, borderpad=6, font=dict(size=10, family="monospace"), align="left"
        )
        
        fig.update_xaxes(title_text=var_x, row=1, col=idx + 1)
        if idx == 0: fig.update_yaxes(title_text=var_y, row=1, col=idx + 1)

    # Tabel Ranking
    rank_df = df_filter.groupby('Kota')[var_y].mean().round(2).reset_index()
    rank_df = rank_df.rename(columns={var_y: f'Rata-rata {var_y}'})
    rank_df = rank_df.sort_values(by=f'Rata-rata {var_y}', ascending=False).reset_index(drop=True)
    rank_df.index = rank_df.index + 1
    rank_df = rank_df.reset_index().rename(columns={'index': 'Peringkat'})

    warna_zebra = ['#ecf0f1' if i % 2 == 0 else '#ffffff' for i in range(len(rank_df))]
    warna_header_cells = ['#FFD700' if i == 0 else '#COCOCO' if i == 1 else '#CD7F32' if i == 2 else warna_zebra[i] for i in range(len(rank_df))]

    fig.add_trace(
        go.Table(
            header=dict(values=list(rank_df.columns), fill_color='#2c3e50', align='center', font=dict(color='white', size=11)),
            cells=dict(values=[rank_df[col] for col in rank_df.columns], fill_color=[['#34495e'] * len(rank_df), warna_header_cells, warna_header_cells], align='center', font=dict(size=10))
        ),
        row=1, col=n_x + 1
    )

    # Bar Chart Grouped
    bar_data = df_filter.groupby('Kota')[var_x_list].mean().round(2).reset_index()
    for idx, var_x in enumerate(var_x_list):
        fig.add_trace(go.Bar(x=bar_data['Kota'], y=bar_data[var_x], name=var_x, marker_color=colors[idx % len(colors)], showlegend=True), row=2, col=1)
    
    fig.update_xaxes(title_text="Daerah", row=2, col=1, tickangle=-45)
    fig.update_yaxes(title_text="Nilai Rata-rata", row=2, col=1)

    # Line Chart Tren Tahunan
    trend_data = df_filter.groupby('Tahun')[var_x_list].mean().round(2).reset_index()
    for idx, var_x in enumerate(var_x_list):
        fig.add_trace(go.Scatter(x=trend_data['Tahun'], y=trend_data[var_x], mode='lines+markers', name=var_x, line=dict(color=colors[idx % len(colors)], width=2), marker=dict(size=8), showlegend=True), row=2, col=n_x + 1)
        
    fig.update_xaxes(title_text="Tahun", row=2, col=n_x + 1)
    fig.update_yaxes(title_text="Nilai Rata-rata", row=2, col=n_x + 1)

    fig.update_layout(height=900, width=1300, title_text=f"Analisis Regresi Multiple: Pengaruh {', '.join(var_x_list)} terhadap {var_y}", title_x=0.5, title_font=dict(size=15), showlegend=True, legend_title_text="Variabel/Daerah", margin=dict(l=60, r=40, t=100, b=80), barmode='group')
    fig.show()

# Tampilkan UI Widget
print("DASHBOARD ANALISIS REGRESI MULTIPLE")
print("Pilih daerah, beberapa variabel bebas (X), dan variabel terikat (Y):\n")
widgets.interact(buat_dashboard_regresi, kota_list=widget_kota, var_x_list=widget_x, var_y=widget_y)