import random as rand
import sys
#values by order: Name, Hipoints, Size, Alligment

elements = ["Fire", "Water", "Ice", "Earth", "Wind", "Light", "Dark", "Electricity", None]
alligment = ["Lawful good", "Neutral good", "Chaotic good", "Lawful neutral", "(True) neutral", "Chaotic neutral","Lawful evil", "Neutral evil", "Chaotic evil"]
sizeAndhitpoints = {
    "tiny": rand.randint(1, 20),
    "small": rand.randint(20, 60), 
    "medium": rand.randint(40, 100),
    "large": rand.randint(100, 200),
    "huge": rand.randint(200, 500),
    "gargantuan": rand.randint(500, 1000)
}

name = ["Rat", 
        "Cyclop", 
        "Evil Gnome", 
        "Spider", 
        "Iron Golem", 
        "Orc Warrior", 
        "Hell Hound", 
        "Ogre",
        "Gargoyle", 
        "Crab",
        "Killer Whale",
        "Narwhal",
        "Sperm Whale",
        "Wight",
        "Dire Wolf",
        "Wolf",
        "Wraith",
        "Wyvern",
        "Yellow Mold",
        "Zombie",
        "Vampire"
        "Minotaur"
        "Bandit",
        "Bandit Leader",
        "Ant",
        "Snake",
        "Pit Fighter",
        "Ghoul",
        "Knight",
        "Acolyte",
        "Mage",
        "Archer",
        "Hell Spawn"
        "Wendigo",
        "Scorpion",
        "WereWolf",
        "Samurai",
        "Cursed Chest",
        "Iron Maiden",
        "Penguin",
        "Elemental",
        "Mammoth",
        "Golem",
        "Spirit",
        "Basilisk",
        "Phoenix",
        "Bugbear",
        "Drake",
        "Felldrake",
        "Metallic Dragon",
        "Chromatic Dragon",
        "Planar Dragon",
        "Displacer Beast",
        "Griffon",
        "Hydra",
        "Skeleton Guard",
        "Skeleton Ranger",
        "Beholder"
        ]
