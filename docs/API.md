# 📡 API e Protocolos - Sistema de Teste Estático

## 📋 Visão Geral

Este documento descreve os protocolos de comunicação e interfaces disponíveis para interação com o sistema de ignição e teste estático. O sistema suporta múltiplos protocolos de comunicação para flexibilidade em diferentes cenários de uso.

## 🔌 Protocolos Suportados

| Protocolo  | Tipo     | Velocidade  | Alcance | Caso de Uso              |
| ---------- | -------- | ----------- | ------- | ------------------------ |
| Serial USB | Fio      | 115200 baud | Local   | Configuração e debug     |
| Bluetooth  | Wireless | 115200 baud | 10m     | Controle remoto          |
| ESP-NOW    | Wireless | 1-2 Mbps    | 100m    | Telemetria em tempo real |

## 💻 Comunicação Serial/Bluetooth

### Configuração da Comunicação

```
// Parâmetros padrão
BAUD_RATE = 115200
DATA_BITS = 8
PARITY = NONE
STOP_BITS = 1
FLOW_CONTROL = NONE
```

### Estrutura de Comandos

```
COMANDO[,PARÂMETRO]*[\n|\r\n]
```

## 🎮 Comandos Disponíveis

### 1. Modo de Configuração

```
# Iniciar modo de calibração
COMANDO: INIT CONFIG
RESPOSTA: Aguardando fator de carga...
USO: Entra no modo de configuração para calibração da célula de carga

# Definir fator de carga
COMANDO: SET LOAD FACTOR <valor>
EXEMPLO: SET LOAD FACTOR 277306.0
RESPOSTA: Fator de carga atualizado: 277306.00
USO: Define o fator de calibração da célula de carga
```

### 2. Controle do Sistema

```
# Zerar célula de carga (equivalente ao botão físico)
COMANDO: TARE
RESPOSTA: Célula zerada!
USO: Realiza o tara da célula de carga
```

## 🎯 Exemplos de Interação

### Exemplo 1: Calibração da Célula de Carga

```
# Terminal → ESP32
INIT CONFIG

# ESP32 → Terminal
Aguardando fator de carga...
# (ESP32 começa a enviar leituras RAW)
152345
152348
152350

# Terminal → ESP32
SET LOAD FACTOR 277306.0

# ESP32 → Terminal
Fator de carga atualizado: 277306.00
Modo configuração finalizado
```

## 📡 Protocolo ESP-NOW

### Configuração

```cpp
// Endereço MAC do receptor (broadcast)
uint8_t enderecoReceptor[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

// Estrutura da mensagem
typedef struct struct_message {
    char data[60]; // "timestamp,empuxo,pressao"
} struct_message;
```

### Formato da Mensagem

```cpp
<timestamp>,<empuxo>,<pressao>
```

Exemplo

```
123456,1.234567,1850
```

### Callback de Confirmação

```cpp
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
    Serial.print("Status ESP-NOW: ");
    Serial.println(status == ESP_NOW_SEND_SUCCESS ?
                   "Entregue" : "Falha");
}
```

### Arduino - Receptor ESP-NOW

Acessar o código utilizado no [receptor](../extras/receiver-esp-now/receiver-esp-now.ino)
