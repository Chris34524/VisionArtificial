# Vision-Inspector 🚗🔍
Prototipo de inspección visual para la línea de ensamble **FOTON**.  
Detecta defectos en carrocería y llantas usando **YOLOv9** y se desplegará como API con **FastAPI**.

---

## ✨ Estado del proyecto
| Paso | Descripción | Estado |
|------|-------------|--------|
| E0 | Instalación base (Anaconda + VS Code) | ✅ |
| E1–E4 | Entorno `vision-2025` + `environment.yml` | ✅ |
| E5 | Repo Git inicializado | ✅ |
| E6 | `hello_opencv.py` (prueba I/O) | 🔄 En progreso |
| E7–E12 | Dataset, etiquetado, entrenamiento YOLOv9 | 📅 Próximos |

---

## ⚙️ Reproducir el entorno
```bash
# 1. Clona el repo
git clone https://github.com/<tu_usuario>/vision-inspector.git
cd vision-inspector

# 2. Crea el entorno Conda
conda env create -f environment.yml
conda activate vision-2025
