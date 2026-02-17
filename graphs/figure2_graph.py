"""
Graph for figure 2
Adjacency list where each city maps to a list of (neighbour, cost) tuples.
"""

figure2_graph = {
    # ── Northern Region ──
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Asmera": [("Adwa", 6), ("Adigrat", 9)],
    "Humera": [("Kartum", 21), ("Shire", 8), ("Gondar", 9)],
    "Shire": [("Humera", 8), ("Axum", 2), ("Debarke", 7)],
    "Axum": [("Shire", 2), ("Adwa", 1), ("Adigrat", 4)],
    "Adwa": [("Axum", 1), ("Adigrat", 2), ("Asmera", 6)],
    "Adigrat": [("Adwa", 2), ("Asmera", 9), ("Axum", 4), ("Mekelle", 4)],
    "Debarke": [("Shire", 7), ("Gondar", 4)],
    "Mekelle": [("Adigrat", 4), ("Sekota", 9), ("Alamata", 5), ("Kilbet Rasu", 6)],
    "Sekota": [("Mekelle", 9), ("Alamata", 6), ("Lalibela", 6)],
    "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],

    # ── Afar / North-East ──
    "Samara": [("Woldia", 8), ("Alamata", 11), ("Gabi Rasu", 10), ("Fenti Rasu", 7)],
    "Fenti Rasu": [("Samara", 7), ("Kilbet Rasu", 6)],
    "Kilbet Rasu": [("Fenti Rasu", 6), ("Mekelle", 6)],
    "Gabi Rasu": [("Samara", 10), ("Awash", 5)],

    # ── North-West ──
    "Metema": [("Kartum", 19), ("Gondar", 7), ("Azezo", 7)],
    "Gondar": [("Humera", 9), ("Azezo", 1), ("Debarke", 4), ("Metema", 7), ("Debre Tabor", 6)],
    "Azezo": [("Gondar", 1), ("Metema", 7), ("Bahir Dar", 7)],
    "Bahir Dar": [("Azezo", 7), ("Debre Tabor", 4), ("Injibara", 4), ("Metekel", 11)],
    "Debre Tabor": [("Bahir Dar", 4), ("Woldia", 12), ("Lalibela", 8), ("Gondar", 6)],
    "Lalibela": [("Debre Tabor", 8), ("Woldia", 7), ("Sekota", 6)],
    "Woldia": [("Lalibela", 7), ("Debre Tabor", 12), ("Alamata", 3), ("Dessie", 6), ("Samara", 8)],

    # ── Central-West ──
    "Metekel": [("Bahir Dar", 11), ("Assosa", 11)],
    "Assosa": [("Metekel", 11), ("Gimbi", 12)],
    "Injibara": [("Bahir Dar", 4), ("Finote Selam", 2)],
    "Finote Selam": [("Injibara", 2), ("Debre Markos", 3), ("Bahir Dar", 6)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17)],

    # ── Central ──
    "Dessie": [("Woldia", 6), ("Kemise", 4)],
    "Kemise": [("Dessie", 4), ("Debre Sina", 6)],
    "Debre Sina": [("Kemise", 6), ("Debre Birhan", 2), ("Debre Markos", 17)],
    "Debre Birhan": [("Debre Sina", 2), ("Addis Ababa", 5)],
    "Addis Ababa": [("Debre Birhan", 5), ("Debre Markos", 13), ("Ambo", 5), ("Adama", 3)],

    # ── West ──
    "Ambo": [("Addis Ababa", 5), ("Nekemte", 9), ("Wolkite", 6)],
    "Nekemte": [("Ambo", 9), ("Gimbi", 4), ("Bedelle", 5)],
    "Gimbi": [("Nekemte", 4), ("Dembi Dollo", 6), ("Assosa", 12)],
    "Dembi Dollo": [("Gimbi", 6), ("Gambella", 4)],
    "Gambella": [("Dembi Dollo", 4), ("Gore", 5)],
    "Gore": [("Gambella", 5), ("Tepi", 9), ("Bedelle", 6), ("Metu", 7)],
    "Metu": [("Gore", 7), ("Bedelle", 7)],
    "Bedelle": [("Nekemte", 5), ("Metu", 7), ("Gore", 6), ("Jimma", 7)],

    # ── East ──
    "Adama": [("Addis Ababa", 3), ("Matahara", 3), ("Asella", 4), ("Batu", 4)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Awash": [("Matahara", 1), ("Gabi Rasu", 5), ("Chiro", 4)],
    "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
    "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
    "Harar": [("Dire Dawa", 4), ("Babile", 2)],
    "Babile": [("Harar", 2), ("Jigjiga", 3), ("Gode", 28)],
    "Jigjiga": [("Babile", 3), ("Dega Habur", 5)],
    "Dega Habur": [("Jigjiga", 5), ("Kebri Dehar", 6), ("Gode", 17)],
    "Kebri Dehar": [("Dega Habur", 6), ("Werder", 6), ("Gode", 5)],
    "Werder": [("Kebri Dehar", 6)],
    "Gode": [("Kebri Dehar", 5), ("Sof Oumer", 23), ("Dollo", 17), ("Babile", 28), ("Dega Habur", 17), ("Mokadisho", 22)],
    "Dollo": [("Gode", 17), ("Mokadisho", 18)],
    "Mokadisho": [("Dollo", 18), ("Gode", 22)],

    # ── South-East ──
    "Sof Oumer": [("Gode", 23), ("Goba", 6), ("Bale", 23)],
    "Goba": [("Sof Oumer", 6), ("Bale", 18), ("Dodolla", 5)],
    "Bale": [("Goba", 18), ("Sof Oumer", 23), ("Liben", 11)],
    "Liben": [("Bale", 11)],
    "Dodolla": [("Goba", 5), ("Assasa", 1), ("Shashemene", 8)],
    "Assasa": [("Dodolla", 1), ("Asella", 4)],
    "Asella": [("Assasa", 4), ("Adama", 4)],

    # ── South / Central ──
    "Batu": [("Adama", 4), ("Butajira", 2), ("Shashemene", 3)],
    "Butajira": [("Batu", 2), ("Worabe", 2), ("Wolkite", 4)],
    "Worabe": [("Butajira", 2), ("Hossana", 2), ("Jimma", 13), ("Wolkite", 5)],
    "Wolkite": [("Worabe", 5), ("Butajira", 4), ("Ambo", 6), ("Jimma", 8), ("Hossana", 5)],
    "Hossana": [("Worabe", 2), ("Shashemene", 7), ("Wolaita Sodo", 4), ("Wolkite", 5)],
    "Wolaita Sodo": [("Hossana", 4), ("Dawro", 6), ("Arba Minch", 5)],
    "Shashemene": [("Batu", 3), ("Dodolla", 8), ("Hossana", 7), ("Hawassa", 3)],
    "Hawassa": [("Shashemene", 3), ("Dilla", 4)],
    "Dilla": [("Hawassa", 4), ("Bule Hora", 7)],
    "Bule Hora": [("Dilla", 7), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 3), ("Konso", 3), ("Moyale", 6)],
    "Konso": [("Yabello", 3), ("Arba Minch", 4)],
    "Arba Minch": [("Konso", 4), ("Wolaita Sodo", 5), ("Basketo", 10)],
    "Moyale": [("Yabello", 6), ("Nairobi", 22)],
    "Nairobi": [("Moyale", 22)],

    # ── South-West ──
    "Dawro": [("Wolaita Sodo", 6), ("Basketo", 4), ("Bonga", 10)],
    "Basketo": [("Dawro", 4), ("Arba Minch", 10), ("Bench Maji", 5)],
    "Bonga": [("Dawro", 10), ("Jimma", 4), ("Tepi", 8), ("Mizan Teferi", 4)],
    "Jimma": [("Bonga", 4), ("Bedelle", 7), ("Wolkite", 8), ("Worabe", 13)],
    "Tepi": [("Gore", 9), ("Bonga", 8), ("Mizan Teferi", 4)],
    "Mizan Teferi": [("Tepi", 4), ("Bonga", 4)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Juba": [("Bench Maji", 22)],
}
