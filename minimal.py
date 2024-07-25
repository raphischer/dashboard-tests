from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

app.layout = (
    html.Div([
        html.H1(children='Minimal Dash App', style={'textAlign':'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        html.Button('Click me!', id='test-button'),
        html.Div(id='button-out', children='Press Button to test!')
    ])
)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

@callback(
    Output('button-out', 'children'),
    Input('test-button', 'n_clicks'),
    prevent_initial_call=True
)
def on_click(n_clicks):
    return f'Button was pressed {n_clicks} times!'

if __name__ == '__main__':
    app.run(debug=True)