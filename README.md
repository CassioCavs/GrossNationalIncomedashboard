# Projeto de Análise de Renda Nacional Bruta Per Capita

Este repositório contém um projeto de análise de Renda Nacional Bruta (RNB) per capita, utilizando a biblioteca Dash para a criação de visualizações interativas. O projeto visa visualizar e comparar a RNB per capita de diferentes países ao longo dos anos, bem como fornecer insights sobre o crescimento econômico ao longo do tempo.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- Dash
- Dash Bootstrap Components
- Plotly Express
- Plotly Graph Objects
- Pandas
- dash-bootstrap-templates

Você pode instalá-las utilizando o seguinte comando:




```sh
pip install dash dash-bootstrap-components plotly pandas dash-bootstrap-templates
```





## Como Executar
Clone este repositório para o seu ambiente local.
Certifique-se de que os dados do arquivo "Gross National Income Per Capita.csv" estão disponíveis no diretório.
Navegue até o diretório do projeto e execute o arquivo app.py:





```
python app.py
```


Isso iniciará o servidor de desenvolvimento e você poderá acessar o painel interativo no seu navegador em http://localhost:8052/.

## Recursos
- Painel de Visualização
O painel de visualização é composto por várias seções interativas:

- Seleção de Países: Escolha os países para visualizar no gráfico de linha e nas seções de indicadores.
- Gráfico de Linha: Exibe a RNB per capita ao longo dos anos para os países selecionados.
- Indicadores: Apresenta indicadores econômicos para os dois países selecionados, incluindo o valor final, variação percentual e valor absoluto.
- Gráficos de Dispersão: Mostra a distribuição da Renda Interna Bruta ao longo dos anos para os países selecionados.
# Temas Visuais
Você pode alternar entre dois temas visuais diferentes: CYBORG e LUX. O botão de alternância de tema está localizado na parte superior do painel.

# Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para este projeto. Basta abrir uma issue ou enviar um pull request.

# Licença
Este projeto está licenciado sob a MIT License.

