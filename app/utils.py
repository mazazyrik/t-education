# flake8: noqa
import flet as ft
from config import BASE_DIR
from style import colors
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


def create_card(title, description, image_src):
    return ft.Card(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(title, size=15, weight="bold",
                                    color=colors['Dark']["text"], text_align=ft.TextAlign.LEFT),
                            ft.Text(
                                description,
                                color=colors['Dark']["text"], text_align=ft.TextAlign.LEFT, size=13
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=5,
                    ),
                    padding=10,
                ),
                ft.Container(
                    content=ft.Image(
                        src=image_src,
                        fit=ft.ImageFit.COVER
                    ),
                    width=175,
                    height=100,
                    padding=10,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        ),
        elevation=5,
        height=150,
        animate_size=True,
    )


def create_card_for_index(title, description, image_path):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src=image_path, width=None,
                                     height=None, fit=ft.ImageFit.COVER),
                    expand=True,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(title, size=20,
                                    weight=ft.FontWeight.BOLD, max_lines=1),
                            ft.Text(description, max_lines=3)
                        ]
                    ),
                    expand=True,
                )
            ],
            spacing=10,
            expand=True
        ),
        padding=10,
        bgcolor=colors["Dark"]["card"],
        border_radius=10,
        margin=ft.margin.all(10)
    )


controls_for_index = [
    ft.Text("Т-Образование", size=24, weight=ft.FontWeight.BOLD,
            color=colors["Dark"]["text"], text_align=ft.TextAlign.CENTER),
    ft.Text(
        "Бесплатные образовательные программы для школьников, студентов и ИТ-специалистов",
        color=colors["Dark"]["text"],
        text_align=ft.TextAlign.CENTER
    ),
    create_card_for_index(
        "Т‑Банк Финтех",
        "Образовательные ИТ-курсы от топ-менеджеров, техлидов и ведущих специалистов Т‑Банка",
        f"{BASE_DIR}/static/1.webp"
    ),
    create_card_for_index(
        "Т‑Банк Старт",
        "Оплачиваемые стажировки в сфере ИТ",
        f"{BASE_DIR}/static/2.webp"
    ),
    create_card_for_index(
        "Т-банк Академия",
        "Образовательные проекты в вузах России",
        f"{BASE_DIR}/static/3.webp"
    ),
    create_card_for_index(
        "Talents at T-Bank",
        "Ускоренный карьерный рост для тех, кто недавно работает в Т-Банке",
        f"{BASE_DIR}/static/4.webp"
    ),
    create_card_for_index(
        "Стипендия",
        "Поддерживаем талантливых студентов со всей России",
        f"{BASE_DIR}/static/5.webp"
    ),
    create_card_for_index(
        "Программы в Сириусе",
        "Бесплатные образовательные программы на федеральной территории «Сириус» для студентов",
        f"{BASE_DIR}/static/6.webp"
    ),
]

