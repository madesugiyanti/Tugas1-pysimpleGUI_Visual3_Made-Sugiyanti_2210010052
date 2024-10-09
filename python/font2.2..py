import PySimpleGUI as sg 
sg.theme ("DarkRed1") 
sg.theme_text_color ("#00FFFF") 
window =sg.Window(title="Profile",
                  layout=[[sg.Text("FTI UNISKA",
                                   font=("Helvetica",24))],
                          [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                          [sg.Text("UNISKA MAB BANJARMASIN")]
                          ],
                  size=(430,200),
                  font=("Times",18))

window()
window.close()