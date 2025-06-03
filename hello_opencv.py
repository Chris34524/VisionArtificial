import cv2 as cv
from pathlib import Path

# Ruta de la imagen
img_path = Path("data/sample.jpeg")
img = cv.imread(str(img_path))

if img is None:
    raise FileNotFoundError(f"No se encontró {img_path.resolve()}")

# Procesos sencillos
gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 200)

# Carpeta de salida
out_dir = Path("outputs")
out_dir.mkdir(exist_ok=True)

cv.imwrite(str(out_dir / "gray.jpg"),  gray)
cv.imwrite(str(out_dir / "edges.jpg"), edges)

print("✅ Imágenes generadas en", out_dir.resolve())
