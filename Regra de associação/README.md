# 📊 Association Rule Learning

**Association Rule Learning** (Aprendizado de Regras de Associação) é uma técnica de *Data Mining* usada para descobrir padrões e relações entre itens em grandes conjuntos de dados. Seu uso mais comum está na análise de cestas de compras (*Market Basket Analysis*), onde o objetivo é entender que itens são frequentemente comprados juntos.

---

## 🧠 Objetivo

Extrair regras do tipo:


Ou seja, descobrir que, por exemplo, clientes que compram **A** e **B** também tendem a comprar **C**.

---

## ⚙️ Métricas Principais

### ✅ Suporte (Support)

Indica com que frequência um conjunto de itens aparece no banco de dados.

$$
\text{Support}(A \rightarrow B) = \frac{\text{Número de transações contendo } A \cup B}{\text{Número total de transações}}
$$

---

### ✅ Confiança (Confidence)

Mede a probabilidade de encontrar o item **B** em transações que já contêm o item **A**.

$$
\text{Confidence}(A \rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)}
$$

---

### ✅ Lift

Mede o quanto **A** e **B** ocorrem juntos mais frequentemente do que seria esperado se fossem estatisticamente independentes.

$$
\text{Lift}(A \rightarrow B) = \frac{\text{Confidence}(A \rightarrow B)}{\text{Support}(B)}
$$


- **Lift > 1**: associação positiva (B é mais provável dado A)
- **Lift = 1**: independência
- **Lift < 1**: associação negativa

---

## 🧮 Algoritmos Populares

### 🔹 Apriori

- Gera conjuntos candidatos e remove os infrequentes.
- Usa a propriedade de que todos os subconjuntos de um itemset frequente também são frequentes.
- Requer múltiplas passagens sobre o banco de dados.

### 🔹 FP-Growth (Frequent Pattern Growth)

- Usa uma estrutura chamada **FP-Tree** para armazenar a base de dados em formato comprimido.
- Evita geração explícita de candidatos.
- Mais eficiente para grandes volumes de dados.

---


📌 Aplicações
🛒 Market Basket Analysis: descobrir produtos que são comprados juntos

💳 Detecção de Fraude: encontrar padrões incomuns de transações

👨‍⚕️ Diagnóstico Médico: associação entre sintomas e doenças

🧑‍💻 Recomendação de Conteúdo: sugerir produtos ou filmes com base em preferências

🌐 Comportamento Online: analisar cliques e padrões de navegação