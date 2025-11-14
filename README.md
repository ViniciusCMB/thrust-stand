# thrust-stand

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue)

## 📋 Sobre

Sistema embarcado baseado em ESP32 para controle e monitoramento de testes estáticos de motores de foguetes, com aquisição de dados de empuxo e pressão em tempo real, armazenamento em cartão SD e comunicação multi-protocolo.

## 🚀 Quick Start

1. Clone o repositório

```bash
git clone https://github.com/ViniciusCMB/thrust-stand.git
```

2. Configure o hardware conforme [esquemático](./docs/HARDWARE.md)
3. Carregue o firmware

## 📁 Estrutura do Projeto

```
├── 📂 docs/              # Documentação técnica detalhada
├── 📂 extras/            # Códigos extras utilizados
├── 📂 firmware/          # Código do microcontrolador ESP32
├── 📂 hardware/          # Esquemáticos, PCBs e lista de componentes
├── 📂 software/          # Ferramentas de análise e interface
└── 📂 test/              # Testes unitários e de integração
```

## 🔧 Pré-requisitos

- Hardware: ESP32, Célula de carga, Conversor HX711, Sensor de pressão, RTC DS3231, Leitor Micro SD Card.
- Software: Arduino IDE 2.0+
- Bibliotecas: Ver requirements.txt

## 📖 Documentação

- [Esquemático e Montagem](./docs/HARDWARE.md)
- [Firmware e Arquitetura](./docs/FIRMWARE.md)
- [Protocolos e API](./docs/API.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)

## 🎯 Funcionalidades

- ✅ Aquisição de dados de empuxo e pressão em tempo real
- ✅ Armazenamento em cartão SD com timestamp
- ✅ Comunicação multi-protocolo (Serial, Bluetooth, ESP-NOW)
- ✅ Calibração persistente de sensores
- ✅ Feedback visual e audível

## 🤝 Contribuindo

Este projeto segue as [Boas Práticas da Serra Rocketry](https://github.com/Serra-Rocketry/best-practices). Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ✨ Autores

- Equipe Serra Rocketry - Desenvolvimento e documentação
- Contribuidores - [Lista de contribuidores]()
