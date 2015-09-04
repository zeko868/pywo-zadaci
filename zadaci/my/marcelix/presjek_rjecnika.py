
def presjek_rjecnika(r1, r2):
    """
    Ova funkcija racun presjek rjecnika r1 i r2.
    Vraca rjecnik koji ima kljuceve iz presjeka, a
    vrijednosti preuzima od prvog rjecnika.
    """
    kljucevi_r1 = set(r1.keys())
    kljucevi_r2 = set(r2.keys())
    
    R = { k:r1[k] for k in (kljucevi_r1 & kljucevi_r2) } 
    return R