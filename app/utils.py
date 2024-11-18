# flake8: noqa
import flet as ft
from config import BASE_DIR
from style import colors


def create_card_for_index(title, description, image_path, link=None):
    button = ft.ElevatedButton(
        text="Подробнее",
        url=link,
        visible=link is not None,
    )

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
                            ft.Text(title, size=25,
                                    weight=ft.FontWeight.BOLD, max_lines=2,
                                    font_family='Tinkoff Sans Bold'),
                            ft.Text(description, max_lines=6, size=15,
                                    font_family='Tinkoff Sans Regular'),
                            button
                        ]
                    ),
                    expand=True,
                ),
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
    ft.Text("Т-Образование", size=26, weight=ft.FontWeight.BOLD,
            color=colors["Dark"]["text"], text_align=ft.TextAlign.CENTER, font_family='Tinkoff Sans Bold'),
    ft.Text(
        "Бесплатные образовательные программы для школьников, студентов и ИТ-специалистов",
        color=colors["Dark"]["text"],
        text_align=ft.TextAlign.CENTER,
        font_family='Tinkoff Sans Medium',
        size=20
    ),
    create_card_for_index(
        "Т‑Банк Финтех",
        "Образовательные ИТ-курсы от топ-менеджеров, техлидов и ведущих специалистов Т‑Банка",
        f"{BASE_DIR}/static/1.webp",
        'https://education.tbank.ru/study/fintech/'
    ),
    create_card_for_index(
        "Т‑Банк Старт",
        "Оплачиваемые стажировки в сфере ИТ",
        f"{BASE_DIR}/static/2.webp",
        'https://education.tbank.ru/start/'
    ),
    create_card_for_index(
        "Т-банк Академия",
        "Образовательные проекты в вузах России",
        f"{BASE_DIR}/static/3.webp",
        'https://education.tbank.ru/academy/'
    ),
    create_card_for_index(
        "Talents at T-Bank",
        "Ускоренный карьерный рост для тех, кто недавно работает в Т-Банке",
        f"{BASE_DIR}/static/4.webp",
        'https://www.tbank.ru/career/it/talents/'
    ),
    create_card_for_index(
        "Стипендия",
        "Поддерживаем талантливых студентов со всей России",
        f"{BASE_DIR}/static/5.webp",
        'https://education.tbank.ru/scholarship/'
    ),
    create_card_for_index(
        "Программы в Сириусе",
        "Бесплатные образовательные программы на федеральной территории «Сириус» для студентов",
        f"{BASE_DIR}/static/6.webp",
        'https://education.tbank.ru/activities/sirius/'
    ),
]


courses_list = [
    create_card_for_index(
        "Т-Банк Финтех",
        "Образовательные ИТ-курсы от топ-менеджеров, техлидов и ведущих специалистов Т－Банка",
        f"{BASE_DIR}/static/1.webp",
        'https://education.tbank.ru/study/fintech/'
    ),
    create_card_for_index(
        "Android для начинающих",
        "Бесплатный курс для будущих разработчиков",
        f"{BASE_DIR}/static/android.webp",
        'https://education.tbank.ru/school/basic/android/'
    ),
    create_card_for_index(
        "IOS для начинающих",
        "Бесплатный курс для всех желающих попробовать себя в создании мобильных приложений",
        f"{BASE_DIR}/static/ios.webp",
        'https://education.tbank.ru/school/basic/ios/'
    ),
    create_card_for_index(
        "Анализ данных",
        "Знакомство с основами анализа данных и современными инструментами аналитики",
        f"{BASE_DIR}/static/ad.png",
        'https://education.tbank.ru/school/basic/analysis/'
    ),
    create_card_for_index(
        "Информатика решает",
        "Бесплатный онлайн-курс для школьников 7—11 классов",
        f"{BASE_DIR}/static/inf.webp",
        'https://education.tbank.ru/school/basic/programming/'
    ),
    create_card_for_index(
        "Математика решает",
        "Бесплатный онлайн-курс для школьников 4—6 классов",
        f"{BASE_DIR}/static/math.webp",
        'https://education.tbank.ru/school/basic/math/'
    ),
]