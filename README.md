# 🐂 CattleWeight-AI: Predição de Peso Bovino em Tempo Real

Este projeto utiliza visão computacional 3D e Deep Learning para realizar a predição de peso de bovinos em tempo real utilizando câmeras de profundidade **Intel RealSense**. A solução integra dados de sensores RGB-D com metadados zootécnicos (raça, idade, hormônios) para uma estimativa precisa sem estresse animal.

## 🚀 Funcionalidades
* **Captura 3D:** Integração nativa com SDK Librealsense.
* **Segmentação:** Isolamento do animal utilizando modelos YOLOv8-seg/Mask R-CNN.
* **Fusão Multimodal:** Modelo de Deep Learning que combina nuvem de pontos (Point Cloud) com dados tabulares.
* **Estimativa de Volume:** Algoritmo para cálculo de volume corporal a partir do mapa de profundidade.

## 🛠️ Requisitos de Hardware
* **Câmera:** Intel RealSense série D400 (Recomendado D435i ou D455).
* **Processamento:** Host com suporte a USB 3.0/3.1.
* **GPU (Opcional):** NVIDIA dedicada ou Intel integrada com suporte a OpenVINO.

## 📦 Instalação e Configuração

### 1. SDK Intel RealSense
É necessário instalar o `librealsense` antes de rodar o Python wrapper.
[Instruções oficiais de instalação](https://github.com/IntelRealSense/librealsense).

### 2. Ambiente Python
Recomendamos o uso de um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
