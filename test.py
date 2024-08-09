from music21 import stream, note, metadata

# 새로운 스트림 생성
s = stream.Stream()

# 멜로디에 사용될 음표와 지속 시간 정의
notes = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4']
durations = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]
lyrics = ['반', '짝', '반', '짝', '작', '은', '별', '아', '름', '답', '게', '비', '치', '네']

# 음표들, 지속 시간, 가사를 스트림에 추가
for n, d, l in zip(notes, durations, lyrics):
    new_note = note.Note(n, quarterLength=d)
    new_note.lyric = l  # 가사 추가
    s.append(new_note)

# 곡의 메타데이터 추가
s.metadata = metadata.Metadata()
s.metadata.title = '반짝반짝 작은 별'
s.metadata.composer = '전통 민요'

# 스트림을 MusicXML로 내보내기
xml_path = "twinkle_twinkle.xml"
s.write('musicxml', fp=xml_path)
