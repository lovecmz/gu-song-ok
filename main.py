def on_forever():
    music.set_volume(255)
    pins.digital_write_pin(DigitalPin.P1, 1)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.DOUBLE))
basic.forever(on_forever)

def on_in_background():
    while True:
        basic.show_string("HI GUDETAMA")
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
control.in_background(on_in_background)
