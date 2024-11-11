import flet as ft
from config import BASE_DIR

questions = [
    {
        "question": "Какой вид деятельности вам больше нравится?",
        "options": ["Работа с людьми", "Работа с цифрами", "Творческая работа", "Техническая работа"]
    },
    {
        "question": "Какой из следующих предметов вам нравится больше всего?",
        "options": ["История", "Математика", "Искусство", "Физика"]
    },
    {
        "question": "Как вы предпочитаете проводить свободное время?",
        "options": ["Читать книги", "Заниматься спортом", "Рисовать или играть на музыкальных инструментах", "Ремонтировать технику"]
    }
]

controls = []

for question in questions:
    question_card = ft.Card(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                question["question"], size=16, weight=ft.FontWeight.BOLD, color="#FFDD2D"),
                            ft.RadioGroup(
                                content=ft.Column(
                                    controls=[
                                        ft.Radio(value=option, label=option)
                                        for option in question["options"]
                                    ]
                                ),
                                on_change=lambda e: print(e.control.value)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                    ),
                    padding=10,
                    expand=True
                ),
                ft.Container(
                    content=ft.Image(
                        src=f"{BASE_DIR}/static/question_image.png",
                        fit=ft.ImageFit.COVER
                    ),
                    width=100,
                    height=100,
                    padding=10,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        ),
        elevation=5,
        width=None,
        height=None,
        animate_size=True,
    )

    controls.append(question_card)

list_view_content = ft.ListView(
    controls=[
        ft.Text("Тест", size=24, weight=ft.FontWeight.BOLD, color="#FFDD2D"),
        *controls,
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Далее", size=16, weight=ft.FontWeight.BOLD, color="#FFDD2D"),
                        alignment=ft.alignment.center,
                        bgcolor="#313132",
                        width=100,
                        height=40,
                        border_radius=10,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    ],
    expand=True
)
