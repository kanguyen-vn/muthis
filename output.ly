#(set! paper-alist (cons '("snippet" . (cons (* 190 mm) (* 70 mm))) paper-alist))
\paper {
    #(set-paper-size "snippet")
    indent = 0
    tagline = ##f
}

\version "2.20.0"

\pointAndClickTypes #'note-event
I = \once \override NoteColumn.ignore-collision = ##t

staffPiano = \new PianoStaff {
    \set Score.timing = ##f
    \set PianoStaff.followVoice = ##t
    <<
        \new Staff = "RH" {
            \clef treble
            \key fis \minor
            \mergeDifferentlyHeadedOn
            <<
                {
                    \hide Stem
                    \override Stem.length = #0
                    s4 gis'4 fis'4 b'4 cis''4 b'4 e''4 d''4 cis''4 b'4 ais'4 cis''4 d''4 cis''4 b'4 a'4 s4 s4 s4
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \hide Stem
                    \override Stem.length = #0
                    a'2 s2 s2 s2 s2 s2 s2 s2 gis'2
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \hide Stem
                    \override Stem.length = #0
                    s4 s2 s2 s2 s2 s2 s2 s2 s2 fis'2
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \override Beam.positions = #'(8 . 8)
                    \stemUp
                    \override NoteHead.duration-log = #1
                    \hide NoteHead
                    \I a'8[ s8 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 \I gis'8 s8 \I fis'8] s8 
                    \revert Beam.positions
                    \undo \hide NoteHead
                    \revert NoteHead.duration-log
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I a'4 \I gis'4_(\I fis'4) \I b'4 \I cis''4_(\I b'4) \I e''4 \I d''4_(\I cis''4) \I b'4_(\I ais'4)_(\I cis''4) \I d''4 \I cis''4_(\I b'4)_(\I a'4) \I gis'4 \I fis'4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I a'4^(\I gis'4 \I fis'4) \I b'4^(\I cis''4 \I b'4) \I e''4^(\I d''4 \I cis''4)^(\I b'4 \I ais'4) \I cis''4 \I d''4 \I cis''4 \I b'4 \I a'4 \I gis'4 \I fis'4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I a'4 \I gis'4 \I fis'4 \I b'4 \I cis''4 \I b'4 \I e''4^(\I d''4 \I cis''4 \I b'4 \I ais'4 \I cis''4 \I d''4) \I cis''4 \I b'4 \I a'4 \I gis'4 \I fis'4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                     s4 s4 s4 s4 s4 s4
                    \stemDown
                    \I e''8[ s8 s4 s4 s4
                    \stemUp
                    \I ais'8] s8 s4
                    \stemDown
                    \I d''8[ s8 s4
                    \stemUp
                    \I b'8] s8 s4 s4 s4
                }
                \\
                {
                    s4 s4 s4 
                    \stemUp
                    \I b'8 s8s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 
                    \stemUp
                    \I b'8 s8s4 s4 s4 
                }
            >>
            \bar "|."
        }
        \new Staff = "LH" {
            \clef bass
            \key fis \minor
            \mergeDifferentlyHeadedOn
            <<
                {
                    \hide Stem
                    \override Stem.length = #0
                    s4 cis4 fis,4 dis4 e4 d4 cis4 fis4 e4 d4 cis4 fis,4 b,4 fis,4 b,4 s4 s4 s4 s4
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \hide Stem
                    \override Stem.length = #0
                    fis,2 s2 s2 s2 s2 s2 s2 s2 s2
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \hide Stem
                    \override Stem.length = #0
                    s4 s2 s2 s2 s2 s2 s2 s2 cis2 fis,2
                    \undo \hide Stem
                    \revert Stem.length
                }
                \\
                {
                    \override Beam.positions = #'(-8 . -8)
                    \stemDown
                    \override NoteHead.duration-log = #1
                    \hide NoteHead
                    \I fis,8[ s8 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 s4 \I cis8 s8 s4 \I fis,8] s8 
                    \revert Beam.positions
                    \undo \hide NoteHead
                    \revert NoteHead.duration-log
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I fis,4 \I cis4_(\I fis,4) \I dis4_(\I e4) \I d4_(\I cis4) \I fis4_(\I e4) \I d4_(\I cis4)_(\I fis,4) \I b,4 \I fis,4_(\I b,4) \I cis4 \I s4 \I fis,4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I fis,4^(\I cis4 \I fis,4) \I dis4 \I e4^(\I d4 \I cis4) \I fis4 \I e4^(\I d4 \I cis4) \I fis,4 \I b,4^(\I fis,4 \I b,4) \I cis4 \I s4 \I fis,4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                    \hide Stem
                    \hide NoteHead
                    \override Stem.length = #2
                    \I fis,4 \I cis4 \I fis,4 \I dis4 \I e4 \I d4 \I cis4_(\I fis4 \I e4 \I d4 \I cis4) \I fis,4 \I b,4 \I fis,4 \I b,4 \I cis4 \I s4 \I fis,4 
                    \revert Stem.length
                    \undo \hide NoteHead\undo \hide Stem
                }
                \\
                {
                    s4 s4 s4 s4 s4 s4 
                    \stemDown
                    \I cis4 s4 s4 s4 s4 s4 
                    \stemDown
                    \I b,4 s4 s4 s4 s4 s4 
                }
            >>
            \bar "|."
        }
    >>
}

\score {
<< \staffPiano >>
    \layout {
        indent = 0.0
        ragged-right = ##t
        \context {
            \Staff \remove "Time_signature_engraver"
        }
    }
}
