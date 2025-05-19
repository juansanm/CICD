# Taller MLOps  – Despliegue de API IA con CI/CD y GitOps
## Por Juan Gonzalez Sanmiguel

## Tecnologías Utilizadas

- **FastAPI** – API REST con predicción `/predict` y métricas `/metrics`
- **scikit-learn** – Entrenamiento del modelo `model.pkl`
- **Docker** – Contenedores de API y cliente LoadTester
- **GitHub Actions** – Automatización del entrenamiento y despliegue
- **Kubernetes (Minikube)** – Orquestación de servicios
- **Prometheus** – Scraping de métricas
- **Grafana** – Visualización de métricas de rendimiento
- **Argo CD** – Sincronización GitOps con despliegue continuo

##  Cómo Probar: 

 API Local

```bash
cd 4/api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train_model.py
uvicorn app.main:app --reload

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [5.1, 3.5, 1.4, 0.2]}'

### Pipeline CI/CD:


Con cada push a main, GitHub Actions:

    Entrena el modelo

    Construye imágenes Docker

    Sube a DockerHub

Secrets usados:

    DOCKER_USERNAME

    DOCKER_PASSWORD


- Despliegue Kubernetes + Argo CD

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f 4/manifests/argo-cd/app.yaml -n argocd

Argo CD -> kubectl port-forward svc/argocd-server -n argocd 8080:443


Visualización de Métricas
kubectl port-forward svc/grafana 3000:3000



