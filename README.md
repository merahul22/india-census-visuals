

## 🇮🇳 India Data Visualisation Dashboard

An interactive web application built using **Streamlit** and **Plotly** to visualize state-wise and district-wise data across India with dynamic filters and beautiful map-based charts.


---

### 🔧 Features

* Sidebar controls for selecting state and metrics.
* Bubble map with:

  * Size representing **primary parameter**
  * Color representing **secondary parameter**
* Support for viewing **overall India** or a specific state.
* Responsive layout using Streamlit + Plotly Mapbox.

---

### 📁 Folder Structure

```
.
├── app.py                     # Main Streamlit application
├── final_df.csv              # Processed dataset
├── requirements.txt          # Python dependencies
└── .streamlit/
    └── config.toml           # Theme and server configuration
```

---

### 🛠️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/india-data-visualisation.git
cd india-data-visualisation
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Streamlit app**

```bash
streamlit run app.py
```

---

### 🧪 Sample Config (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
enableCORS = false
```

---

### 📊 Data Format (`final_df.csv`)

The CSV should contain columns like:

* `State`
* `District`
* `Latitude`, `Longitude`
* Multiple metrics (e.g., population, literacy, healthcare index)

---





