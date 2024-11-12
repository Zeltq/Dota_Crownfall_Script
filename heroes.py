
class Hero:
    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens

heroes_list = [
    Hero("Invoker", ["Pride", "Pride", "Pride"]),
    Hero("Doom", ["Pride", "Pride", "Gluttony"]),
    Hero("Sniper", ["Pride", "Pride", "Mountain"]),
    Hero("Storm Spirit", ["Pride", "Pride", "Sky"]),
    Hero("Tinker", ["Pride", "Pride", "City"]),
    Hero("Wraith King", ["Pride", "Pride", "City"]),
    Hero("Alchemist", ["Pride", "Greed", "City"]),
    Hero("Axe", ["Pride", "Wrath", "Desert"]),
    Hero("Centaur Warrunner", ["Pride", "Plains", "Plains"]),
    Hero("Clockwerk", ["Pride", "City", "Plains"]),
    Hero("Juggernaut", ["Pride", "Discipline", "Sea"]),
    Hero("Lina", ["Pride", "Plains", "Desert"]),
    Hero("Luna", ["Pride", "Envy", "Plains"]),
    Hero("Magnus", ["Pride", "Mountain", "Tundra"]),
    Hero("Mars", ["Pride", "Discipline", "Sky"]),
    Hero("Medusa", ["Pride", "Wrath", "Sea"]),
    Hero("Mirana", ["Pride", "Discipline", "Cosmos"]),
    Hero("Monkey King", ["Pride", "Mischief", "Forest"]),
    Hero("Omniknight", ["Pride", "Discipline", "Plains"]),
    Hero("Phantom Assasin", ["Pride", "Discipline", "Forest"]),
    Hero("Razor", ["Pride", "Discipline", "Discipline"]),
    Hero("Rubick", ["Pride", "Mischief", "City"]),
    Hero("Shadow Fiend", ["Pride", "Gluttony", "Gluttony"]),
    Hero("Spirit Breaker", ["Pride", "Gluttony", "Cosmos"]),
    Hero("Techies", ["Pride", "Mischief", "Mischief"]),
    Hero("Ursa", ["Pride", "Wrath", "Tundra"]),
    Hero("Vengeful Spirit", ["Pride", "Wrath", "Sky"]),
    Hero("Viper", ["Pride", "Wrath", "Sky"]),
    Hero("Windranger", ["Pride", "Discipline", "Forest"]),

    Hero("Pudge", ["Gluttony", "Gluttony", "Gluttony"]),
    Hero("Brewmaster", ["Gluttony", "Gluttony", "Mountain"]),
    Hero("Tidehunter", ["Gluttony", "Gluttony", "Sea"]),
    Hero("Tusk", ["Gluttony", "Gluttony", "Tundra"]),
    Hero("Bloodseeker", ["Gluttony", "Greed", "Wrath"]),
    Hero("Crystal Maiden", ["Gluttony", "Tundra", "Tundra"]),
    Hero("Kunkka", ["Gluttony", "Sea", "Sea"]),
    Hero("Marci", ["Gluttony", "Discipline", "Love"]),
    Hero("Primal Beast", ["Gluttony", "Wrath", "Forest"]),
    Hero("Undying", ["Gluttony", "Discipline", "Discipline"]),
    Hero("Venomancer", ["Gluttony", "Wrath", "Forest"]),

    Hero("Underlord", ["Sloth", "Sloth", "Sloth"]),
    Hero("Bane", ["Sloth", "Sloth", "Greed"]),
    Hero("Tiny", ["Sloth", "Sloth", "Mountain"]),
    Hero("Ancient Apparition", ["Sloth", "Tundra", "Tundra"]),
    Hero("Dazzle", ["Sloth", "Greed", "Cave"]),
    Hero("Elder Titan", ["Sloth", "Envy", "Mountain"]),
    Hero("KOTL", ["Sloth", "Lust", "Cosmos"]),
    Hero("Night Stalker", ["Sloth", "Greed", "Cave"]),
    Hero("Ogre Magi", ["Sloth", "Lust", "Plains"]),
    Hero("Oracle", ["Sloth", "Cosmos", "Cosmos"]),
    Hero("Phantom Lancer", ["Sloth", "Envy", "Discipline"]),
    Hero("Shadow Shaman", ["Sloth", "Greed", "Mischief"]),
    Hero("Treant Protector", ["Sloth", "Forest", "Forest"]),
    Hero("Witch Doctor", ["Sloth", "Love", "Sea"]),

    Hero("Bounty Hunter", ["Greed", "Greed", "Greed"]),
    Hero("Pugna", ["Greed", "Greed", "Greed"]),
    Hero("Meepo", ["Greed", "Greed", "City"]),
    Hero("Slark", ["Greed", "Greed", "Sea"]),
    Hero("Gyrocopter", ["Greed", "City", "Sky"]),
    Hero("Leshrac", ["Greed", "Envy", "Cosmos"]),
    Hero("Leech", ["Greed", "Wrath", "Tundra"]),
    Hero("Lifestealer", ["Greed", "Envy", "Envy"]),
    Hero("Naga Siren", ["Greed", "Sea", "Sea"]),
    Hero("Necrophos", ["Greed", "Envy", "City"]),
    Hero("Pangolier", ["Greed", "Lust", "City"]),
    Hero("Riki", ["Greed", "Envy", "Mischief"]),
    Hero("Templar Assasin", ["Greed", "Discipline", "Desert"]),
    Hero("Warlock", ["Greed", "City", "Desert"]),
    Hero("Winter Wyvern", ["Greed", "Tundra", "Tundra"]),

    Hero("Silencer", ["Envy", "Envy", "Envy"]),
    Hero("Death Prophet", ["Envy", "Envy", "Wrath"]),
    Hero("Drow Ranger", ["Envy", "Envy", "Forest"]),
    Hero("Arc Warden", ["Envy", "Discipline", "Mountain"]),
    Hero("Faceless Void", ["Envy", "Wrath", "Cosmos"]),
    Hero("Huskar", ["Envy", "Wrath", "Lust"]),
    Hero("Jakiro", ["Envy", "Mountain", "Tundra"]),
    Hero("Morphling", ["Envy", "Sea", "Cosmos"]),
    Hero("Outworld Destroyer", ["Envy", "Wrath", "Cosmos"]),
    Hero("Shadow Demon", ["Envy", "Wrath", "Wrath"]),
    Hero("Terrorblade", ["Envy", "Discipline", "Discipline"]),
    Hero("Weaver", ["Envy", "Cosmos", "Cosmos"]),

    Hero("Grimstroke", ["Wrath", "Wrath", "Love"]),
    Hero("Muerta", ["Wrath", "Wrath", "Discipline"]),
    Hero("Troll Warlord", ["Wrath", "Wrath", "Cave"]),
    Hero("Anti-Mage", ["Wrath", "Mountain", "Discipline"]),
    Hero("Bristleback", ["Wrath", "City", "Tundra"]),
    Hero("Chaos Knight", ["Wrath", "Cosmos", "Cosmos"]),
    Hero("Clinkz", ["Wrath", "Discipline", "Forest"]),
    Hero("Lion", ["Wrath", "Plains", "Cave"]),
    Hero("Lycan", ["Wrath", "City", "Cave"]),
    Hero("Ringmaster", ["Wrath", "Mischief", "City"]),
    Hero("Skywrath Mage", ["Wrath", "Love", "Sky"]),
    Hero("Slardar", ["Wrath", "Sea", "Sea"]),
    Hero("Spectre", ["Wrath", "Discipline", "Cosmos"]),
    Hero("Sven", ["Wrath", "Discipline", "Sea"]),

    Hero("Queen of Pain", ["Lust", "Lust", "Lust"]),
    Hero("Zeus", ["Lust", "Lust", "Sky"]),
    Hero("Broodmother", ["Lust", "Cave", "Cave"]),
    Hero("Legion Commander", ["Lust", "City", "Desert"]),
    Hero("Snapfire", ["Lust", "Plains", "Desert"]),

    Hero("Visage", ["Discipline", "Discipline", "Cave"]),
    Hero("Abaddon", ["Discipline", "City", "Tundra"]),
    Hero("Beastmaster", ["Discipline", "Love", "Forest"]),
    Hero("Dark Seer", ["Discipline", "Cave", "Cosmos"]),
    Hero("Disruptor", ["Discipline", "Plains", "Plains"]),
    Hero("Dragon Knight", ["Discipline", "Love", "Sky"]),
    Hero("Earth Spirit", ["Discipline", "Cave", "Cave"]),
    Hero("Ember Spirit", ["Discipline", "Mountain", "Cosmos"]),
    Hero("Kez", ["Discipline", "Mischief", "City"]),
    Hero("Lone Druid", ["Discipline", "Cave", "Forest"]),
    Hero("Void Spirit", ["Discipline", "Cosmos", "Cosmos"]),

    Hero("Chen", ["Love", "Love", "Desert"]),
    Hero("Enchantress", ["Love", "Love", "Forest"]),
    Hero("Batrider", ["Love", "Mischief", "Sky"]),
    Hero("Dawnbreaker", ["Love", "Sky", "Cosmos"]),
    Hero("Hoodwink", ["Love", "Mischief", "Forest"]),
    Hero("Io", ["Love", "Cosmos", "Cosmos"]),
    Hero("Nature's Prophet", ["Love", "Forest", "Forest"]),
    Hero("Nyx Assassin", ["Love", "Cave", "Cave"]),
    Hero("Puck", ["Love", "Mischief", "Cave"]),

    Hero("Dark Willow", ["Mischief", "Mischief", "Mischief"]),

    Hero("Earthshaker", ["Mountain", "Mountain", "Mountain"]),

    Hero("Timbersaw", ["City", "City", "Forest"]),

    Hero("Sand King", ["Desert", "Desert", "Desert"]),

    Hero("Phoenix", ["Sky", "Sky", "Cosmos"]),

    Hero("Enigma", ["Cosmos", "Cosmos", "Cosmos"]),

    
    

    
]
