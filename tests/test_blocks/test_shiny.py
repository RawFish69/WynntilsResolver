def test_shiny_decoding():
    from wynntilsresolver.blocks import Shiny, Version

    assert Shiny.from_bytes([7, 0], parsed_blocks=[Version(0)]) == Shiny(
        name="deaths", internal_id=7, display_name="Deaths", value=0, reroll=0
    )

    assert Shiny.from_bytes([7, 0, 2], parsed_blocks=[Version(1)]) == Shiny(
        name="deaths", internal_id=7, display_name="Deaths", value=0, reroll=2
    )
