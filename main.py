from elements.constants import MajorAccidentals, MinorAccidentals, VoiceType, Clef
from elements.score import Score
from elements.staff import Staff
from elements.voice import Voice
from elements.note import Note


def is_valid_key(key, quality):
    return ((quality == "major" or quality == "minor") and
            (key in MajorAccidentals if quality == "major" else key in MinorAccidentals))


# key = input("Key: ").lower()
# quality = input("Quality: ").lower()
# key = "g"
# quality = "major"
# print("Key: g\nQuality: major")
key = "f_sharp"
quality = "minor"
while not is_valid_key(key, quality):
    print(r"Usage: root(_accidental) quality")
    key = input("Key: ").lower()
    quality = input("Quality: ").lower()

# left_input = "g2 a2 b2 c3 d3 e3 f3 g3"
# right_input = "g5 f5 e5 d5 c5 b4 a4 g4"
right_input = "a4 g4 f4 b4 c5 b4 e5 d5 c5 b4 a#4 c5 d5 c5 b4 a4 g4 f4"
left_input = "f2 c3 f2 d#3 e3 d3 c3 f3 e3 d3 c3 f2 b2 f2 b2 c3 skip f2"

left = Voice(
    key=key,
    quality=quality,
    voice_type=VoiceType.MAIN,
    note_input=left_input
)
right = Voice(
    key=key,
    quality=quality,
    voice_type=VoiceType.MAIN,
    note_input=right_input
)
left_staff = Staff(
    name="LH",
    clef=Clef.BASS,
    key=key,
    quality=quality,
    main_voice=left
)
right_staff = Staff(
    name="RH",
    clef=Clef.TREBLE,
    key=key,
    quality=quality,
    main_voice=right
)

score = Score(
    key=key,
    quality=quality,
    staves=[
        right_staff,
        left_staff
    ]
)

three_line = "makeUrlinie1 staffUp makeUrlinie1 left makeUrlinie2 left makeUrlinie3 staffDown left makeUrlinie5 left left left left makeUrlinie1 engrave quit"
three_line_navigate = "makeUrlinie navigateTo[1:4] makeUrlinie navigateTo[1:0] makeUrlinie navigateTo[0:5] makeUrlinie3 right makeUrlinie2 right makeUrlinie1"
slurs_right = "slur[0:0][0:3] slur[0:1][0:2] slur[0:2][0:3] slur[0:3][0:5] slur[0:4][0:5]"
slurs_left = "slur[1:0][1:2] slur[1:1][1:2] slur[1:3][1:4] slur[1:4][1:6] slur[1:5][1:6]"
five_line = "makeUrlinie1 staffUp makeUrlinie1 left makeUrlinie2 left makeUrlinie3 left makeUrlinie4 left makeUrlinie5 staffDown right makeUrlinie5 left left left left makeUrlinie1 engrave quit"
eight_line = "makeUrlinie1 staffUp makeUrlinie1 left makeUrlinie2 left makeUrlinie3 left makeUrlinie4 left makeUrlinie5 left makeUrlinie6 left makeUrlinie7 left makeUrlinie8 staffDown makeUrlinie1 right right right right makeUrlinie5 engrave quit"
example_urlinie = "makeUrlinie navigateTo[1:15] makeUrlinie navigateTo[1:0] makeUrlinie navigateTo[0:0] makeUrlinie navigateTo[0:16] makeUrlinie navigateTo[0:17] makeUrlinie"
example_slurs_l = "[1:0][1:2] [1:1][1:2] [1:3][1:4] [1:4][1:6] [1:5][1:6] [1:6][1:10] [1:7][1:8] [1:8][1:10] [1:9][1:10] [1:10][1:11] [1:12][1:14] [1:13][1:14]"
example_slurs_left = " ".join(
    ["slur" + indices for indices in example_slurs_l.split()])
example_slurs_r = "[0:0][0:2] [0:1][0:2] [0:3][0:5] [0:4][0:5] [0:6][0:12] [0:6][0:8] [0:7][0:8] [0:8][0:10] [0:9][0:10] [0:10][0:11] [0:13][0:14] [0:14][0:15]"
example_slurs_right = " ".join(
    ["slur" + indices for indices in example_slurs_r.split()])
example_unfoldings = "unfolding[0:6][0:10] unfolding[0:12][0:14]"
example_stems = "quarter_stem[1:6] quarter_stem[1:12] eighth_stem[0:3] eighth_stem[0:14]"

# for command in (f"{slurs_right} {slurs_left} {three_line_navigate} engrave quit").split():
for command in f"{example_urlinie} {example_slurs_left} {example_slurs_right} {example_unfoldings} {example_stems} engrave quit".split():
    # for command in f"{example_urlinie} {example_slurs_left} {example_slurs_right} engrave quit".split():
    # while True:
    current_note, current_staff = score.current["note"], score.current["staff"]
    print("Current staff:", current_staff.name)
    print("Current note:", str(current_note))
    if score.slur_from:
        slur_from_note, slur_from_staff = score.slur_from["note"], score.slur_from["staff"]
        print(
            f"Slur starting from: {str(slur_from_note)}\n" +
            f"    index {slur_from_staff.main_voice.index(slur_from_note)} staff {score.staves.index(slur_from_staff)}" +
            "    - Navigate to end of slur and use \"endSlur\" or" +
            "    - Use \"endSlur[staff_index_from_top:note_index_from_left]\""
        )
    all_slurs = []
    for staff in score.staves:
        for note in staff.main_voice.notes:
            for slur in note.slurs:
                if slur not in all_slurs:
                    all_slurs.append(slur)

    if len(all_slurs) > 0:
        print("Slurs:", " ".join([
            f"[{str(slur.before)}:{str(slur.after)}]" for slur in all_slurs])
        )
    #command = input("Enter command: ")
    print("Command:", command, "\n")
    if command == "quit":
        break
    score.cmd(command)
