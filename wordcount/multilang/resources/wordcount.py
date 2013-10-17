from collections import defaultdict
import storm

class WordCountBolt(storm.BasicBolt):
    def initialize(self, conf, context):
        self._count = defaultdict(int)

    def process(self, tup):
        word = tup.values[0]
        self._count[word] += 1
        storm.emit([word, self._count[word]])

WordCountBolt().run()
