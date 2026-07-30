import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from database.db_manager import DatabaseManager
from utils.constants import OUTFITS_PATH

def render(db: DatabaseManager) -> None:
    st.markdown('<div class="page-title"><span>STYLE INTELLIGENCE</span><h1>Your taste, in focus.</h1><p>A living view of your recommendations and saved collection.</p></div>',unsafe_allow_html=True)
    data=db.analytics(); catalog=pd.read_csv(OUTFITS_PATH)
    m1,m2,m3,m4=st.columns(4)
    m1.metric("Average match",f'{data["average_score"]:.0f}%')
    m2.metric("Saved outfits",len(data["favorites"]))
    m3.metric("Recommendations",len(data["recommendations"]))
    m4.metric("Positive feedback",f'{data["accuracy"]:.0f}%')
    left,right=st.columns(2,gap="large")
    template=dict(layout=go.Layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",font_color="#d9d5e8"))
    with left:
        styles=catalog.groupby("style")["popularity"].mean().sort_values().reset_index()
        fig=px.bar(styles,x="popularity",y="style",orientation="h",title="Most recommended styles",color="popularity",color_continuous_scale=["#6c3cf0","#ef5da8"]); fig.update_layout(**template["layout"].to_plotly_json(),coloraxis_showscale=False); st.plotly_chart(fig,use_container_width=True)
    with right:
        colors=catalog.assign(color=catalog.colors.str.split(",")).explode("color").groupby("color").size().reset_index(name="looks")
        fig=px.pie(colors,values="looks",names="color",hole=.65,title="Favorite color signals",color_discrete_sequence=["#7c4dff","#ef5da8","#35d1c5","#ffb86b","#8d91a8"]); fig.update_layout(**template["layout"].to_plotly_json()); st.plotly_chart(fig,use_container_width=True)
    fig=px.histogram(catalog,x="price",nbins=8,title="Budget distribution",color_discrete_sequence=["#9f6bff"]); fig.update_layout(**template["layout"].to_plotly_json(),xaxis_title="Price ($)",yaxis_title="Outfits"); st.plotly_chart(fig,use_container_width=True)