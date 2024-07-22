from dash import Dash, dcc, html, Input, Output, callback, dash_table
import data
import pandas as pd

app = Dash(__name__)

areas = [tup[0] for tup in data.get_areas()]
print(areas[0])

app.layout = html.Div([
    dcc.Dropdown(
       options=areas,
       value=areas[0],  # 設置初始值為第一個區域的值
       id='areas'
    ),
    html.Hr(),
    dash_table.DataTable(id='sites_table')
])

@callback(
    Output('sites_table', 'data'),
    Input('areas', 'value')
)
def selected_area(area_value):
    # 根據選定的區域獲取數據
    content = data.get_snaOfArea(area=area_value)
    df = pd.DataFrame(content)
    df.columns = ['站點名稱', '總數', '可借', '可還', '日期', '狀態']
    return df.to_dict('records') 

if __name__ == '__main__':
    app.run(debug=True)
