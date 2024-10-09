import PySimpleGUI as sg 
sg.theme ("DarkPurple3") 
sg.theme_text_color ("#E3CF57") 
window =sg.Window(title="Contoh Button",
                  layout=[[sg.Text("Contoh Button")],
                          [sg.Button("Button Simpan")],
                          [sg.Button("Button keluar")]
                          ],
                  size=(400,200),
                  font=("Times",18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()