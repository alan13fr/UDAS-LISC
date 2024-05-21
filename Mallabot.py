from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Datos almacenados en listas de diccionarios
data = [
    {'materia': 'calculo integral', 'prerequisitos': 'calculo diferencial', 'creditos': 6, 'area': 'basica comun'},
    {'materia': 'responsabilidad social', 'prerequisitos': 'ninguno', 'creditos': 3, 'area': 'general'},
    {'materia': 'compiladores', 'prerequisitos': 'algoritmos', 'creditos': 6, 'area': 'basica diciplinar'},
    {'materia': 'informatica industrial', 'prerequisitos': 'microprocesadores', 'creditos': 6, 'area': 'profundizacion'},
    {'materia': 'topicos', 'prerequisitos': 'ninguno', 'creditos': 6, 'area': 'optativa disciplinar'}
]

# Funciones de búsqueda
def buscar_prerequisitos(materia):
    for item in data:
        if item['materia'] == materia:
            return item['prerequisitos']
    return "No se encontró esa materia."

def buscar_creditos(materia):
    for item in data:
        if item['materia'] == materia:
            return item['creditos']
    return "No se encontró esa materia."

def buscar_area(materia):
    for item in data:
        if item['materia'] == materia:
            return item['area']
    return "No se encontró esa materia."

# Widget para mostrar las respuestas
class RespuestaWidget(BoxLayout):
    def actualizar_respuesta(self, resultado):
        self.clear_widgets()  # Limpiar widgets anteriores
        result_label = Label(text=str(resultado))  # Asegurar que el resultado es una cadena
        self.add_widget(result_label)

# Ventana principal de la aplicación
class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.menu_layout = BoxLayout(orientation='vertical')
        self.respuesta_widget = RespuestaWidget(size_hint=(1, 0.3))
        self.layout.add_widget(self.menu_layout)
        self.layout.add_widget(self.respuesta_widget)
        self.show_menu()
        return self.layout

    def show_menu(self):
        self.menu_layout.clear_widgets()
        welcome_label = Label(text="Bienvenido, selecciona una opción:")
        self.menu_layout.add_widget(welcome_label)

        button1 = Button(text="1. Prerequisitos de materias")
        button1.bind(on_press=self.show_prerequisitos)
        self.menu_layout.add_widget(button1)

        button2 = Button(text="2. Número de créditos por materia")
        button2.bind(on_press=self.show_creditos)
        self.menu_layout.add_widget(button2)

        button3 = Button(text="3. Área de materias")
        button3.bind(on_press=self.show_area)
        self.menu_layout.add_widget(button3)

        button4 = Button(text="4. Información acerca de optativas disciplinares")
        button4.bind(on_press=lambda x: self.show_text("Las materias del tipo optativa disciplinar son:\n- Topicos"))
        self.menu_layout.add_widget(button4)

        button5 = Button(text="5. Información acerca de optativas de profundización")
        button5.bind(on_press=lambda x: self.show_text("Las materias del tipo optativa de profundización son:\n- Informatica Industrial"))
        self.menu_layout.add_widget(button5)

        button6 = Button(text="6. Información acerca de optativas complementarias")
        button6.bind(on_press=lambda x: self.show_text("Las materias del tipo optativa complementaria son:\n- Materia Complementaria"))
        self.menu_layout.add_widget(button6)

    def show_prerequisitos(self, instance):
        self.show_input_screen(buscar_prerequisitos)

    def show_creditos(self, instance):
        self.show_input_screen(buscar_creditos)

    def show_area(self, instance):
        self.show_input_screen(buscar_area)

    def show_text(self, text):
        self.respuesta_widget.actualizar_respuesta(text)
        self.menu_layout.clear_widgets()
        back_button = Button(text='Regresar al menú principal')
        back_button.bind(on_press=lambda x: self.show_menu())
        self.menu_layout.add_widget(back_button)

    def show_input_screen(self, buscar_func):
        self.menu_layout.clear_widgets()
        materia_input = TextInput(hint_text='Escribe la materia', multiline=False)
        self.respuesta_widget.actualizar_respuesta('')
        search_button = Button(text='Buscar')
        search_button.bind(on_press=lambda x: self.display_result(buscar_func, materia_input.text))
        self.menu_layout.add_widget(materia_input)
        self.menu_layout.add_widget(search_button)
        back_button = Button(text='Regresar al menú principal')
        back_button.bind(on_press=lambda x: self.show_menu())
        self.menu_layout.add_widget(back_button)

    def display_result(self, funcion_busqueda, materia):
        resultado = funcion_busqueda(materia)
        self.respuesta_widget.actualizar_respuesta(resultado)

# Ejecutar la aplicación
if __name__ == '__main__':
    MyApp().run()
