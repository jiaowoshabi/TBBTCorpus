#!/usr/bin/python3

import json
from collections import namedtuple

corpus = {}
DialogUtterance = namedtuple("DialogUtterance",("Speaker","Words","Recipients","Scene","Topics","Act_Tag"))

def loadCorpus(loadfile):
	global corpus
	with open(loadfile,"r") as corpus_file:
		corpus = json.load(corpus_file)
		corpus_file.close()
	return corpus
	
def getNextTurn(season,episode):
	global corpus
	key = str(season)+"_"+str(episode)
	info = corpus[key]
	turns = []
	for scene in info:
		for turn in scene["Turns"]:
			yield __dictToDialogUtterance(turn)

def __dictToDialogUtterance(dialog):
	return DialogUtterance(**dialog)


