from pyfiglet import Figlet
from main import get_inf


def get_inf_command():
   ip = input('IP: ')
   
   preview = Figlet(font='slant')
   final_text = Figlet(font='slant')
   print(preview.renderText('INFO'))
   
   get_inf(ip=ip)
   
   print(final_text.renderText('IP'))
   