# quiz-ardu-no

A proposta do código é fazer um quiz sobre arduíno com 50 questões, e nele precisa ter um menu, que mostre as regras do jogo e para iniciar o jogo. As funcionalidades principais são:

<br> As alternativas de cada questão são embaralhadas dinamicamente.
<br> Cada questão correta vale 0.5 ponto, totalizando uma pontuação máxima de 10.0 pontos.
<br> Exibe uma mensagem de desempenho final baseada na pontuação obtida.
<br> Um menu principal para iniciar o quiz, visualizar as regras ou encerrar o programa.

Ao executar, o programa exibirá o menu principal:

===== MENU PRINCIPAL =====
<br> 1 - Responder Quiz
<br> 2 - Exibir Regras
<br> 3 - Encerrar Programa
<br> Escolha uma opção: 

Digite 1 para iniciar o quiz e começar a responder as 20 questões sorteadas.

Visão Técnica:

O código é estruturado em funções Python para modularidade e clareza:

banco_questoes: É uma lista de dicionários que armazena todas as 50 perguntas, suas alternativas e o índice da resposta correta.

mostrar_menu() / mostrar_regras(): Funções para exibição das opções e regras do quiz.

sortear_questoes(): Utiliza a função random.sample() da biblioteca random para selecionar 20 questões de forma não repetida.

exibir_questao(): Imprime a pergunta e as alternativas. Crucialmente, ele embaralha as alternativas (random.shuffle()) e retorna o índice correto para a verificação.

verificar_resposta(): Recebe a entrada do usuário (A, B, C, D ou E), valida o formato e compara com a resposta correta.

responder_quiz(): É a função principal que itera sobre as 20 questões sorteadas e calcula a pontuação total.

main(): Contém o loop principal do programa, que controla a navegação pelo menu.
