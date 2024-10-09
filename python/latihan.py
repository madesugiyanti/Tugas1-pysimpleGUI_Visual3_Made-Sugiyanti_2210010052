import PySimpleGUI as sg 
sg.theme ("DarkGreen4") 
sg.theme_text_color ("#888378") 
window =sg.Window(title="Profile",
                  layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                                   font=("Arial",25))],
                          [sg.Text("NPM     : 2210010052")],
                          [sg.Text("Nama    : Made Sugiyanti")],
                          [sg.Text("Kelas   : 5N Reguler Pagi Banjarmasin")],
                          [sg.Text("Matkul  : Pemrograman Visual 3")] 
                          ],
                  size=(500,200),
                  font=("Times",18))

window()
window.close()