# from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QScrollArea
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QFont


# class AppManager:
#     def __init__(self):
#         self.app = QApplication([])
#         self.main_window = QMainWindow()
#         self.full_screen_window = QMainWindow()
#         self.apply_dark_mode()

#         self.create_control_window()
#         self.show_dashboard()

#     def exit_app(self):
#         self.app.quit()

#     def create_window_with_info(self, screen):
#         size = screen.size()
#         resolution = screen.physicalDotsPerInch()
#         refresh_rate = screen.refreshRate()
#         scaled_font_size = resolution / 4
#         font = QFont()
#         font.setPointSizeF(scaled_font_size)

#         label = QLabel(
#             f"Size: {size.width()}x{size.height()}, Resolution: {resolution} DPI, Refresh Rate: {refresh_rate} Hz")
#         label.setFont(font)

#         return label
    
#     def add_text_box(self):
#         # Create a text box (QTextEdit)
#         text_box = QTextEdit()
#         text_box.setPlaceholderText("Enter text here...")

#         # Assuming self.target_window is the window where you want to add the text box
#         target_widget = self.full_screen_window.centralWidget()

#         # Get the layout of the target widget
#         target_layout = target_widget.layout()

#         # Add the text box to the layout
#         target_layout.addWidget(text_box)


#     def create_control_window(self):
#         self.main_window.setWindowTitle('Control Window')
#         widget = QWidget()
#         layout = QVBoxLayout(widget)

#         dashboard_button = QPushButton('Dashboard')
#         dashboard_button.clicked.connect(self.show_dashboard)
#         layout.addWidget(dashboard_button)

#         page_button = QPushButton('Page')
#         page_button.clicked.connect(self.show_page)
#         layout.addWidget(page_button)

#         desktop_button = QPushButton('Desktop')
#         desktop_button.clicked.connect(self.show_desktop)
#         layout.addWidget(desktop_button)

#         add_textbox_button = QPushButton('Add Text Box')
#         add_textbox_button.clicked.connect(self.add_text_box)
#         layout.addWidget(add_textbox_button)

#         exit_button = QPushButton('Exit')
#         exit_button.clicked.connect(self.exit_app)
#         layout.addWidget(exit_button)

#         self.main_window.setCentralWidget(widget)

#         # Set a reasonable size for the control window
#         self.main_window.resize(400, 300)
        
#         self.main_window.show()

#         # Move control window to the secondary screen if available
#         screens = self.app.screens()
#         if len(screens) > 1:
#             screen_geometry = screens[1].geometry()
#             self.main_window.move(screen_geometry.x(), screen_geometry.y())

#     def show_dashboard(self):
#         self.show_full_screen_window('Dashboard')

#     def show_page(self):
#         self.show_full_screen_window('Page', vertical_scroll=True)

#     def show_desktop(self):
#         self.show_full_screen_window('Desktop', horizontal_scroll=True)

#     def show_full_screen_window(self, title, vertical_scroll=False, horizontal_scroll=False):
#         self.full_screen_window.setWindowTitle(title)
#         widget = QWidget()
#         layout = QVBoxLayout(widget)

#         label = self.create_window_with_info(self.app.screens()[0])
#         layout.addWidget(label)

#         if vertical_scroll:
#             scroll_area = QScrollArea()
#             scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
#             scroll_area.setWidgetResizable(True)
#             layout.addWidget(scroll_area)

#         if horizontal_scroll:
#             scroll_area = QScrollArea()
#             scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
#             scroll_area.setWidgetResizable(True)
#             layout.addWidget(scroll_area)

#         self.full_screen_window.setCentralWidget(widget)
#         self.full_screen_window.showFullScreen()

#     def apply_dark_mode(self):
#         self.app.setStyle('Fusion')
#         palette = self.app.palette()
#         palette.setColor(palette.ColorRole.Window, Qt.GlobalColor.black)
#         palette.setColor(palette.ColorRole.WindowText, Qt.GlobalColor.white)
#         self.app.setPalette(palette)

#     def run(self):
#         self.app.exec()


# app_manager = AppManager()
# app_manager.run()

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class AppManager:
    def __init__(self):
        self.app = QApplication([])
        self.main_window = QMainWindow()
        self.full_screen_window = QMainWindow()
        self.apply_dark_mode()

        self.create_control_window()
        self.show_dashboard()

    def exit_app(self):
        self.app.quit()

    def create_window_with_info(self, screen):
        size = screen.size()
        resolution = screen.physicalDotsPerInch()
        refresh_rate = screen.refreshRate()
        scaled_font_size = resolution / 4
        font = QFont()
        font.setPointSizeF(scaled_font_size)

        label = QLabel(f"Size: {size.width()}x{size.height()}, Resolution: {resolution} DPI, Refresh Rate: {refresh_rate} Hz")
        label.setFont(font)

        return label

    def current_content_layout(self):
        target_widget = self.full_screen_window.centralWidget()
        target_layout = target_widget.layout()
        for i in range(target_layout.count()):
            item = target_layout.itemAt(i)
            if isinstance(item.widget(), QScrollArea):
                return item.widget().widget().layout()
        return target_layout

    def add_text_box(self):
        text_box = QTextEdit()
        text_box.setPlaceholderText("Enter text here...")

        # Create a QFont object with a specific point size
        font = QFont()
        font.setPointSize(24)  # Set the size you want here

        # Apply the QFont to the text box
        text_box.setFont(font)
        
        content_layout = self.current_content_layout()
        content_layout.addWidget(text_box)

    def create_control_window(self):
        self.main_window.setWindowTitle('Control Window')
        widget = QWidget()
        layout = QVBoxLayout(widget)

        dashboard_button = QPushButton('Dashboard')
        dashboard_button.clicked.connect(self.show_dashboard)
        layout.addWidget(dashboard_button)

        page_button = QPushButton('Page')
        page_button.clicked.connect(self.show_page)
        layout.addWidget(page_button)

        desktop_button = QPushButton('Desktop')
        desktop_button.clicked.connect(self.show_desktop)
        layout.addWidget(desktop_button)

        add_textbox_button = QPushButton('Add Text Box')
        add_textbox_button.clicked.connect(self.add_text_box)
        layout.addWidget(add_textbox_button)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.exit_app)
        layout.addWidget(exit_button)

        self.main_window.setCentralWidget(widget)

        # Set a reasonable size for the control window
        self.main_window.resize(400, 300)
        
        self.main_window.show()

        # Move control window to the secondary screen if available
        screens = self.app.screens()
        if len(screens) > 1:
            screen_geometry = screens[1].geometry()
            self.main_window.move(screen_geometry.x(), screen_geometry.y())

    def show_dashboard(self):
        self.show_full_screen_window('Dashboard')

    def show_page(self):
        self.show_full_screen_window('Page', vertical_scroll=True)

    def show_desktop(self):
        self.show_full_screen_window('Desktop', horizontal_scroll=True)

    def show_full_screen_window(self, title, vertical_scroll=False, horizontal_scroll=False):
        self.full_screen_window.setWindowTitle(title)
        widget = QWidget()
        layout = QVBoxLayout(widget)

        label = self.create_window_with_info(self.app.screens()[0])
        layout.addWidget(label)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        if vertical_scroll or horizontal_scroll:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            layout.addWidget(scroll_area)
            scroll_area.setWidget(content_widget)
            if vertical_scroll:
                scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            if horizontal_scroll:
                scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        else:
            layout.addWidget(content_widget)

        self.full_screen_window.setCentralWidget(widget)
        self.full_screen_window.showFullScreen()

    def apply_dark_mode(self):
        self.app.setStyle('Fusion')
        palette = self.app.palette()
        palette.setColor(palette.ColorRole.Window, Qt.GlobalColor.black)
        palette.setColor(palette.ColorRole.WindowText, Qt.GlobalColor.white)
        self.app.setPalette(palette)

    def run(self):
        self.app.exec()

app_manager = AppManager()
app_manager.run()
