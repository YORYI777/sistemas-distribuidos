
---

# 🚀 Sistema Distribuido con FastAPI + Kubernetes (Minikube)

![Arquitectura del sistema](assets/arquitectura.png)

Proyecto desarrollado para la materia de **Sistemas Distribuidos**.
Se implementó una arquitectura distribuida desplegando una API en **FastAPI** dentro de un clúster local **Kubernetes (Minikube)**, con múltiples réplicas (pods), balanceo de carga, cache y persistencia.

---

## 📦 Componentes del sistema

| Componente            | Función                                       |
| --------------------- | --------------------------------------------- |
| FastAPI + Uvicorn     | API HTTP que responde con el hostname del pod |
| Redis                 | Cache y contador de visitas (`/hits`)         |
| PostgreSQL            | Persistencia de datos                         |
| Nginx                 | Balanceador / Proxy de entrada al sistema     |
| Docker                | Empaquetado de la aplicación                  |
| Kubernetes (Minikube) | Orquestación y administración de pods         |
| Deployment            | Mantiene múltiples réplicas (3 pods)          |
| Service               | Comunicación interna y exposición externa     |

---

## 🗂️ Estructura del proyecto

```
sistemas-distribuidos/
├── app/
│   └── main.py
├── k8s/
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── redis.yaml
│   ├── postgres.yaml
│   ├── nginx.yaml
│   └── nginx-config.yaml
├── assets/
│   └── arquitectura.png
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🚀 Ejecución paso a paso

### 1️⃣ Iniciar Minikube

```bash
minikube start --driver=docker
```

### 2️⃣ Construir imagen dentro de Minikube

```bash
eval $(minikube docker-env)
docker build -t fastapi-app:latest .
```

### 3️⃣ Desplegar en Kubernetes

```bash
kubectl apply -f k8s/
```

### 4️⃣ Verificar recursos

```bash
kubectl get pods -o wide
kubectl get svc
```

### 5️⃣ Obtener URL del servicio

```bash
minikube service nginx --url
```

---

# 🧪 Evidencia de Distribución (Balanceo de Carga)

Cada petición puede ser atendida por un pod diferente.
El endpoint devuelve el `hostname` para evidenciar la distribución.

```bash
URL=$(minikube service nginx --url)
for i in {1..10}; do curl -s $URL/; echo; done
```

Ejemplo de salida esperada:

```json
{"mensaje":"Sistema Distribuido funcionando","hostname":"fastapi-app-xxxxx"}
{"mensaje":"Sistema Distribuido funcionando","hostname":"fastapi-app-yyyyy"}
```

Esto demuestra que Kubernetes distribuye las solicitudes entre múltiples pods.

---

# 🛡️ Pruebas de Resiliencia

Estas pruebas validan la tolerancia a fallos y la auto-recuperación del sistema.

## 🔧 Simular caída de un Pod (Self-Healing)

Eliminar un pod manualmente:

```bash
kubectl delete pod -l app=nginx
```

Kubernetes recreará automáticamente el pod gracias al Deployment.

Monitorear recreación:

```bash
kubectl get pods -l app=nginx -w
```

El servicio continúa funcionando sin interrupciones.

---

## 📈 Escalabilidad Horizontal

Escalar la API a 5 réplicas:

```bash
kubectl scale deployment fastapi-app --replicas=5
kubectl get pods
```

Reducir nuevamente:

```bash
kubectl scale deployment fastapi-app --replicas=3
```

---

## ❌ No recomendado: eliminar el Service

```bash
kubectl delete svc nginx
```

Esto elimina el punto de entrada del sistema y la URL pública dejará de funcionar.

---

# 🧹 Limpieza del entorno

```bash
kubectl delete -f k8s/
```

---

# 🎯 Características del sistema

* ✔ Balanceo de carga
* ✔ Escalabilidad horizontal
* ✔ Auto-recuperación (Self-healing)
* ✔ Persistencia con PostgreSQL
* ✔ Cache con Redis
* ✔ Arquitectura distribuida real

---

# 👤 Autor

GitHub: [https://github.com/YORYI777](https://github.com/YORYI777)

---

