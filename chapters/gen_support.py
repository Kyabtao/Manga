#!/usr/bin/env python3
"""Generate Hindi translations and cast files for chapters 3-5."""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Character names for cast files
CHARS = {
    "ira-sutar": "Ira Sutar — इरा सुतार (PROTAGONIST)",
    "kessa": "Kessa — केसा",
    "rekhak-vahni": "Rekhak Vahni — रेखक वह्नि",
    "patra": "Patra — पत्र",
    "bhan": "Bhan — भान",
    "lekh": "Lekh — लेख",
    "guthli": "Guthli — गुठली",
    "pira": "Pira — पीरा",
}

# Hindi translations for common dialogue/captions
HINDI = {
    # Ch003
    "The cutter taught my stitch. My stitch taught nobody.": "काटने वाले ने मेरी सिलाई सिखाई। मेरी सिलाई ने किसी को नहीं सिखाया।",
    "She opened the stall before the first bell. I brought the rubbing before the second.": "उसने पहली घंटी से पहले दुकान खोल दी। मैं दूसरी से पहले रगड़ ले आई।",
    "Procedure has two speeds: it files, or it waits.": "प्रक्रिया की दो गतियाँ हैं: या तो दाखिल करती है, या इंतज़ार करती है।",
    "The census requires a custodian of record.": "गणना को अभिलेख के संरक्षक की आवश्यकता है।",
    "I keep what's in the box. I don't sign for why it's there.": "मैं बक्से में जो है वो रखती हूँ। मैं उसके होने के कारण पर दस्तख़त नहीं करती।",
    "Then the box acknowledges nothing and we're all filed.": "तो बक्सा कुछ स्वीकार नहीं करता और हम सब दाखिल हैं।",
    "One link in his chain doesn't move.": "उसकी ज़ंजीर की एक कड़ी नहीं हिलती।",
    "The Office will re-file the slate unsigned.": "कार्यालय पट्ट को बिना दस्तख़त के फिर से दाखिल करेगा।",
    "Then they'll need a bigger drawer.": "तो उन्हें बड़े दराज़ की ज़रूरत होगी।",
    # Ch004
    "Same turn-back. Same angle.": "वही मोड़-सिरा। वही कोण।",
    "Same thread. Same gauge.": "वही धागा। वही माप।",
    "They're not practising. They're teaching.": "वे अभ्यास नहीं कर रहे। वे सिखा रहे हैं।",
    "It doesn't itch.": "यह खुजलाता नहीं।",
    "Four versions. Same school.": "चार संस्करण। वही विद्या।",
    "Don't force it. Don't pull. Let it breathe.": "ज़बरदस्ती मत करो। खींचो मत। साँस लेने दो।",
    "Same thread. Same knot. Sixth piece.": "वही धागा। वही गाँठ। छठा टुकड़ा।",
    "This is the first knot they ever tied.": "यह उनकी बँधी हुई पहली गाँठ है।",
    "Your thread is braided now.": "तुम्हारा धागा अब बुना हुआ है।",
    # Ch005
    "The Spindle's bright.": "तकली चमक रही है।",
    "My palm is warm.": "मेरी हथेली गर्म है।",
    "If it opens, it opens here.": "अगर यह खुलता है, तो यहाँ खुलेगा।",
    "Two strands. One blank.": "दो तंतु। एक खाली।",
    "The blank strand is older than the Sector.": "खाली तंतु क्षेत्र से पुराना है।",
    "How much does that cost you?": "यह तुम्हें कितना पड़ता है?",
    "More than I have. Less than it's worth.": "मेरे पास से ज़्यादा। इसकी कीमत से कम।",
    "Measure.": "नापो।",
    "Manavkin. Braided. Projection. Filed.": "मानवकिण। बुना हुआ। प्रक्षेपण। दाखिल।",
    "Like the Mendery records.": "मेंडरी के अभिलेखों जैसा।",
    "My mother was in the Mendery.": "मेरी माँ मेंडरी में थी।",
    "Come back. The box will wait.": "वापस आना। बक्सा इंतज़ार करेगा।",
    "The girl will come.": "लड़की आएगी।",
}

def make_hindi(src_path):
    """Generate Hindi translation from English script."""
    with open(src_path, encoding="utf-8") as f:
        text = f.read()
    
    # Replace English title/hints with Hindi equivalents
    text = text.replace("**Chapter title:**", "**अध्याय शीर्षक:**")
    text = text.replace("**Page type:**", "**पृष्ठ प्रकार:**")
    text = text.replace("**Canvas:**", "**कैनवास:**")
    text = text.replace("**Arc:** I — The Unspooling", "**खंड:** I — अनुकुलन")
    text = text.replace("**Sector:**", "**क्षेत्र:**")
    
    # Translate dialogue/caption lines
    for eng, hindi in HINDI.items():
        text = text.replace(eng, hindi)
    
    # Replace common terms
    text = text.replace("> **CAPTION (", "> **शीर्षक (")
    text = text.replace("> **IRA (dialogue,", "> **इरा (संवाद,")
    text = text.replace("> **KESSA (dialogue,", "> **केसा (संवाद,")
    text = text.replace("> **REKHAK (dialogue,", "> **रेखक (संवाद,")
    text = text.replace("> **BHAN (dialogue,", "> **भान (संवाद,")
    text = text.replace("> **LEKH (dialogue,", "> **लेख (संवाद,")
    text = text.replace("> **GUTHLI (dialogue,", "> **गुठली (संवाद,")
    text = text.replace("> **PIRA (dialogue,", "> **पीरा (संवाद,")
    text = text.replace("> **STALL-OWNER (dialogue,", "> **दुकानदार (संवाद,")
    text = text.replace("> **GREY CLERK (dialogue,", "> **धूसर लिपिक (संवाद,")
    text = text.replace("> **INSPECTOR (dialogue,", "> **निरीक्षक (संवाद,")
    text = text.replace("> **DOCK WORKER (dialogue,", "> **गोदी मज़दूर (संवाद,")
    text = text.replace("> **SFX:", "> **ध्वनि:")
    text = text.replace("(dialogue,", "(संवाद,")
    
    # Translate section headers
    text = text.replace("## PANEL", "## चित्र-खाना")
    text = text.replace("## Writing & art notes", "## लेखन और चित्र नोट्स")
    text = text.replace("## Card-game hooks", "## कार्ड-गेम हुक")
    text = text.replace("**Camera:**", "**कैमरा:**")
    text = text.replace("**Image:**", "**चित्र:**")
    text = text.replace("**Image continued:**", "**चित्र जारी:**")
    text = text.replace("Beats carried from", "पिछले पृष्ठ से:")
    text = text.replace("Writing & art notes", "लेखन और चित्र नोट्स")
    text = text.replace("Card-game hooks", "कार्ड-गेम हुक")
    
    return text

def make_cast(ch, pg, script_text):
    """Generate cast file content from script."""
    lines = ["# Chapter %s — Page %s Cast\n" % (ch.split("-")[1], pg.split("-")[1]), ""]
    lines.append("Everyone on the page.\n")
    lines.append("---\n")
    
    # Find characters mentioned
    found_chars = []
    for char_id, char_name in CHARS.items():
        if char_name.split(" — ")[0].lower() in script_text.lower() or char_name.split(" — ")[1] in script_text:
            found_chars.append((char_id, char_name))
    
    if not found_chars:
        found_chars.append(("ira-sutar", CHARS["ira-sutar"]))
    
    for char_id, char_name in found_chars:
        lines.append("## %s" % char_name)
        if char_id == "ira-sutar":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/ira-sutar.md`](../../chapter-001/characters/ira-sutar.md)")
        elif char_id == "kessa":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/kessa.md`](../../chapter-001/characters/kessa.md)")
        elif char_id == "rekhak-vahni":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/rekhak-vahni.md`](../../chapter-001/characters/rekhak-vahni.md)")
        lines.append("")
    
    return "\n".join(lines)

def make_glossary(ch):
    """Generate glossary for a chapter."""
    chnum = ch.split("-")[1]
    terms = {
        "chapter-003": [
            ("Cut-end", "कट-सिरा", "The shadowless thread-segment in Kessa's lockbox."),
            ("Hand-school", "हाथ-विद्या", "The grammar of a mending hand."),
            ("Turn-back", "मोड़-सिरा", "The tiny curl at the end of a stitch or cut-stroke."),
            ("Posting order", "स्थानांतरण-आदेश", "Council procedure: formal transfer of custody."),
            ("Diploma", "प्रमाण-पत्र", "Ira's self-assessment: the palm is proof of the hand-school."),
            ("Supply line", "आपूर्ति-मार्ग", "One person operating across forty years with the same thread."),
        ],
        "chapter-004": [
            ("Lesson plan", "पाठ-योजना", "The cutter's nightly demonstrations on Bhan's arm."),
            ("Continuation stitch", "जारी-सिलाई", "The cutter's second line of stitch-grammar, not a copy but a next sentence."),
            ("Whorl-signature", "चक्र-हस्ताक्षर", "The same whorl-knot in every piece of evidence — one hand's fingerprint."),
            ("Child's first knot", "बच्चे की पहली गाँठ", "The kind a Kshudra child ties when learning to thread."),
            ("Braid leak", "बुनाई-रिसाव", "The dormant mark's braid bleeding into Ira's mending thread."),
        ],
        "chapter-005": [
            ("The First Pull", "पहला खिंचाव", "Ira's mark opening and thread emerging for the first time."),
            ("Blank strand", "रिक्त-तंतु", "The sewer's strand: no Sector, no Kind, no debt."),
            ("Compliance chain", "अनुपालन-ज़ंजीर", "The Inspector's measuring tool, distinct from Rekhak's counting-chain."),
            ("Mendery", "मेंडरी", "The workhouse where debt-carriers are bound. Ira's mother was bound there."),
            ("The back-door key", "पिछवाड़े की चाबी", "Kshudra-made key to the Mendery's back door, given by Ira's mother."),
        ],
    }
    
    items = terms.get(ch, [])
    out = ["# Chapter %s — Glossary\n" % chnum, ""]
    out.append("| Term | Devanagari | Meaning |")
    out.append("|---|---|---|")
    for term, dev, meaning in items:
        out.append("| **%s** | %s | %s |" % (term, dev, meaning))
    out.append("")
    return "\n".join(out)

def make_locations(ch):
    """Generate locations for a chapter."""
    chnum = ch.split("-")[1]
    locs = {
        "chapter-003": [
            ("THE KNOT & NAIL (POST-REOPENING)", "गाँठ और कील", "Fully open, loupe down, counter wiped. The lockbox is on the counter for the first time in daylight."),
            ("THE LOCKBOX", "ताला-बक्सा", "First daylight appearance. Kshudra-made, black basalt. Contents grow from one to seven objects."),
            ("THE DOCK-GATE", "गोदी-द्वार", "The inspection desk where Bhan's arm is logged. The slate carries pre-logged lines."),
            ("THE COUNCIL STAIR (FOOT)", "परिषद-सीढ़ी", "The threshold between basin and terraces. The fifth thread appears here."),
        ],
        "chapter-004": [
            ("THE KNOT & NAIL", "गाँठ और कील", "The filing queue grows and thins. The coin-on-slate discourages casual requests."),
            ("DOCK THREE", "गोदी तीन", "Bhan's nightly station. The cutter finishes the lesson and seals the arm."),
            ("THE LOCKBOX", "ताला-बक्सा", "Seven objects now. The box is a portrait of one girl's history."),
        ],
        "chapter-005": [
            ("THE KNOT & NAIL", "गाँठ और कील", "The mark opens here. The Spindle brightens. The Inspector arrives."),
            ("THE RECKONING OFFICE", "उपर-छत लेखा-कक्ष", "Rekhak files the report. Lekh receives it. The Inspector is sent."),
            ("THE ASH-SLUMS", "राख-बस्ती", "The crater's base, deepest part of the basin. The Mendery is here."),
            ("THE MENDERY", "मेंडरी", "Low, broad, no windows, one door. The back door opens with Kessa's key. The archive inside."),
        ],
    }
    
    items = locs.get(ch, [])
    out = ["# Chapter %s — Locations\n" % chnum, ""]
    for name, dev, desc in items:
        out.append("## %s — %s" % (name, dev))
        out.append(desc)
        out.append("")
    return "\n".join(out)

def main():
    for ch in ["chapter-003", "chapter-004", "chapter-005"]:
        chdir = os.path.join(ROOT, "chapters", ch)
        story_dir = os.path.join(chdir, "story")
        chars_dir = os.path.join(chdir, "characters")
        
        # Generate Hindi translations
        for md in sorted(glob.glob(os.path.join(story_dir, "page-*.md"))):
            base = os.path.basename(md)
            if base.endswith(".hi.md"):
                continue
            hi_path = os.path.join(story_dir, base.replace(".md", ".hi.md"))
            if os.path.exists(hi_path):
                continue
            hindi = make_hindi(md)
            with open(hi_path, "w", encoding="utf-8") as f:
                f.write(hindi)
            print("  wrote", os.path.relpath(hi_path, ROOT))
        
        # Generate cast files
        for md in sorted(glob.glob(os.path.join(story_dir, "page-*.md"))):
            base = os.path.basename(md)
            if base.endswith(".hi.md"):
                continue
            pg = base.replace(".md", "")
            cast_path = os.path.join(chars_dir, "cast-%s.md" % pg)
            if os.path.exists(cast_path):
                continue
            with open(md, encoding="utf-8") as f:
                text = f.read()
            cast = make_cast(ch, pg, text)
            with open(cast_path, "w", encoding="utf-8") as f:
                f.write(cast)
            print("  wrote", os.path.relpath(cast_path, ROOT))
        
        # Generate glossary
        gloss_path = os.path.join(chdir, "other", "glossary.md")
        if not os.path.exists(gloss_path) or os.path.getsize(gloss_path) < 200:
            with open(gloss_path, "w", encoding="utf-8") as f:
                f.write(make_glossary(ch))
            print("  wrote", os.path.relpath(gloss_path, ROOT))
        
        # Generate locations
        loc_path = os.path.join(chdir, "other", "locations.md")
        if not os.path.exists(loc_path) or os.path.getsize(loc_path) < 200:
            with open(loc_path, "w", encoding="utf-8") as f:
                f.write(make_locations(ch))
            print("  wrote", os.path.relpath(loc_path, ROOT))
    
    print("done.")

if __name__ == "__main__":
    main()
