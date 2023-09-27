import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input,Output
#base de datos de la Huasteca
ca=pd.read_csv('cultivos_asociados2.csv')
ud=pd.read_csv('unidaddomestica_copy.csv')
pc=pd.read_csv('productor_ciclo.csv')
s=pd.read_csv('productor_huasteca.csv')
al=pd.read_csv('alimentos_copy.csv')
pg=pd.read_csv('plaga_copy.csv')

#base de datos del valle del mezquital 
df=pd.read_csv('productor_cop.csv')
rc=pd.read_csv('recoleccion_copy.csv')
m=pd.read_csv('Encuesta_productores.csv')
p_valle=pd.read_csv('productoyvalle.csv')
df_valle=pd.read_csv('productor_Mezquital.csv')
df_hectareas=pd.read_csv('hectareas.csv')
df_productores=pd.read_csv('Encuesta_productores2.csv')
df_productores2=pd.read_csv('Encuesta_productores3.csv')



app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div(children=[
        html.H1(children='Dashboard de los resultados en las regiones de Hidalgo'),
                html.Img(src='assets/Ciad.png'),

        html.Div(children= "La siguiente seccion es recopilacion de los datos de la base de datos de la huasteca Hidalguense"),
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Selecciona la Region', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'radioitms', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'LA HUASTECA', 'value' : 'region'},
                                {'label' : 'VALLE DEL MEZQUITAL', 'value' : 'region2'},
                            ], value = 'region',
                            style = {'text-aling': 'justify', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'bottom': 'center'}),
    ], className = 'row flex-display'),

#1 fecha de cosecha vs alimentos
    html.Div([
        html.Div([
         html.H2('Edad y cantidades de Hectareas'),
        dcc.Graph(id = 'barra_graph', figure = {})
        ], className = 'create_container2 eight columns'),

#2 estructura familiar
        html.Div([
        html.H2('Estructura Familiar'),
        dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 six columns')
    ], className = 'row flex-display'),

#3 produccion por H

html.Div([
        html.Div([
         html.H2('Produccion por Hectareas'),
        dcc.Graph(id = 'barra_graph2', figure = {})
        ], className = 'create_container2 eight columns'),

#4 Encuestados por municipio
        html.Div([
        html.H2('Numero de encuestados por municipios de cada Region'),
        dcc.Graph(id = 'pie_graph4', figure = {})
        ], className = 'create_container2 six columns')
    ], className = 'row flex-display'),


# 5 Consumos de alimentos  
 html.Div([
        html.Div([
        html.H2('Frecuencia en la que se consumen los alimentos.'),
        dcc.Graph(id = 'barra_graph3', figure = {})
        ], className = 'create_container2 eight columns'),

#6 plagas
        html.Div([
        html.H2('', className= 'fix_label'),
        dcc.Graph(id = 'pie_graph6', figure = {})
        ], className = 'create_container2 six columns')
    ], className = 'row flex-display'),

# 7 Estudio  
 html.Div([
        html.Div([
        html.H2('NIVEL DE ESTUDIO'),
        dcc.Graph(id = 'pie_graph7', figure = {})
        ], className = 'create_container2 eight columns'),

#8 plagas
        html.Div([
        dcc.Graph(id = 'box', figure = {})
        ], className = 'create_container2 six columns')
    ], className = 'row flex-display'),
    

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})


#1 fecha de cosecha vs alimentos
@app.callback(
    Output('barra_graph', component_property='figure'),
    [Input('radioitms', component_property='value')])

def update_graph(value):

    if value == 'region':
        fig = px.bar(
            data_frame = ca,
            x = 'nombre_modif',
            y = 'fecha_cosecha_modif')
    else:
        fig = px.bar(
            data_frame= ca,
            x = 'CLASE',
            y = 'fecha_siembra_modif')
    return fig

#2 estructura familiar
@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('radioitms', component_property='value')])

def update_graph_pie(value):

    if value == 'region':
        fig2 = px.pie(
            data_frame = ud,
            names = 'familiar_modif',
            values = 'id')
    else:
        fig2 = px.pie(
            data_frame = df_productores2,
            names = 'parentesco',
            values = '_index')
    return fig2
#3 produccion por H
@app.callback(
    Output('barra_graph2', component_property='figure'),
    [Input('radioitms', component_property='value')])

def display_color(value):

    if value == 'region':
        fig3 = px.bar(
            data_frame =pc,
            x = 'edad',
             y = 'prod_hect')
    else:
        fig3 = px.bar(
            data_frame= p_valle,
            x = 'edad',
            y = 'prod_hec')
    return fig3


#cuatro ya quedo 

#4 Encuestados por municipio     
@app.callback(
    Output('pie_graph4', component_property='figure'),
    [Input('radioitms', component_property='value')])
def update_graph_sunburst (value):
    if value == 'region':
        fig4 = px.sunburst(
            data_frame=s,
            path=['municipio', 'sexo', 'edad'], 
            values='idUsuario')

    else:
        fig4 = px.sunburst(
            data_frame=df_valle,
            path=['municipio', 'sexo', 'edad'], 
            values='idUsuario')
    return fig4



#5 Consumos de alimentos 
@app.callback(

Output('barra_graph3', component_property='figure'),
[Input('radioitms', component_property='value')])

def display_structure(value):

    if value == 'region':
        fig5 = px.bar(
            data_frame =al,
            x = 'articulos',
             y = 'frecuencia_modif')
    else:
        fig5 = px.bar(
            data_frame= df_productores,
            x = '¿Que edad tiene?',
             y = '¿Número de terrenos que utiliza la familia?')
    return fig5

#6 plagas
@app.callback(
    Output('pie_graph6', component_property='figure'),
    [Input('radioitms', component_property='value')])
def update_graph_sunburst (value):
    if value == 'region':
        fig6 = px.sunburst(
            title='Tipo de Plagas',
            data_frame = pg,
            path=['nombre_modif','combate_modif'], 
            values='CantidadPlaga', hover_name="nombre_modif")
        fig6.update_traces(hovertemplate='<b>Numero Total de plaga:%{value}<b><br><b>Como lo Combate:%{label}<b>')        

    else:
        fig6 = px.sunburst(
            title='Actividades realizadas en el espacio de vida, y productos generados ',
            data_frame = df_productores2,
            path=['Nombre del espacio de vida','¿Cuantos productos obtiene de la actividad?'],
            names='Nombre del espacio de vida',
            values='¿Cuantas actividades realiza en el espacio de vida?', hover_name="Nombre del espacio de vida",
            hover_data={'Nombre del espacio de vida':False})
        fig6.update_traces(hovertemplate='<b>Numero de personas que realizan la actividad:%{value}<b><br><b>Numero de actividades Realizadas:%{label}<b>')        
    return fig6

#7 Estudio
@app.callback(
    Output('pie_graph7', component_property='figure'),
    [Input('radioitms', component_property='value')])

def update_graph_sunburst (value):
    if value == 'region':
        fig7 = px.sunburst(
            data_frame=ud,
            path=['sexo','estudio_modif', 'edad'], 
            values='id')
        fig7.update_traces(hovertemplate='<b>Numero de personas que realizan la actividad:%{value}<b><br><b>Numero de actividades Realizadas:%{label}<b>')        


    else:
        fig7 = px.sunburst(
            data_frame=m,
            path=['Estudio','Edad'], 
            values='Edad', hover_name="Estudio")
    return fig7

#8 Barra
@app.callback(
    Output('box', component_property='figure'),
    [Input('radioitms', component_property='value')])

def update_graph_box (value):
    if value == 'region':
        fig8 = px.box(
            data_frame=ud,
            title='Edad vs migración',
            y='edad',
            x='migracion_modif',)
    else:
        fig8 = px.box(
            data_frame=df_productores,
            title='Actividades vs edad',
            y='¿Que edad tiene?',
            x='¿Cuantas actividades realiza en el espacio de vida?',)
    return fig8

if __name__ == ('__main__'):
    app.run_server(debug=True)