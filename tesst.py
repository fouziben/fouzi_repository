from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit




def btn_charger_action():
    print("btn charger action")
def btn_sauvegarder_action():
    print("btn sauvegarder action")
def btn_analyser_action():
    print("btn analyser action")
    somme = int(input12.text())+int(input22.text())+int(input32.text())+int(input42.text())
    moy = somme/4
    lbl_totalPoint.setText(f" la somme totale est de {somme}")
    lbl_moyenne.setText(f"La moyenne est de {moy}")
    print ("moyenne : " , moy)
    if int(input12.text()) > int(input22.text()) and int(input12.text()) > int(input32.text()) and int(input12.text()) > int(input42.text()) :
        lbl_gagnant.setText(f"le gagnant est {input1.setText()}")
    elif int(input22.text()) > int(input12.text()) and int(input22.text()) > int(input32.text()) and int(input22.text()) > int(input42.text()) :
        lbl_gagnant.setText(f"Le gagnant est {input2.text()}")
    elif int(input32.text()) > int(input12.text()) and int(input32.text()) > int(input22.text()) and int(input32.text()) > int(input42.text()):
        lbl_gagnant.setText(f"Le gagnant est {input3.setText()}")
    elif int(input42.text()) > int(input12.text()) and int(input42.text()) > int(input22.text()) and int(input42.text()) > int(input32.text()):
        lbl_gagnant.setText(f"Le gagnant est {input4.setText()}")



app = QApplication([])
fen = QWidget()

# Créer un  Grid layout et l'associer a la fenetre
grid = QGridLayout()
fen.setLayout(grid)

grid.addWidget(QLabel("Nom_Joueur"),0,1)
grid.addWidget(QLabel("Points_Joueur"),0,2)

lbl1 = QLabel("joueur1")
grid.addWidget(lbl1, 1, 0)
lbl2 = QLabel("joueur2")
grid.addWidget(lbl2, 2, 0)
lbl3 = QLabel("joueur3")
grid.addWidget(lbl3, 3, 0)
lbl4 = QLabel("joueur4")
grid.addWidget(lbl4, 4, 0)

input1 = QLineEdit()
grid.addWidget(input1, 1, 1)
input2 = QLineEdit()
grid.addWidget(input2, 2, 1)
input3 = QLineEdit()
grid.addWidget(input3, 3, 1)
input4 = QLineEdit()
grid.addWidget(input4, 4, 1)

input12 = QLineEdit()
grid.addWidget(input12, 1, 2)
input22 = QLineEdit()
grid.addWidget(input22, 2, 2)
input32 = QLineEdit()
grid.addWidget(input32, 3, 2)
input42 = QLineEdit()
grid.addWidget(input42, 4, 2)

inp_totalPoint = QLineEdit(fen)
grid.addWidget(inp_totalPoint, 5, 2)

lbl_totalPoint = QLabel("total_point : 0")
grid.addWidget(lbl_totalPoint, 5, 1)
lbl_moyenne = QLabel("moyenne : 0")
grid.addWidget(lbl_moyenne, 5, 3)
lbl_gagnant = QLabel("gagnant : x")
grid.addWidget(lbl_gagnant, 6, 1)


btn_charger = QPushButton("Charger")
grid.addWidget(btn_charger, 7, 0)
btn_charger.clicked.connect(btn_charger_action)

btn_sauvegarde = QPushButton("Sauvegarde")
grid.addWidget(btn_sauvegarde, 7, 1)
btn_sauvegarde.clicked.connect(btn_sauvegarder_action)

btn_analyse = QPushButton("Analyser")
grid.addWidget(btn_analyse, 7, 2)
btn_analyse.clicked.connect(btn_analyser_action)


fen.show()
app.exec()