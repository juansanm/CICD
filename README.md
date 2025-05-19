# Taller MLOps – Despliegue de API IA con CI/CD y GitOps  
**Por Juan González Sanmiguel**

---

## 🚀 Tecnologías Utilizadas

- **FastAPI** – API REST con endpoint de predicción `/predict` y métricas `/metrics`
- **scikit-learn** – Entrenamiento del modelo de Machine Learning (`model.pkl`)
- **Docker** – Contenedores para la API y cliente LoadTester
- **GitHub Actions** – Pipeline automatizado de entrenamiento y construcción de imágenes
- **Kubernetes (Minikube)** – Orquestación de servicios
- **Prometheus** – Recolección de métricas expuestas por la API
- **Grafana** – Visualización de métricas en dashboards
- **Argo CD** – GitOps: despliegue automático desde repositorio GitHub

---

##  Cómo Probar
### 🧪 API Local

```bash
cd 4/api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train_model.py
uvicorn app.main:app --reload
```
---

Probar la API con:
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [5.1, 3.5, 1.4, 0.2]}'
```
---

## Pipeline CI/CD (GitHub Actions)

Cada vez que se hace push a la rama main, se ejecuta un pipeline que:

Entrena el modelo (train_model.py), Construye la imagen Docker de la API y el LoadTester

Publica las imágenes en DockerHub

Secrets necesarios: DOCKER_USERNAME y DOCKER_PASSWORD

---

## Despliegue Kubernetes + Argo CD
```
kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl apply -f 4/manifests/argo-cd/app.yaml -n argocd

kubectl port-forward svc/argocd-server -n argocd 8080:443

```

Para obtener contraseña de Argo

kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d && echo

## Visualización de Métricas en Grafana

kubectl port-forward svc/grafana 3000:3000


## Funcionamiento en Argo Cd
![Captura de pantalla 2025-05-19 114525](https://github.com/user-attachments/assets/7c2e41cb-fdef-4657-9be0-10cee0b5f366)






