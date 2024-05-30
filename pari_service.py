pari_map = {}


def add_pari(_id, pari):
    if _id not in pari_map:
        pari_map[_id] = []
    pari_map[_id].append(pari)


def get_pari(_id):
    if _id not in pari_map:
        return []
    return pari_map[_id]
