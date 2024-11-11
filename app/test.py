import flet as ft


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

test_screen = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text("Тест", size=24, weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.Text("Вопрос 1", size=20,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.Text(questions[0]["question"], size=16,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.RadioGroup(
                options=questions[0]["options"],
                on_change=lambda e: print(e.control.value),
            ),
            ft.Text("Вопрос 2", size=20,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.Text(questions[1]["question"], size=16,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.RadioGroup(
                options=questions[1]["options"],
                on_change=lambda e: print(e.control.value),
            ),
            ft.Text("Вопрос 3", size=20,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.Text(questions[2]["question"], size=16,
                    weight=ft.FontWeight.BOLD, color="#FFDD2D"),
            ft.RadioGroup(
                options=questions[2]["options"],
                on_change=lambda e: print(e.control.value),
            ),
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
                    ],))]))
