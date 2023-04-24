import streamlit as st
import pandas as pd
import altair as alt

# JSON data
data = {"last1h":14,"last24h":256,"last7d":256,"last30d":256,"postsByDay":{"2023-4-23":55,"2023-4-24":201,"2023-4-22":0,"2023-4-21":0,"2023-4-20":0,"2023-4-19":0,"2023-4-18":0,"2023-4-17":0,"2023-4-16":0,"2023-4-15":0,"2023-4-14":0,"2023-4-13":0,"2023-4-12":0,"2023-4-11":0,"2023-4-10":0,"2023-4-9":0,"2023-4-8":0,"2023-4-7":0,"2023-4-6":0,"2023-4-5":0,"2023-4-4":0,"2023-4-3":0,"2023-4-2":0,"2023-4-1":0,"2023-3-31":0,"2023-3-30":0,"2023-3-29":0,"2023-3-28":0,"2023-3-27":0,"2023-3-26":0},"endpoints":[{"url":"/","requests":49},{"url":"/s/","requests":36},{"url":"/api/files/upload","requests":14},{"url":"/api/stats","requests":12},{"url":"/Core/Skin/Login.aspx","requests":12},{"url":"/favicon.ico","requests":9},{"url":"/.env","requests":6},{"url":"/api/upload","requests":5},{"url":"/geoip/","requests":4},{"url":"/wp-login.php","requests":4},{"url":"/client/get_targets","requests":3},{"url":"/upl.php","requests":3},{"url":"/robots.txt","requests":3},{"url":"/tftpboot/","requests":3},{"url":"/api/ai/vulgarity","requests":2},{"url":"/geoserver/web/","requests":1},{"url":"/GponForm/diag_Form?images/","requests":1},{"url":"/boaform/admin/formLogin","requests":1},{"url":"/systembc/password.php","requests":1},{"url":"/index.php?option=com_acym&ctrl=frontmails&task=setNewIconShare","requests":1},{"url":"/_html/main.asp","requests":1},{"url":"/conf/.env","requests":1},{"url":"/wp-content/.env","requests":1},{"url":"/wp-admin/.env","requests":1},{"url":"/library/.env","requests":1},{"url":"/new/.env","requests":1},{"url":"/vendor/.env","requests":1},{"url":"/old/.env","requests":1},{"url":"/local/.env","requests":1},{"url":"/api/.env","requests":1},{"url":"/blog/.env","requests":1},{"url":"/crm/.env","requests":1},{"url":"/admin/.env","requests":1},{"url":"/laravel/.env","requests":1},{"url":"/app/.env","requests":1},{"url":"/app/config/.env","requests":1},{"url":"/apps/.env","requests":1},{"url":"/audio/.env","requests":1},{"url":"/cgi-bin/.env","requests":1},{"url":"/backend/.env","requests":1},{"url":"/src/.env","requests":1},{"url":"/base/.env","requests":1},{"url":"/core/.env","requests":1},{"url":"/vendor/laravel/.env","requests":1},{"url":"/storage/.env","requests":1},{"url":"/protected/.env","requests":1},{"url":"/newsite/.env","requests":1},{"url":"/www/.env","requests":1},{"url":"/sites/all/libraries/mailchimp/.env","requests":1},{"url":"/database/.env","requests":1},{"url":"/public/.env","requests":1},{"url":"/__tests__/test-become/.env","requests":1},{"url":"/redmine/.env","requests":1},{"url":"/gists/cache","requests":1},{"url":"/uploads/.env","requests":1},{"url":"/lib/.env","requests":1},{"url":"/sendgrid.env","requests":1},{"url":"/aws.env","requests":1},{"url":"/.env.example","requests":1},{"url":"/main/.env","requests":1},{"url":"/docs/.env","requests":1},{"url":"/client/.env","requests":1},{"url":"/.env.dev","requests":1},{"url":"/blogs/.env","requests":1},{"url":"/shared/.env","requests":1},{"url":"/download/.env","requests":1},{"url":"/.env.php","requests":1},{"url":"/site/.env","requests":1},{"url":"/sites/.env","requests":1},{"url":"/web/.env","requests":1},{"url":"//.env","requests":1},{"url":"/provisioning/","requests":1},{"url":"/config/","requests":1},{"url":"/aastra/","requests":1},{"url":"/configs/","requests":1},{"url":"/xml/","requests":1},{"url":"/admin/","requests":1},{"url":"/etc/selinux","requests":1},{"url":"/3cx/","requests":1},{"url":"/tftpboot/polycom","requests":1},{"url":"/grandstream/","requests":1},{"url":"/etc/asterisk","requests":1},{"url":"/cisco/","requests":1},{"url":"/usr/lib/asterisk/modules/","requests":1},{"url":"/yealink/","requests":1},{"url":"/pbx/","requests":1},{"url":"/etc/","requests":1},{"url":"/prov/","requests":1},{"url":"/conf/","requests":1},{"url":"/provisioning/spa","requests":1},{"url":"/spa/","requests":1},{"url":"/updates/","requests":1},{"url":"/linksys/","requests":1},{"url":"/snom/","requests":1},{"url":"/asterisk/","requests":1},{"url":"/tools/","requests":1},{"url":"/polycom/","requests":1},{"url":"/digium/","requests":1},{"url":"/sip/","requests":1},{"url":"/ftp/","requests":1},{"url":"/phone/","requests":1},{"url":"/cfg/","requests":1},{"url":"/voice/","requests":1},{"url":"/release/","requests":1},{"url":"/users/","requests":1},{"url":"/wp-22.php?sfilename=on.php&sfilecontent=<%3F%3D409723%2A20%3B&supfiles=on.php","requests":1}]}

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
