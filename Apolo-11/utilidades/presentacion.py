import os


class PresentacionUtil:

    @staticmethod
    def progress_bar(progress, total):
        percent = 100 * (progress/float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        print(f"\r|{bar}| {percent:.2f}%", end="\r")
        if progress == total:
            print(f"\r|{bar}| {percent:.2f}%", end="\r\n\n")


    @staticmethod
    def limpiar_consola():
        os.system("cls")
