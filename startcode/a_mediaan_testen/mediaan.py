
def mediaan(getallen):
    """Geeft de mediaan van een lijst getallen."""
    if not getallen:
        raise ValueError("Lege lijst")

    getallen = sorted(getallen)
    midden = len(getallen) // 2
    return getallen[midden]

