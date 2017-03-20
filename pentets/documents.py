import yaml
import glob
import pdb

class Info(yaml.YAMLObject):
    yaml_tag = u'!Info'

    def __init__(self, name):
        self.name = name
        
class Passive(yaml.YAMLObject):
    yaml_tag = u'!Passive'

    regexes = 0
    
    def __init__(self):
        pass

    def __iter__(self):
        for each in self.regexes:
            yield each

    def count(self):
        return len(self.regexes)
        
class Active(yaml.YAMLObject):
    yaml_tag = u'!Active'

    entries = []
    
    def __init__(self):
        pass

    def __iter__(self):
        for each in self.entries:
            yield each

    def count(self):
        return len(self.entries)


            
def load_document(file):
    return yaml.load_all(open(file,'r'))

def load_documents(search_glob):
    return map(load_document, glob.glob(search_glob))
