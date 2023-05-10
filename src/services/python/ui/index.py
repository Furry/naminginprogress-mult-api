import streamlit as st
import pandas as pd
import altair as alt
import requests
from streamlit_javascript import st_javascript

# JSON data
# data = {"last1h":10,"last24h":324,"last7d":2240,"last30d":4097,"postsByDay":{"2023-4-23":55,"2023-4-24":365,"2023-4-25":506,"2023-4-26":123,"2023-4-27":815,"2023-4-28":267,"2023-4-29":275,"2023-4-30":225,"2023-5-1":317,"2023-5-2":438,"2023-5-3":401,"2023-5-4":310,"2023-4-22":0,"2023-4-21":0,"2023-4-20":0,"2023-4-19":0,"2023-4-18":0,"2023-4-17":0,"2023-4-16":0,"2023-4-15":0,"2023-4-14":0,"2023-4-13":0,"2023-4-12":0,"2023-4-11":0,"2023-4-10":0,"2023-4-9":0,"2023-4-8":0,"2023-4-7":0,"2023-4-6":0,"2023-4-5":0},"endpoints":[{"url":"/","requests":942},{"url":"/s/","requests":644},{"url":"/.env","requests":224},{"url":"/Core/Skin/Login.aspx","requests":165},{"url":"/api/files/upload","requests":132},{"url":"/wp-comments-post.php","requests":102},{"url":"/favicon.ico","requests":79},{"url":"/wp-login.php","requests":38},{"url":"/robots.txt","requests":34},{"url":"/geoip/","requests":33}]}

# Needed for preload
data = st_javascript(
"""(async () => { 
    let location = window.location.hostname
    let url = location.includes("localhost") ? "http://localhost:8080/api/stats" : "http://" + location + ":8080/api/stats"
    return await fetch(url)
        .then(function(response) {return response.json();})
    })()"""
)

if data:
    st.write("## Time-based stats")
    time_based_stats = pd.DataFrame({
        "Time Range": ["Last 1 hour", "Last 24 hours", "Last 7 days", "Last 30 days"],
        "Posts": [data["last1h"], data["last24h"], data["last7d"], data["last30d"]]
    })
    st.write(alt.Chart(time_based_stats).mark_bar().encode(
        x="Time Range",
        y="Posts"
    ))

    # Display posts by day
    st.write("## Posts by day")
    posts_by_day = pd.DataFrame({
        "Date": list(data["postsByDay"].keys()),
        "Posts": list(data["postsByDay"].values())
    })
    st.write(alt.Chart(posts_by_day).mark_line().encode(
        x=alt.X("Date:T", axis=alt.Axis(title="Date")),
        y=alt.Y("Posts:Q", axis=alt.Axis(title="Posts"))
    ))

    # Display endpoint requests
    st.write("## Endpoint requests")
    endpoints = pd.DataFrame(data["endpoints"])
    pie_chart = alt.Chart(endpoints).mark_arc(innerRadius=50).encode(
        theta='requests:Q',
        color='url:N',
        tooltip=['url', 'requests']
    )

    labels = alt.Chart(endpoints).mark_text(align='left', baseline='middle', dx=7).encode(
        x=alt.X('dx:Q', axis=alt.Axis(title='dx')),
        y=alt.Y('dy:Q', axis=alt.Axis(title='dy')),
        theta='requests:Q',
        radius=alt.value(100),
        text='url:N'
    )

    st.altair_chart(pie_chart + labels, use_container_width=True)