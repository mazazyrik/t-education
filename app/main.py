# flake8: noqa
import flet as ft
import time
from pathlib import Path
from style import colors
from test import test_screen

BASE_DIR = Path(__file__).parent.resolve()


def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 700
    page.title = "T-Education"
    page.bgcolor = ft.colors.BLACK

    theme = colors["Dark"]

    loading_screen = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src=f"{BASE_DIR}/static/logo.png",
                    width=550, height=600),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
        bgcolor=theme["background"],
        height=page.window.height - 100
    )

    main_screen = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Т-Образование", size=24,
                                weight=ft.FontWeight.BOLD, color=theme["text"])
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "Бесплатные образовательные программы для школьников, студентов и ИТ-специалистов",
                    color=theme["text"],
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Card(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text("Т‑Банк Финтех", size=15, weight="bold",
                                                color=theme["text"], text_align=ft.TextAlign.LEFT),
                                        ft.Text(
                                            "Образовательные ИТ-курсы от топ-менеджеров, техлидов и ведущих специалистов Т‑Банка",
                                            color=theme["text"], text_align=ft.TextAlign.LEFT, size=13
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                    width=175,
                                ),
                                padding=10,
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src=f"{BASE_DIR}/static/1.webp",
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
                    width=375,
                    height=150,
                    animate_size=True,
                )

            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        ),
        bgcolor=theme["background"],
        height=page.window.height - 130
    )

    # test_screen = ft.Container(
    #     content=ft.Column(
    #         controls=[
    #             ft.Row(
    #                 controls=[ft.Text(
    #                     "Тестовый экран", size=24, weight=ft.FontWeight.BOLD, color=theme["text"])],
    #                 alignment=ft.MainAxisAlignment.CENTER,
    #                 spacing=10
    #             ),
    #             ft.Text(
    #                 "Здесь может быть ваш контент для тестового экрана.", color=theme["text"]),
    #             ft.Image(
    #                 src=f"{BASE_DIR}/static/bigboss.jpg",
    #                 width=550, height=500),
    #         ],
    #         alignment=ft.MainAxisAlignment.START,
    #         spacing=10,
    #     ),
    #     bgcolor=theme["background"],
    #     height=page.window.height - 130
    # )

    def show_screen(screen):
        page.controls.clear()
        page.add(screen)
        page.add(bottom_nav)
        page.update()

        for i in range(0, 101, 5):
            page.controls[0].opacity = i / 100
            page.update()
            time.sleep(0.02)

    def on_navigation_change(selected_index):
        if selected_index == 0:
            show_screen(main_screen)
        elif selected_index == 1:
            show_screen(test_screen)

    bottom_nav = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(
                            ft.icons.HOME, on_click=lambda e: on_navigation_change(0), icon_size=24),
                        ft.Text("Главная", size=12,
                                color=colors["Dark"]["text"]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        ft.IconButton(
                            ft.icons.INFO, on_click=lambda e: on_navigation_change(1), icon_size=24),
                        ft.Text("Информация", size=12,
                                color=colors["Dark"]["text"]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=50,
        ),
        height=70,
        bgcolor=colors["Dark"]["card"],
        border_radius=8,
    )

    page.add(loading_screen)
    page.update()

    time.sleep(3)
    show_screen(main_screen)


ft.app(target=main)
