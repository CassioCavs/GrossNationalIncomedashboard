
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO


url_theme1 = dbc.themes.CYBORG
url_theme2 = dbc.themes.LUX
template_theme1 = 'Cyborg'
template_theme2 = 'lux'


df = pd.read_csv('D:\codes\gross of pib per capita\Gross National Income Per Capita.csv', sep = ",")
country_options = [{'label': x, 'value': x} for x in df['Country'].unique()]
hemisphere_options = [{'label': x, 'value': x} for x in df['Hemisphere'].unique()]


app.layout = dbc.Container([
    dbc.Row([
         dbc.Col([
             ThemeSwitchAIO(aio_id = 'theme', themes = [url_theme1, url_theme2]),
             html.H3("Renda Nacional Bruta Per Capita"),
            
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
            dcc.Graph(id = 'line_graph')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                dcc.Dropdown(
                id = 'pais1',
                value = country_options[0]['label'],
                options = country_options
                ), # pode usar o sm e o md aqui também
                dcc.Graph(id = 'indicator1'),
                dcc.Graph(id = 'box1')
            ])
        ]),

        dbc.Col([
            dbc.Row([
                dcc.Dropdown(
                id = 'pais2',
                value = country_options[1]['label'],
                options = country_options
                ),
                dcc.Graph(id = 'indicator2'),
                dcc.Graph(id = 'box2')
            ])
        ])
    ])
])

@app.callback(
    Output('line_graph', 'figure'),
    [Input('country', 'value')]
)
def update_line_graph(selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    
    fig = go.Figure()
    for country in selected_countries:
        country_data = filtered_df[filtered_df['Country'] == country]
        x_data = country_data.columns[7:]  # Colunas de anos
        y_data = country_data.iloc[0, 7:]  # Valores de GNI per capita
        
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name=country))
    
    fig.update_layout(title="Renda per capita",
                      xaxis_title="Ano",
                      yaxis_title="RNB per Capita",
                      template='plotly_dark',
                      height=800,  
                     width=1250   
                     )

    
    return fig

@app.callback(
    Output('indicator1', 'figure'),
    Output('indicator2', 'figure'),
    Input('pais1', 'value'),
    Input('pais2', 'value')
)
def indicators(pais1, pais2):
    df_data = df.copy(deep=True)

    data_pais1 = df_data[df_data['Country'] == pais1]
    data_pais2 = df_data[df_data['Country'] == pais2]

    indicator_figs = []

    for pais, data in [(pais1, data_pais1), (pais2, data_pais2)]:
        initial_value = data.at[data.index[0], 'Gross National Income Per Capita (1990)']
        final_value = data.at[data.index[-1], 'Gross National Income Per Capita (2021)']
        percent_increase = ((final_value - initial_value) / initial_value) * 100

        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode='number+delta',
            title={'text': pais},
            value=final_value,
            number={'prefix': '$', 'valueformat': '.2f'},
            delta={'relative': True, 'valueformat': '.1%', 'reference': initial_value}
        ))

        indicator_figs.append(fig)
    
    return indicator_figs


@app.callback(
    Output('box1', 'figure'),
    Input('pais1', 'value'),
)
def box1(pais1):
    df_data = df.copy(deep=True)
    data_pais = df_data[df_data['Country'] == pais1]
    
    # Filtrar as colunas correspondentes aos anos de 1990 a 2021
    columns = df_data.columns[8:30]
    data_pais_filtered = data_pais[columns]

    # Criar um DataFrame com os anos e os valores de renda interna bruta
    data = {'Ano': data_pais_filtered.columns, 'Renda Interna Bruta': data_pais_filtered.values[0]}
    df_renda = pd.DataFrame(data)

    # Criar o gráfico de dispersão
    fig = px.scatter(df_renda, x='Ano', y='Renda Interna Bruta', title=f'Renda Interna Bruta - {pais1} (1990-2021)', template='plotly_dark')

    return fig


@app.callback(
    Output('box2', 'figure'),
    Input('pais2', 'value'),
)
def box1(pais2):
    df_data = df.copy(deep=True)
    data_pais = df_data[df_data['Country'] == pais2]
    
    # Filtrar as colunas correspondentes aos anos de 1990 a 2021
    columns = df_data.columns[8:30]
    data_pais_filtered = data_pais[columns]

    # Criar um DataFrame com os anos e os valores de renda interna bruta
    data = {'Ano': data_pais_filtered.columns, 'Renda Interna Bruta': data_pais_filtered.values[0]}
    df_renda = pd.DataFrame(data)

    # Criar o gráfico de dispersão
    fig = px.scatter(df_renda, x='Ano', y='Renda Interna Bruta', title=f'Renda Interna Bruta - {pais2} (1990-2021)', template='plotly_dark')

    return fig



if __name__ == '__main__':
    app.run_server(debug = True, port='8052')