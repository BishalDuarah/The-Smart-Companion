# 🧠 Smart Companion  
### Bridging the Executive Function Gap with Neuro-Inclusive AI  

## 🚀 Overview

Smart Companion is an AI-powered assistant designed to support neurodivergent individuals (Autism, ADHD, Dyslexia) by transforming overwhelming goals into granular, actionable “Micro-Wins.”

Instead of showing intimidating to-do lists, the system provides:

- One step at a time
- Short, atomic actions
- Voice assistance
- Dyslexia-friendly typography
- Visual progress indicators
- Encrypted personal cognitive profiles

The goal is autonomy through structure.

---

## 🧩 Problem We Solve

Neurodivergent users often struggle with:

- **Task Paralysis**
- **Time Blindness**
- **Decision Fatigue**
- **Visual Stress from cluttered interfaces**

Smart Companion reduces cognitive load by decomposing high-level tasks into neuro-friendly micro-actions.

---

## 🏗️ System Architecture

User Input  
→ PII Masking  
→ Profile-Aware Prompt Engineering  
→ Gemini LLM Decomposition  
→ Atomic Post-Processing Engine  
→ Encrypted Storage  
→ Single-Step Neuro UI  

---

## 🔐 Privacy-First Design

- User neuro-profiles stored locally using SQLite
- Sensitive fields encrypted using Fernet (AES-based symmetric encryption)
- PII masking before sending to LLM
- No personal identifiers transmitted to model

---

## 🧠 AI Granularity Engine

The system ensures true "Micro-Wins" by:

- Enforcing <15-word steps
- Splitting compound actions
- Removing explanatory fluff
- Converting instructions into verb-first actions
- Adapting granularity based on user profile

This guarantees atomic actions instead of generic task lists.

---

## ♿ Neuro-Inclusive UX Features

- OpenDyslexic / Lexend font toggle
- Single-task view (prevents overwhelm)
- Progress bar for time blindness
- Dopamine streak counter
- Voice input (speech-to-text)
- Voice guidance (text-to-speech)
- Minimalist UI design

---

## 🐳 Docker Deployment

### Build

docker build -t smart-companion .

### Run
docker run -p 8000:8000 smart-companion

### Access Application
http://localhost:8000/ui

## 🛠 Tech Stack
### Backend
-FastAPI
-SQLite
-Fernet Encryption
-Gemini 1.5 Flash (Google Generative AI)
-Uvicorn
### Frontend
-React (Vite)
-TailwindCSS
-Web Speech API

### Deployment
Docker (single container)

