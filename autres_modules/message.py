

def message(valeur: str,val=None) -> dict:
    if valeur == "update":
        return {"detail": "Mise à jour effectuée avec succès"}
    elif valeur == "delete":
        return {"detail": "Suppression effectuée avec succès"}
    elif valeur == "save":
        return {"detail": "Enregistrement effectué avec succès"}
    elif valeur == "not_found":
        return {"detail": f" {val} non trouvé(e)"}
    elif valeur == "multiple_obj":
        return print({"detail": f" Plusieurs {val} ont été trouvé(es)"})
    else:
        return {"detail": " "}
