# 📦 Workshop on Kubernetes & DevOps

This repository contains the complete codebase for the Workshop on Kubernetes & DevOps
. It includes the backend API, database integration, and containerized deployment.

---

## 🔗 Repository

> [My GitHub Repository](https://github.com/mohitsinghgit02/NAGP_Workshop_Kubernetes_DevOps.git)  
This repository hosts the code for Workshop on Kubernetes & DevOps
. It includes the backend API, database integration, and containerized deployment

---

## 🐳 Docker Images

> Docker Hub: [https://hub.docker.com/r/mohitsinghhub/k8s-multi-tier-api]

You can pull the image using:

```bash
docker pull mohitsinghhub/k8s-multi-tier-api:v3
```

## 🌐 Service API Tier
Use the following endpoint to view the records from the backend tier:

```bash
http://<your-ingress-domain-or-ip>/api/items
```
## 🚀 How to Run

1. **Build Docker Image:**
   ```bash
   kubectl apply -f k8s-gcp/
   ```
2. **Login to PostgreSQL POD CLI**
    
    ```bash
    kubectl get pods -l app=postgres
    kubectl exec -it <postgres-pod-name> -- bash
    ```
3. **SQL script to create tables and insert initial records**

    ```bash
    psql -U <postgres-user> -d <database-name>

    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        description TEXT
    );

    INSERT INTO items (name, description) VALUES
        ('Laptop', 'A portable computer'),
        ('Phone', 'A smart mobile device'),
        ('Tablet', 'A touchscreen device');
    ```

## 🎬 Screen Recording Video
 [Link to the video showing all objects deployed in Kubernetes cluster](https://nagarro-my.sharepoint.com/:u:/r/personal/mohit_singh02_nagarro_com/Documents/NAGP-2025/Mohit_Kumar_Singh_3211145_Kubernetes_and_DevOps_Advance.zip?csf=1&web=1&e=BXigeR)