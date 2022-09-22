# zad2testy.py
from testy import *

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]


TESTS = [
    # 0
    {
        "arg": [[56, 15, 31, 43, 54, 35, 12, 23], 1],
        "hint": [12, 23, 31, 15, 54, 43, 35, 56]
    },
    # 1
    {
        "arg": [[1223, 1256, 2334, 3412, 3456, 4534, 5645, 5667], 2],
        "hint": [1223, 2334, 3412, 1256, 5645, 4534, 3456, 5667]
    },
    # 2
    {
        "arg": [[12342345, 12345678, 23453456, 34561234, 34565678, 45673456, 56784567, 56786789], 4],
        "hint": [12342345, 23453456, 34561234, 12345678, 56784567, 45673456, 34565678, 56786789]
    },
    # 3
    {
        "arg": [[12346789, 12345678, 67893456, 34561234, 34565678, 45673456, 56784567, 56782345], 4],
        "hint": None
    },
    # 4
    {
        "arg": [[12342345, 12345678, 23453456, 34561234, 34565678, 45673456, 56784567, 56786789, 67897899], 4],
        "hint": [12342345, 23453456, 34561234, 12345678, 56784567, 45673456, 34565678, 56786789, 67897899]
    },
    # 5
    {
        "arg": [[100133, 101109, 101139, 102105, 102130, 102134, 103110, 103120, 104120, 105105, 105107, 105109, 105118,
                 105135, 106103, 106140,
                 107110, 107119, 107123, 107138, 107140, 108130, 109107, 109128, 109132, 109139, 110101, 110103, 110104,
                 110128, 112122, 113102,
                 113107, 113119, 113135, 116113, 116133, 117118, 117124, 118105, 118117, 118123, 119102, 119110, 119125,
                 119137, 120113, 120119,
                 120130, 120132, 121120, 121133, 122122, 122133, 122136, 123105, 123127, 123137, 124108, 124138, 125140,
                 127131, 127139, 128117,
                 128129, 129120, 129127, 129133, 130106, 130107, 130119, 131123, 132118, 132124, 133109, 133113, 133135,
                 133137, 133138, 134106,
                 135102, 135107, 135116, 135200, 136105, 137121, 137129, 137135, 138101, 138121, 138139, 139110, 139113,
                 139116, 139129, 140109,
                 140112, 140122, 200000], 3],
        "hint": [100133, 133138, 138101, 101139, 139129, 129127, 127139, 139113, 113119, 119137, 137129, 129120, 120113,
                 113107, 107110, 110104, 104120,
                 120130, 130119, 119125, 125140, 140109, 109139, 139110, 110101, 101109, 109107, 107119, 119102, 102105,
                 105107, 107140, 140112, 112122,
                 122122, 122133, 133135, 135107, 107123, 123127, 127131, 131123, 123105, 105135, 135102, 102130, 130107,
                 107138, 138121, 121120, 120119,
                 119110, 110103, 103110, 110128, 128129, 129133, 133109, 109132, 132124, 124108, 108130, 130106, 106103,
                 103120, 120132, 132118, 118123,
                 123137, 137121, 121133, 133137, 137135, 135116, 116113, 113102, 102134, 134106, 106140, 140122, 122136,
                 136105, 105109, 109128, 128117,
                 117118, 118105, 105105, 105118, 118117, 117124, 124138, 138139, 139116, 116133, 133113, 113135, 135200,
                 200000]
    },
    # 6
    {
        "arg": [[23694167, 10002427, 62401014, 48072346, 15465131, 10143937, 11263875, 46622345, 28741938, 56965655,
                 60774022, 14012356, 17474755,
                 38574450, 60614807, 31982632, 23561573, 37582188, 51311333, 26324554, 24297000, 32603857, 36553260,
                 18841400, 12654080, 13331126,
                 10631284, 14416101, 66942480, 47553655, 11262911, 66126156, 68606240, 47165537, 14844403, 49482429,
                 40223801, 70000000, 13541721,
                 19503758, 38694716, 55374662, 14003565, 45132174, 45541126, 29536685, 52616786, 19386612, 68791806,
                 33194948, 15005067, 15733227,
                 38012800, 53383319, 44503813, 60694225, 12841884, 56456077, 61561441, 49416285, 19242206, 69226860,
                 21883869, 24801887, 24273905,
                 38756061, 29111484, 18065486, 67864065, 35183030, 56552953, 32275338, 50675696, 41556860, 17213173,
                 18873518, 62856694, 35162369,
                 39371354, 40652293, 42251924, 66853516, 31733198, 44031500, 34165645, 41671401, 54861546, 32344513,
                 38132874, 40804155, 56345261,
                 61014941, 21741063, 22061265, 30306879, 68603234, 23453416, 22931747, 35651950, 39055634, 28006069,
                 23466922], 4],
        "hint": [10002427, 24273905, 39055634, 56345261, 52616786, 67864065, 40652293, 22931747, 17474755, 47553655,
                 36553260, 32603857, 38574450,
                 44503813, 38132874, 28741938, 19386612, 66126156, 61561441, 14416101, 61014941, 49416285, 62856694,
                 66942480, 24801887, 18873518,
                 35183030, 30306879, 68791806, 18065486, 54861546, 15465131, 51311333, 13331126, 11263875, 38756061,
                 60614807, 48072346, 23466922,
                 69226860, 68603234, 32344513, 45132174, 21741063, 10631284, 12841884, 18841400, 14003565, 35651950,
                 19503758, 37582188, 21883869,
                 38694716, 47165537, 55374662, 46622345, 23453416, 34165645, 56456077, 60774022, 40223801, 38012800,
                 28006069, 60694225, 42251924,
                 19242206, 22061265, 12654080, 40804155, 41556860, 68606240, 62401014, 10143937, 39371354, 13541721,
                 17213173, 31733198, 31982632,
                 26324554, 45541126, 11262911, 29111484, 14844403, 44031500, 15005067, 50675696, 56965655, 56552953,
                 29536685, 66853516, 35162369,
                 23694167, 41671401, 14012356, 23561573, 15733227, 32275338, 53383319, 33194948, 49482429, 24297000,
                 70000000]
    },

]


def printarg(L, K):
    print("Lista: ", limit(L, 120))
    print("K: ", K)


def printhint(hint):
    print("Przykladowy wynik:", limit(hint, 120))


def printsol(sol):
    print("Uzyskany wynik   :", limit(sol, 120))


def check(L, K, hint, sol):
    def check_int(inp, K, res, ans):

        if res == None and ans == None: return True
        if type(res) is not list: return False
        if len(res) != len(inp): return False
        if min(res) != min(inp): return False
        if max(res) != max(inp): return False
        if set(res) != set(inp): return False
        for i in range(1, len(res)):
            if res[i - 1] % 10 ** K != res[i] // 10 ** K:
                return False
        return True

    if check_int(L, K, sol, hint):
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests(f):
    internal_runtests(printarg, printhint, printsol, check, TESTS, f)
