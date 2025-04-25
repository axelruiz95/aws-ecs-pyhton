# Proyecto Backend CV - Despliegue en AWS ECS

Este proyecto consiste en una aplicación backend desarrollada en **Python** usando **FastAPI**, que expone un endpoint para consultar un Currículum Vitae (CV).  
La aplicación se empaqueta en una imagen Docker y se despliega en **AWS ECS (Elastic Container Service)** detrás de un **Application Load Balancer (ALB)**, con políticas de **Auto Scaling** para escalar automáticamente el número de tareas (tasks) según la carga.

---

## 📦 Tecnologías utilizadas

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Docker**
- **AWS ECS (Fargate)**
- **AWS Application Load Balancer (ALB)**
- **AWS Auto Scaling Policy**
- **Amazon ECR** (para alojar la imagen Docker)

---

## 🚀 Estructura general

backend-cv/ 
├── app/ 
│ ├── init.py 
│ ├── main.py 
│ ├── cv_data.py 
│ └── models.py (opcional) 
├── Dockerfile 
├── requirements.txt 
├── README.md 
└── .gitignore

---

## 🐳 Proceso de despliegue

### 1. Construir y etiquetar la imagen Docker

docker build -t backend-cv .

### 2. Crear repositorio en ECR y subir imagen

aws ecr create-repository --repository-name task-proyecto
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 891377197834.dkr.ecr.us-east-1.amazonaws.com
docker tag backend-cv:latest 891377197834.dkr.ecr.us-east-1.amazonaws.com/task-proyecto:latest
docker push 891377197834.dkr.ecr.us-east-1.amazonaws.com/task-proyecto:latest
Nota: Para automatizar procesos posteriores, asegúrate de siempre usar la URL de imagen:
891377197834.dkr.ecr.us-east-1.amazonaws.com/task-proyecto:latest

🛠️ 3. Crear infraestructura en AWS

🔹 ECS Cluster y Service
    Crear un Cluster ECS tipo Fargate ($ECS_CLUSTER)
    Crear una Task Definition que use tu imagen desde Amazon ECR
    Crear un Service ECS ($ECS_SERVICE) y conectarlo a un Application Load Balancer (ALB):
        Configurar el ALB para enrutar tráfico HTTP al puerto 8000 del contenedor
        Asegurar que el Service ECS tenga asignado un Security Group adecuado
        Activar auto-assign public IP si usas subnets públicas



