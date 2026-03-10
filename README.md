# Projeto Gerenciador de Catálogo (Python + JSON)

> **Status:** Concluído ✔️

Este projeto é uma aplicação de terminal (console) desenvolvida em Python. O objetivo foi aplicar e consolidar conceitos fundamentais de programação, criando um sistema completo de **CRUD** (Create, Read, Update, Delete) que utiliza um arquivo `json` local como "banco de dados" para persistência de dados.

Este projeto serviu como a base fundamental (Etapa 1) para a minha jornada de aprendizado em desenvolvimento Back-End.

---

## Funcionalidades

A aplicação permite ao usuário gerenciar um catálogo de itens (como jogos, filmes, livros, etc.) através de um menu interativo com as seguintes operações:

* **[1] Adicionar:** Cria um novo item (título e gênero) e o salva no catálogo.
* **[2] Listar:** Exibe todos os itens atualmente salvos no catálogo, com seus respectivos índices.
* **[3] Buscar por Gênero:** Filtra e exibe todos os itens que correspondem a um gênero específico (ignorando maiúsculas/minúsculas).
* **[4] Excluir Item:** Remove um item do catálogo com base no seu título.
* **[0] Sair:** Encerra a aplicação.

---

## O que eu aprendi e apliquei

Este projeto foi um desafio prático focado em ir além da teoria. As principais habilidades e conceitos aplicados foram:

* **Modularização:** Estruturação do código em funções coesas e reutilizáveis (`carregar_dados`, `salvar_dados`, `adicionar_item`, etc.).
* **Estruturas de Dados:** Uso intensivo de **Listas** (para o catálogo) e **Dicionários** (para os itens) como a principal forma de organizar os dados em memória.
* **Persistência de Dados (I/O):**
    * Uso do módulo `json` para serializar (salvar) e desserializar (carregar) dados.
    * Gerenciamento de arquivos (`with open(...)`) de forma segura, especificando `encoding='utf-8'`.
* **Robustez e Tratamento de Erros:**
    * Uso de `try/except` para lidar com cenários reais, como `FileNotFoundError` (quando o programa roda pela primeira vez) e `json.JSONDecodeError` (em caso de arquivo corrompido).
* **Lógica de Programação Avançada (Bug Fixing):**
    * Ao implementar a função `excluir_item()`, evitei o bug de "índice deslizante" (mutar uma lista durante a iteração).
    * Em vez disso, implementei o padrão de **"Reconstrução de Lista"** (criar uma nova lista apenas com os itens a serem mantidos), que é uma solução mais segura, limpa e profissional.

---

## Como Rodar

Este projeto usa apenas bibliotecas padrão do Python (como `json`).

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/lucaslibe/projeto-catalogo-json.git](https://github.com/lucaslibe/projeto-catalogo-json.git)
    ```
2.  Navegue até a pasta:
    ```bash
    cd projeto-catalogo-json
    ```
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

---
