from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey

#from serpent.machine_learning.reinforcement_learning.agents.ppo_agent import PPOAgent

import os
import time


class SerpentMeltyBloodTypeLuminaGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        self.input_controller.tap_key(KeyboardKey.KEY_J)
        time.sleep(2)
        self.input_controller.tap_key(KeyboardKey.KEY_J)

        time.sleep(2)

        self.input_controller.tap_key(KeyboardKey.KEY_DOWN)
        self.input_controller.tap_key(KeyboardKey.KEY_J)
        time.sleep(1)
        self.input_controller.tap_key(KeyboardKey.KEY_J)
        time.sleep(1)
        self.input_controller.tap_key(KeyboardKey.KEY_J)

        time.sleep(1)

        self.input_controller.tap_key(KeyboardKey.KEY_A)
        self.input_controller.tap_key(KeyboardKey.KEY_RIGHT)
        self.input_controller.tap_key(KeyboardKey.KEY_J)
        self.input_controller.tap_key(KeyboardKey.KEY_NUMPAD_4)

        time.sleep(4)

        self.game.randomize_char(1)
        self.game.randomize_char(2)

        self.input_controller.tap_key(KeyboardKey.KEY_J)
        self.input_controller.tap_key(KeyboardKey.KEY_NUMPAD_4)

        self.game.randomize_color(1)
        self.game.randomize_color(2)

    def handle_play(self, game_frame):

        p1_mem, p2_mem = self.game.pull_memory()
        os.system('cls')
        print(str(p1_mem['score']) + " - " + str(p2_mem['score']))
        print(p1_mem)
        print(p2_mem)

        '''for i, game_frame in enumerate(self.game_frame_buffer.frames):
            self.visual_debugger.store_image_data(
                game_frame.frame,
                game_frame.frame.shape,
                str(i)
            )'''

        #self.input_controller.tap_key(KeyboardKey.KEY_DOWN)
