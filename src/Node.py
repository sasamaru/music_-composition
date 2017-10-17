# coding: UTF-8

import pretty_midi

class Node:
	# length: 16分音符を1とした時の音符の長さ
	# pitch: 音の高さ 整数
	# start: 曲の開始から16分音符何個目か(4/4拍子では１小節＝四分音符x4＝16分音符x16)
	def __init__(self, length, pitch, start, tempo):
		self.length = length
		self.pitch = pitch
		self.start = start
		self.tempo = tempo
		self.note = pretty_midi.Note(velocity=120, pitch=pitch, start=(start/8), end=((start+length)/8))
		