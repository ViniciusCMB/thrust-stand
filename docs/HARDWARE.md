# 🔌 Hardware - Sistema de Teste Estático

## 📋 Visão Geral do Sistema

Sistema embarcado baseado em ESP32 para aquisição de dados de empuxo e pressão em testes estáticos de motores de foguetes, com capacidade de armazenamento e comunicação multi-protocolo.

## 🧩 Lista de Componentes (BOM)

| Componente        | Quantidade | Especificações           |
| ----------------- | ---------- | ------------------------ |
| ESP32 DevKit V1   | 1          | 38 pinos, WiFi/BT        |
| Célula de Carga   | 2          | 50kg                     |
| Módulo HX711      | 1          | ADC 24 bits              |
| Sensor de Pressão | 1          | 0-10 MPa, Saída 0.5-4.5V |
| RTC DS3231        | 1          | I2C                      |
| Cartão SD         | 1          | Módulo leitor, SPI       |
| Buzzer Ativo      | 1          | 5V, 12mm                 |
| LED               | 1          | 5mm, Vermelho            |
| Botão Táctil      | 1          | 6x6mm, 4 pinos           |
| Resistores        | 2          | 2.2kΩ e 3.3kΩ            |
| Fonte Alimentação | 1          | 5V 2A, USB-C             |

## 🔄 Diagrama de Conexões

Esquemático Simplificado

```
+-------------------+      +-------------------+      +-------------------+
|   Célula Carga    |      |   Sensor Pressão  |      |      RTC          |
|                   |      |                   |      |   DS3231          |
| DT  ------------ GPIO26  | OUT ------------ GPIO35  | SDA --------- GPIO21
| SCK ------------ GPIO27  | VCC ------------ 3.3V    | SCL --------- GPIO22
| VCC ------------ 3.3V    | GND ------------ GND     | VCC --------- 3.3V
| GND ------------ GND     |                   |      | GND --------- GND
+-------------------+      +-------------------+      +-------------------+

+-------------------+      +-------------------+      +-------------------+
|   Cartão SD       |      |     Buzzer        |      |      LED          |
|                   |      |                   |      |                   |
| CS  ------------ GPIO5   | + ------------ GPIO33    | Ânodo -------- GPIO4
| MOSI ----------- GPIO23  | - ------------ GND       | Catodo ------- GND
| MISO ----------- GPIO19  +-------------------+      +-------------------+
| SCK ------------ GPIO18
| VCC ------------ 3.3V
| GND ------------ GND
+-------------------+

+-------------------+
|     Botão         |
|                   |
| Pino1 --------- GPIO32
| Pino2 --------- GND
+-------------------+
```

## 🛠️ Procedimento de Montagem

1. Preparação dos Componentes

- Verifique todos os componentes na lista BOM
- Teste individual de cada sensor antes da montagem

2. Sequência de Montagem Recomendada

- Conecte a alimentação (5V e GND)
- Monte os sensores I2C (RTC DS3231)
- Conecte a célula de carga (HX711)
- Instale o cartão SD
- Adicione os periféricos (LED, Buzzer, Botão)
- Conecte o sensor de pressão com divisor resistivo

3. Divisor Resistivo para Sensor de Pressão

```
Vsensor (0.5-4.5V) --- R1 (2.2kΩ) --- ESP32_GPIO35
                         |
                        R2 (3.3kΩ)
                         |
                        GND
```

Cálculo do divisor:

```
Vout = Vsensor * (R2 / (R1 + R2))

# Exemplo
Vout_max = 4.5V * (3300 / (2200 + 3300)) = 2.7V (dentro da faixa 3.3V do ESP32)
```

## 📷 Fotos de Referência

Montagem Completa

![Esquematico](./Equematico.png)

## ⚠️ Considerações de Projeto

- [x] Divisor resistivo para sensor de pressão
- [x] Capacitores de desacoplamento em cada IC
- [x] Fixação da célula de carga deve ser rígida
- [ ] Isolamento contra vibrações
- [ ] Proteção contra ambiente (poeira, umidade)

## 🧪 Testes de Hardware

### Testes Pré-Montagem

- Continuidade dos cabos
- Funcionamento do ESP32
- Leitura dos sensores individuais
- Comunicação I2C/SPI

### Testes Pós-Montagem

- Consumo de energia
- Estabilidade das leituras
- Comunicação integrada
- Resposta a comandos
