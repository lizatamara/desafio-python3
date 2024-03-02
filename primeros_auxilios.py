estimulos = input("responde a estimulos?: ")

if estimulos == "si":
    print("valorar la necesidad de llevarlo al hospital mas cercano")
else:
    print("abrir la via aerea")
    
    respira = input("respira?: ")
    if respira == "si":
        print("permitirle posición de suficiente ventilación")

    else:
        print("administrar 5 ventilaciones y llamar a la ambulancia")

        ambulacia = "no"
        
        while ambulacia == "no":
            
            signos = input("tiene signos de vida?: ")
            if signos == "si":
                print("reevaluar a la espera de la ambulancia")
            else:
                print("administrar compresiones torácicas hasta que llegue ambulancia")
                
            ambulacia = input("llegó la ambulancia? ")

