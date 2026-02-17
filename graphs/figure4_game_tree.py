"""
Graph for figure 2

The game tree is a nested dictionary.
  - Interior nodes map city names to their children dict.
  - Terminal nodes map city names to their utility values.

Structure:
  Addis Ababa (MAX)
  ├── Ambo (MIN)
  │   ├── Gedo (MAX)
  │   │   ├── Shambu → 4
  │   │   └── Fincha → 5
  │   └── Nekemte (MAX)
  │       ├── Gimbi → 8
  │       └── Limu → 8
  ├── Buta Jirra (MIN)
  │   ├── Worabe (MAX)
  │   │   ├── Hossana → 6
  │   │   └── Durame → 5
  │   └── Wolkite (MAX)
  │       ├── Bench Naji → 5
  │       └── Tepi → 6
  └── Adama (MIN)
      ├── Diredawa (MAX)
      │   ├── Harar → 10
      │   └── Chiro → 6
      └── Mojo (MAX)
          ├── Kaffa → 7
          └── Dilla → 9
"""

# Terminal utility values
terminal_utilities = {
    "Shambu": 4,
    "Fincha": 5,
    "Gimbi": 8,
    "Limu": 8,
    "Hossana": 6,
    "Durame": 5,
    "Bench Naji": 5,
    "Tepi": 6,
    "Harar": 10,
    "Chiro": 6,
    "Kaffa": 7,
    "Dilla": 9,
}

# Game tree structure  {parent: [children]}
game_tree = {
    "Addis Ababa": ["Ambo", "Buta Jirra", "Adama"],
    "Ambo": ["Gedo", "Nekemte"],
    "Buta Jirra": ["Worabe", "Wolkite"],
    "Adama": ["Diredawa", "Mojo"],
    "Gedo": ["Shambu", "Fincha"],
    "Nekemte": ["Gimbi", "Limu"],
    "Worabe": ["Hossana", "Durame"],
    "Wolkite": ["Bench Naji", "Tepi"],
    "Diredawa": ["Harar", "Chiro"],
    "Mojo": ["Kaffa", "Dilla"],
}
