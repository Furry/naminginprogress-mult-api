import streamlit as st
import pandas as pd
import altair as alt

# JSON data
data = {
    "last1h": 16,
    "last24h": 542,
    "last7d": 887,
    "last30d": 887,
    "postsByDay": {
        "2023-4-23": 77,
        "2023-4-24": 388,
        "2023-4-25": 422,
        "2023-4-22": 0,
        "2023-4-21": 0,
        "2023-4-20": 0,
        "2023-4-19": 0,
        "2023-4-18": 0,
        "2023-4-17": 0,
        "2023-4-16": 0,
        "2023-4-15": 0,
        "2023-4-14": 0,
        "2023-4-13": 0,
        "2023-4-12": 0,
        "2023-4-11": 0,
        "2023-4-10": 0,
        "2023-4-9": 0,
        "2023-4-8": 0,
        "2023-4-7": 0,
        "2023-4-6": 0,
        "2023-4-5": 0,
        "2023-4-4": 0,
        "2023-4-3": 0,
        "2023-4-2": 0,
        "2023-4-1": 0,
        "2023-3-31": 0,
        "2023-3-30": 0,
        "2023-3-29": 0,
        "2023-3-28": 0,
        "2023-3-27": 0
    },
    "endpoints": [
        {
            "url": "/",
            "requests": 149
        },
        {
            "url": "/s/",
            "requests": 126
        },
        {
            "url": "/wp-comments-post.php",
            "requests": 102
        },
        {
            "url": "/api/files/upload",
            "requests": 36
        },
        {
            "url": "/Core/Skin/Login.aspx",
            "requests": 32
        },
        {
            "url": "/.env",
            "requests": 29
        },
        {
            "url": "/favicon.ico",
            "requests": 19
        },
        {
            "url": "/api/stats",
            "requests": 16
        },
        {
            "url": "/wp-login.php",
            "requests": 9
        },
        {
            "url": "/geoip/",
            "requests": 8
        }
    ]
}


def display_data(data):
    # Display time-based stats
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



# Create the Streamlit app
st.title("Website Stats Dashboard")
display_data(data)
