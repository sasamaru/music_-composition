# coding: UTF-8

import pretty_midi

class Chord:
	# 'Dm'などを引数にもち、
	#・コードの持つ音程intの配列を返す
	#・コードの許容する音程intの配列を返す
	#・コードはC3~B4で構成
	# 参考サイト http://www.gakki.me/code_p.html#p_codeA
	# 主旋律は C4~C5~C6~G6(60)~(91)
	# self.pitch_strings : コードの文字
    # self.pitch_ints : それをintにしたやつ
    # self.permit_pitch_ints : コードの許容する音程intの配列
	def __init__(self, chord_name):
		if chord_name == "A":
			self.pitch_strings = ["A3", "C#4", "E4"]
			self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
			self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "A/C#":#暫定Aと同じ
			self.pitch_strings = ["A3", "C#4", "E4"]
			self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
			self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "Bm":
		    self.pitch_strings = ["B3", "D4", "F#4"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "C":
		    self.pitch_strings = ["C3", "E3", "G3"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "C#":
		    self.pitch_strings = ["C#3", "F3", "G#3"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "D":
		    self.pitch_strings = ["D3", "F#3", "A3"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "D/F#":#暫定Dと同じ
		    self.pitch_strings = ["D3", "F#3", "A3"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "Em":
		    self.pitch_strings = ["E3", "G3", "B3"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "F#m":
		    self.pitch_strings = ["F#3", "A3", "C#4"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "G":
		    self.pitch_strings = ["G3", "B3", "D4"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		elif chord_name == "Gm":
		    self.pitch_strings = ["G#3", "A4", "D#4"]
		    self.pitch_ints = self.pitchlist_to_int(self.pitch_strings)
		    self.permit_pitch_ints = self.permit_int_pitchlist(self.pitch_ints)
		else:
			self.pitch_strings = []
			self.pitch_ints = []
			self.permit_pitch_ints = []


	def pitchlist_to_int(self, pitch_strings):
		pitch_int_list = []
		for pitch_string in pitch_strings:
			note_int = pretty_midi.note_name_to_number(pitch_string)
			pitch_int_list.append(note_int)
		return pitch_int_list

	def permit_int_pitchlist(self, pitch_ints):
		pitch_int_list = []
		for pitch_int in pitch_ints:
			i = pitch_int - 12
			while i >= 60:
				pitch_int_list.append(i)
				i -= 12
			j = pitch_int + 12
			while j <= 91:
				pitch_int_list.append(j)
				j += 12
			pitch_int_list.append(pitch_int)
		return pitch_int_list

	# # コードの持つ音程をint配列で返す
	# def getPitches(self):
	# 	pass
	# # コード上に問題なく乗れる主旋律の音程をint配列で返す
	# def getPermitPitches(self):
	# 	pass
