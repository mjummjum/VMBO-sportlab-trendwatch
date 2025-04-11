import streamlit as st
import pandas as pd
import streamlit_pandas as sp
from streamlit_elements import elements, mui, html

def shorten_text(s, n):
    return " ".join( s.split()[:n] )

@st.cache_data
def load_data():
    df = pd.read_csv(file, sep = '|')
    return df


file = 'data/grey_literature_vmbo_sportlab_full_data copy.csv', 
#sep = '|'
#f = load_data()

df = pd.read_csv('data/trendwatch_modded.csv', sep = '|')
create_data = {"organisation": "multiselect",
                "query": "multiselect",
                "media_class": "multiselect",
                "date": "multiselect",
                "short_link": "multiselect",
                "scope_lbl": "multiselect",
                "focus_lbl": "multiselect",
                "type_lbl": "multiselect",
                "exclude": "multiselect"}


all_widgets = sp.create_widgets(df, create_data, ignore_columns=["description","webtext","webtext_wordcount","title","link",'timestamp','scope','focus','type'])
                                                                
res = sp.filter_df(df, all_widgets)

st.title("VMBO sportlab trendwatch database")
#st.header("Original DataFrame (N=" + str(df.shape[0]) +")")
#st.write(df)
unique_df = res.drop_duplicates(subset=['link'], keep='last').sort_values(by='visibility_score', ascending = False)
st.subheader("Result DataFrame (N=" +str(res.shape[0]) + "/" + str(df.shape[0]) + ") waarvan " + str(unique_df.shape[0]) + " unieke links")
st.write(unique_df)
    #print(res.groupby('organisation_type').mean())
dict_bold = {'sport':'***sport***',
    'gezond':'***gezond***',
    'beweeg':'***beweeg***',
    'bewegen':'***bewegen***',
    'beweging':'***beweging***',
    'jeugd':'***jeugd***',
    'jongeren':'***jongeren***',
    'preventie':'***preventie***',
    'interventie':'***interventie***',
    'vmbo':'***vmbo***'}

st.subheader("De teksten van de top 3 links", divider="gray")
    
try:
    st.write(unique_df['organisation'].values[0])
    st.write(unique_df['link'].values[0])
    website_tekst = shorten_text(unique_df['webtext'].values[0],300)
    for key in dict_bold.keys():
        website_tekst = website_tekst.replace(key, dict_bold[key])
    st.info(website_tekst.replace(". ",".  \n"))
except:
    st.warning("geen tekst beschikbaar voor deze link")
    
try:
    st.write(unique_df['organisation'].values[1])
    st.write(unique_df['link'].values[1])
    website_tekst = shorten_text(unique_df['webtext'].values[1],300)
    for key in dict_bold.keys():
        website_tekst = website_tekst.replace(key, dict_bold[key])
    st.success(website_tekst.replace(". ",".  \n"))
except:
    st.warning("geen tekst beschikbaar voor deze link")
    
try:
    st.write(unique_df['organisation'].values[2])
    st.write(unique_df['link'].values[2])
    website_tekst = shorten_text(unique_df['webtext'].values[2],300)
    for key in dict_bold.keys():
        website_tekst = website_tekst.replace(key, dict_bold[key])
    st.info(website_tekst.replace(". ",".  \n"))
except:
    st.warning("geen tekst beschikbaar voor deze link")
#print(tekstje, res['webtext_wordcount'].values[0])

st.header("Figuren", divider="gray")
with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 4, 3),
        dashboard.Item("second_item", 0, 2, 4, 2, isDraggable=True, moved=False),
        dashboard.Item("third_item", 0, 2, 4, 2, isResizable=True),
        dashboard.Item("fourth_item", 0, 4, 4, 4, isResizable=True)
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        #mui.Card(
        #    mui.CardContent(st.write(res), sx={"maxHeight": "100%", "maxWidth": "100%", "width": "unset", }
        #    ), key="first_item"
        #)
        
        with elements("nivo_charts"):
            from streamlit_elements import nivo
            # Streamlit Elements includes 45 dataviz components powered by Nivo.

            #DATA = res.webtext_wordcount.to_dict('records')
            DATA = res[['organisation','scope','focus','type','count','pagerank','visibility_score']].groupby('organisation').mean().sort_values(by='visibility_score', ascending = False).dropna().head(5).T[:3].reset_index()
            #print(DATA)
            DATA55 = [
                { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
                { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
                { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
                { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
                { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
            ]

            DATA2 = [
                {
                    "country": "AD",
                    "hot dog": 162,
                    "hot dogColor": "hsl(289, 70%, 50%)",
                    "burger": 139,
                    "burgerColor": "hsl(178, 70%, 50%)",
                    "sandwich": 157,
                    "sandwichColor": "hsl(255, 70%, 50%)",
                    "kebab": 140,
                    "kebabColor": "hsl(26, 70%, 50%)",
                    "fries": 67,
                    "friesColor": "hsl(92, 70%, 50%)",
                    "donut": 122,
                    "donutColor": "hsl(298, 70%, 50%)"
                },
                {
                    "country": "AE",
                    "hot dog": 180,
                    "hot dogColor": "hsl(46, 70%, 50%)",
                    "burger": 190,
                    "burgerColor": "hsl(309, 70%, 50%)",
                    "sandwich": 149,
                    "sandwichColor": "hsl(124, 70%, 50%)",
                    "kebab": 13,
                    "kebabColor": "hsl(1, 70%, 50%)",
                    "fries": 20,
                    "friesColor": "hsl(270, 70%, 50%)",
                    "donut": 114,
                    "donutColor": "hsl(115, 70%, 50%)"
                },
                {
                    "country": "AF",
                    "hot dog": 194,
                    "hot dogColor": "hsl(184, 70%, 50%)",
                    "burger": 175,
                    "burgerColor": "hsl(300, 70%, 50%)",
                    "sandwich": 57,
                    "sandwichColor": "hsl(72, 70%, 50%)",
                    "kebab": 39,
                    "kebabColor": "hsl(19, 70%, 50%)",
                    "fries": 76,
                    "friesColor": "hsl(85, 70%, 50%)",
                    "donut": 18,
                    "donutColor": "hsl(192, 70%, 50%)"
                },
                {
                    "country": "AG",
                    "hot dog": 154,
                    "hot dogColor": "hsl(142, 70%, 50%)",
                    "burger": 35,
                    "burgerColor": "hsl(186, 70%, 50%)",
                    "sandwich": 48,
                    "sandwichColor": "hsl(151, 70%, 50%)",
                    "kebab": 29,
                    "kebabColor": "hsl(192, 70%, 50%)",
                    "fries": 50,
                    "friesColor": "hsl(144, 70%, 50%)",
                    "donut": 24,
                    "donutColor": "hsl(323, 70%, 50%)"
                },
                {
                    "country": "AI",
                    "hot dog": 141,
                    "hot dogColor": "hsl(295, 70%, 50%)",
                    "burger": 122,
                    "burgerColor": "hsl(293, 70%, 50%)",
                    "sandwich": 121,
                    "sandwichColor": "hsl(308, 70%, 50%)",
                    "kebab": 80,
                    "kebabColor": "hsl(296, 70%, 50%)",
                    "fries": 33,
                    "friesColor": "hsl(162, 70%, 50%)",
                    "donut": 44,
                    "donutColor": "hsl(9, 70%, 50%)"
                },
                {
                    "country": "AL",
                    "hot dog": 104,
                    "hot dogColor": "hsl(219, 70%, 50%)",
                    "burger": 10,
                    "burgerColor": "hsl(36, 70%, 50%)",
                    "sandwich": 81,
                    "sandwichColor": "hsl(125, 70%, 50%)",
                    "kebab": 21,
                    "kebabColor": "hsl(47, 70%, 50%)",
                    "fries": 28,
                    "friesColor": "hsl(342, 70%, 50%)",
                    "donut": 172,
                    "donutColor": "hsl(314, 70%, 50%)"
                },
                {
                    "country": "AM",
                    "hot dog": 127,
                    "hot dogColor": "hsl(143, 70%, 50%)",
                    "burger": 155,
                    "burgerColor": "hsl(312, 70%, 50%)",
                    "sandwich": 17,
                    "sandwichColor": "hsl(29, 70%, 50%)",
                    "kebab": 77,
                    "kebabColor": "hsl(1, 70%, 50%)",
                    "fries": 4,
                    "friesColor": "hsl(264, 70%, 50%)",
                    "donut": 43,
                    "donutColor": "hsl(229, 70%, 50%)"
                }
            ]
            
            DATA3 = [
                {
                    "id": "Serie 1",
                    "data": [
                    {
                        "x": "2000",
                        "y": 5
                    },
                    {
                        "x": "2001",
                        "y": 12
                    },
                    {
                        "x": "2002",
                        "y": 10
                    },
                    {
                        "x": "2003",
                        "y": 5
                    },
                    {
                        "x": "2004",
                        "y": 11
                    }
                    ]
                },
                {
                    "id": "Serie 2",
                    "data": [
                    {
                        "x": "2000",
                        "y": 7
                    },
                    {
                        "x": "2001",
                        "y": 6
                    },
                    {
                        "x": "2002",
                        "y": 5
                    },
                    {
                        "x": "2003",
                        "y": 8
                    },
                    {
                        "x": "2004",
                        "y": 3
                    }
                    ]
                },
                {
                    "id": "Serie 3",
                    "data": [
                    {
                        "x": "2000",
                        "y": 11
                    },
                    {
                        "x": "2001",
                        "y": 2
                    },
                    {
                        "x": "2002",
                        "y": 4
                    },
                    {
                        "x": "2003",
                        "y": 6
                    },
                    {
                        "x": "2004",
                        "y": 6
                    }
                    ]
                },
                {
                    "id": "Serie 4",
                    "data": [
                    {
                        "x": "2000",
                        "y": 6
                    },
                    {
                        "x": "2001",
                        "y": 8
                    },
                    {
                        "x": "2002",
                        "y": 6
                    },
                    {
                        "x": "2003",
                        "y": 1
                    },
                    {
                        "x": "2004",
                        "y": 12
                    }
                    ]
                },
                {
                    "id": "Serie 5",
                    "data": [
                    {
                        "x": "2000",
                        "y": 9
                    },
                    {
                        "x": "2001",
                        "y": 10
                    },
                    {
                        "x": "2002",
                        "y": 1
                    },
                    {
                        "x": "2003",
                        "y": 12
                    },
                    {
                        "x": "2004",
                        "y": 4
                    }
                    ]
                },
                {
                    "id": "Serie 6",
                    "data": [
                    {
                        "x": "2000",
                        "y": 8
                    },
                    {
                        "x": "2001",
                        "y": 3
                    },
                    {
                        "x": "2002",
                        "y": 3
                    },
                    {
                        "x": "2003",
                        "y": 10
                    },
                    {
                        "x": "2004",
                        "y": 8
                    }
                    ]
                },
                {
                    "id": "Serie 7",
                    "data": [
                    {
                        "x": "2000",
                        "y": 4
                    },
                    {
                        "x": "2001",
                        "y": 9
                    },
                    {
                        "x": "2002",
                        "y": 9
                    },
                    {
                        "x": "2003",
                        "y": 7
                    },
                    {
                        "x": "2004",
                        "y": 10
                    }
                    ]
                },
                {
                    "id": "Serie 8",
                    "data": [
                    {
                        "x": "2000",
                        "y": 12
                    },
                    {
                        "x": "2001",
                        "y": 5
                    },
                    {
                        "x": "2002",
                        "y": 7
                    },
                    {
                        "x": "2003",
                        "y": 11
                    },
                    {
                        "x": "2004",
                        "y": 5
                    }
                    ]
                },
                {
                    "id": "Serie 9",
                    "data": [
                    {
                        "x": "2000",
                        "y": 3
                    },
                    {
                        "x": "2001",
                        "y": 1
                    },
                    {
                        "x": "2002",
                        "y": 12
                    },
                    {
                        "x": "2003",
                        "y": 2
                    },
                    {
                        "x": "2004",
                        "y": 9
                    }
                    ]
                },
                {
                    "id": "Serie 10",
                    "data": [
                    {
                        "x": "2000",
                        "y": 2
                    },
                    {
                        "x": "2001",
                        "y": 4
                    },
                    {
                        "x": "2002",
                        "y": 11
                    },
                    {
                        "x": "2003",
                        "y": 3
                    },
                    {
                        "x": "2004",
                        "y": 7
                    }
                    ]
                },
                {
                    "id": "Serie 11",
                    "data": [
                    {
                        "x": "2000",
                        "y": 1
                    },
                    {
                        "x": "2001",
                        "y": 11
                    },
                    {
                        "x": "2002",
                        "y": 8
                    },
                    {
                        "x": "2003",
                        "y": 9
                    },
                    {
                        "x": "2004",
                        "y": 2
                    }
                    ]
                },
                {
                    "id": "Serie 12",
                    "data": [
                    {
                        "x": "2000",
                        "y": 10
                    },
                    {
                        "x": "2001",
                        "y": 7
                    },
                    {
                        "x": "2002",
                        "y": 2
                    },
                    {
                        "x": "2003",
                        "y": 4
                    },
                    {
                        "x": "2004",
                        "y": 1
                    }
                    ]
                }
            ]

            DATA4 = [
                {
                    "temp": 37.346871668760635,
                    "cost": 31550,
                    "weight": 56,
                    "volume": 5.290061157709532,
                    "id": "A"
                },
                {
                    "temp": 39.203129938207056,
                    "cost": 20689,
                    "weight": 255,
                    "volume": 5.765066753556938,
                    "id": "B"
                },
                {
                    "temp": 8.11208883862766,
                    "cost": 31072,
                    "weight": 65,
                    "volume": 0.3009248368574762,
                    "id": "C"
                },
                {
                    "temp": 17.360229192635266,
                    "cost": 10306,
                    "weight": 299,
                    "volume": 3.7965255088629135,
                    "id": "D"
                },
                {
                    "temp": 29.518816978523652,
                    "cost": 23360,
                    "weight": 47,
                    "volume": 7.188959500493091,
                    "id": "E"
                },
                {
                    "temp": 27.243905247409558,
                    "cost": 35130,
                    "weight": 278,
                    "volume": 7.446804252241811,
                    "id": "F"
                },
                {
                    "temp": 6.487951640522645,
                    "cost": 28197,
                    "weight": 252,
                    "volume": 5.125224143938657,
                    "id": "G"
                },
                {
                    "temp": 22.288645856050778,
                    "cost": 7350,
                    "weight": 190,
                    "volume": 0.305474722658341,
                    "id": "H"
                },
                {
                    "temp": -2.9168777249833155,
                    "cost": 1589,
                    "weight": 242,
                    "volume": 4.729513879286149,
                    "id": "I"
                },
                {
                    "temp": 20.309294430801582,
                    "cost": 20605,
                    "weight": 42,
                    "volume": 5.758527179284894,
                    "id": "J"
                }
            ]

            DATA5 = [
                {
                    "id": "japan",
                    "color": "hsl(40, 70%, 50%)",
                    "data": [
                    {
                        "x": "plane",
                        "y": 219
                    },
                    {
                        "x": "helicopter",
                        "y": 82
                    },
                    {
                        "x": "boat",
                        "y": 14
                    },
                    {
                        "x": "train",
                        "y": 176
                    },
                    {
                        "x": "subway",
                        "y": 216
                    },
                    {
                        "x": "bus",
                        "y": 16
                    },
                    {
                        "x": "car",
                        "y": 111
                    },
                    {
                        "x": "moto",
                        "y": 160
                    },
                    {
                        "x": "bicycle",
                        "y": 193
                    },
                    {
                        "x": "horse",
                        "y": 37
                    },
                    {
                        "x": "skateboard",
                        "y": 237
                    },
                    {
                        "x": "others",
                        "y": 80
                    }
                    ]
                },
                {
                    "id": "france",
                    "color": "hsl(178, 70%, 50%)",
                    "data": [
                    {
                        "x": "plane",
                        "y": 273
                    },
                    {
                        "x": "helicopter",
                        "y": 25
                    },
                    {
                        "x": "boat",
                        "y": 10
                    },
                    {
                        "x": "train",
                        "y": 219
                    },
                    {
                        "x": "subway",
                        "y": 75
                    },
                    {
                        "x": "bus",
                        "y": 68
                    },
                    {
                        "x": "car",
                        "y": 69
                    },
                    {
                        "x": "moto",
                        "y": 121
                    },
                    {
                        "x": "bicycle",
                        "y": 259
                    },
                    {
                        "x": "horse",
                        "y": 206
                    },
                    {
                        "x": "skateboard",
                        "y": 115
                    },
                    {
                        "x": "others",
                        "y": 41
                    }
                    ]
                },
                {
                    "id": "us",
                    "color": "hsl(279, 70%, 50%)",
                    "data": [
                    {
                        "x": "plane",
                        "y": 23
                    },
                    {
                        "x": "helicopter",
                        "y": 135
                    },
                    {
                        "x": "boat",
                        "y": 105
                    },
                    {
                        "x": "train",
                        "y": 85
                    },
                    {
                        "x": "subway",
                        "y": 233
                    },
                    {
                        "x": "bus",
                        "y": 51
                    },
                    {
                        "x": "car",
                        "y": 129
                    },
                    {
                        "x": "moto",
                        "y": 268
                    },
                    {
                        "x": "bicycle",
                        "y": 102
                    },
                    {
                        "x": "horse",
                        "y": 113
                    },
                    {
                        "x": "skateboard",
                        "y": 10
                    },
                    {
                        "x": "others",
                        "y": 91
                    }
                    ]
                },
                {
                    "id": "germany",
                    "color": "hsl(343, 70%, 50%)",
                    "data": [
                    {
                        "x": "plane",
                        "y": 120
                    },
                    {
                        "x": "helicopter",
                        "y": 114
                    },
                    {
                        "x": "boat",
                        "y": 296
                    },
                    {
                        "x": "train",
                        "y": 106
                    },
                    {
                        "x": "subway",
                        "y": 95
                    },
                    {
                        "x": "bus",
                        "y": 120
                    },
                    {
                        "x": "car",
                        "y": 4
                    },
                    {
                        "x": "moto",
                        "y": 133
                    },
                    {
                        "x": "bicycle",
                        "y": 270
                    },
                    {
                        "x": "horse",
                        "y": 206
                    },
                    {
                        "x": "skateboard",
                        "y": 81
                    },
                    {
                        "x": "others",
                        "y": 154
                    }
                    ]
                },
                {
                    "id": "norway",
                    "color": "hsl(287, 70%, 50%)",
                    "data": [
                    {
                        "x": "plane",
                        "y": 202
                    },
                    {
                        "x": "helicopter",
                        "y": 135
                    },
                    {
                        "x": "boat",
                        "y": 210
                    },
                    {
                        "x": "train",
                        "y": 157
                    },
                    {
                        "x": "subway",
                        "y": 214
                    },
                    {
                        "x": "bus",
                        "y": 57
                    },
                    {
                        "x": "car",
                        "y": 247
                    },
                    {
                        "x": "moto",
                        "y": 23
                    },
                    {
                        "x": "bicycle",
                        "y": 234
                    },
                    {
                        "x": "horse",
                        "y": 55
                    },
                    {
                        "x": "skateboard",
                        "y": 43
                    },
                    {
                        "x": "others",
                        "y": 264
                    }
                    ]
                }
            ]

            with mui.Box(key = "first_item"):
                nivo.Radar(
                    data=DATA.to_dict('records'),
                    #data=DATA55,
                    keys=DATA.columns[1:],
                    #keys= ["chardonay", "carmenere", "syrah"],
                    indexBy="index",
                    valueFormat=">-.2f",
                    margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                    borderColor={ "from": "color" },
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={ "theme": "background" },
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ],
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#31333F",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#31333F",
                            }
                        }
                    }
                )

            with mui.Box(key = "second_item"):
                    nivo.Bar(
                        data=DATA2,
                        keys=[ "hot dog", "burger", "sandwich", 'kebab', 'fries', 'donut' ],
                        indexBy="country",
                        valueFormat=">-.2f",
                        margin={ "top": 50, "right": 130, "bottom": 50, "left": 60 },
                        borderColor={ "from": "color" },
                        valuescale={'type': 'linear'},
                        indexscale={ 'type': 'band', 'round': 'true'},
                        colors={ 'scheme': 'nivo'},
                        #gridLabelOffset=36,
                        #dotSize=12,
                        #dotColor={ "theme": "background" },
                        #dotBorderWidth=2,
                        #motionConfig="wobbly",
                        legends=[
                            {
                                "anchor": "top-left",
                                "direction": "column",
                                "translateX": -50,
                                "translateY": -40,
                                "itemWidth": 80,
                                "itemHeight": 20,
                                "itemTextColor": "#999",
                                "symbolSize": 12,
                                "symbolShape": "circle",
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemTextColor": "#000"
                                        }
                                    }
                                ]
                            }
                        ],
                        theme={
                            "background": "#FFFFFF",
                            "textColor": "#31333F",
                            "tooltip": {
                                "container": {
                                    "background": "#FFFFFF",
                                    "color": "#31333F",
                                }
                            }
                        }
                    )

            with mui.Box(key = "third_item"):
                    nivo.Bump(
                        data=DATA3,
                        colors={'scheme': 'spectral'},
                        lineWidth=3,
                        activeLineWidth=6,
                        inactiveLineWidth=3,
                        inactiveOpacity=0.15,
                        pointSize=10,
                        activePointSize=16,
                        inactivePointSize=0,
                        pointColor={'theme': 'background'},
                        pointBorderWidth=3,
                        activePointBorderWidth=3,
                        pointBorderColor={'from': 'serie.color'},
                        axisTop={
                            'tickSize': 5,
                            'tickPadding': 5,
                            'tickRotation': 0,
                            'legend': '',
                            'legendPosition': 'middle',
                            'legendOffset': -36,
                            'truncateTickAt': 0
                        },
                        axisBottom={
                            'tickSize': 5,
                            'tickPadding': 5,
                            'tickRotation': 0,
                            'legend': '',
                            'legendPosition': 'middle',
                            'legendOffset': 32,
                            'truncateTickAt': 0
                        },
                        axisLeft={
                            'tickSize': 5,
                            'tickPadding': 5,
                            'tickRotation': 0,
                            'legend': 'ranking',
                            'legendPosition': 'middle',
                            'legendOffset': -40,
                            'truncateTickAt': 0
                        },
                        margin={'top': 40, 'right': 100, 'bottom': 40, 'left': 60},
                        axisRight=None
                    )
            
            with mui.Box(key = "fourth_item"):
                nivo.Line(
                    data = DATA5,
                    margin = {'top': 50, 'right': 110, 'bottom': 50, 'left': 60},
                    x_scale = {'type': 'point'},
                    y_scale = {
                        'type': 'linear',
                        'min': 'auto',
                        'max': 'auto',
                        'stacked': True,
                        'reverse': False
                    },
                    y_format = " >-.2f",
                    axis_top = None,
                    axis_right = None,
                    axis_bottom = {
                        'tickSize': 5,
                        'tickPadding': 5,
                        'tickRotation': 0,
                        'legend': 'transportation',
                        'legendOffset': 36,
                        'legendPosition': 'middle',
                        'truncateTickAt': 0
                    },
                    axis_left = {
                        'tickSize': 5,
                        'tickPadding': 5,
                        'tickRotation': 0,
                        'legend': 'count',
                        'legendOffset': -40,
                        'legendPosition': 'middle',
                        'truncateTickAt': 0
                    },
                    point_size = 10,
                    point_color = {'theme': 'background'},
                    point_border_width = 2,
                    point_border_color = {'from': 'serieColor'},
                    point_label = "data.yFormatted",
                    point_label_y_offset = -12,
                    enable_touch_crosshair = True,
                    use_mesh = True,
                    legends = [
                        {
                            'anchor': 'bottom-right',
                            'direction': 'column',
                            'justify': False,
                            'translateX': 100,
                            'translateY': 0,
                            'itemsSpacing': 0,
                            'itemDirection': 'left-to-right',
                            'itemWidth': 80,
                            'itemHeight': 20,
                            'itemOpacity': 0.75,
                            'symbolSize': 12,
                            'symbolShape': 'circle',
                            'symbolBorderColor': 'rgba(0, 0, 0, .5)',
                            'effects': [
                                {
                                    'on': 'hover',
                                    'style': {
                                        'itemBackground': 'rgba(0, 0, 0, .03)',
                                        'itemOpacity': 1
                                    }
                                }
                            ]
                        }
                    ]      
                )
            
            # with mui.Box(key = "fourth_item"):
            #         nivo.ParallelCoordinatesCanvas(
            #             data=DATA4,
            #             variables=[
            #                 {
            #                     'id': 'temp',
            #                     'label': 'temperature',
            #                     'value': 'temp',
            #                     'min': 'auto',
            #                     'max': 'auto',
            #                     'ticksPosition': 'before',
            #                     'legendPosition': 'start',
            #                     'legendOffset': 20
            #                 },
            #                 {
            #                     'id': 'cost',
            #                     'value': 'cost',
            #                     'min': 0,
            #                     'max': 'auto',
            #                     'ticksPosition': 'before',
            #                     'legendPosition': 'start',
            #                     'legendOffset': 20
            #                 },
            #                 {
            #                     'id': 'weight',
            #                     'value': 'weight',
            #                     'min': 'auto',
            #                     'max': 'auto',
            #                     'legendPosition': 'start',
            #                     'legendOffset': -20
            #                 },
            #                 {
            #                     'id': 'volume',
            #                     'value': 'volume',
            #                     'min': 0,
            #                     'max': 'auto',
            #                     'legendPosition': 'start',
            #                     'legendOffset': -20
            #                 }
            #             ],
            #             margin={'top': 50, 'right': 120, 'bottom': 50, 'left': 60},
            #             lineWidth=3,
            #             legends=[
            #                 {
            #                     'anchor': 'right',
            #                     'direction': 'column',
            #                     'justify': False,
            #                     'translateX': 100,
            #                     'translateY': 0,
            #                     'itemsSpacing': 2,
            #                     'itemWidth': 60,
            #                     'itemHeight': 20,
            #                     'itemDirection': 'left-to-right',
            #                     'itemOpacity': 0.85,
            #                     'symbolSize': 20,
            #                     'effects': [
            #                         {
            #                             'on': 'hover',
            #                             'style': {
            #                                 'itemOpacity': 1
            #                             }
            #                         }
            #                     ]
            #                 }
            #             ]
            #         )
            

            # with mui.Box(key = "fourth_item"):
            #         nivo.Bump(
            #             data=DATA3,
            #             colors={'scheme': 'spectral'},
            #             lineWidth=3,
            #             activeLineWidth=6,
            #             inactiveLineWidth=3,
            #             inactiveOpacity=0.15,
            #             pointSize=10,
            #             activePointSize=16,
            #             inactivePointSize=0,
            #             pointColor={'theme': 'background'},
            #             pointBorderWidth=3,
            #             activePointBorderWidth=3,
            #             pointBorderColor={'from': 'serie.color'},
            #             axisTop={
            #                 'tickSize': 5,
            #                 'tickPadding': 5,
            #                 'tickRotation': 0,
            #                 'legend': '',
            #                 'legendPosition': 'middle',
            #                 'legendOffset': -36,
            #                 'truncateTickAt': 0
            #             },
            #             axisBottom={
            #                 'tickSize': 5,
            #                 'tickPadding': 5,
            #                 'tickRotation': 0,
            #                 'legend': '',
            #                 'legendPosition': 'middle',
            #                 'legendOffset': 32,
            #                 'truncateTickAt': 0
            #             },
            #             axisLeft={
            #                 'tickSize': 5,
            #                 'tickPadding': 5,
            #                 'tickRotation': 0,
            #                 'legend': 'ranking',
            #                 'legendPosition': 'middle',
            #                 'legendOffset': -40,
            #                 'truncateTickAt': 0
            #             },
            #             margin={'top': 40, 'right': 100, 'bottom': 40, 'left': 60},
            #             axisRight=None
            #         )

            #mui.Card("Fourth Item", key="fourthe_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    # with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    #     mui.Paper("First item", key="first_item")
    #     mui.Paper("Second item (cannot drag)", key="second_item")
    #     mui.Paper("Third item (cannot resize)", key="third_item")