# efut - quiz futebolistico

Desafio de criar uma aplicação de quiz futebolístico. Usando dados de resultados de partidas, times e campeonatos de futebol provenientes de uma API desenvolver um mini game de perguntas e respostas.

Neste quiz a máquina fará perguntas como: "Quem foi o último campeão do Campeonato Brasileiro?", "Quantos jogos o flamengo ganhou este ano?" ao usuário, que irá ganhar ou perder pontos de acordo com as respostas

## Dados

O [RapidAPI](https://rapidapi.com/) é um site que reúne diversas APIs (as mais diversas) onde você pode se cadastrar e usa-las. 

Neste projeto será usada a [API Football](https://www.api-football.com/documentation#general-api-demo) para obter dados de partidas, campeonatos e times de futebol

## Stack

Uma aplicação python com framework **Django no backend** que irá:
- Baixar dados sobre partidas,times e campeonatos providos pela API e armazenar ( para diminuir o volume de requisições à API, que é paga, vamos salvar os dados localmente)
- Prover para o frontend uma API final que entregue perguntas, receba respostas e gerencie a pontuação
- Criar um ranking entre os usuários

Um aplicação **React no frontend** que irá:
- Receber um nome de usuário e iniciar uma seção
- Solicitar ao backend perguntas a serem feitas ao usuário e devolver as respectivas respostas
- Exibir ranking e pontuação do jogador atual

