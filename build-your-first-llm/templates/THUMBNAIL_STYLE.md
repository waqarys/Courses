# Thumbnail style — Zero to LLM

| Element | Rule |
|---|---|
| Size | 1280×720 PNG/JPG, < 2 MB |
| Background | Grok Imagine "Thumbnail background" prompt from each module's `imagine.md` (dark navy, one cyan glow) |
| Face | your cut-out (CapCut *Remove background* on a still from the CAM take), 45–55 % of height, looking at the text, expressive |
| Text | **max 3 words**, Montserrat ExtraBold 150–190 px, white with 6 px cyan (#22D3EE) outer glow; one word may be amber (#F59E0B) |
| Badge | top-left rounded square "#5" navy with cyan border — series number |
| Keep clear | bottom-right 20 % (YouTube timestamp) |
| Consistency | same face side (right), same fonts, same badge for every module |

Workflow (≈10 min): Imagine background → CapCut new 1280×720 project ("ZTL_THUMB" template with face/text/badge layers) → swap background + face + word → *Export frame* as PNG → `D:\ZeroToLLM\M05\export\M05_thumb.png`.
Quick test: shrink to 25 % — can you still read the word? If not, fewer letters.
Suggested words per module are in `modules/*/imagine.md` (§2).
