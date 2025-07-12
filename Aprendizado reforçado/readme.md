🤖 Reinforcement Learning (Aprendizado por Reforço)
O Aprendizado por Reforço (RL) é uma área do Machine Learning focada em treinar agentes para tomar decisões sequenciais em ambientes dinâmicos, maximizando recompensas cumulativas. Ele é inspirado no comportamento de aprendizado por tentativa e erro observado em humanos e animais.

🧠 Conceitos Fundamentais
No Reinforcement Learning, o agente interage com um ambiente seguindo este ciclo:

O agente observa o estado atual do ambiente (
𝑠
𝑡
s 
t
​
 ).

Ele escolhe uma ação (
𝑎
𝑡
a 
t
​
 ) com base em uma política (
𝜋
π).

O ambiente retorna uma recompensa (
𝑟
𝑡
r 
t
​
 ) e um novo estado (
𝑠
𝑡
+
1
s 
t+1
​
 ).

O agente atualiza sua política para melhorar suas decisões futuras.

Esse processo é modelado como um Processo de Decisão de Markov (MDP), definido por:

𝑆
S: Conjunto de estados.

𝐴
A: Conjunto de ações.

𝑃
(
𝑠
′
∣
𝑠
,
𝑎
)
P(s 
′
 ∣s,a): Probabilidade de transição.

𝑅
(
𝑠
,
𝑎
)
R(s,a): Função de recompensa.

𝛾
γ: Fator de desconto (importância de recompensas futuras).

📐 Fórmula chave
O objetivo do agente é encontrar uma política 
𝜋
(
𝑎
∣
𝑠
)
π(a∣s) que maximize o retorno esperado:

𝐺
𝑡
=
∑
𝑘
=
0
∞
𝛾
𝑘
𝑟
𝑡
+
𝑘
+
1
G 
t
​
 = 
k=0
∑
∞
​
 γ 
k
 r 
t+k+1
​
 
A função-valor 
𝑉
𝜋
(
𝑠
)
V 
π
 (s) para uma política 
𝜋
π é:

𝑉
𝜋
(
𝑠
)
=
𝐸
𝜋
[
𝐺
𝑡
 
∣
 
𝑆
𝑡
=
𝑠
]
V 
π
 (s)=E 
π
​
 [G 
t
​
 ∣S 
t
​
 =s]
🚀 Abordagens Populares
✅ Métodos Baseados em Valor

Q-Learning: Aprende a função-ação valor 
𝑄
(
𝑠
,
𝑎
)
Q(s,a).

SARSA: Similar ao Q-Learning, mas segue a política durante o aprendizado.

✅ Métodos Baseados em Política

Policy Gradient: Ajusta diretamente a política 
𝜋
(
𝑎
∣
𝑠
,
𝜃
)
π(a∣s,θ).

✅ Métodos Ator-Crítico (Actor-Critic)

Combina os dois: um ator atualiza a política e um crítico estima os valores.

✅ Aprendizado Profundo por Reforço

Deep Q-Networks (DQN): Usa redes neurais para aproximar 
𝑄
(
𝑠
,
𝑎
)
Q(s,a).

PPO (Proximal Policy Optimization): Algoritmo eficiente para políticas contínuas.

📦 Aplicações
🎮 Jogos: AlphaGo, OpenAI Five.

🚗 Veículos Autônomos: Controle de direção e navegação.

📈 Finanças: Estratégias de negociação adaptativas.

🤖 Robótica: Aprendizado de movimentos complexos.

