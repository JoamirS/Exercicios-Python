# Keeping states inside the class

class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f'{self.name} já está filmando')
            return

        print(f'{self.name} está filmando')
        self.filming = True

    def photograph(self):
        if self.filming:
            print(f'{self.name} não pode fotografar filmando')
            return

    def stop_film(self):
        if not self.filming:
            print(f'{self.name} não está filmando')
            return

        print(f'{self.name} está parando de filmar')
        self.filming = False


camera_01 = Camera('Canon')
camera_02 = Camera('Sony')
camera_01.film()
camera_01.film()
camera_01.photograph()
camera_02.stop_film()
camera_01.stop_film()
