from Backend import Backend
from Calendar import Calendar
from Event import Event
from Interface import Interface
from User import User
import datetime

if __name__ == '__main__':
    # Создаем экземпляр интерфейса
    interface = Interface()

    # Регистрируем нового пользователя
    interface.register_user("1", "Orkhan", "12345")

    # Входим в систему под созданным пользователем
    user = interface.login("1", "12345")

    # Если вход успешен, добавляем событие в календарь пользователя
    if user:
        user.create_calendar()
        user.create_event("event1", "Встреча", "Обсудить проект", ["Orkhan"])

        events = user.get_calendar().get_events()
        for event_id, event_data in events.items():
            participants = ', '.join(event_data['participants'])
            print(
                f"Event ID: {event_id}, Title: {event_data['title']}, Description: {event_data['description']}, Participants: {participants}")
