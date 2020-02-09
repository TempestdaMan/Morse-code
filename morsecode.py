#Imports
import tkinter
import datetime
import serial
import time
import os 

ARser = serial.Serial('COM4', '9600')





#Definitions
def bsos():
    currentDT = datetime.datetime.now()
    print("-> SOS button  #", str(currentDT))
    S1 = ("S")
    ARser.write(S1.encode())
    O = ("O")
    ARser.write(O.encode())
    S2 = ("S")
    ARser.write(S2.encode())
    
def bgo():
    currentDT = datetime.datetime.now()
    print("-> GO button   #", str(currentDT))
    GO = (">")
    ARser.write(GO.encode())

def bcmd():
    os.system("Start cmd")
    
def bstop():
    currentDT = datetime.datetime.now()
    print("-> STOP button #", str(currentDT))
    STOP = ("|")
    ARser.write(STOP.encode())

def A():
    A = ("A")
    ARser.write(A.encode())
    currentDT = datetime.datetime.now()
    print("-> A button   #", str(currentDT))
    
def B():
    B = ("B")
    ARser.write(B.encode())
    currentDT = datetime.datetime.now()
    print("-> B button   #", str(currentDT))

def C():
    C = ("C")
    ARser.write(C.encode())
    currentDT = datetime.datetime.now()
    print("-> C button   #", str(currentDT))    

def D():
    D = ("D")
    ARser.write(D.encode())
    currentDT = datetime.datetime.now()
    print("-> D button   #", str(currentDT))
    
def E():
    E = ("E")
    ARser.write(E.encode())
    currentDT = datetime.datetime.now()
    print("-> E button   #", str(currentDT))
    
def F():
    F = ("F")
    ARser.write(F.encode())
    currentDT = datetime.datetime.now()
    print("-> F button   #", str(currentDT))

def G():
    G = ("G")
    ARser.write(G.encode())
    currentDT = datetime.datetime.now()
    print("-> G button   #", str(currentDT))

def H():
    H = ("H")
    ARser.write(H.encode())
    currentDT = datetime.datetime.now()
    print("-> H button   #", str(currentDT))

def I():
    I = ("I")
    ARser.write(I.encode())
    currentDT = datetime.datetime.now()
    print("-> I button   #", str(currentDT))

def J():
    J = ("J")
    ARser.write(J.encode())
    currentDT = datetime.datetime.now()
    print("-> J button   #", str(currentDT))

def K():
    K = ("K")
    ARser.write(K.encode())
    currentDT = datetime.datetime.now()
    print("-> K button   #", str(currentDT))

def L():
    L = ("L")
    ARser.write(L.encode())
    currentDT = datetime.datetime.now()
    print("-> L button   #", str(currentDT))

def M():
    M = ("M")
    ARser.write(M.encode())
    currentDT = datetime.datetime.now()
    print("-> M button   #", str(currentDT))

def N():
    N = ("N")
    ARser.write(N.encode())
    currentDT = datetime.datetime.now()
    print("-> N button   #", str(currentDT))

def O():
    O = ("O")
    ARser.write(O.encode())
    currentDT = datetime.datetime.now()
    print("-> O button   #", str(currentDT))

def P():
    P = ("P")
    ARser.write(P.encode())
    currentDT = datetime.datetime.now()
    print("-> P button   #", str(currentDT))

def Q():
    Q = ("Q")
    ARser.write(Q.encode())
    currentDT = datetime.datetime.now()
    print("-> Q button   #", str(currentDT))

def R():
    R = ("R")
    ARser.write(R.encode())
    currentDT = datetime.datetime.now()
    print("-> R button   #", str(currentDT))

def S():
    S = ("S")
    ARser.write(S.encode())
    currentDT = datetime.datetime.now()
    print("-> S button   #", str(currentDT))

def Z():
    Z = ("Z")
    ARser.write(Z.encode())
    currentDT = datetime.datetime.now()
    print("-> Z button   #", str(currentDT))

def T():
    T = ("T")
    ARser.write(T.encode())
    currentDT = datetime.datetime.now()
    print("-> T button   #", str(currentDT))


    





    
    

#Kod
print("   Button         Time")






#Main
root = tkinter.Tk()
root.geometry("385x700")
root.title("Morsekod[Alex.S]")


#Button för SOS diod
btnsos = tkinter.Button(root, text = 'SOS', width = 10, height = 5, fg = 'Red', command = bsos)
btnsos.pack()
btnsos.place(y = 5, x = 5)
#Button för A
btnA = tkinter.Button(root, text = "A", width = 10, height = 5, fg = "Black", command = A)
btnA.pack()
btnA.place(y = 105, x = 5)

#Button för B
btnA = tkinter.Button(root, text = "B", width = 10, height = 5, fg = "Black", command = B)
btnA.pack()
btnA.place(y = 105, x = 100)

#Button för C
btnA = tkinter.Button(root, text = "C", width = 10, height = 5, fg = "Black", command = C)
btnA.pack()
btnA.place(y = 105, x = 200)

#Button för D
btnA = tkinter.Button(root, text = "D", width = 10, height = 5, fg = "Black", command = D)
btnA.pack()
btnA.place(y = 105, x = 300)

#Button för E
btnA = tkinter.Button(root, text = "E", width = 10, height = 5, fg = "Black", command = E)
btnA.pack()
btnA.place(y = 205, x = 5)

#Button för F
btnA = tkinter.Button(root, text = "F", width = 10, height = 5, fg = "Black", command = F)
btnA.pack()
btnA.place(y = 205, x = 100)

#Button för G
btnA = tkinter.Button(root, text = "G", width = 10, height = 5, fg = "Black", command = G)
btnA.pack()
btnA.place(y = 205, x = 200)

#Button för H
btnA = tkinter.Button(root, text = "H", width = 10, height = 5, fg = "Black", command = H)
btnA.pack()
btnA.place(y = 205, x = 300)

#Button för I
btnA = tkinter.Button(root, text = "I", width = 10, height = 5, fg = "Black", command = I)
btnA.pack()
btnA.place(y = 305, x = 5)

#Button för J
btnA = tkinter.Button(root, text = "J", width = 10, height = 5, fg = "Black", command = J)
btnA.pack()
btnA.place(y = 305, x = 100)

#Button för K
btnA = tkinter.Button(root, text = "K", width = 10, height = 5, fg = "Black", command = K)
btnA.pack()
btnA.place(y = 305, x = 200)

#Button för L
btnA = tkinter.Button(root, text = "L", width = 10, height = 5, fg = "Black", command = L)
btnA.pack()
btnA.place(y = 305, x = 300)

#Button för M
btnA = tkinter.Button(root, text = "M", width = 10, height = 5, fg = "Black", command = M)
btnA.pack()
btnA.place(y = 405, x = 5)

#Button för N
btnA = tkinter.Button(root, text = "N", width = 10, height = 5, fg = "Black", command = N)
btnA.pack()
btnA.place(y = 405, x = 100)

#Button för O
btnA = tkinter.Button(root, text = "O", width = 10, height = 5, fg = "Black", command = O)
btnA.pack()
btnA.place(y = 405, x = 200)

#Button för P
btnA = tkinter.Button(root, text = "P", width = 10, height = 5, fg = "Black", command = P)
btnA.pack()
btnA.place(y = 405, x = 300)

#Button för Q
btnA = tkinter.Button(root, text = "Q", width = 10, height = 5, fg = "Black", command = Q)
btnA.pack()
btnA.place(y = 505, x = 5)

#Button för R
btnA = tkinter.Button(root, text = "R", width = 10, height = 5, fg = "Black", command = R)
btnA.pack()
btnA.place(y = 505, x = 100)

#Button för S
btnA = tkinter.Button(root, text = "S", width = 10, height = 5, fg = "Black", command = S)
btnA.pack()
btnA.place(y = 505, x = 200)

#Button för Z
btnA = tkinter.Button(root, text = "Z", width = 10, height = 5, fg = "Black", command = Z)
btnA.pack()
btnA.place(y = 505, x = 300)

#Button för T
btnA = tkinter.Button(root, text = "T", width = 10, height = 5, fg = "Black", command = T)
btnA.pack()
btnA.place(y = 605, x = 5) 


#Button för kör diod
btnkor = tkinter.Button(root, text = 'GO', width = 10, height = 5, fg = 'Green', command = bgo)
btnkor.pack()
btnkor.place(y = 5, x = 100)

#Button för stopp diod
btnstopp = tkinter.Button(root, text = 'STOP', width = 10, height = 5, fg = 'Red', command = bstop)
btnstopp.pack()
btnstopp.place(y = 5, x = 200)

#Button för CMD
btncmd = tkinter.Button(root, text = 'CMD', width = 10, height = 5, fg = 'Black', command = bcmd)
btncmd.pack()
btncmd.place(y = 5, x = 300)





root.mainloop()

