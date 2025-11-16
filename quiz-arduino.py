import random # a biblioteca para sortear as perguntas

# logo abaixo o banco com as 50 perguntas
banco_questoes = [
    {
        "pergunta": "O que é o Arduino?",
        "alternativas": [
            "Um software de edição",
            "Um microcontrolador de placa aberta usado em projetos",
            "Um tipo de capacitor",
            "Um sensor de temperatura",
            "Um motor DC"
        ],
        "correta": 1
    },
    {
        "pergunta": "Quem criou o projeto Arduino?",
        "alternativas": [
            "Bill Gates",
            "Paul Allen",
            "Massimo Banzi e David Cuartielles",
            "Steve Jobs",
            "Elon Musk"
        ],
        "correta": 2
    },
    {
        "pergunta": "Qual a principal linguagem usada no Arduino IDE?",
        "alternativas": [
            "Java",
            "C/C++",
            "Python",
            "Ruby",
            "Assembler"
        ],
        "correta": 1
    },
    {
        "pergunta": "Qual a voltagem de operação do Arduino Uno?",
        "alternativas": ["3.3V", "7V", "9V", "5V", "12V"],
        "correta": 3
    },
    {
        "pergunta": "Qual microcontrolador equipa o Arduino Uno?",
        "alternativas": ["ESP8266", "ATmega328P", "PIC18F2550", "ATtiny85", "STM32F1"],
        "correta": 1
    },
    {
        "pergunta": "Qual placa é maior e mais potente que o Arduino Uno?",
        "alternativas": ["Nano", "Micro", "Mega 2560", "Pro Mini", "LilyPad"],
        "correta": 2
    },
    {
        "pergunta": "Quantas portas digitais possui o Arduino Uno?",
        "alternativas": ["6", "8", "10", "12", "14"],
        "correta": 4
    },
    {
        "pergunta": "Quantas portas analógicas possui o Arduino Uno?",
        "alternativas": ["2", "4", "6", "8", "10"],
        "correta": 2
    },
    {
        "pergunta": "O que significa IDE no Arduino IDE?",
        "alternativas": [
            "Integrated Development Environment",
            "Internal Data Execution",
            "Interface Device Emulator",
            "Input Direct Engine",
            "Interchangeable Device Editor"
        ],
        "correta": 0
    },
    {
        "pergunta": "Qual função define um pino como entrada ou saída?",
        "alternativas": ["delay()", "digitalWrite()", "pinMode()", "loop()", "analogRead()"],
        "correta": 2
    },
    {
        "pergunta": "Qual comando envia nível alto a um pino digital?",
        "alternativas": [
            "digitalHigh()",
            "pinMode()",
            "digitalWrite(HIGH)",
            "pinHigh()",
            "analogWrite()"
        ],
        "correta": 2
    },
    {
        "pergunta": "Qual comando lê um valor digital (0 ou 1)?",
        "alternativas": [
            "digitalRead()",
            "analogRead()",
            "readDigital()",
            "readPin()",
            "pinRead()"
        ],
        "correta": 0
    },
    {
        "pergunta": "Qual comando lê valores analógicos?",
        "alternativas": ["analogRead()", "digitalRead()", "analogWrite()", "serialRead()", "sensorRead()"],
        "correta": 0
    },
    {
        "pergunta": "O que é PWM?",
        "alternativas": [
            "Controle de motores AC",
            "Modulação por largura de pulso",
            "Leitura analógica",
            "Sistema de rádio",
            "Redução de ruído"
        ],
        "correta": 1
    },
    {
        "pergunta": "Para que serve a função delay()?",
        "alternativas": [
            "Controlar temperatura",
            "Pausar o programa por um tempo",
            "Acelerar o código",
            "Alterar portas",
            "Ler sensores"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é o setup()?",
        "alternativas": [
            "Função repetida infinitamente",
            "Configurações que rodam uma vez",
            "Função que encerra o programa",
            "Função de comunicação serial",
            "Biblioteca interna"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é o loop()?",
        "alternativas": [
            "Função que roda apenas uma vez",
            "Função que roda repetidamente",
            "Função de CPU",
            "Função de conexão USB",
            "Função de desligamento"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que significa GND?",
        "alternativas": ["Energia 5V", "Porta analógica", "Terra", "Sinal invertido", "Memória interna"],
        "correta": 2
    },
    {
        "pergunta": "Para que serve o pino 5V?",
        "alternativas": ["Enviar dados", "Receber dados", "Alimentar componentes externos", "Resetar o Arduino", "Alocar memória"],
        "correta": 2
    },
    {
        "pergunta": "Para que serve o Vin?",
        "alternativas": [
            "Enviar dados USB",
            "Conectar LED",
            "Entrada de alimentação (7–12V)",
            "Controle PWM",
            "Porta analógica"
        ],
        "correta": 2
    },
    {
        "pergunta": "O que é um resistor?",
        "alternativas": [
            "Sensor de luz",
            "Motor elétrico",
            "Componente que limita corrente",
            "Saída digital",
            "Cabo USB"
        ],
        "correta": 2
    },
    {
        "pergunta": "O que é um LED?",
        "alternativas": [
            "Capacitor",
            "Componente que emite luz",
            "Ponteira USB",
            "Sensor de som",
            "Driver de motor"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um LDR?",
        "alternativas": [
            "Sensor de luz",
            "Sensor de som",
            "Motor DC",
            "Botão",
            "Display"
        ],
        "correta": 0
    },
    {
        "pergunta": "Para que serve um protoboard?",
        "alternativas": [
            "Imprimir código",
            "Montar circuitos sem solda",
            "Salvar arquivos",
            "Carregar o Arduino",
            "Medir temperatura"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um servo motor?",
        "alternativas": [
            "Motor de rotação contínua",
            "Motor com controle preciso de ângulo",
            "Sensor de movimento",
            "LED de alta potência",
            "Relé"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um motor DC?",
        "alternativas": [
            "Motor digital",
            "Motor que funciona com corrente contínua",
            "Motor de alta precisão",
            "Motor senoidal",
            "Sensor magnético"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um buzzer?",
        "alternativas": [
            "Gerador de luz",
            "Dispositivo para emitir som",
            "Potenciômetro",
            "Sensor de distância",
            "Microcontrolador"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um relé?",
        "alternativas": [
            "Interruptor controlado eletronicamente",
            "Motor AC",
            "Sensor de toque",
            "Display",
            "Transformador"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é um shield?",
        "alternativas": [
            "Placa que adiciona funções ao Arduino",
            "Motor auxiliar",
            "Sensor de água",
            "Tipo de transistor",
            "Módulo de LED"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é I2C?",
        "alternativas": [
            "Protocolo de dois fios",
            "Tipo de sensor",
            "Tipo de motor",
            "Sistema operacional",
            "Comando de repetição"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é SPI?",
        "alternativas": [
            "Protocolo de comunicação rápida",
            "Sensor de pressão",
            "Motor servo",
            "Porta USB",
            "Display gráfico"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é a Serial?",
        "alternativas": [
            "Comunicação entre Arduino e PC",
            "Menu de vídeos",
            "Motor DC",
            "Driver de LED",
            "Display LCD"
        ],
        "correta": 0
    },
    {
        "pergunta": "Para que serve Serial.begin()?",
        "alternativas": [
            "Ligar o Arduino",
            "Iniciar comunicação serial",
            "Ler sensor",
            "Gerar PWM",
            "Enviar corrente"
        ],
        "correta": 1
    },
    {
        "pergunta": "Para que serve Serial.println()?",
        "alternativas": [
            "Criar arquivo",
            "Imprimir texto na tela serial",
            "Enviar corrente",
            "Reiniciar Arduino",
            "Configurar pinos"
        ],
        "correta": 1
    },
    {
        "pergunta": "Qual é a função map()?",
        "alternativas": [
            "Converter um valor de uma faixa para outra",
            "Aumentar tensão",
            "Armazenar código",
            "Controlar motores AC",
            "Criar delays"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é um sensor ultrassônico?",
        "alternativas": [
            "Sensor de som ambiente",
            "Sensor que mede distância",
            "Sensor de temperatura",
            "Sensor de luz",
            "Sensor de pressão"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um sensor PIR?",
        "alternativas": [
            "Sensor de vibração",
            "Sensor de movimento baseado em calor",
            "Sensor de distância",
            "Sensor de água",
            "Sensor de cor"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um display LCD?",
        "alternativas": [
            "Componente de som",
            "Tela para exibir caracteres",
            "Motor com tela",
            "Sensor de toque",
            "Barra de LED"
        ],
        "correta": 1
    },
    {
        "pergunta": "O que é um potenciômetro?",
        "alternativas": [
            "Resistor variável",
            "Motor DC",
            "Sensor de pressão",
            "Relé",
            "Display colorido"
        ],
        "correta": 0
    },
    {
        "pergunta": "Qual porta do Arduino usa comunicação USB?",
        "alternativas": ["Serial", "PWM", "I2C", "SPI", "LAN"],
        "correta": 0
    },
    {
        "pergunta": "Qual placa é a menor?",
        "alternativas": ["Uno", "Mega", "Nano", "Due", "Omega"],
        "correta": 2
    },
    {
        "pergunta": "O que são bibliotecas no Arduino?",
        "alternativas": [
            "Arquivos que adicionam funções extras",
            "Sensores internos",
            "Motores",
            "Aplicativos de vídeo",
            "Drivers USB"
        ],
        "correta": 0
    },
    {
        "pergunta": "Onde o código do Arduino é escrito?",
        "alternativas": ["Notepad", "Arduino IDE", "Excel", "Word", "Chrome"],
        "correta": 1
    },
    {
        "pergunta": "Qual a função do botão RESET?",
        "alternativas": [
            "Apagar código",
            "Reiniciar o Arduino",
            "Desligar energia",
            "Converter PWM",
            "Salvar memória"
        ],
        "correta": 1
    },
    {
        "pergunta": "Para que serve o GND?",
        "alternativas": ["Alimentar módulo", "Enviar dados", "Referência de terra", "Gerar pulsos", "Transmitir vídeo"],
        "correta": 2
    },
    {
        "pergunta": "O que é a placa Arduino Due?",
        "alternativas": [
            "Placa com processador ARM",
            "Placa de som",
            "Placa para motores AC",
            "Sensor ultrassônico",
            "Protoboard"
        ],
        "correta": 0
    },
    {
        "pergunta": "O que é o bootloader?",
        "alternativas": [
            "Microcontrolador",
            "Programa que permite carregar código no Arduino",
            "Driver USB",
            "Resistor interno",
            "Memória RAM externa"
        ],
        "correta": 1
    },
    {
        "pergunta": "Como o Arduino é geralmente alimentado?",
        "alternativas": ["Ethernet", "USB", "Bluetooth", "Som", "Rádio"],
        "correta": 1
    },
    {
        "pergunta": "O que NÃO é um tipo de placa Arduino?",
        "alternativas": ["Uno", "Mega", "Nano", "RTX 4090", "Due"],
        "correta": 3
    }
]
# mostra o menu do jogo
def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Responder Quiz")
    print("2 - Exibir Regras")
    print("3 - Encerrar Programa")

# mostra as regras do jogo
def mostrar_regras():
    print("\n===== REGRAS DO JOGO =====")
    print("→ O quiz contém 20 perguntas sorteadas aleatoriamente.")
    print("→ Cada questão vale 0,5 pontos.")
    print("→ As alternativas são embaralhadas a cada execução.")
    print("→ Nota máxima: 10 pontos.")
    print("→ Digite apenas A, B, C, D ou E para responder.\n")

# sortea 20 questoes das 50
def sortear_questoes():
    return random.sample(banco_questoes, 20)

# exibe uma questao
def exibir_questao(numero, questao):
    print(f"\n{numero}. {questao['pergunta']}")

    alternativas = questao["alternativas"][:]  
    random.shuffle(alternativas)  

    indice_correto = alternativas.index(questao["alternativas"][questao["correta"]])

    letras = ["A", "B", "C", "D", "E"]

    for i, alt in enumerate(alternativas):
        print(f"   {letras[i]}) {alt}")

    return indice_correto

# verifica a resposta
def verificar_resposta(indice_correto):
    letras = ["A", "B", "C", "D", "E"]
    resposta = input("Sua resposta: ").strip().upper()

    while resposta not in letras:
        resposta = input("Digite apenas A, B, C, D ou E: ").strip().upper()

    return letras.index(resposta) == indice_correto

# mostra o resultado final
def exibir_resultado(pontos):
    print("\n===== RESULTADO FINAL =====")
    print(f"Pontuação: {pontos:.1f} / 10.0")
    
    if pontos == 10:
        print("Excelente! Você acertou tudo!")
    elif pontos >= 7:
        print("Muito bom! Você foi bem.")
    elif pontos >= 5:
        print("Você acertou mais da metade. Pode melhorar.")
    else:
        print("Estude mais e tente novamente!")

# a funcao principal do quiz
def responder_quiz():
    questoes = sortear_questoes()
    pontos = 0

    for i, questao in enumerate(questoes, start=1):
        indice_correto = exibir_questao(i, questao)
        acertou = verificar_resposta(indice_correto)

        if acertou:
            pontos += 0.5
            print("✔ Resposta correta!")
        else:
            print("✘ Resposta incorreta.")

    exibir_resultado(pontos)

# O loop principal do código
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            responder_quiz()
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "3":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")

main()
