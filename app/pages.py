# flake8: noqa
import flet as ft
from config import BASE_DIR
from style import colors
from utils import controls, controls_for_index
from texts import first_class


list_view_content = ft.ListView(
    controls=[
        ft.Text("Тест на профориентацию", size=24, weight=ft.FontWeight.BOLD, color=colors['Dark']['text']),
        *controls,
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Далее", size=16, weight=ft.FontWeight.BOLD, color=colors['Dark']['text']),
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


list_view_index = ft.ListView(
    controls=[
        *controls_for_index,
    ],
    expand=True,

)
test_screen_content = ft.Column(
    controls=[
        ft.Row(
            controls=[ft.Text(
                "Тестовый экран", size=24, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"])],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        ft.Text(
            "Здесь может быть ваш контент для тестового экрана.", color=colors["Dark"]["text"]),
        ft.Image(
            src=f"{BASE_DIR}/static/bigboss.jpg",
            width=550, height=500),
    ],
    alignment=ft.MainAxisAlignment.START,
    expand=True
)


class Course:
    @staticmethod
    def second_page() -> ft.Column:
        page = ft.ListView(
            controls=[
                ft.Text(
                    '1.1 Как будет устроен курс', size=24, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"]
                ),
                ft.Container(
                    content=ft.Text(
                        first_class, max_lines=None
                    ),
                )
            ],
            expand=True
        )
        return page

    @staticmethod
    def first_page() -> ft.Column:
        page = ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Text(
                        "Анализ данных", size=24, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"])],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "В демо версии приложения доступна только небольшая часть курса по теме Анализ Данных, с которой вы можете ознакомиться.",
                    color=colors["Dark"]["text"]),
                ft.Image(
                    src=f"{BASE_DIR}/static/ad.png",
                    width=500, height=550, ),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True
        )

        return page
