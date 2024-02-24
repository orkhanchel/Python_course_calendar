import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QPushButton, QMessageBox, QDialog, QLabel, QLineEdit, QDialogButtonBox
from Interface import Interface

class AddEventDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Event")
        layout = QVBoxLayout()

        self.date_label = QLabel("Date:")
        layout.addWidget(self.date_label)

        self.date_edit = QLineEdit()
        layout.addWidget(self.date_edit)

        self.title_label = QLabel("Title:")
        layout.addWidget(self.title_label)

        self.title_edit = QLineEdit()
        layout.addWidget(self.title_edit)

        self.description_label = QLabel("Description:")
        layout.addWidget(self.description_label)

        self.description_edit = QLineEdit()
        layout.addWidget(self.description_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)


class CalendarApp(QWidget):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.setWindowTitle("Calendar App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.show_event_dialog)
        layout.addWidget(self.calendar)

        self.setLayout(layout)

    def show_event_dialog(self):
        dialog = AddEventDialog()
        if dialog.exec_():
            date = self.calendar.selectedDate().toString("dd-MM-yyyy")
            title = dialog.title_edit.text()
            description = dialog.description_edit.text()
            self.interface.add_event(date, title, description)
            QMessageBox.information(self, "Event Added", f"Event added for {date}\nTitle: {title}\nDescription: {description}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = Interface()
    window = CalendarApp(interface)
    window.show()
    sys.exit(app.exec_())
