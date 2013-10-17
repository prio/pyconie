from random import choice
import storm


class SentenceSpout(storm.Spout):
    sentences = ["a little brown dog", "the man petted the dog",
"four score and seven years ago",
"an apple a day keeps the doctor away"]

    def nextTuple(self):
        storm.emit([choice(self.sentences)])

SentenceSpout().run()
