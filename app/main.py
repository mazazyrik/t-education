# flake8: noqa
import flet as ft
import time

from style import colors
from config import BASE_DIR
from pages import list_view_index, list_view_content, test_screen_content


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
    )

    main_screen = ft.Container(
        content=list_view_index,
        bgcolor=theme["background"],
        expand=True
    )

    test_screen = ft.Container(
        content=test_screen_content,
        expand=True
    )

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
        elif selected_index == 2:
            page.add(list_view_content)
            page.update()
            show_screen(list_view_content)

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
                            ft.icons.QUESTION_ANSWER, on_click=lambda e: on_navigation_change(2), icon_size=24),
                        ft.Text("Тест", size=12, color=colors["Dark"]["text"]),
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
