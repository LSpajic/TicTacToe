def k_n_pascal_trokut(stupanj, clan):

    if clan == 1 or clan - 1 == stupanj:
        return 1
    return k_n_pascal_trokut(stupanj - 1, clan - 1) + k_n_pascal_trokut(stupanj -1, clan)

# rijecnik = {}
# rijecnik[kljuc] = vrijednost
def k_n_pascal_trokut_cached(stupanj, clan, cache):
    #ako je (stupanj, clan) u cacheu, neka vrati vrijednost
    #ako nije izracunaj
    if (stupanj, clan) in cache:
        return cache[(stupanj, clan)]
    if clan == 1 or clan - 1 == stupanj:
        return 1
    cache[(stupanj, clan)] = k_n_pascal_trokut_cached(stupanj - 1, clan - 1, cache) + k_n_pascal_trokut_cached(stupanj -1, clan, cache)
    return cache[(stupanj, clan)]


def k_n_pascal_fast_cache(stupanj, clan, cache):
    in_cache = cache.get((stupanj, clan))
    if in_cache is not None:
        return in_cache

    if clan == 1 or clan - 1 == stupanj:
        cache[(stupanj, clan)] = 1
        return 1

    rezultat = k_n_pascal_trokut_cached(stupanj - 1, clan - 1, cache) + k_n_pascal_trokut_cached(stupanj -1, clan, cache)
    cache[(stupanj, clan)] = rezultat
    return rezultat

if __name__ == '__main__':
    print(k_n_pascal_trokut(3, 2)) #3
    print(k_n_pascal_trokut(4, 3)) #6
    print(k_n_pascal_trokut(5, 3)) #10

    cache = {}
    print(k_n_pascal_trokut_cached(3, 2, cache))
    print(k_n_pascal_trokut_cached(4, 3, cache))
    print(k_n_pascal_trokut_cached(5, 3, cache))

    cache = {}
    print(k_n_pascal_fast_cache(3, 2, cache))
    print(k_n_pascal_fast_cache(4, 3, cache))
    print(k_n_pascal_fast_cache(5, 3, cache))
