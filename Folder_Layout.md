# Folder layout
```
Courses/  (branch python-kids-fast-pipeline)
├─ Fast_Pipeline.md  OBS_Setup.md  Troubleshooting.md  All_Intros_Outros.md  Lessons.md  Folder_Layout.md
├─ Character/Minty_reference.png        attach in Grok Imagine every time
├─ tools/
│  ├─ render_video.py                   the one command
│  ├─ import_images.py                  Imagine downloads -> images/scene_NN
│  ├─ make_lessons.py                   builds lesson folders from slides/notes/code (no overwrite)
│  ├─ prep_video.py                     shared parsers
│  ├─ fonts/Fredoka.ttf
│  └─ kokoro/  (git-ignored)            kokoro-v1.0.onnx + voices-v1.0.bin
├─ lessons/01_Hello_World/
│  ├─ Script.md          AI narration per scene (Kokoro reads it)
│  ├─ Segments.txt       order: explain / code / yourturn / quiz
│  ├─ Visual_Prompts.md  Imagine prompts (🎬 = good as a video clip)
│  ├─ Live_Coding.md     what you type and say, expected output, deliberate mistakes
│  ├─ Challenge.md       Your-turn text
│  ├─ Intro_Outro.md     ≈10 s intro + outro lines (you or AI voice)
│  ├─ YouTube.md         title, description, tags, settings
│  ├─ images/   YOU: scene_01.jpg … (or scene_NN.mp4), thumb_art.jpg
│  ├─ live/     YOU: live_01.mp4 … (+ optional trim.json)
│  ├─ voice/    YOU (optional): intro.m4a, outro.m4a
│  └─ render/   OUTPUT (git-ignored)
├─ slides/ notes/ code/ videos/ studio/   original course material (kept; source for the lessons)
```
