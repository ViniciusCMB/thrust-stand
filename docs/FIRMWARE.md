# ⚙️ Firmware - Sistema de Teste Estático

## 🏗️ Arquitetura do Sistema

### Visão Geral

O firmware implementa um sistema de aquisição de dados em tempo real para testes estáticos de foguetes, com capacidade de processamento, armazenamento e comunicação multi-protocolo.

### Diagrama de Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   SENSORES      │    │    PROCESSAMENTO │    │     SAÍDAS       │
│                 │    │                  │    │                  │
│  Célula Carga   │───▶│   Aquisição      │───▶│  Cartão SD       │
│  Sensor Pressão │    │   Filtragem      │    │  Serial/BT       │
│  RTC DS3231     │    │   Timestamp      │    │  ESP-NOW         │
└─────────────────┘    └──────────────────┘    └──────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                         ┌──────────────────┐
                         │   CONTROLE       │
                         │                  │
                         │  Estados         │
                         │  Configuração    │
                         │  Segurança       │
                         └──────────────────┘
```

## 📁 Estrutura de Código

### Módulos Principais

```
firmware/
├── 📄 firmware.ino              # Arquivo principal
└── 📄 Pressure.h                # Classe sensor pressão
```

### Dependências e Bibliotecas

- Wire
- RTClib
- HX711
- FS
- SD
- SPI
- PushButton
- BluetoothSerial
- esp_now
- WiFi
- Preferences

## 🔧 Configuração e Calibração

### Preferências Persistentes

O sistema usa a biblioteca Preferences para armazenar configurações na EEPROM

```cpp
// Chaves de preferência
const char* PREF_NAMESPACE = "app";
const char* PREF_LOAD_FACTOR = "loadFactor";

// Carregar configuração
loadFactor = preferences.getFloat("loadFactor", 277306.0);

// Salvar configuração
preferences.putFloat("loadFactor", loadFactor);
```

## 🔄 Fluxo de Execução

1. Inicialização (setup())

```cpp
void setup() {
    // 1. Comunicação
    Serial.begin(115200);
    SerialBT.begin("ESP32_BT");

    // 2. Configuração persistente
    preferences.begin("app", false);
    loadFactor = preferences.getFloat("loadFactor", 277306.0);

    // 3. Hardware
    setupRTC();
    setupSDCard();
    setupHX711();

    // 4. Comunicação wireless
    setupESPNow();
}
```

2. Loop Principal

```cpp
void loop() {
    // Coleta contínua de dados
    staticTest();

    // Tratamento de botão
    if (button.getSingleDebouncedPress()) {
        handleButtonPress();
    }

    // Comandos via serial
    if (Serial.available()) {
        handleSerialCommand();
    }
}
```

## 📊 Aquisição de Dados

### Estrutura de Leitura

```cpp
struct SensorData {
    unsigned long timestamp;
    float thrust;      // Empuxo em Kg
    float pressureMPa; // Pressão convertida para MPa
};
```

### Função de Log de Dados

```cpp
void logData(unsigned long millis) {
    float peso = escala.get_units();
    float pressao = pressureSensor.readMPA();

    // Detecção de valores máximos
    if (peso > maxValues[0]) maxValues[0] = peso;
    if (pressao > maxValues[1]) maxValues[1] = pressao;

    // Formatação e armazenamento
    leitura = String(millis) + "," + String(peso, 6) + "," + String(pressao);
    appendFile(SD, filedir, leitura);

    // Transmissão (opcional)
    if (espNowPeerReady) {
        transmitDataESPNow(leitura);
    }
}
```

## 🎮 Sistema de Comandos

### Interface Serial/Bluetooth

```cpp
void handleSerialCommand() {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command.startsWith("INIT CONFIG")) {
        enterConfigurationMode();
    }
    else if (command.startsWith("SET LOAD FACTOR")) {
        processLoadFactorCommand(command);
    }
    // ... outros comandos
}
```

### Comandos Disponíveis

| Comando         | Descrição                | Exemplo                    | Resposta            |
| --------------- | ------------------------ | -------------------------- | ------------------- |
| INIT CONFIG     | Entra em modo calibração | `INIT CONFIG`              | Aguarda fator       |
| SET LOAD FACTOR | Define fator de carga    | `SET LOAD FACTOR 277306.0` | Confirmação         |
| Botão Físico    | Zera célula de carga     | -                          | Beep de confirmação |

## 💾 Sistema de Arquivos

### Estrutura no Cartão SD

```
/SD_CARD/
└── 📁 2024-11-15_14-30-25/          # Diretório por data/hora
   └── 📄 2024-11-15_14-30-25_raw.txt  # Arquivo de dados
```

### Formato do Arquivo de Dados

```csv
Tempo,Empuxo,Pressao
0,0.000000,1850
100,1.234567,1902
200,2.345678,1955
...
```

### Funções de Arquivo

```cpp
bool writeFile(fs::FS &fs, String path, String message) {
    File file = fs.open(path, FILE_WRITE);
    if (!file) return false;
    bool success = file.print(message);
    file.close();
    return success;
}

void appendFile(fs::FS &fs, const String &path, const String &message) {
    File file = fs.open(path, FILE_APPEND);
    if (file) {
        file.print(message + "\n");
        file.close();
    }
}
```

## 📡 Comunicação

### Protocolo ESP-NOW

```cpp
typedef struct struct_message {
    char data[60]; // "timestamp,empuxo,pressao"
} struct_message;

void setupESPNow() {
    WiFi.mode(WIFI_STA);
    if (esp_now_init() == ESP_OK) {
        esp_now_register_send_cb(OnDataSent);
        // Configurar peer
    }
}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
    // Callback de confirmação de entrega
}
```

### Bluetooth Serial

```cpp
BluetoothSerial SerialBT;

void setupBluetooth() {
    SerialBT.begin("ESP32_BT");
}

void printToSerials(const String &message) {
    Serial.println(message);      // USB Serial
    SerialBT.println(message);    // Bluetooth
}
```

## 🎵 Sistema de Feedback

### Controle do Buzzer

```cpp
void buzzSignal(String signal) {
    int frequency = 1000;

    if (signal == "Alerta") {
        // 5 bips rápidos
        for (int i = 0; i < 5; i++) {
            tone(BUZZER_PIN, frequency, 200);
            delay(350);
        }
    }
    else if (signal == "Sucesso") {
        // 3 bips curtos
        for (int i = 0; i < 3; i++) {
            tone(BUZZER_PIN, frequency, 100);
            delay(200);
        }
    }
    // ... outros sinais
}
```

### Estados do LED

- Constante: Gravando dados
- Apagado: Sistema inativo/erro

## 🚀 Compilação e Upload

### Arduino IDE

1. Selecione a placa "ESP32 Dev Module"
2. Configure a porta COM
3. Defina as opções de partição (se necessário)
4. Faça o upload
