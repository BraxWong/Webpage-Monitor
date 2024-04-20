class UnusualToCodeMode:
    def __init__(self):
        self.map = {
            "Community Sparkle": 4,
            "Holy Glow": 5,
            "Green Confetti": 6,
            "Purple Confetti": 7,
            "Haunted Ghosts": 8,
            "Green Energy": 9,
            "Purple Energy": 10,
            "Circling TF Logo": 11,
            "Massed Flies": 12,
            "Burning Flames":13,
            "Scorching Flames": 14,
            "Searing Plasma": 15,
            "Vivid Plasma": 16,
            "Sunbeams": 17,
            "Circling Peace Sign": 18,
            "Circling Heart": 19,
            "Stormy Storm": 29,
            "Blizzardy Storm": 30,
            "Nuts n' Bolts": 31,
            "Orbiting Planets": 32,
            "Orbiting Fire": 33,
            "Bubbling": 34,
            "Smoking": 35,
            "Steaming": 36,
            "Flaming Lantern": 37,
            "Cloudy Moon": 38,
            "Cauldron Bubbles": 39,
            "Eerie Orbiting Fire": 40,
            "Knifestorm": 43,
            "Misty Skull": 44,
            "Harvest Moon": 45,
            "It's A Secret To Everybody": 46,
            "Stormy 13th Hour": 47,
            "Kill-a-Watt": 56,
            "Terror-Watt": 57,
            "Cloud 9": 58,
            "Aces High": 59,
            "Dead Presidents": 60,
            "Miami Nights": 61,
            "Disco Beat Down": 62,
            "Phosphorous": 63,
            "Sulphurous": 64,
            "Memory Leak": 65,
            "Overclocked": 66,
            "Electrostatic": 67,
            "Power Surge": 68,
            "Anti-Freeze": 69,
            "Time Warp": 70,
            "Green Black Hole": 71,
            "Roboactive":72,
            "Arcana": 73,
            "Spellbound": 74,
            "Chiroptera Venenata": 75,
            "Poisoned Shadows": 76,
            "Something Burning This Way Comes": 77,
            "Hellfire": 78,
            "Darkblaze": 79,
            "Demonflame": 80,
            "Bonzo The All-Gnawing": 81,
            "Amaranthine": 82,
            "Stare From Beyond": 83,
            "THe Ooze": 84,
            "Ghastly Ghosts Jr": 85,
            "Haunted Phantasm Jr": 86,
            "Frostbite": 87,
            "Molten Mallard": 88,
            "Morning Glory": 89,
            "Death at Dusk": 90,
            "Abduction": 91,
            "Atomic": 92,
            "Subatomic": 93,
            "Electric Hat Protector": 94,
            "Magnetic Hat Protector": 95,
            "Voltaic Hat Protector": 96,
            "Galactic Codex": 97,
            "Ancient Codex": 98,
            "Nebula": 99,
            "Death by Disco": 100,
            "It's a mystery to everyone": 101,
            "It's a puzzle to me": 102,
            "Ether Trail": 103,
            "Nether Trail": 104,
            "Ancient Eldritch": 105,
            "Eldritch Flame": 106,
            "Neutron Star": 107,
            "Tesla Coil": 108,
            "Starstorm Insomnia": 109,
            "Starstorm Slumber": 110,
            "Brain Drain": 111,
            "Open Mind": 112,
            "Head of Steam": 113,
            "Galactic Gateway": 114,
            "The Eldritch Opening": 115,
            "The Dark Doorway": 116,
            "Ring of Fire": 117,
            "Vicious Circle": 118,
            "White Lightning": 119,
            "Omniscient Orb": 120,
            "Clairvoyance": 121,
            "Fifth Dimension": 122,
            "Vicious Vortex": 123,
            "Menacing Miasma": 124,
            "Abyssal Aura": 125,
            "Wicked Wood": 126,
            "Ghastly Grove": 127,
            "Mystical Medley": 128,
            "Ethereal Essence": 129,
            "Twisted Radiance": 130,
            "Violet Vortex": 131,
            "Verdant Vortex": 132,
            "Valiant Vortex": 133,
            "Sparkling Lights": 134,
            "Frozen Icefall": 135,
            "Fragmented Gluons": 136,
            "Fragmented Quarks": 137,
            "Fragmented Photons": 138,
            "Defragmenting Reality": 139,
            "Fragmenting Reality": 140,
            "Refragmenting Reality": 142,
            "Snowfallen": 143,
            "Snowblinded": 144,
            "Pyroland Daydream": 145,
            "Verdatica Horrific": 147,
            "Aromatica": 148,
            "Chromatica": 149,
            "Prismatica": 150,
            "Bee Swarm": 151,
            "Frisky Fireflies": 152,
            "Smoldering Spirits": 153,
            "Wandering Wisps": 154,
            "Kaleidoscope": 155,
            "Green Giggler": 156,
            "Laugh-O-Lantern": 157,
            "Plum Prankster": 158,
            "Pyroland Nightmare": 159,
            "Gravelly Ghoul": 160,
            "Vexed Volcanics": 161,
            "Gourdian Angel": 162,
            "Pumpkin Party": 163,
            "Frozen Fractals": 164,
            "Lavender Landfall": 165,
            "Special Snowfall": 166,
            "Divine Desire": 167,
            "Distant Dream": 168,
            "Violent Wintertide": 169,
            "Blighted Snowstorm": 170,
            "Pale Nimbus": 171,
            "Genus Plasmos": 172,
            "Serenus Lumen": 173,
            "Ventum Maris": 174,
            "Mirthful Mistletoe": 175,
            "Resonation": 177,
            "Aggradation": 178,
            "Lucidation": 179,
            "Stunning": 180,
            "Ardentum Saturnalis": 181,
            "Fragrancium Elementalis": 182,
            "Reverium Irregularis": 183,
            "Perennial Petals": 185,
            "Flavorsome Sunset": 186,
            "Raspberry Bloom": 187,
            "Iridescence": 188,
            "Tempered Thorns": 189,
            "Devilish Diablo": 190,
            "Severed Serration": 191,
            "Shrieking Shades": 192,
            "Restless Wraiths": 193,
            "Infernal Wraith": 195,
            "Phantom Crown": 196,
            "Ancient Specter": 197,
            "Viridescent Peeper": 198,
            "Eyes of Molten": 199,
            "Ominous Stare": 200,
            "Pumpkin Moon": 201,
            "Frantic Spooker": 202,
            "Frightened Poltergeist": 203,
            "Energetic Haunter": 204,
            "Smissmas Tree": 205,
            "Hospitable Festivity": 206,
            "Condescending Embrace": 207,
            "Sparkling Spruce": 209,
            "Glittering Juniper": 210,
            "Prismatic Pine": 211,
            "Spiraling Lights": 212,
            "Twisting Lights": 213,
            "Stardust Pathway": 214,
            "Flurry Rush": 215,
            "Spark of Smissmas": 216,
            "Polar Forecast": 218,
            "Shining Stag": 219,
            "Holiday Horns": 220,
            "Ardent Antlers": 221,
            "Festive Lights": 223,
            "Crustacean Sensation": 224,
            "Frosted Decadence": 226,
            "Sprinkled Delights": 228,
            "Terrestrial Favor": 229,
            "Tropical Thrill": 230,
            "Flourishing Passion": 231,
            "Dazzling Fireworks": 232,
            "Blazing Fireworks": 233,
            "Shimmering Fireworks": 234,
            "Twinkling Fireworks": 235,
            "Sparkling Fireworks": 236,
            "Glowing Fireworks": 237,
            "Glimmering Fireworks": 238,
            "Flying Lights": 239, 
            "Limelight": 241,
            "Shining Star": 242,
            "Cold Cosmos": 243,
            "Refracting Fractals": 244,
            "Startrance": 245,
            "Starlush": 247,
            "Starfire": 248,
            "Stardust": 249,
            "Contagious Eruption": 250,
            "Daydream Eruption": 251,
            "Volcanic Eruption": 252,
            "Divine Sunlight": 253,
            "Audiophile": 254,
            "Soundwave": 255,
            "Synesthesia": 256,
            "Haunted Kraken": 257,
            "Eerie Kraken": 258,
            "Soulful Slice": 259,
            "Horsemann's Hack": 260,
            "Haunted Forever!": 261,
            "Forever And Forever!": 263,
            "Cursed Forever!": 264,
            "Moth Plague": 265,
            "Malevolent Monoculi": 266,
            "Haunted Wick": 267,
            "Wicked Wick": 269,
            "Spectral Wick": 270,
            "Musical Maelstrom": 271,
            "Verdant Virtuoso": 272,
            "Silver Serenade": 273,
            "Cosmic Constellations": 274,
            "Dazzling Constellations": 276,
            "Tainted Frost": 277,
            "Starlight Haze": 278,
            "Hard Carry": 279,
            "Jellyfish Field": 281,
            "Jellyfish Hunter": 283,
            "Jellyfish Jam": 284,
            "Global Clusters": 285,
            "Celestial Starburst": 286,
            "Sylicone Succiduous": 287,
            "Sakura Smoke Bomb": 288,
            "Treasure Trove": 289,
            "Bubble Breeze": 290,
            "Fireflies": 291,
            "Mountain Halo": 292,
            "Celestial Summit": 293,
            "Stellar Ascent": 294,
            "Sapped": 295,
            "Hellspawned Horns": 297,
            "Demonic Impaler": 299,
            "Revenant's Rack": 300,
            "Sixth Sense": 301,
            "Amygdala": 303,
            "The Bone Zone": 304,
            "Arachne's Web": 305,
            "Acidic Climate": 306,
            "Otherworldly Weather": 307,
            "Nightmarish Storm": 308,
            "Icestruck": 309,
            "Goldstruck": 311,
            "Radiant Rivalry": 312,
            "Radiant Legacy": 314,
            "Mint Frost": 317,
            "North Star": 318,
            "Prettiest Star": 320,
            "Festive Falling Star": 321,
            "Lunar Lights": 322,
            "Fairy Lights": 324,
            "Natural Lights": 325,
            ""
        }
