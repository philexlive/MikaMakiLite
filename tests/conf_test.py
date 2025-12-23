import unittest
import src.config as cfg
import os

class TestConfProvision(unittest.TestCase):
    def test_tgconf_init(self):
        c = cfg.TgConfig("-1003076574670_118")
        self.assertTrue(not c.chat_id is None, msg=f"Chat ID: {c.chat_id}")
        self.assertTrue(c.chat_id[0] == -1003076574670)
        self.assertTrue(c.chat_id[1] == 118)
    
    def test_tgconf_setchat(self):
        c = cfg.TgConfig()
        c.set_chat("-1003076574670_118")
        self.assertIsNotNone(c.chat_id, msg=f"Chat ID: {c.chat_id}")
        self.assertTrue(c.chat_id[0] == -1003076574670)
        self.assertTrue(c.chat_id[1] == 118)
    
    def test_conf_tgconf(self):
        c = cfg.tg_config
        self.assertIsNotNone(c)
        self.assertTrue(c.chat_id[0] == -1003076574670)
        self.assertTrue(c.chat_id[1] == 118)