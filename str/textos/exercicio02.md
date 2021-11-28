## Exercicio 02
#### [Algoritmo](../algoritmos/exercicio02.c)

Considere um sistema que monitore as condições de operação de um Data
Center. O sistema deve monitorar a temperatura e a existência de fumaça no ambiente,
além da tensão da rede elétrica. Caso alguma dessas variáveis esteja fora do limite
estabelecido, um sinal sonoro deve ser emitido por uma sirene (buzzer) enquanto essa
condição persistir. Ao mesmo tempo, um led vermelho deverá ser aceso indicando a
ocorrência do sinistro. Se a situação voltar ao normal, a sirene deve parar de tocar, mas o led deverá continuar aceso, indicando que algo ocorreu. Esse led só pode apagar quando o administrador do Data Center pressionar uma chave. Além de acionar a sirene e acender o
led, o sistema deverá também enviar, pela interface serial, uma única vez, uma mensagem
avisando sobre qual sinistro ocorreu, tipo “Temperatura elevada”. O sistema possui ainda um sensor (uma chave) na porta de entrada do Data Center. Toda vez que a porta por aberta (chave acionada), uma mensagem deverá ser enviada pela interface serial avisando sobre essa ocorrência, também uma única vez.  

Utilizando a IDE do Arduino e o FreeRTOS, elaborar 4 tarefas, de acordo com o indicado
abaixo:

-  Uma tarefa para a leitura do sensor de temperatura, com uma pilha de tamanho 64, e período da tarefa igual a 500 ms;
- Uma tarefa para a leitura do sensor de fumaça, com uma pilha de tamanho 64, e período da tarefa igual a 1 seg;
-  Uma tarefa para a leitura do sensor de tensão, com uma pilha de tamanho 64, e período da tarefa igual a 100 ms;
-  Uma tarefa para gerenciar a leitura das duas chaves e desligar o sinal sonoro, com uma pilha de tamanho 128, e período da tarefa igual a 200 ms;   

Como cada tarefa terá que enviar informações pela interface serial, <u>utilizar um mutex para controlar o acesso a esse periférico</u>.

A tarefa de maior prioridade deve ser a tarefa de leitura da tensão da rede elétrica, as tarefas de leitura da temperatura e fumaça deverão ter uma prioridade intermediária, e a tarefa de leitura das chaves será a de menor prioridade.  
Considere que os 3 sensores (temperatura, fumaça e tensão) estão ligados às entradas
analógicas do microcontrolador, devendo ser lidos pela instrução de leitura da entrada
analógica da IDE do Arduino. Além disso considere como limites para acionamento do
sistema, as constantes LIMIAR_TEMPERATURA, LIMIAR_FUMAÇA e LIMIAR_TENSÃO. 

Considere também que as duas chaves (desligamento do led vermelho e porta de entrada),
o buzzer e o próprio led vermelho estão ligados, cada um deles, à pinos de entrada/saída digitais do microcontrolador.

Faça as inicializações necessárias na função setup() da IDE Arduino, tais como porta serial,
pinos (entradas/saídas digitais) e criação das tarefas e do mutex.
