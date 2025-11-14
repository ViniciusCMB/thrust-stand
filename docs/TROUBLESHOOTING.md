# 🐛 Troubleshooting - Sistema de Teste Estático

## 📋 Visão Geral

Este documento fornece soluções para problemas comuns encontrados durante a instalação, configuração e operação do sistema de ignição e teste estático.

## 🔍 Diagnóstico Rápido

### LEDs Indicadores

| Estado do LED    | Significado     | Ação                  |
| ---------------- | --------------- | --------------------- |
| 🔵 LED constante | Gravando dados  | Operação normal       |
| 🔴 Apagado       | Erro no sistema | Verificar alimentação |

### Sinais do Buzzer

| Padrão Sonoro     | Significado | Ação               |
| ----------------- | ----------- | ------------------ |
| 🎵 3 bips curtos  | Sucesso     | Operação normal    |
| 🚨 5 bips rápidos | Alerta/Erro | Verificar sensores |

## 🚨 Problemas Comuns e Soluções

### 1. 🔌 Problemas de Alimentação

Sintomas

- Sistema não liga
- Reinicializações aleatórias
- Leituras instáveis dos sensores

Soluções

```bash
# Verificar tensão de alimentação
1. Medir 3.3V no pino VCC do ESP32
2. Verificar se > 3.2V sob carga
3. Verificar corrente > 500mA disponível

# Soluções:
✅ Usar fonte 5V 2A dedicada
✅ Verificar cabos USB (evitar extensões longas)
✅ Adicionar capacitor 1000μF na alimentação
✅ Verificar regulador 3.3V do ESP32
```

### 2. 💾 Problemas com Cartão SD

Sintomas

- "Falha no SD" no boot
- "Cartão SD não encontrado"
- Erros ao escrever arquivos
  Soluções

```
# Diagnóstico:
1. Verificar formatação (deve ser FAT32)
2. Verificar tamanho (recomendado ≤ 32GB)
3. Testar cartão em outro dispositivo
4. Verificar pino CS (GPIO 5)

# Comandos de diagnóstico:
LIST FILES          # Lista arquivos no SD
STATUS              # Verifica status do SD

# Soluções:
✅ Reformatar cartão como FAT32
✅ Usar cartão de marca confiável (SanDisk, Kingston)
✅ Limpar contatos do leitor SD
✅ Verificar solda do módulo SD
```

### 3. ⚖️ Problemas com Célula de Carga

Sintomas

- Leituras instáveis ou zeradas
- "HX711 não conectado"
- Valores fora do esperado
  Soluções

```
# Diagnóstico:
1. Verificar conexões DT (GPIO 26) e SCK (GPIO 27)
2. Verificar alimentação 3.3V do HX711
3. Testar com peso conhecido

# Comandos de diagnóstico:
TARE                # Zerar célula

# Procedimento de calibração:
1. INIT CONFIG
2. Anotar leituras RAW com peso conhecido
3. Calcular: fator = leitura_raw / peso_kg
4. SET LOAD FACTOR <valor_calculado>

# Soluções:
✅ Verificar fixação mecânica da célula
✅ Afastar fontes de interferência elétrica
✅ Usar cabos blindados para conexões
✅ Verificar ground comum
```

### 4. 📡 Problemas de Comunicação

Serial/Bluetooth Não Conecta

```
# Diagnóstico Serial:
1. Verificar porta COM no Gerenciador de Dispositivos
2. Verificar baud rate (115200)
3. Testar com outro cabo USB
4. Verificar drivers CP210x/CH340

# Diagnóstico Bluetooth:
1. Verificar se ESP32_BT aparece na lista
2. Tentar pairing com PIN 1234
3. Verificar distância (< 10m)
4. Reiniciar dispositivo Bluetooth

# Soluções:
✅ Instalar drivers USB-ESP32 mais recentes
✅ Usar terminal serial confiável (PuTTY, Arduino Serial Monitor)
✅ Resetar pairing Bluetooth
```

ESP-NOW Não Funciona

```
# Diagnóstico:
1. Verificar endereço MAC do receptor
2. Verificar se ambos estão no mesmo canal WiFi
3. Verificar distância (< 100m em campo aberto)

# Soluções:
✅ Usar endereço MAC correto do receptor
✅ Verificar antenas WiFi
✅ Reduzir distância entre dispositivos
```

### 5. 🕐 Problemas com RTC (Relógio)

Sintomas

- Data/hora incorretas
- "DS3231 não encontrado"
- Horas resetam após desligar

Soluções

```
# Diagnóstico:
1. Verificar bateria CR2032 (≥ 3V)
2. Verificar conexões I2C (SDA GPIO 21, SCL GPIO 22)

# Soluções:
✅ Substituir bateria CR2032
✅ Verificar solda do módulo RTC
✅ Resetar RTC: desconectar bateria por 10 segundos
```

### 6. 📊 Problemas com Sensor de Pressão

Sintomas

- Leituras constantes em 0 ou 4095
- Valores fora da faixa esperada
- Ruído excessivo nas leituras

Soluções

```
# Diagnóstico:
1. Verificar alimentação 5V do sensor
2. Verificar divisor resistivo (R1=2.2kΩ, R2=3.3kΩ)
3. Medir tensão no pino GPIO 35 (deve ser 0-3.3V)

# Cálculo do divisor:
Vout = Vsensor * (R2 / (R1 + R2))
Vout_max = 4.5V * (3300 / (2200 + 3300)) = 2.7V ✅

# Soluções:
✅ Verificar valores dos resistores
✅ Adicionar capacitor 100nF no pino ADC
✅ Verificar conexão de ground
✅ Usar fonte estável 5V para o sensor
```
