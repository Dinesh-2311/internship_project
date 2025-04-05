# dashboard_app.py - DO NOT name this dash.py
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import webbrowser
from threading import Timer
import os
import sys

# 1. Data Loading Function
def load_data():
    """Load and validate the dataset"""
    try:
        # Try multiple possible file locations
        possible_paths = [
            os.path.join(os.path.dirname(__file__), 'Global_AI_Content_Impact_Dataset.csv'),
            r"C:\Users\dines\OneDrive\Desktop\Internship Project\Task3_Dashboard\Global_AI_Content_Impact_Dataset.csv",
            r"C:\Users\dines\OneDrive\Desktop\job preparation\eli tech\Global_AI_Content_Impact_Dataset.csv"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(f"Found data at: {path}")
                df = pd.read_csv(path)
                
                # Validate required columns
                required_columns = [
                    'Country', 'Year', 'Industry', 'AI Adoption Rate (%)',
                    'Job Loss Due to AI (%)', 'Revenue Increase Due to AI (%)',
                    'AI-Generated Content Volume (TBs per year)', 'Top AI Tools Used'
                ]
                missing = [col for col in required_columns if col not in df.columns]
                if missing:
                    raise ValueError(f"Missing columns: {missing}")
                
                return df
        
        raise FileNotFoundError("CSV file not found in any searched locations")
    
    except Exception as e:
        print(f"Data loading error: {str(e)}", file=sys.stderr)
        sys.exit(1)

# 2. Dashboard Creation Function
def create_dashboard_app():
    """Create and configure the Dash application"""
    # Load data
    df = load_data()
    
    # Initialize app
    app = dash.Dash(__name__)
    
    # Layout
    app.layout = html.Div([
        html.H1("Global AI Impact Dashboard", style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginBottom': '20px'
        }),
        
        # Filters
        html.Div([
            dcc.Dropdown(
                id='year-selector',
                options=[{'label': str(year), 'value': year} 
                        for year in sorted(df['Year'].unique())],
                value=[df['Year'].max()],
                multi=True,
                placeholder="Select Year(s)",
                style={'width': '48%', 'display': 'inline-block', 'marginRight': '2%'}
            ),
            
            dcc.Dropdown(
                id='industry-selector',
                options=[{'label': industry, 'value': industry} 
                        for industry in sorted(df['Industry'].unique())],
                multi=True,
                placeholder="Select Industry(s)",
                style={'width': '48%', 'display': 'inline-block'}
            )
        ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '10px'}),
        
        # Visualizations
        html.Div([
            dcc.Graph(id='heatmap', style={'width': '49%', 'display': 'inline-block'}),
            dcc.Graph(id='scatter-plot', style={'width': '49%', 'display': 'inline-block'})
        ]),
        
        dcc.Graph(id='tools-chart', style={'marginTop': '20px'})
    ])
    
    # 3. Callback for Interactive Updates
    @app.callback(
        [Output('heatmap', 'figure'),
         Output('scatter-plot', 'figure'),
         Output('tools-chart', 'figure')],
        [Input('year-selector', 'value'),
         Input('industry-selector', 'value')]
    )
    def update_figures(selected_years, selected_industries):
        # Filter data
        filtered_df = df[df['Year'].isin(selected_years)]
        if selected_industries:
            filtered_df = filtered_df[filtered_df['Industry'].isin(selected_industries)]
        
        # Create visualizations
        heatmap = px.density_heatmap(
            filtered_df,
            x='Year',
            y='Country',
            z='AI Adoption Rate (%)',
            title='AI Adoption Rate by Country/Year',
            color_continuous_scale='Viridis',
            height=500
        )
        
        scatter = px.scatter(
            filtered_df,
            x='Job Loss Due to AI (%)',
            y='Revenue Increase Due to AI (%)',
            size='AI-Generated Content Volume (TBs per year)',
            color='Industry',
            hover_name='Country',
            hover_data=['Top AI Tools Used'],
            title='Job Impact vs Revenue Gain',
            height=500
        )
        
        tools = px.bar(
            filtered_df['Top AI Tools Used'].value_counts().reset_index(),
            x='Top AI Tools Used',
            y='count',
            title='Most Frequently Used AI Tools',
            labels={'count': 'Usage Count', 'Top AI Tools Used': 'AI Tool'},
            height=400
        )
        
        return heatmap, scatter, tools
    
    return app

# 4. Browser Automation
def open_browser():
    """Automatically open browser when app starts"""
    webbrowser.open_new("http://127.0.0.1:8050/")

# 5. Main Execution
if __name__ == '__main__':
    # Create app
    app = create_dashboard_app()
    
    # Configure browser opening
    Timer(1, open_browser).start()  # Open after 1 second delay
    
    # Run server
    print("\n" + "="*40)
    print("AI Impact Dashboard Starting...")
    print(f"• Access at: http://127.0.0.1:8050")
    print("• Press CTRL+C to stop the server")
    print("="*40 + "\n")
    
    app.run(debug=True, use_reloader=False)