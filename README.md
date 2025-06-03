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

---

## 🛡️ Checklist de Ética de Datos
- [ ] **Consentimiento:**  Solo uso imágenes capturadas en planta con aprobación de la empresa y sin información personal identificable.  
- [ ] **Privacidad:**  Recorto o difumino cualquier rostro, matrícula o dato sensible antes de subirlos al repositorio.  
- [ ] **Propósito claro:**  Las imágenes se emplean exclusivamente para mejorar la calidad del producto FOTON, no para fines comerciales externos.  
- [ ] **Almacenamiento seguro:**  Los datasets completos viven en servidores internos / DVC remoto con acceso restringido.  
- [ ] **Trazabilidad:**  Versiono cambios de dataset con DVC para saber siempre qué imágenes entrenaron cada modelo.

