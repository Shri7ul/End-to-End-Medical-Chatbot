
# 🧠 End-to-End Medical Chatbot

An AI-powered medical assistant that uses **RAG (Retrieval-Augmented Generation)** to provide accurate, context-aware responses based on medical knowledge.

Built with a focus on **real-world usability, scalability, and production deployment**.

---

## 🚀 Features

* 💬 AI-powered medical chatbot (context-aware responses)
* 📚 Semantic search using vector embeddings
* 🧠 RAG pipeline with external knowledge retrieval
* ⚡ Fast API responses with optimized backend
* ☁️ Ready for cloud deployment (AWS + Docker + CI/CD)

---

## 🛠 Tech Stack

* Python
* Flask
* LangChain
* OpenAI (LLM)
* Pinecone (Vector DB)
* Docker
* AWS (EC2, ECR)
* GitHub Actions (CI/CD)

---

## ⚙️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/Shri7ul/End-to-End-Medical-Chatbot.git
cd End-to-End-Medical-Chatbot
```

---

### 2. Create Virtual Environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

### 5. Store Embeddings

```bash
python store_index.py
```

---

### 6. Run Application

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## ☁️ AWS + Docker + CI/CD Deployment (Future Integration)

### 🔐 IAM Setup

Create an IAM user with:

* AmazonEC2FullAccess
* AmazonEC2ContainerRegistryFullAccess

---

### 📦 ECR (Elastic Container Registry)

* Create a repository
* Save the repository URI

---

### 🖥 EC2 Setup

Launch Ubuntu EC2 and install Docker:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker
```

---

### 🔁 CI/CD Pipeline (GitHub Actions)

Workflow:

1. Build Docker image
2. Push to ECR
3. Pull on EC2
4. Run container

---

### 🔑 GitHub Secrets Required

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `ECR_REPO`
* `PINECONE_API_KEY`
* `OPENAI_API_KEY`

---

## 📈 Project Architecture

* Document ingestion → Chunking → Embedding
* Vector storage (Pinecone)
* Query → Semantic retrieval
* Context + LLM → Final response

---

## 🎯 Learning Outcomes

* End-to-end RAG system design
* Vector databases & embeddings
* API + backend structuring
* Production deployment workflow
* CI/CD automation

---

## 👤 Author

**Shriful Islam (InHuman)**

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
