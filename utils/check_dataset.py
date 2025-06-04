from pathlib import Path
import cv2

root = Path("data/raw")
classes = [p.name for p in root.iterdir() if p.is_dir()]
print("Clases encontradas:", classes)

for cls in classes:
    imgs = list((root / cls).glob("*.*"))
    print(f"  {cls}: {len(imgs)} imágenes")
    if imgs:
        sample = cv2.imread(str(imgs[0]))
        print("    Tamaño ejemplo:",
              sample.shape if sample is not None else "⚠️ error de lectura")
