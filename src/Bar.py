# coding: UTF-8

import pretty_midi
import random
import Node
import Chord

class Bar:
	def __init__(self, chord, tempo, start):
		self.chord = chord
		self.tempo = tempo
		self.Nodes = self.making_main_melody(chord, tempo, start)

	# Node配列を返す chord:コードクラス, tempo
	def making_main_melody(self, chord, tempo, start):
		melodies = []
		leave_length = 16
		prev_pitch_int = chord.pitch_ints[0]
		start_pos = start
		# １６分音符何個分か
		while leave_length>0:
			length = self.making_length()
			length = leave_length if leave_length<length else length
			leave_length -= length
			pitch = self.making_pitchint(chord, prev_pitch_int, length)
			melodies.append(Node.Node(length, pitch, start_pos, tempo))
			prev_pitch_int = pitch
			start_pos += length
		return melodies

	def making_pitchint(self, chord, prev_pitch, length):
		# ## 分類 あとで生データを集めてもいいかもしれない
		# # 16分音符
		# length 1
		# 	|diff| 0~2 : 80%
		# 	|diff| 3~5 : 20%
		# # 8分音符
		# length 2~3
		# 	|diff| 0~2 : 50%
		# 	|diff| 3~5 : 40%
		# 	|diff| 6~8 : 10%
		# # 4分音符
		# length 4~7
		# 	|diff| 0~2 : 25%
		# 	|diff| 3~5 : 25%
		# 	|diff| 6~8 : 25%
		# 	|diff| 9~10 : 25%
		# # 2分音符以上
		# lentth 8~16
		# 	|diff| 0~5 : 20%
		# 	|diff| 6~8 : 30%
		# 	|diff| 9~10 : 30%
		# 	|diff| 11~12 : 20%
		random_int = random.randint(1,20)
		is_plus = random.randint(0,1)==1
		if length<2:
			pitch_diff = random.randint(0,2) if random_int<17 else random.randint(3,5)
		elif length<4:
			if random_int<11:
				pitch_diff = random.randint(0,2)
			elif random_int<19:
				pitch_diff = random.randint(3,5)
			else:
				pitch_diff = random.randint(6,8)
		elif length<8:
			pitch_diff = random.randint(0,10)
		else:
			if random_int<5:
				pitch_diff = random.randint(0,5)
			elif random_int<11:
				pitch_diff = random.randint(6,8)
			elif random_int<17:
				pitch_diff = random.randint(9,10)
			else:
				pitch_diff = random.randint(11,12)
		pitch = prev_pitch+pitch_diff if is_plus else prev_pitch-pitch_diff
		random_int = random.randint(1,20)
		if length*4 + random_int > 20:
			pitch = self.making_pitch_chord(pitch, chord)
		return pitch


	def making_pitch_chord(self, pitch, chord):
		d = 0
		while True:
			if pitch+d in chord.permit_pitch_ints:
				return pitch+d
			elif pitch-d in chord.permit_pitch_ints:
				return pitch-d
			d+=1

	def making_length(self):
		rand_int = random.randint(0,1)
		if rand_int == 0:
			return 2
		else:
			return random.randint(3,4)
		#----------------------------------
		rand_int = random.randint(1,20)
		if rand_int<10:
			return random.randint(1,4)
		elif rand_int < 16:
			return random.randint(5,8)
		else:
			return random.randint(9, 16)





		