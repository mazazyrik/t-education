# flake8: noqa
import flet as ft
from config import BASE_DIR
from config import questions as qs
from style import colors
from utils import controls_for_index, courses_list
from texts import first_class


# TODO: везде сделать паддинг сверху

list_view_index = ft.ListView(
    controls=[
        *controls_for_index,
    ],
    expand=True,
    spacing=20

)
test_screen_content = ft.Column(
    controls=[
        ft.Row(
            controls=[ft.Text(
                "Тестовый экран", size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                font_family='Tinkoff Sans Bold')],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        ft.Text(
            "Здесь может быть ваш контент для тестового экрана.", color=colors["Dark"]["text"],
            font_family='Tinkoff Sans Medium', size=20, text_align=ft.TextAlign.CENTER),
        ft.Row(
            controls=[
                ft.Image(
                    src=f"{BASE_DIR}/static/bigboss.jpg",
                    width=500, height=500
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ],
    alignment=ft.MainAxisAlignment.START,
    expand=True,
    spacing=20
)


class Test:
    def __init__(self, questions=qs):
        self.answers = []
        self.current_question_index = 0
        self.questions = questions

    def what_course(self):
        if 'Школьник' in self.answers:
            if 'заниматься творчеством' in self.answers:
                return [
                    courses_list[4], courses_list[5]
                ]
            elif 'анализировать, работать с цифрами' in self.answers:
                return [
                    courses_list[3], courses_list[5]
                ]
            else:
                return [
                    courses_list[3], courses_list[5], courses_list[4]
                ]
        elif 'Студент' or 'У меня уже есть профессия, хочу освоить что-то новое' in self.answers:
            if 'анализировать, работать с цифрами' in self.answers:
                return [courses_list[3]]
            elif 'заниматься творчеством' in self.answers:
                return [courses_list[1], courses_list[2]]
            elif 'использовать технологичные способы решения' in self.answers:
                return [courses_list[0], courses_list[1], courses_list[2]]
            else:
                return [
                    courses_list[0], courses_list[1], courses_list[3]
                ]
        else:
            return [
                courses_list[0], courses_list[1], courses_list[2], courses_list[3], courses_list[4], courses_list[5]
            ]

    def second_page(self, navigate_to: callable = None) -> ft.Column:
        return ft.ListView(
            controls=[
                ft.Text("Тест на профориентацию", size=26,
                        weight=ft.FontWeight.BOLD, color=colors['Dark']['text'],
                        font_family='Tinkoff Sans Bold',
                        text_align=ft.TextAlign.CENTER),
                ft.Text("Этот тест поможет вам выбрать курс, который максимально вам подходит", size=20,
                        color=colors['Dark']['text'],
                        font_family='Tinkoff Sans Medium',
                        text_align=ft.TextAlign.CENTER),
                ft.Row(
                    controls=[
                        ft.Image(
                            src=f"{BASE_DIR}/static/6.webp",
                            width=500, height=300
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Перейти к тесту",
                            on_click=lambda e: navigate_to(
                                self.create_question_page(navigate_to)),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            expand=True,
            spacing=20
        )

    def create_question_page(self, navigate_to: callable = None):
        question = self.questions[self.current_question_index]

        question_card = ft.Card(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    question["question"], size=20, color=colors['Dark']['text'],
                                    font_family='Tinkoff Sans Medium',
                                    text_align=ft.TextAlign.START
                                ),
                                ft.RadioGroup(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Radio(value=option),
                                                    ft.Text(
                                                        option, font_family="Tinkoff Sans Regular", size=16,
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.START
                                            )
                                            for option in question["options"]
                                        ]
                                    ),
                                    on_change=lambda e: self.save_answer(
                                        e.control.value)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
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
            animate_size=True,
        )

        navigation_controls = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    tooltip="Назад",
                    on_click=lambda e: navigate_to(
                        self.previous_question(navigate_to)),
                ),
                ft.IconButton(
                    icon=ft.icons.NAVIGATE_NEXT,
                    tooltip="Далее",
                    on_click=lambda e: navigate_to(
                        self.next_question(navigate_to)),

                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        return ft.Column(
            controls=[
                question_card,
                navigation_controls
            ],
            expand=True,
            spacing=20
        )

    def create_result_page(self, navigate_to: callable = None):
        return ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Результаты теста", size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                                font_family='Tinkoff Sans Bold'
                            ),
                            ft.Text(
                                f"Больше всего вам подходят:", size=20, color=colors["Dark"]["text"],
                                font_family='Tinkoff Sans Medium'
                            ),
                            *self.what_course(),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text="Перейти к курсам",
                                        on_click=lambda e: navigate_to(
                                            Course.first_page(navigate_to)),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    bgcolor=colors["Dark"]["background"],
                )
            ], expand=True, spacing=20
        )

    def save_answer(self, answer):
        if self.current_question_index < len(self.questions):
            if len(self.answers) <= self.current_question_index:
                self.answers.append(answer)
            else:
                self.answers[self.current_question_index] = answer

    def next_question(self, navigate_to: callable):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return self.create_question_page(navigate_to)
        elif self.current_question_index == len(self.questions) - 1:
            return self.create_result_page(navigate_to)

    def previous_question(self, navigate_to: callable):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            return self.create_question_page(navigate_to)


class Course:
    @staticmethod
    def second_page(navigate_to: callable) -> ft.Column:
        page = ft.Column(
            controls=[
                ft.ListView(
                    controls=[
                        ft.Text(
                            '1.1 Как будет устроен курс', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                            font_family='Tinkoff Sans Bold'
                        ),
                        ft.Container(
                            content=ft.Text(
                                first_class, max_lines=None, size=19, color=colors["Dark"]["text"],
                                font_family='Tinkoff Sans Regular'
                            ),
                        )
                    ],
                    expand=True
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            tooltip="Назад",
                            on_click=lambda e: navigate_to(
                                Course.first_page(navigate_to))
                        ),
                        ft.IconButton(
                            icon=ft.icons.NAVIGATE_NEXT,
                            tooltip="Далее",
                            on_click=lambda e: navigate_to(
                                Course.third_page(navigate_to))
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
            expand=True, spacing=20
        )
        return page

    @staticmethod
    def first_page(navigate_to: callable) -> ft.Column:
        page = ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Text(
                        "Анализ данных", size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                        font_family='Tinkoff Sans Bold')],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "В демо версии приложения доступна только небольшая часть курса по теме Анализ Данных, с которой вы можете ознакомиться.",
                    color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', size=20,
                    text_align=ft.TextAlign.CENTER),
                ft.Row(
                    controls=[
                        ft.Image(
                            src=f"{BASE_DIR}/static/ad.png",
                            width=500, height=300
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Перейти к курсу",
                            on_click=lambda e: navigate_to(
                                Course.second_page(navigate_to))
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True, spacing=20
        )

        return page

    @staticmethod
    def third_page(navigate_to: callable) -> ft.Column:
        page = ft.ListView(
            controls=[
                ft.Text(
                    'В демо версии приложения недоступен плеер', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.Image(
                            src=f"{BASE_DIR}/static/vid.png",
                            width=450, height=200
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Вернуться в начало",
                            on_click=lambda e: navigate_to(
                                Course.first_page(navigate_to))
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ], expand=True, padding=20, spacing=20
        )
        return page


class Prizes:
    @staticmethod
    def first_page(navigate_to: callable) -> ft.Column:
        page = ft.ListView(
            controls=[
                ft.Text(
                    'Меняй знания на мерч Т-образование', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    'Брендированная продукция', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Подробнее",
                            on_click=lambda e: navigate_to(
                                Prizes.prize_page(navigate_to)),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/prize.png",
                    width=600, height=300
                ),
                ft.Text(
                    'Проходи курсы и обменивай баллы на мерч Т-образование', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER

                ),
                ft.Text(
                    'Стикеры', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    '57-66 баллов', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/stickers.png",
                    width=700, height=300
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Обменять",
                            on_click=lambda e: navigate_to(
                                Prizes.prize_page(navigate_to)),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Text(
                    'Подушка', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    '67-73 баллов', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/pillow.png",
                    width=600, height=300
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Обменять",
                            on_click=lambda e: navigate_to(
                                Prizes.prize_page(navigate_to)),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Text(
                    'Термокружка', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    '74-82 баллов', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/pot.png",
                    width=600, height=300
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Обменять",
                            on_click=lambda e: navigate_to(
                                Prizes.prize_page(navigate_to)),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

            ], expand=True, padding=20, spacing=20
        )
        return page

    @staticmethod
    def prize_page(navigate_to: callable) -> ft.Column:
        page = ft.ListView(
            controls=[
                ft.Text(
                    'Как получить баллы?', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    'Просматривая занятия и вовремя выполняя задания, вы можете получить баллы.', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/money.png",
                    width=600, height=300
                ),
                ft.Text(
                    'Где посмотреть количество баллов?', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    'Количество баллов и курс обмена вы можете посмотреть  в разделе “Достижения”.', size=20, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Medium', text_align=ft.TextAlign.CENTER
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/points.png",
                    width=600, height=300
                ),
                ft.Text(
                    'Как обменять баллы на  мерч от Т-образование?', size=26, weight=ft.FontWeight.BOLD, color=colors["Dark"]["text"],
                    font_family='Tinkoff Sans Bold', text_align=ft.TextAlign.CENTER,
                ),
                ft.Image(
                    src=f"{BASE_DIR}/static/questions.png",
                    width=600, height=600
                ),
            ], expand=True, padding=20, spacing=20
        )
        return page