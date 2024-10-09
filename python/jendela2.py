import PySimpleGUI as sg  
window =sg.Window(title="Profile",
                  layout=[[sg.Text("NPM     : 2210010052")],
                          [sg.Text("Nama    : Made Sugiyanti")],
                          [sg.Text("Kelas   : 5N Reguler Pagi Banjarmasin")],
                          [sg.Text("Matkul  : Pemrograman Visual 3")] 
                          ],
                  size=(400,200))
window()
window.close()