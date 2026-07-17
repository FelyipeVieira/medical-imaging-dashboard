param([int]$Port = 8501)
$ErrorActionPreference = "Stop"
python -m streamlit run src/app.py --server.port $Port

