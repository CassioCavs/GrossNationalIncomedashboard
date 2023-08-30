# Análise de Renda Nacional Bruta Per Capita

Este projeto realiza uma análise da Renda Nacional Bruta (Gross National Income - GNI) per capita ao longo do tempo para diferentes países e hemisférios. O objetivo é visualizar e comparar a evolução da renda per capita entre países e também analisar a distribuição do GNI per capita em cada país.

## Dados

O repositório de dados utilizado para este projeto é o [Gross National Income Per Capita Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/gross-national-income-per-capita) disponível no Kaggle. Este conjunto de dados contém informações sobre o GNI per capita de diversos países ao longo dos anos.

## Bibliotecas e Ferramentas

Este projeto utiliza a biblioteca Dash para criar uma aplicação web interativa que permite a visualização dos gráficos e análises. Além disso, são utilizadas as bibliotecas Plotly e pandas para a criação e manipulação dos gráficos e dos dados, respectivamente.

## Como Executar

Certifique-se de ter as bibliotecas necessárias instaladas no seu ambiente Python. Você pode instalá-las utilizando o seguinte comando:






```sh
pip install dash dash-bootstrap-components plotly pandas dash-bootstrap-templates
```





## Como Executar

Após a instalação das bibliotecas, você pode executar a aplicação utilizando o seguinte comando:






```
python app.py
```


Isso iniciará o servidor da aplicação e você poderá acessar a interface através do seu navegador utilizando o endereço `http://localhost:8052/`.

## Funcionalidades

- **Seleção de Países e Hemisférios:** É possível selecionar os países e hemisférios para visualizar os gráficos específicos para essas seleções.

- **Troca de Tema:** A aplicação oferece um switch para troca de tema, permitindo alternar entre os temas "CYBORG" e "LUX".

- **Gráficos de Linha:** O gráfico principal exibe a evolução da Renda Nacional Bruta per capita ao longo do tempo para os países selecionados.

- **Indicadores:** Os gráficos de indicadores apresentam o valor final da Renda Nacional Bruta per capita, juntamente com a variação percentual em relação ao valor inicial.

- **Gráficos de Dispersão:** Os gráficos de dispersão exibem a distribuição da Renda Interna Bruta para os anos de 1990 a 2021 para os países selecionados.

- **Comparação de Soma de GNI per capita por Ano:** Este gráfico compara a soma dos valores de GNI per capita para os anos de 1990 a 2021, agrupados por hemisfério.
  
# Temas Visuais
Você pode alternar entre dois temas visuais diferentes: CYBORG e LUX. O botão de alternância de tema está localizado na parte superior do painel.

## Autor

[Cássio Lima Cavalcante](https://github.com/CassioCavs) e [Andrey Souza Ranieri](https://github.com/andreysrx)

# Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para este projeto. Basta abrir uma issue ou enviar um pull request.

# Licença
Este projeto está licenciado sob a [MIT License](https://github.com/CassioCavs/GrossNationalIncomedashboard/blob/main/LICENSE).

