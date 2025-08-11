"""
Author       : FYWinds i@windis.cn
Date         : 2024-03-08 15:30:39
LastEditors  : FYWinds i@windis.cn
LastEditTime : 2024-03-08 15:56:11
FilePath     : /tests/test_item.py
"""

from wynntilsresolver.blocks import End, GearItem, Identification, Identifications, Name, Powder, Reroll, Shiny, Version
from wynntilsresolver.item import GearItemResolver


def test_decoding_item():
    # shiny_warp = "󰀀󰄀󰉗󶅲󷀀󰌉󰀘󵜢󴵅󶈑󴝑󷐙󵀄󶸥󵠦󶠄󰌃󿞼󰘄󸨁􏿮"
    shiny_warp_v2 = "󰀁󰄀󰉗󶅲󷀀󰌉󰄁󲤲󴖴󰅚󱅤󷼢󵥔󱢏󰍕󱦯󰥌󱜻󵘄󱹀󵇨󰉧󲛖󰑱󰐃󰏷󻰅󰈆󰄁󰃿"

    # sw = GearItemResolver.from_utf16(shiny_warp)
    sw2 = GearItemResolver.from_utf16(shiny_warp_v2)

    assert GearItemResolver._attrs == {
        "start": Version,
        "item_type": GearItem,
        "_name": Name,
        "_identifications": Identifications,
        "powder": Powder,
        "shiny": Shiny,
        "_reroll": Reroll,
        "end": End,
    }

    # Test shiny warp
    # assert sw.name == "Warp"
    # assert sw.identifications
    # assert sw.identifications == [
    #     Identification(id="rawAgility", internal_id=41, base=20, roll=-1, value=20),
    #     Identification(id="healthRegen", internal_id=24, base=-200, roll=87, value=-174),
    #     Identification(id="manaRegen", internal_id=34, base=-45, roll=77, value=-35),
    #     Identification(id="reflection", internal_id=69, base=90, roll=98, value=88),
    #     Identification(id="exploding", internal_id=17, base=50, roll=71, value=36),
    #     Identification(id="walkSpeed", internal_id=81, base=180, roll=116, value=209),
    #     Identification(id="healthRegenRaw", internal_id=25, base=-600, roll=80, value=-480),
    #     Identification(id="airDamage", internal_id=4, base=15, roll=110, value=16),
    #     Identification(id="raw1stSpellCost", internal_id=37, base=4, roll=88, value=4),
    #     Identification(id="raw2ndSpellCost", internal_id=38, base=-299, roll=104, value=-311),
    # ]
    # assert sw.powder
    # assert sw.powder.powder_slots == 3
    # assert sw.powder.powders == ["A6", "A6", "A6"]
    # assert sw.shiny
    # assert sw.shiny.name == "warsWon"
    # assert sw.shiny.value == 69
    # assert sw.shiny.display_name == "Wars Won"
    # assert sw.shiny.internal_id == 4
    # assert sw.reroll == 0

    # Test shiny warp v2
    assert sw2.name == "Warp"
    assert sw2.identifications
    assert sw2.identifications == [
        Identification(id="rawAgility", internal_id=41, base=25, roll=-1, value=25),
        Identification(id="reflection", internal_id=69, base=90, roll=90, value=81),
        Identification(id="exploding", internal_id=17, base=50, roll=127, value=64),
        Identification(id="manaRegen", internal_id=34, base=-45, roll=84, value=-38),
        Identification(id="healthRegen", internal_id=24, base=-200, roll=85, value=-170),
        Identification(id="healthRegenRaw", internal_id=25, base=-600, roll=76, value=-456),
        Identification(id="healingEfficiency", internal_id=23, base=-30, roll=86, value=-26),
        Identification(id="airDamage", internal_id=4, base=15, roll=64, value=10),
        Identification(id="walkSpeed", internal_id=81, base=180, roll=103, value=185),
        Identification(id="raw2ndSpellCost", internal_id=38, base=299, roll=113, value=338),
    ]
    assert sw2.powder
    assert sw2.powder.powder_slots == 3
    assert sw2.powder.powders == ["A6", "A6", "A6"]
    assert sw2.shiny
    assert sw2.shiny.name == "mobsKilled"
    assert sw2.shiny.value == 0
    assert sw2.shiny.display_name == "Mobs Killed"
    assert sw2.shiny.internal_id == 1
    assert sw2.reroll == 2
