# coding: UTF-8

import pretty_midi
import Node
import Chord
import Bar

chord_name_a = "A" 
chord_name_ac = "A/C#" #暫定Aと同じ
chord_name_bm = "Bm" 
chord_name_c = "C" 
chord_name_cc = "C#" 
chord_name_d = "D" 
chord_name_df = "D/F#" #暫定Dと同じ
chord_name_em = "Em" 
chord_name_fm = "F#m" 
chord_name_g = "G" 
chord_name_gm = "Gm" 

# さび〜
chord_list = [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_g, chord_name_a, chord_name_d, chord_name_d]
chord_list += [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_em, chord_name_a, chord_name_d, chord_name_d]

# A〜
chord_list += [chord_name_d, chord_name_g, chord_name_a, chord_name_d]
chord_list += [chord_name_g, chord_name_df, chord_name_em, chord_name_a]
chord_list += [chord_name_d, chord_name_g, chord_name_a, chord_name_bm]
chord_list += [chord_name_g, chord_name_a, chord_name_d, chord_name_d]

# B〜
chord_list += [chord_name_g, chord_name_g, chord_name_a, chord_name_a]
chord_list += [chord_name_fm, chord_name_fm, chord_name_bm, chord_name_d]
chord_list += [chord_name_em, chord_name_em, chord_name_gm, chord_name_gm]
chord_list += [chord_name_a, chord_name_a, chord_name_a, chord_name_a]
chord_list += [chord_name_a, chord_name_a, chord_name_a, chord_name_a]
chord_list += [chord_name_a, chord_name_a, chord_name_a, chord_name_a]

# さび〜
chord_list += [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_g, chord_name_a, chord_name_d, chord_name_d]
chord_list += [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_em, chord_name_a, chord_name_d, chord_name_d]
# さび〜
chord_list += [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_g, chord_name_a, chord_name_d, chord_name_d]
chord_list += [chord_name_g, chord_name_a, chord_name_fm, chord_name_bm]
chord_list += [chord_name_em, chord_name_a, chord_name_d, chord_name_d]

tempo = 200.0
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)
music_program = pretty_midi.instrument_name_to_program('Vibraphone')
chord_program = pretty_midi.instrument_name_to_program('Marimba')
music_part = pretty_midi.Instrument(program=music_program)
chord_part = pretty_midi.Instrument(program=chord_program)

## 本番
# now_pos: 16分音符何個分の位置にいるか
now_pos = 0
for chord_s in chord_list:
	chord = Chord.Chord(chord_s)
	# 主旋律
	bar = Bar.Bar(chord, tempo, now_pos)
	nodes = bar.Nodes
	for node in nodes:
		note = node.note
		music_part.notes.append(note)
	# コードの貼り付け
	for pitch_int in chord.pitch_ints:
		node = Node.Node(16, pitch_int, now_pos, tempo)
		note = node.note
		chord_part.notes.append(note)
	# 共通
	now_pos += 16


# コードだけ
# for chord_s in chord_list:
# 	chord = Chord.Chord(chord_s)
# 	for pitch_int in chord.pitch_ints:
# 		note = pretty_midi.Note(velocity=100, pitch=pitch_int, start=s, end=s+l)
# 		chord_part.notes.append(note)
# 	s+=l

midi.instruments.append(music_part)
midi.instruments.append(chord_part)
midi.write('../music/chord_test.mid')



