label skip_kevin_skip_choice:
    if persistent.playedkevin:#completed kevin's meeting
        $ renpy.pause (0.3)
        play sound "fx/system3.wav"
        call syscheck from skip_kevin_syscheck
        call skiptut from skip_kevin_skiptut
        if skipbeginning == False:
            if system == "normal":
                s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to the hatchery?"
            elif system == "advanced":
                s "It looks like you've seen this before. Skip to the hatchery?"
            else:
                s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the hatchery."
        $ skipbeginning = False
        menu:
            "Yes. I want to skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                play music "mx/elegant.ogg" fadein 1.0
                $ persistent.skipnumber += 1
                call skipcheck from skip_kevin_skipcheck
                scene hatchery at Pan ((0, 0), (0, 180), 3.0) with dissolveslow
                $ renpy.pause (1.3)
                label skip_kevin_skip_yes:
                    pass
            "No. Don't skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
    else:
        pass
    label skip_kevin_skip_no:
        pass