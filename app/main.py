# flake8: noqa
import flet as ft
import time

from style import colors
from config import BASE_DIR
from pages import list_view_index, list_view_content, test_screen_content, Course


import flet as ft
import time


class MainApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = 400
        self.page.window.height = 700
        self.page.title = "T-Education"
        self.page.bgcolor = ft.colors.BLACK

        self.theme = colors["Dark"]
        self.loading_screen = self.create_loading_screen()
        self.main_screen = self.create_main_screen()
        self.test_screen = self.create_test_screen()
        self.bottom_nav = self.create_bottom_nav()
        self.course_screen = self.create_course_screen()

        self.page.add(self.loading_screen)
        self.page.update()

        time.sleep(3)
        self.show_screen(self.main_screen)

    def create_loading_screen(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=f"{BASE_DIR}/static/logo.png",
                        width=550, height=600),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            bgcolor=self.theme["background"],
        )

    def create_main_screen(self):
        return ft.Container(
            content=list_view_index,
            bgcolor=self.theme["background"],
            expand=True
        )
    def create_course_screen(self):
        return ft.Container(
            content=Course.first_page(),
            bgcolor=self.theme['background'],
            expand=True
        )

    def create_test_screen(self):
        return ft.Container(
            content=test_screen_content,
            expand=True
        )

    def create_bottom_nav(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                ft.icons.HOME, on_click=lambda e: self.on_navigation_change(0), icon_size=24),
                            ft.Text("Главная", size=12,
                                    color=self.theme["text"]),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                ft.icons.QUESTION_ANSWER, on_click=lambda e: self.on_navigation_change(2), icon_size=24),
                            ft.Text("Тест", size=12, color=self.theme["text"]),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                ft.icons.PLAY_ARROW, on_click=lambda e: self.on_navigation_change(3), icon_size=24),
                            ft.Text("Демо курс", size=12,
                                    color=self.theme["text"]),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                ft.icons.INFO, on_click=lambda e: self.on_navigation_change(1), icon_size=24),
                            ft.Text("Информация", size=12,
                                    color=self.theme["text"]),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=50,
            ),
            height=70,
            bgcolor=self.theme["card"],
            border_radius=8,
        )

    def show_screen(self, screen):
        self.page.controls.clear()
        self.page.add(screen)
        self.page.add(self.bottom_nav)
        self.page.update()

        for i in range(0, 101, 5):
            screen.opacity = i / 100
            self.page.update()
            time.sleep(0.02)

    def on_navigation_change(self, selected_index):
        if selected_index == 0:
            self.show_screen(self.main_screen)
        elif selected_index == 1:
            self.show_screen(self.test_screen)
        elif selected_index == 2:
            self.page.add(list_view_content)
            self.page.update()
            self.show_screen(list_view_content)
        elif selected_index == 3:
            self.show_screen(self.course_screen)


def main(page: ft.Page):
    app = MainApp(page)


ft.app(target=main)
