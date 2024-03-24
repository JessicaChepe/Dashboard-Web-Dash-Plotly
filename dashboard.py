import dash
from dash import dcc, html
import plotly.express as px # Diseñar los graficos
import pandas as pd # Manejo de la data
from dash.dependencies import Input,Output

#df = pd.read_csv('data.csv', sep=';')
df = pd.read_csv('data.csv', sep=';', encoding='ISO-8859-1')

external_stylesheets = ['assets/styles.css', 'assets/s1.css']
#print(df)
#print(df.nombre.nunique())
#print(df.info())  # Muestra las primeras filas del DataFrame
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Ordenar los años de menor a mayor
sorted_years = sorted(df['anio'].unique())

app.layout = html.Div([
    html.Div([
        html.H1('TLBA Dashboard BI')
    ], className = 'banner'),
    html.Div([
        html.Div([
            html.P('Selecciona', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'ventas-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Adultos', 'value' : 'adultos_cantidad'},
                                {'label' : 'Adolescentes', 'value' : 'adolescentes_cantidad'},
                                {'label' : 'Niños', 'value' : 'menor_cantidad'},
                                {'label' : 'All', 'value' : 'all'}
                            ], value = 'all',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
            dcc.RadioItems(
                id='year-radioitems',
                labelStyle={'display': 'inline-block'},
                options=[{'label': year, 'value': year} for year in sorted_years],
                value=sorted_years[-1],
                style={'text-aling': 'center', 'color': 'black'},
                className='dcc_compon'
            ),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),

        html.Div([
            html.P('Imforme Anual', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            html.Div(id='total-sales-counter-pie', className='total-counter'),
            html.Div(id='total-sales-by-sede-year-pie', className='total-counter'),
            ], className='create_container2 five columns')
       

    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            html.Div([
                dcc.Interval(
                    id='update-interval',
                    interval=1000,  # Actualiza cada 1 segundo (puedes ajustar esto)
                    n_intervals=0
                ),
                html.Div(id='total-sales-counter', className='total-counter'),
            ], className='create_container2 five columns')
        ], className='row flex-display'),


        html.Div([

            html.Div([
                dcc.Graph(id = 'my_graph', figure = {})
                    ], className = 'create_container2 five columns'),

           

            html.Div([
                dcc.Graph(id = 'pie_graph', figure = {})
                    ], className = 'create_container2 five columns'),
        ]),              
               
    ], style={'display':'flex', 'flex-direction':'column'})

],id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('ventas-radioitems', component_property='value'),
    Input('year-radioitems', component_property='value')])

def update_graph(value, selected_year):
    filtered_df = df[df['anio'] == selected_year]

    if value == 'adultos_cantidad':
        fig = px.bar(
            data_frame=filtered_df,
            x='mes',
            y='adultos_cantidad',
            color='mes',
            title='Ventas x Mes',
            template='plotly_dark')
    else:
        if value == 'adolescentes_cantidad':
            fig = px.bar(
                data_frame=filtered_df,
                x='mes',
                y='adolescentes_cantidad',
                color='mes',
                title='Ventas x Mes',
                template='plotly_dark')
        else:
            if value == 'menor_cantidad':
                fig = px.bar(
                    data_frame=filtered_df,
                    x='mes',
                    y='menor_cantidad',
                    color='mes',
                    title='Ventas x Mes',
                    template='plotly_dark')
            else:
                fig = px.bar(
                    data_frame=filtered_df,
                    x='mes',
                    y='all',
                    title='Ventas x Mes',
                    color='mes')

    return fig

@app.callback(
    [Output('pie_graph', component_property='figure'),
    Output('total-sales-counter-pie', 'children'),
    Output('total-sales-by-sede-year-pie', 'children')],
    [Input('ventas-radioitems', component_property='value'),
    Input('year-radioitems', component_property='value')])

def update_graph_pie(value, selected_year):
    filtered_df = df[df['anio'] == selected_year]

    if value == 'adultos_cantidad':
        fig2 = px.pie(
            data_frame=filtered_df,
            names='nombre_sede',
            values='adultos_cantidad',
            title='Ventas x Sede',
            template='plotly_dark')
    else:
        if value == 'adolescentes_cantidad':
            fig2 = px.pie(
                data_frame=filtered_df,
                names='nombre_sede',
                values='adolescentes_cantidad',
                title='Ventas x Sede',
                template='plotly_dark')
        else:
            if value == 'menor_cantidad':
                fig2 = px.pie(
                    data_frame=filtered_df,
                    names='nombre_sede',
                    values='menor_cantidad',
                    title='Ventas x Sede',
                    template='plotly_dark')
            else:
                fig2 = px.pie(
                    data_frame=filtered_df,
                    names='nombre_sede',
                    values='all',
                    title='Ventas x Sede')
    total_sales_by_sede_year_pie = calculate_total_sales_by_sede_and_year_pie(filtered_df, value)
    total_sales = total_sales_by_sede_year_pie.sum()
    total_sales_by_sede_year_str = '  --  '.join([f' {key}: {value}' 
                                              for key, value in total_sales_by_sede_year_pie.items()])
    return fig2, f'Total de Ventas: {total_sales}', f'{total_sales_by_sede_year_str}'


def calculate_total_sales_by_sede_and_year_pie(filtered_df, selected_value):
    if selected_value == 'adultos_cantidad':
        total_sales_by_sede_year = filtered_df.groupby(['nombre_sede', 'anio'])['adultos_cantidad'].sum()
    elif selected_value == 'adolescentes_cantidad':
        total_sales_by_sede_year = filtered_df.groupby(['nombre_sede', 'anio'])['adolescentes_cantidad'].sum()
    elif selected_value == 'menor_cantidad':
        total_sales_by_sede_year = filtered_df.groupby(['nombre_sede', 'anio'])['menor_cantidad'].sum()
    else:
        total_sales_by_sede_year = filtered_df.groupby(['nombre_sede', 'anio'])['all'].sum()

    return total_sales_by_sede_year


@app.callback(
    Output('total-sales-counter', 'children'),
    Input('update-interval', 'n_intervals'),
    Input('ventas-radioitems', 'value'))
def update_total_sales_counter(n_intervals, selected_value):
    # Calcula el total de ventas según el valor seleccionado
    if selected_value == 'adultos_cantidad':
        total_sales = df['adultos_cantidad'].sum()
    elif selected_value == 'adolescentes_cantidad':
        total_sales = df['adolescentes_cantidad'].sum()
    elif selected_value == 'menor_cantidad':
        total_sales = df['menor_cantidad'].sum()
    else:
        total_sales = df['all'].sum()

    return f'Total de Ventas Consolidadas: {total_sales}'

if __name__ == ('__main__'):
    app.run_server(debug=True)
