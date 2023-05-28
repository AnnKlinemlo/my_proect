from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import buildozer
import ctypes
import numpy as np

Window.clearcolor = (230 / 250, 230 / 250, 250 / 250, 1)

class MainApp(App):
    def build(self):
        # здесь я добавляю основной и второй экраны в менеджер, этот класс больше ничего не делает
        sm.add_widget(MainScreen())
        sm.add_widget(Win1())
        sm.add_widget(Win2())
        return sm  # Я возвращаю менеджера, чтобы поработать с ним позже


class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Main'  # установка значения экранного имени для диспетчера экранов
        main_layout = BoxLayout(orientation='vertical', padding=100,
                                spacing=70)  # создание пустого макета, который не привязан к экрану
        self.add_widget(main_layout)  # добавление main_layout на экран
        but_open1 = Button(text='Матрица 2х2', on_press=self.win1,
                           background_color=(2 / 250, 230 / 250, 250 / 250, 1))
        main_layout.add_widget(but_open1)
        but_open2 = Button(text='Матрица 3х3', on_press=self.win2,
                           background_color=(2 / 250, 230 / 250, 250 / 250, 1))
        main_layout.add_widget(but_open2)

    def win1(self, *args):
        self.manager.current = 'win1'  # выбор экрана по названию

    def win2(self, *args):
        self.manager.current = 'win2'  # выбор экрана по названию


class Win1(Screen):
    def __init__(self):
        super().__init__()
        # на этом экране я делаю все то же самое, что и на главном экране, чтобы иметь возможность переключаться туда и обратно
        self.name = 'win1'
        superBox = BoxLayout(orientation='vertical')

        b1 = BoxLayout(orientation="horizontal", padding=50, spacing=70)

        l1 = Label(text="a11 = ", font_size=40, color=(0, 0, 0, 1), size_hint=(0.15, 1))
        self.t11 = TextInput(text="0", font_size=50, size_hint_y=None, height=100, size_hint=(0.35, 1))
        l2 = Label(text="a12 = ", font_size=40, color=(0, 0, 0, 1), size_hint=(0.15, 1))
        self.t12 = TextInput(text="0", font_size=50, size_hint_y=None, height=100, size_hint=(0.35, 1))

        b1.add_widget(l1)
        b1.add_widget(self.t11)
        b1.add_widget(l2)
        b1.add_widget(self.t12)

        b2 = BoxLayout(orientation="horizontal", padding=50, spacing=70)

        l3 = Label(text="a21 = ", font_size=40, color=(0, 0, 0, 1), size_hint=(0.15, 1))
        self.t21 = TextInput(text="0", font_size=50, size_hint_y=None, height=100, size_hint=(0.35, 1))
        l4 = Label(text="a22 = ", font_size=40, color=(0, 0, 0, 1), size_hint=(0.15, 1))
        self.t22 = TextInput(text="0", font_size=50, size_hint_y=None, height=100, size_hint=(0.35, 1))

        b2.add_widget(l3)
        b2.add_widget(self.t21)
        b2.add_widget(l4)
        b2.add_widget(self.t22)

        b3 = BoxLayout(orientation="vertical")

        but_answer = Button(text='Ответ', size_hint=(.5, 1), pos_hint={'center_x': .5, 'center_y': .5},on_press=self.but_answer)

        Go_Back = Button(text='Назад', size_hint=(.3, .5),
                         pos_hint={'center_x': .8, 'center_y': .5}, on_press=self.win1)

        self.text_answer = Label(text="", font_size=40, color=(0, 0, 0, 1))

        b3.add_widget(but_answer)
        b3.add_widget(self.text_answer)
        b3.add_widget(Go_Back)

        superBox.add_widget(b1)
        superBox.add_widget(b2)
        superBox.add_widget(b3)

        self.add_widget(superBox)

    def but_answer(self, *args):
        try:
            a = (str(self.t11.text) + " " + str(self.t12.text) + " " + str(self.t21.text) + " " + str(self.t22.text)).replace(',', '.')
            a = np.fromstring(a, dtype=float, sep=' ')
            mat = a.reshape(2, 2)
            det = round(np.linalg.det(mat),3)
            self.text_answer.text = "Ответ: "+str(det)
        except ValueError:
            self.text_answer.text = "Введите числа!"

    def clean(self):
        self.t11.text = ""
        self.t12.text = ""
        self.t21.text = ""
        self.t22.text = ""
        self.text_answer.text = ""

    def win1(self, *args):  # одновременно с нажатием кнопки он передает информацию о себе.
        # Чтобы не выскакивала ошибка, я добавляю *args в функцию

        self.clean()
        self.manager.current = 'Main'


class Win2(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'win2'
        second2_layout = BoxLayout()
        self.add_widget(second2_layout)
        Go_Back = Button(text='Третий экран', size_hint=(.5, .5),
                         pos_hint={'center_x': .5, 'center_y': .5}, on_press=self.win2)
        second2_layout.add_widget(Go_Back)

    def win2(self, *args):  # одновременно с нажатием кнопки он передает информацию о себе.
        self.manager.current = 'Main'


sm = ScreenManager()  # необходимо создать переменную manager, которая будет собирать экраны и управлять ими

if __name__ == '__main__':
    MainApp().run()
