import sys

import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

def connect(node,next):
    hook=modast.hook_opcode(node,None)
    hook.chain(next)
    #node.next=next
    #thanks 4onen for explaining this
    """
    node_i_want_to_hook=modast.find_say("Ooh, I do hope what I'm saying now is unique across all time, or I might link the wrong spot!")
    my_hook=modast.hook_opcode(node_i_want_to_hook,None) # makes my_hook the next node, but preserves the old next as an old_next on the my_hook object, as well as making my_hook.next equal to the old next.
    my_hook.chain(modast.find_label('my_unique_mod_label')) # replaces my_hook.next, but leaves my_hook.old_next intact
    """

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Skip Kevin", "v0.1", "joeyjumper94")

    def mod_load(self):
        """
        c4hatchery = modast.find_label("c4hatchery")
        skip_kevin_skip_choice = modast.find_label("skip_kevin_skip_choice")
        hook = modast.hook_opcode(c4hatchery, None)
        #modast.call_hook(c4hatchery, skip_kevin_skip_choice, None)
        """
        #start=modast.find_say("I was on my way to the hatchery when I heard a voice call out to me.")
        c4hatchery=modast.find_label("c4hatchery")
        c4hatchery_next=c4hatchery.next
        skipped=modast.find_say("(Here we are again.)")
        connect(c4hatchery,modast.find_label("skip_kevin_skip_choice"))
        connect(modast.find_label("skip_kevin_skip_no"),c4hatchery_next)
        connect(modast.find_label("skip_kevin_skip_yes"),skipped)

    def mod_complete(self):
        pass
