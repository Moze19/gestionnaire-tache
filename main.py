
taches = []

while True:
    print("\n--- GESTIONNAIRE DE TACHES ---")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        tache = input("Entrez une tâche : ")
        taches.append(tache)
        print("Tâche ajoutée avec succès.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche enregistrée.")
        else:
            for numero, tache in enumerate(taches, start=1):
                print(numero, "-", tache)

    elif choix == "3":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")
