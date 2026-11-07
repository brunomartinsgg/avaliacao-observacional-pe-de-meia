import os
import sys
from pathlib import Path

DATASETS = [
    "hugobovaretohorsth/censo-escolar-2022-brazil",
    "adilshamim8/predict-students-dropout-and-academic-success",
    "joaoassaoka/taxa-de-abandono-escolar-por-renda-mdia-brasil"
]

def download_kaggle_datasets():
    base_dir = Path(__file__).resolve().parent.parent.parent
    target_dir = base_dir / "dados_brutos" / "kaggle"
    target_dir.mkdir(parents=True, exist_ok=True)
    
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_json.exists() and "KAGGLE_USERNAME" not in os.environ:
        print(f"[AVISO] kaggle.json não encontrado em {kaggle_json}.")
        print("Para baixar via Kaggle API, coloque suas credenciais em ~/.kaggle/kaggle.json ou defina KAGGLE_USERNAME/KAGGLE_KEY.")
        return False
        
    try:
        import kaggle
        for ds in DATASETS:
            print(f"Baixando Kaggle Dataset: {ds} ...")
            kaggle.api.dataset_download_files(ds, path=str(target_dir), unzip=True)
            print(f"[OK] {ds} baixado em {target_dir}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao baixar datasets do Kaggle: {e}")
        return False

if __name__ == "__main__":
    download_kaggle_datasets()
