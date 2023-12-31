# Importando as bibliotecas necessárias
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Importando outros módulos do seu aplicativo (verifique a sua implementação real)
from app import *
from dash_bootstrap_templates import ThemeSwitchAIO

# Definindo URLs e templates de temas para uso posterior
url_theme1 = dbc.themes.CYBORG
url_theme2 = dbc.themes.LUX
template_theme1 = 'cyborg'
template_theme2 = 'lux'

# Carregando os dados do arquivo CSV
df = pd.read_csv('GNI_per_capita_processed.csv', sep = ",")
# Criando opções para seleção de país e hemisfério
country_options = [{'label': x, 'value': x} for x in df['Country'].unique()]
hemisphere_options = [{'label': x, 'value': x} for x in df['Hemisphere'].unique()]

# Definindo o layout da aplicação usando o framework Bootstrap
app.layout = dbc.Container([
    dbc.Row([
         dbc.Col([
             # Componente de troca de tema
             ThemeSwitchAIO(aio_id='theme', themes=[url_theme1, url_theme2]),
             # Título da página
             html.H3("Renda Nacional Bruta Per Capita"),
             # Dropdown para seleção de países
            dcc.Dropdown(
                id='country',
                value = [country['label'] for country in country_options[:3]],
                multi = True,
                options = country_options
            ),
         ])
    ]),
    dbc.Row([
        dbc.Col([
            # Gráfico de linha para exibir a renda per capita ao longo do tempo
            dcc.Graph(id='line_graph')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                # Dropdown para selecionar o primeiro país para análise
                dcc.Dropdown(
                id = 'pais1',
                value = country_options[0]['label'],
                options = country_options
                ), 
                # Gráfico de indicador para exibir informações sobre o primeiro país
                dcc.Graph(id = 'indicator1'),
                # Gráfico de dispersão para exibir a renda interna bruta do primeiro país
                dcc.Graph(id = 'box1')
            ])
        ]),
        dbc.Col([
            dbc.Row([
                # Dropdown para selecionar o segundo país para análise
                dcc.Dropdown(
                id = 'pais2',
                value = country_options[1]['label'],
                options = country_options
                ),
                # Gráfico de indicador para exibir informações sobre o segundo país
                dcc.Graph(id = 'indicator2'),
                # Gráfico de dispersão para exibir a renda interna bruta do segundo país
                dcc.Graph(id = 'box2')
            ])
        ]),
    ]),
    dbc.Row([
        dbc.Col([
                # Dropdown para seleção de hemisfério
                dcc.Dropdown(
                id='Hemisphere',
                value = [hemisphere['label'] for hemisphere in hemisphere_options[:2]],
                multi = True,
                options = hemisphere_options),
                # Gráfico de linha para comparar a soma de GNI per capita por ano
            dcc.Graph(id='line_graph2'),
    ])
])
])

# Definindo o callback para atualizar o gráfico de linha principal
@app.callback(
    Output('line_graph', 'figure'),
    Input('country', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def update_line_graph(selected_countries, toggle):
    filtered_df = df[df['Country'].isin(selected_countries)]
    template = template_theme1 if toggle else template_theme2
    
    # Criando um objeto de gráfico
    fig = go.Figure()
    for country in selected_countries:
        country_data = filtered_df[filtered_df['Country'] == country]
        x_data = country_data.columns[7:]  # Colunas de anos
        y_data = country_data.iloc[0, 7:]  # Valores de GNI per capita
        
        # Adicionando uma linha para cada país no gráfico
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name=country))
    
    # Atualizando o layout do gráfico
    fig.update_layout(
        template=template,
        title="Renda per capita",
        xaxis_title="Ano",
        yaxis_title="RNB per Capita",
        height=800,
        width=1250
    )
    return fig

# Definindo o callback para atualizar os gráficos de indicadores
@app.callback(
    Output('indicator1', 'figure'),
    Output('indicator2', 'figure'),
    Input('pais1', 'value'),
    Input('pais2', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def indicators(pais1, pais2, toggle):
    df_data = df.copy(deep=True)
    template = template_theme1 if toggle else template_theme2

    # Obtendo dados para os países selecionados
    data_pais1 = df_data[df_data['Country'] == pais1]
    data_pais2 = df_data[df_data['Country'] == pais2]

    indicator_figs = []

    for pais, data in [(pais1, data_pais1), (pais2, data_pais2)]:
        # Calculando valores para os indicadores
        initial_value = data.at[data.index[0], 'Gross National Income Per Capita (1990)']
        final_value = data.at[data.index[-1], 'Gross National Income Per Capita (2021)']
        percent_increase = ((final_value - initial_value) / initial_value) * 100

        # Criando um gráfico de indicador
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode='number+delta',
            title={'text': pais},
            value=final_value,
            number={'prefix': '$', 'valueformat': '.2f'},
            delta={'relative': True, 'valueformat': '.1%', 'reference': initial_value}
        ))

        fig.update_layout(template=template)

        indicator_figs.append(fig)
    
    return indicator_figs

# Definindo o callback para atualizar o gráfico de dispersão do primeiro país
@app.callback(
    Output('box1', 'figure'),
    Input('pais1', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def box1(pais1, toggle):
    df_data = df.copy(deep=True)
    data_pais = df_data[df_data['Country'] == pais1]
    template = template_theme1 if toggle else template_theme2

    # Filtrando as colunas de 1990 a 2021
    columns = df_data.columns[8:39]
    data_pais_filtered = data_pais[columns]

    # Criando um DataFrame para a renda interna bruta
    data = {'Ano': data_pais_filtered.columns, 'Renda Interna Bruta': data_pais_filtered.values[0]}
    df_renda = pd.DataFrame(data)

    # Criando o gráfico de dispersão
    fig = px.scatter(df_renda, x='Ano', y='Renda Interna Bruta', title=f'Renda Interna Bruta - {pais1} (1990-2021)', template=template)

    return fig

# Definindo o callback para atualizar o gráfico de dispersão do segundo país
@app.callback(
    Output('box2', 'figure'),
    Input('pais2', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'),'value')
)
def box2(pais2, toggle):
    df_data = df.copy(deep=True)
    data_pais = df_data[df_data['Country'] == pais2]
    template = template_theme1 if toggle else template_theme2
    
    # Filtrando as colunas de 1990 a 2021
    columns = df_data.columns[8:39]
    data_pais_filtered = data_pais[columns]

    # Criando um DataFrame para a renda interna bruta
    data = {'Ano': data_pais_filtered.columns, 'Renda Interna Bruta': data_pais_filtered.values[0]}
    df_renda = pd.DataFrame(data)

    # Criando o gráfico de dispersão
    fig = px.scatter(df_renda, x='Ano', y='Renda Interna Bruta', title=f'Renda Interna Bruta - {pais2} (1990-2021)', template=template)

    return fig

# Definindo o callback para atualizar o gráfico de linha do hemisfério
@app.callback(
    Output('line_graph2', 'figure'),
    Input('Hemisphere', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_line_graph(selected_hemisphere, toggle):
    filtered_df = df[df['Hemisphere'].isin(selected_hemisphere)]
    template = template_theme1 if toggle else template_theme2
    
    fig = go.Figure()

    # Calculando a soma dos valores de GNI per capita para cada ano
    columns = df.columns[8:39]
    grouped_data = filtered_df.groupby('Hemisphere')[columns].sum()

    # Adicionando linhas para os hemisférios selecionados
    for hemisphere in selected_hemisphere:
        fig.add_trace(go.Scatter(x=columns, y=grouped_data.loc[hemisphere], mode='lines+markers', name=hemisphere))
    
    fig.update_layout(
        template=template,
        title="Comparação de Soma de RNB per capita por Ano",
        xaxis_title="Ano",
        yaxis_title="Soma de RNB per Capita",
        
    )

    return fig

# Iniciando o servidor da aplicação
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
