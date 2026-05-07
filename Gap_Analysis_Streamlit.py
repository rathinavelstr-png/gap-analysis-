import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="ThemeForest Gap Analysis Dashboard",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("📊 ThemeForest Gap Analysis Dashboard")
st.markdown("Analysis of Website Readiness vs ThemeForest Standards")

# =========================
# SCORECARD DATA
# =========================
score_data = {
    "Category": [
        "Product Quality",
        "Functionality & UX",
        "Support & Updates",
        "Marketplace Experience",
        "Technical Performance"
    ],
    "Technology (Tecko)": [6, 5, 4, 5, 5],
    "Affiliated Marketing": [7, 6, 4, 6, 6],
    "Architecture": [7, 7, 5, 6, 6]
}

df_scores = pd.DataFrame(score_data)

# =========================
# KPI METRICS
# =========================
st.subheader("📌 Overall Readiness Scores")

col1, col2, col3 = st.columns(3)

col1.metric("Technology (Tecko)", "5.0 / 10")
col2.metric("Affiliated Marketing", "5.8 / 10")
col3.metric("Architecture", "6.2 / 10")

# =========================
# BAR CHART
# =========================
st.subheader("📈 Category Wise Performance")

melted = df_scores.melt(
    id_vars="Category",
    var_name="Website",
    value_name="Score"
)

fig = px.bar(
    melted,
    x="Category",
    y="Score",
    color="Website",
    barmode="group",
    text="Score",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# RADAR CHART
# =========================
st.subheader("🕸 Comparative Radar Analysis")

categories = df_scores["Category"].tolist()

fig_radar = go.Figure()

for site in df_scores.columns[1:]:
    fig_radar.add_trace(go.Scatterpolar(
        r=df_scores[site].tolist(),
        theta=categories,
        fill='toself',
        name=site
    ))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )),
    showlegend=True,
    height=600
)

st.plotly_chart(fig_radar, use_container_width=True)

# =========================
# CRITICAL ISSUES
# =========================
st.subheader("🚨 Critical Issues")

critical_issues = pd.DataFrame({
    "Priority": ["CRITICAL", "CRITICAL", "CRITICAL", "HIGH", "HIGH"],
    "Issue": [
        "Broken 404 links",
        "No documentation page",
        "No branded 404 page",
        "No dark mode",
        "Missing legal pages"
    ],
    "Applies To": [
        "All Sites",
        "All Sites",
        "All Sites",
        "All Sites",
        "All Sites"
    ]
})

st.dataframe(critical_issues, use_container_width=True)

# =========================
# GAP ANALYSIS
# =========================
st.subheader("🔍 Gap Analysis")

tabs = st.tabs([
    "Technology",
    "Affiliated Marketing",
    "Architecture"
])

with tabs[0]:
    st.markdown("""
    ### Technology (Tecko)
    
    #### Current Gaps
    - Brand inconsistency
    - Broken CTA links
    - Contact form failure
    - No search functionality
    - Mobile optimization issues
    
    #### Recommendations
    - Fix all 404 links
    - Unify branding
    - Add form validation
    - Improve UX flow
    """)

with tabs[1]:
    st.markdown("""
    ### Affiliated Marketing
    
    #### Current Gaps
    - Footer links broken
    - Resource pages incomplete
    - CTA buttons non-functional
    - Missing buyer journey
    
    #### Recommendations
    - Build missing pages
    - Add signup workflow
    - Improve content completeness
    """)

with tabs[2]:
    st.markdown("""
    ### Architecture
    
    #### Current Gaps
    - Missing legal pages
    - Counter animations rely on JS
    - No portfolio filters
    
    #### Recommendations
    - Add category filters
    - Pre-render values
    - Improve accessibility
    """)

# =========================
# COMPETITOR ANALYSIS
# =========================
st.subheader("🏆 USA Market Competitors")

competitors = pd.DataFrame({
    "Niche": [
        "Technology",
        "Technology",
        "Finance",
        "Architecture",
        "Architecture"
    ],
    "Competitor": [
        "Saasland",
        "Startapp",
        "FinBank",
        "Archi",
        "Renovation"
    ],
    "Estimated Sales": [
        "20,000+",
        "8,500+",
        "6,000+",
        "15,000+",
        "9,000+"
    ]
})

st.table(competitors)

# =========================
# ACTION PLAN
# =========================
st.subheader("✅ Prioritized Action Plan")

action_plan = pd.DataFrame({
    "Priority": [
        "CRITICAL",
        "CRITICAL",
        "HIGH",
        "HIGH",
        "MEDIUM"
    ],
    "Action": [
        "Fix broken links",
        "Create documentation",
        "Add dark mode",
        "Build legal pages",
        "Improve accessibility"
    ],
    "Status": [
        "Pending",
        "Pending",
        "Pending",
        "Pending",
        "Pending"
    ]
})

st.data_editor(action_plan, use_container_width=True)

# =========================
# TECHNICAL PERFORMANCE
# =========================
st.subheader("⚡ Technical Performance")

tech_data = pd.DataFrame({
    "Metric": [
        "Image Optimization",
        "Responsive Design",
        "Core Web Vitals",
        "Hosting Speed"
    ],
    "Technology": [6, 5, 4, 4],
    "Affiliated Marketing": [7, 6, 5, 4],
    "Architecture": [8, 6, 5, 4]
})

fig2 = px.line(
    tech_data,
    x="Metric",
    y=["Technology", "Affiliated Marketing", "Architecture"],
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# FINAL RECOMMENDATION
# =========================
st.subheader("📌 Final Recommendation")

st.success("""
Before ThemeForest submission:

✔ Fix all broken links  
✔ Add documentation pages  
✔ Implement dark mode  
✔ Build legal/privacy pages  
✔ Optimize performance  
✔ Improve mobile responsiveness  
✔ Add accessibility support  

Target minimum readiness score: 8/10
""")