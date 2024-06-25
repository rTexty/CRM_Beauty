import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Flet Data Viewer"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    output = ft.ListView(expand=True, spacing=10)  # Используем ListView для прокрутки
    error_message = ft.Text("", color=ft.colors.RED)

    def fetch_data(e):
        try:
            url = "http://127.0.0.1:8000/api/services/"  # замените на ваш URL
            headers = {
                "Authorization": "Token YOUR_TOKEN"  # замените YOUR_TOKEN на ваш действительный токен
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                output.controls.clear()
                if data:
                    for item in data:
                        name = item.get('name', 'N/A')
                        price = item.get('price', 'N/A')
                        output.controls.append(
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(f"Название: {name}", color=ft.colors.WHITE, size=18, weight="bold"),
                                        ft.Text(f"Цена услуги: {price}", color=ft.colors.GREEN, size=16)
                                    ]
                                ),
                                padding=10,
                                margin=5,
                                border_radius=10,
                                bgcolor=ft.colors.BLACK
                            )
                        )
                else:
                    output.controls.append(ft.Text("No data found.", color=ft.colors.YELLOW))
                error_message.value = ""
            else:
                output.controls.clear()
                error_message.value = f"Error: {response.status_code} {response.text}"
        except Exception as ex:
            output.controls.clear()
            error_message.value = f"Exception: {str(ex)}"
        
        page.update()

    def get_clients(e=None):
        try:
            url = "http://127.0.0.1:8000/api/clients/"
            headers = {
                "Authorization": "Token YOUR_TOKEN"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                clients_data = response.json()
                output.controls.clear()
                if clients_data:
                    for item in clients_data:
                        client_first_name = item.get('first_name', 'Unknown')
                        client_last_name = item.get('last_name', 'Unknown')
                        client_phone_number = item.get('phone_number', 'Unknown')
                        client_email = item.get('email', 'Unknown')
                        output.controls.append(ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"Client: {client_first_name} {client_last_name}", color=ft.colors.WHITE, size=18, weight="bold"),
                                    ft.Text(f"Phone number: {client_phone_number}", color=ft.colors.GREEN, size=16),
                                    ft.Text(f"Email: {client_email}", color=ft.colors.GREEN, size=16),
                                ]
                            ),
                            padding=10,
                            margin=5,
                            border_radius=10,
                            bgcolor=ft.colors.BLACK
                        ))
                else:
                    output.controls.append(ft.Text("No data found.", color=ft.colors.YELLOW))
                error_message.value = ""
            else:
                output.controls.clear()
                error_message.value = f"Error: {response.status_code} {response.text}"
        except Exception as ex:
            output.controls.clear()
            error_message.value = f"Exception: {str(ex)}"

        page.update()

    def get_services():
        try:
            url = "http://127.0.0.1:8000/api/services/"
            headers = {
                "Authorization": "Token YOUR_TOKEN"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                services_data = response.json()
                return {service['id']: service.get('name', 'Unknown Service') for service in services_data}
            else:
                return {}
        except Exception as ex:
            return {}

    clients = get_clients() or {}
    services = get_services() or {}

    def get_orders(e=None):
        try:
            url = 'http://127.0.0.1:8000/api/appointments/'
            headers = {
                "Authorization": "Token YOUR_TOKEN"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                output.controls.clear()
                if data:
                    for item in data:
                        client_name = clients.get(item['client'], 'Unknown Client')
                        service_name = services.get(item['service'], 'Unknown Service')
                        date = item.get('date', 'N/A')
                        notes = item.get('notes', 'N/A')
                        output.controls.append(
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(f"Client: {client_name}", color=ft.colors.WHITE, size=18, weight="bold"),
                                        ft.Text(f"Service: {service_name}", color=ft.colors.GREEN, size=16),
                                        ft.Text(f"Date: {date}", color=ft.colors.WHITE, size=16),
                                        ft.Text(f"Notes: {notes}", color=ft.colors.WHITE, size=14)
                                    ]
                                ),
                                padding=10,
                                margin=5,
                                border_radius=10,
                                bgcolor=ft.colors.BLACK
                            )
                        )
                else:
                    output.controls.append(ft.Text("No data found.", color=ft.colors.YELLOW))
                error_message.value = ""
            else:
                output.controls.clear()
                error_message.value = f"Error: {response.status_code} {response.text}"
        except Exception as ex:
            output.controls.clear()
            error_message.value = f"Exception: {str(ex)}"

        page.update()

    fetch_button = ft.ElevatedButton("Fetch Data", on_click=fetch_data, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)
    get_orders_button = ft.ElevatedButton("Заказы", on_click=get_orders, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)

    # Нижние кнопки
    bottom_buttons = ft.Row(
        controls=[
            ft.TextButton(icon=ft.icons.COMMUTE, text="Заказы", on_click=get_orders),
            ft.TextButton(icon=ft.icons.EXPLORE, text="Мои Услуги", on_click=fetch_data),
            ft.TextButton(icon=ft.icons.EXPLORE, text="Клиенты", on_click=get_clients),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Data Viewer", color=ft.colors.WHITE, size=24),
                    ft.Container(
                        content=output,
                        expand=True,  # Ensure the container expands to fill available space
                    ),
                    error_message
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20  # Добавим расстояние между элементами
            ),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.BLACK,
            expand=True  # Ensure the container expands to fill available space
        ),
        bottom_buttons  # Добавляем нижние кнопки
    )

ft.app(target=main)