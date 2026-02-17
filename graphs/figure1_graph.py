"""
Graph for Figure 1

An adjacency list representation where each city maps to a list of its
neighbouring cities.
"""

figure1_graph = {
    # ── Northern Region ──
    "Kartum": ["Humera", "Metema"],
    "Asmera": ["Axum", "Adigrat"],
    "Humera": ["Kartum", "Shire", "Gondar"],
    "Shire": ["Humera", "Axum", "Debarke"],
    "Axum": ["Shire", "Adwa", "Asmera"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Adigrat": ["Adwa", "Asmera", "Mekelle"],
    "Debarke": ["Shire", "Gondar"],
    "Mekelle": ["Adwa", "Adigrat", "Sekota", "Alamata", "Kilbet Rasu"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],

    # ── Afar / North-East ──
    "Samara": ["Alamata", "Gabi Rasu", "Fenti Rasu", "Woldia"],
    "Fenti Rasu": ["Samara", "Kilbet Rasu"],
    "Kilbet Rasu": ["Fenti Rasu", "Mekelle"],
    "Gabi Rasu": ["Samara", "Awash"],

    # ── North-West ──
    "Metema": ["Kartum", "Gondar", "Azezo"],
    "Gondar": ["Humera", "Azezo", "Debarke", "Metema", "Debre Tabor"],
    "Azezo": ["Gondar", "Metema", "Bahir Dar"],
    "Bahir Dar": ["Azezo", "Debre Tabor", "Injibara", "Metekel"],
    "Debre Tabor": ["Bahir Dar", "Woldia", "Lalibela", "Gondar"],
    "Lalibela": ["Debre Tabor", "Woldia", "Sekota"],
    "Woldia": ["Lalibela", "Debre Tabor", "Alamata", "Dessie", "Samara"],

    # ── Central-West ──
    "Metekel": ["Bahir Dar", "Injibara", "Assosa"],
    "Assosa": ["Metekel", "Gimbi"],
    "Injibara": ["Bahir Dar", "Metekel", "Finote Selam"],
    "Finote Selam": ["Injibara", "Debre Markos"],
    "Debre Markos": ["Finote Selam", "Debre Sina", "Addis Ababa"],

    # ── Central ──
    "Dessie": ["Woldia", "Kemise"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Debre Sina": ["Kemise", "Debre Birhan", "Debre Markos"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Addis Ababa": ["Debre Birhan", "Debre Markos", "Ambo", "Adama"],

    # ── West ──
    "Ambo": ["Addis Ababa", "Wolkite", "Nekemte"],
    "Nekemte": ["Ambo", "Gimbi", "Bedelle"],
    "Gimbi": ["Nekemte", "Dembi Dollo", "Assosa"],
    "Dembi Dollo": ["Gimbi", "Gambella", "Assosa"],
    "Gambella": ["Dembi Dollo", "Gore"],
    "Gore": ["Gambella", "Tepi", "Bedelle", "Metu"],
    "Metu": ["Gore", "Bedelle"],
    "Bedelle": ["Nekemte", "Metu", "Gore", "Jimma"],

    # ── East ──
    "Adama": ["Addis Ababa", "Matahara", "Asella", "Batu"],
    "Matahara": ["Adama", "Awash"],
    "Awash": ["Matahara", "Gabi Rasu", "Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babile"],
    "Babile": ["Harar", "Jigjiga", "Goba"],
    "Jigjiga": ["Babile", "Dega Habur"],
    "Dega Habur": ["Jigjiga", "Kebri Dehar"],
    "Kebri Dehar": ["Dega Habur", "Werder", "Gode"],
    "Werder": ["Kebri Dehar"],
    "Gode": ["Kebri Dehar", "Sof Oumer", "Dollo"],
    "Dollo": ["Gode", "Mokadisho"],
    "Mokadisho": ["Dollo"],

    # ── South-East ──
    "Sof Oumer": ["Gode", "Goba", "Bale"],
    "Goba": ["Sof Oumer", "Bale", "Babile"],
    "Bale": ["Goba", "Sof Oumer", "Dodolla", "Liben"],
    "Liben": ["Bale"],
    "Dodolla": ["Bale", "Assasa", "Shashemene"],
    "Assasa": ["Dodolla", "Asella"],
    "Asella": ["Assasa", "Adama"],

    # ── South / Central ──
    "Batu": ["Adama", "Butajira", "Shashemene"],
    "Butajira": ["Batu", "Addis Ababa", "Worabe", "Wolkite"],
    "Worabe": ["Butajira", "Hossana", "Shashemene", "Wolkite"],
    "Wolkite": ["Worabe", "Butajira", "Ambo", "Jimma"],
    "Hossana": ["Worabe", "Shashemene", "Wolaita Sodo"],
    "Wolaita Sodo": ["Hossana", "Dawro", "Arba Minch"],
    "Shashemene": ["Batu", "Dodolla", "Worabe", "Hossana", "Hawassa"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Konso": ["Yabello", "Arba Minch"],
    "Arba Minch": ["Konso", "Wolaita Sodo", "Basketo"],
    "Moyale": ["Yabello", "Nairobi"],
    "Nairobi": ["Moyale"],

    # ── South-West ──
    "Dawro": ["Wolaita Sodo", "Basketo", "Bonga"],
    "Basketo": ["Dawro", "Arba Minch", "Bench Maji"],
    "Bonga": ["Dawro", "Jimma", "Tepi"],
    "Jimma": ["Bonga", "Bedelle", "Wolkite"],
    "Tepi": ["Gore", "Bonga", "Mizan Teferi"],
    "Mizan Teferi": ["Tepi", "Bench Maji"],
    "Bench Maji": ["Mizan Teferi", "Basketo", "Juba"],
    "Juba": ["Bench Maji"],
}
