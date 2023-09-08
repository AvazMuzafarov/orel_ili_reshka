#Орел или решка
#GUI помогает подбросить виртуальную монету и узнать результат - орел или решка

from livewires import games, color
import random

games.init(screen_height=480, screen_width=640, fps=50)

the_sky = games.load_image("sky.jpg", transparent=False)
games.screen.background = the_sky

class Flip(games.Animation):
    """Анимация 'подбросанной' монеты."""
    flipchik = ["orelre.bmp",
                "reshkare.bmp"]
    def __init__(self):
        super(Flip, self).__init__(images=Flip.flipchik,
                                   x=games.screen.width / 2,
                                   y=games.screen.height / 2,
                                   n_repeats=10,
                                   repeat_interval=25)

class Changer(games.Sprite):
    """То на чем все держится - двигателль"""
    def change(self):
        y = random.randrange(2)
        if y == 0:
            orel = Orel()
            games.screen.add(orel)
            orel.update()
        if y == 1:
            reshka = Reshka()
            games.screen.add(reshka)
            reshka.update()

        new_flip = Flip()
        games.screen.add(new_flip)





class F_button (games.Text):
    """Текст подсказка."""
    f_delay = 1000
    def __init__(self):
        super(F_button, self).__init__(value="Нажмите F, чтобы подбросить монету.",
                                       size=30,
                                       color=color.black,
                                       right = games.screen.width - 15,
                                       y = 20)
        self.f_wait = 0

    def update(self):
        """Метод следит за клавишей f и имеет счетчик в 20 сек"""
        if self.f_wait > 0:
            self.f_wait -= 1

        if games.keyboard.is_pressed(games.K_f) and self.f_wait == 0:
            self.f_wait += F_button.f_delay
            retro.change()


class Orel(Changer):
    """Спрайт орел. выходит на экран и вызывает сообщение"""
    orel = games.load_image("orelre.bmp")
    def __init__(self):
        super(Orel, self).__init__(image=Orel.orel,
                                     x=games.screen.width / 2,
                                     y=games.screen.height / 2,
                                     angle=0)
        self.time = 1000
    def ddd(self):
        self.destroy()

    def update(self):
        self.time -=1
        if self.time <1:
            self.ddd()
        if self.time <500:
            hint1 = Hint("Орел")
            games.screen.add(hint1)
retro = Orel() # нужно для вызова метода change
class Reshka(Changer):
    """Спрайт решка. выходит на экран и вызывает сообщение"""
    reshka = games.load_image("reshkare.bmp")
    def __init__(self):
        super(Reshka, self).__init__(image=Reshka.reshka,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2,
                                   angle=0)
        self.time = 1000

    def ddd(self):
        self.destroy()

    def update(self):
        self.time -= 1
        if self.time < 1:
            self.ddd()
        if self.time < 500:
            hint2 = Hint("Решка")
            games.screen.add(hint2)

class Hint(games.Message):
    """сообщение"""
    def __init__(self, value):
        super(Hint, self).__init__(value = value,
                                   size = 40,
                                   color = color.red,
                                   x = games.screen.width/2,
                                   bottom = games.screen.height - 20,
                                   lifetime = 50)




def main():
    f_b = F_button()
    games.screen.add(f_b)
    games.screen.mainloop()


main()


