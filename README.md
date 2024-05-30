## Visão Geral
Este projeto tem como objetivo desenvolver um sistema de inventário doméstico que permita aos usuários registrar, gerenciar e visualizar itens em suas residências. A aplicação será inicialmente desenvolvida em linha de comando e, posteriormente, será expandida para uma interface gráfica. O sistema ajudará os usuários a manterem um controle detalhado de seus pertences, facilitando a organização e gestão de seus bens pessoais.

## Objetivos do Projeto

Permitir aos usuários adicionar novos itens ao inventário, fornecendo informações como identificador único, nome, descrição e quantidade.
Visualizar Itens

Prover uma interface para que os usuários possam visualizar todos os itens cadastrados, com detalhes completos de cada item.
Editar Itens

Oferecer funcionalidade para que os usuários possam editar as informações de itens existentes no inventário, como nome, descrição e quantidade.
Excluir Itens

Implementar a capacidade de remover itens do inventário, garantindo que a lista de itens permaneça atualizada e relevante.
Pesquisar Itens

Adicionar funcionalidades de pesquisa para que os usuários possam encontrar itens específicos rapidamente, utilizando critérios como nome ou identificador.
Persistência de Dados

Utilizar armazenamento em JSON para manter os dados do inventário persistentes entre sessões de uso da aplicação.
Estrutura do Projeto
O projeto será estruturado em módulos para facilitar a manutenção e a escalabilidade. Os principais componentes serão:

Módulo Principal

Ponto de entrada do programa.
Gerencia a interação do usuário.
Módulo de Dados

Gerencia a persistência de dados.
Interage com arquivos JSON para salvar e carregar dados.
Módulo de Itens

Define a estrutura de um item.
Contém métodos para manipulação de itens (criação, edição, exclusão, etc.).
Módulo de Interface de Linha de Comando

Gerencia a interface com o usuário.
Exibe menus e recebe entradas.
Diagrama de Componentes
plaintext
Copiar código

```plaitext
+--------------------+
| Módulo Principal   |
+--------------------+
           |
           v
+--------------------+
| Módulo de Interface|
| de Linha de Comando|
+--------------------+
           |
           v
+--------------------+
|   Módulo de Itens  |
+--------------------+
           |
           v
+--------------------+
|   Módulo de Dados  |
+--------------------+
```