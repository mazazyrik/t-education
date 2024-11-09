colors = {
    "DeepOrange": {
        "200": "#FFDD2D",
        "500": "#FFDD2D",
        "700": "#FFDD2D",
    },

    "Dark": {
        "background": "#000000",
        "text": "#F2F4F7",
        "card": "#313132",
        "button": "#FFDD2D",
        "bars": "#9299A2"
    },

    "Light": {
        "background": "#F2F4F7",
        "text": "#000000",
        "card": "#FFFFFF",
        "button": "#FFDD2D",
        "bars": "#9299A2"
    }
}

KV = '''
MDScreen:

    MDCard:
        orientation: "vertical"
        padding: 0, 0, 0 , "36dp"
        size_hint: .5, .5
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 4
        shadow_radius: 6
        shadow_offset: 0, 2

        MDLabel:
            text: "Theme style - {}".format(app.theme_cls.theme_style)
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"

        MDRaisedButton:
            text: "Set theme"
            on_release: app.switch_theme_style()
            pos_hint: {"center_x": .5}
'''
