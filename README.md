# Projeto_C213 Sistemas Dinâmicos

Projeto de Controle Digital da disciplina C213 laboratório. 

Para cada equipe, é disponibilizado (via portal acadêmico e Teams) uma
sequência de amostras da resposta em malha aberta de uma planta de nível para
uma entrada do tipo degrau de amplitude 50.

## Instalações necessárias

### Python

`$ python -m pip install numpy`

Numpy, Scipy, Matplotlib e Control:

` $ sudo apt-get install python-numpy python-scipy python-matplotlib python-control`

### Matlab

Instalar o pacote Control
`>> pkg install -forge control`

Carregar o pacote Control
`>> pkg load control`

## Controle Digital

### Modelagem  do Sistema Dinâmico

 **Estimador de Mínimos Quadrados**
 
 Utiliza uma sequência de amostras da entrada e da saída do sistema, para criar uma relação entre elas. Essa relação pode ser escrita em forma de uma equação, denominada Equação a Diferenças.
 
 𝒚[𝒎] = 𝒂𝟏. 𝒚[𝒎 − 𝟏] + 𝒃𝟏.𝒖[𝒎 − 𝟏]
 
 Essa equação relaciona a saída em determinada amostra m com a saída e a entrada na amostra m-1.

 ### Sistema Dinâmico
 Em um sistema dinâmico, há duas possibilidades de operação:
- Operação em malha aberta;
- Operação em malha fechada.

Na Operação em **malha aberta**, o sinal de entrada (Set Point - SP) é inserido
no sistema e obtém-se um sinal de saída (Process Value - PV) em resposta a
aquela entrada, de acordo com o comportamento dinâmico do sistema.

Na Operação em **malha fechada**, o sinal que é inserido na entrada sistema é
nomeado como Erro. Esse sinal é obtido a partir da subtração do Set Point por
Process Value: **Erro = SP - PV**

Para reduzir/eliminar a inserção/aumento do erro em regime permanente, pode-se inserir um controlador na malha do sistema. O controlador tem como entrada o Erro do sistema e a saída do controlador é inserido na entrada do sistema. 

O controlador possui três ganhos:
- 𝐾𝑝 – Ganho proporcional
- 𝐾𝑖 – Ganho integral
-  𝐾𝑑 – Ganho derivativo
Cada tipo de ganho gera um comportamento diferente no sistema.









