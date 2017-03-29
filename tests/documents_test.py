import unittest
from pentets.documents import *

class DocumentsTest(unittest.TestCase):
    def test_load_info(self):
        info = yaml.load("""\
--- !Info
name: perdu
website: https://perdu.com/
resources: https://perdu.org/
""")

        self.assertEqual("perdu", info.name)
        self.assertEqual("https://perdu.com/", info.website)
        self.assertEqual("https://perdu.org/", info.resources)

    def test_load_passive(self):
        passive = yaml.load("""\
--- !Passive
regexes:
- /yolo/
- /patate/i
""")

        self.assertEqual(["/yolo/", "/patate/i"], passive.regexes)
        self.assertEqual(2, passive.count())
        self.assertEqual(["/yolo/", "/patate/i"], list(passive))

    def test_passive_defaults(self):
        self.assertEqual([], Passive.regexes)

    def test_load_active(self):
        active = yaml.load("""\
--- !Active
entries:
  - path: /readme.html
    desc: patatepress Version
    regex: <br /> Version ([0-9.]+)
""")

        # self.assertEqual("/readme.html", active[0].path)
        # self.assertEqual("patatepress Version", active[0].desc)
        # self.assertEqual("<br /> Version ([0-9.]+)", active[0].regex)
        pass

    def test_active_defaults(self):
        self.assertEqual([], Active.entries)

    def load_document(self):
        pass

    def load_documents(self):
        pass
