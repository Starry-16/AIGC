import sys
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


# =========================
# Kaggle 下载工具
# =========================
def download_kaggle_dataset(dataset, target_dir="./data"):
    os.makedirs(target_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"🔹 Downloading Kaggle dataset: {dataset}")
    api.dataset_download_files(
        dataset,
        path=target_dir,
        unzip=False,
        quiet=False,
    )

    zip_name = dataset.split("/")[-1] + ".zip"
    zip_path = os.path.join(target_dir, zip_name)

    if os.path.exists(zip_path):
        print("🔹 Extracting...")
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(target_dir)
        print("✅ Done")


# =========================
# 占位：非 Kaggle 数据集
# =========================
def download_bach_cello():
    print("⚠️ Bach Cello Suites downloader 尚未实现（原 bash 脚本）")


def download_bach_chorales():
    print("⚠️ Bach Chorales downloader 尚未实现（原 bash 脚本）")


# =========================
# 主逻辑（等价 if / elif）
# =========================
def main():
    if len(sys.argv) < 2:
        print(
            "❌ Missing dataset name\n"
            "Choose from: faces, bricks, recipes, flowers, wines, cellosuites, chorales"
        )
        return

    dataset = sys.argv[1]

    if dataset == "faces":
        download_kaggle_dataset("jessicali9530/celeba-dataset")

    elif dataset == "bricks":
        download_kaggle_dataset("joosthazelzet/lego-brick-images")

    elif dataset == "recipes":
        download_kaggle_dataset("hugodarwood/epirecipes")

    elif dataset == "flowers":
        download_kaggle_dataset("nunenuh/pytorch-challange-flower-dataset")

    elif dataset == "wines":
        download_kaggle_dataset("zynicide/wine-reviews")

    elif dataset == "cellosuites":
        download_bach_cello()

    elif dataset == "chorales":
        download_bach_chorales()

    else:
        print(
            "❌ Invalid dataset name\n"
            "Choose from: faces, bricks, recipes, flowers, wines, cellosuites, chorales"
        )


if __name__ == "__main__":
    main()