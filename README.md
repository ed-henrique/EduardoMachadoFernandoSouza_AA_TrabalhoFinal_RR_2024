# Trabalho Final de Análise de Algoritmos (DCC606 - 2024)

- [Artigo](./paper.pdf)
- [Apresentação](./presentation.pdf)
- [Roadmap](https://github.com/users/ed-henrique/projects/2)

## Integrantes

- Eduardo Henrique Freire Machado (2020001617);
- Fernando Souza Rodrigues (2019037493).

## Introdução

Este trabalho faz a análise de um algoritmo que utiliza de Programação Dinâmica para resolver o Problema da Mochila 0/1 (*Knapsack Problem 0/1*). A análise engloba:

- Função de custo e complexidade do algoritmo;
- Código em C do algoritmo proposto;
- *Benchmark* do algoritmo com diferentes entradas;
- Gráfico mostrando a relação entrada-tempo e sua tendência de comportamento assintótico;

Ainda mostramos a comparação entre os resultados do algoritmo proposto e de outra solução, utilizando *Backtracking*.

## Aplicações Reais do Problema da Mochila

- **Logística e transporte**: Em operações de transporte, como na escolha de quais itens carregar em um caminhão ou aeronave com espaço limitado, é preciso maximizar o valor ou a importância dos itens, respeitando as restrições de peso ou volume;
- **Gestão de portfólio financeiro**: Investidores podem usar o problema da mochila para decidir como alocar recursos em diferentes ativos financeiros, maximizando o retorno esperado enquanto respeitam limites de investimento, como um orçamento fixo;
- **Planejamento de atividades**: Na gestão de tempo, por exemplo, um profissional pode ter várias tarefas a realizar e um tempo limitado. O problema da mochila ajuda a priorizar quais tarefas realizar para maximizar a produtividade;
- **Seleção de projetos**: Empresas com um orçamento limitado podem usar essa abordagem para selecionar um conjunto de projetos que maximizem o retorno ou o impacto, respeitando a restrição financeira;
- **Planejamento de expedições**: Em atividades ao ar livre, como caminhadas ou viagens, deve-se escolher o que levar em uma mochila limitada em termos de peso ou espaço, maximizando o conforto ou utilidade dos itens selecionados;
- **Planejamento de campanhas publicitárias**: Em marketing, uma empresa pode ter um orçamento de publicidade e diferentes canais de marketing com custos e retornos variados. O problema da mochila pode ajudar a escolher a combinação ideal de investimentos em publicidade.

## Cálculos de Custo e Complexidade

### Programação Dinâmica

<!-- TODO -->

### Algoritmo Guloso

<!-- TODO -->

## Resultados de Benchmark

### Literatura

<!-- TODO -->

### Equipe

<div align="center">

</div>

## Demonstração Visual

<!-- TODO -->

## Objetivos

- [ ] Função de custo e complexidade;
- [x] Código em C do algoritmo proposto;
- [x] Experimentação com a execução do algoritmo com diferentes entradas e coleta de tempo de execução;
- [x] Gráfico de linha com o tempo de execução em relação a cada entrada e análise da tendência de comportamento assintótico.

## Considerações

- Binários em C foram compilados usando o `gcc`, com as flags `Wall`, `Wextra` e `-O3`.

