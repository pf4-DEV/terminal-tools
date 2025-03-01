theme_version = "native 2.1"

color_themes = {
    "default": {
        "lite":    (228, 138, 255),
        "dark":    (137,  83, 153),
        "litered": (228,  86,  73),
        "darkred": (178,  36,  23),
        "yellow":  (255, 255,  100),
        "blue":    (100, 100, 255),
        "green":   (199, 255, 158),
    },
        
    "pur": {
        "lite":    (200, 200, 200),
        "dark":    (100, 100, 100),
        "litered": (255,  50,  50),
        "darkred": (200,  30,  30),
        "yellow":  (255, 255,  50),
        "blue":    ( 70,  70, 255),
        "green":   (150, 255,  50),
    },

    "green": {
        "lite":    (199, 255, 158),
        "dark":    (119, 153,  95),
        "litered": (228,  86,  73),
        "darkred": (178,  36,  23),
        "yellow":  (255, 255, 100),
        "blue":    (80,  140, 255),
        "green":   (150, 255,  50),
    },

    "blue": {
        "lite":    (100, 100, 255),
        "dark":    ( 70,  70, 255),
        "litered": (255,  50,  50),
        "darkred": (200,  30,  30),
        "yellow":  (255, 255,  50),
        "blue":    ( 70,  70, 255),
        "green":   (150, 255,  50),
    },

    "red": {
        "lite":    (228,  86,  73),
        "dark":    (178,  36,  23),
        "litered": (255,  50,  50),
        "darkred": (200,  30,  30),
        "yellow":  (255, 255,  50),
        "blue":    ( 70,  70, 255),
        "green":   (150, 255,  50),
    },
}

input_themes = {
    "kalike": [
        {
            "type": "print",
            "texte": "\n┌──(",
            "color": "dark",
            "code": "k",
        },
        {
            "type": "print",
            "var": "co_user",
            "color": "lite",
            "code": "k",
        },
        {
            "type": "print",
            "texte": " • ",
            "color": "dark",
            "code": "k",
        },
        {
            "type": "print",
            "var": "time",
            "color": "lite",
            "code": "k",
        },
        {
            "type": "print",
            "texte": ")─[",
            "color": "dark",
            "code": "k",
        },
        {
            "type": "print",
            "var": "action_rep",
            "color": "cyan",
            "code": "k",
        },
        {
            "type": "print",
            "texte": "]",
            "color": "dark",
            "code": "",
        },
        {
            "type": "input",
            "texte": "└─} ",
            "color": "dark",
            "code": "k",
        }
    ],
    "old": [
        {
            "type": "print",
            "texte": "",
            "color": "dark",
            "code": "",
        },
        {
            "type": "print",
            "var": "action_rep",
            "color": "lite",
            "code": "k",
        },
        {
            "type": "input",
            "texte": "> ",
            "color": "lite",
            "code": "k",
        }
    ],
    "bash": [
        {
            "type": "print",
            "texte": "",
            "color": "dark",
            "code": "",
        },
        {
            "type": "print",
            "var": "co_user",
            "color": "dark",
            "code": "k",
        },
        {
            "type": "print",
            "texte": ":",
            "color": "lite",
            "code": "k",
        },
        {
            "type": "print",
            "var": "action_rep",
            "color": "dark",
            "code": "k",
        },
        {
            "type": "input",
            "texte": "$ ",
            "color": "lite",
            "code": "k",
        }
    ],
}