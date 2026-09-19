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
    "nandi": "Nandi — नंदी",
    "jadi": "Jadi — जड़ी",
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
    # Ch006
    "Your mother sewed you shut, child. To protect you.": "तुम्हारी माँ ने तुम्हें बंद किया, बच्ची। तुम्हारी रक्षा के लिए।",
    "She is the sewer. She is the cutter.": "वह सीवर है। वह काटने वाली है।",
    "Where is she?": "वह कहाँ है?",
    "You found it.": "तुमने ढूँढ लिया।",
    "Eight objects. All about one family.": "आठ चीज़ें। सब एक परिवार के बारे में।",
    "Then the principal knows you're here.": "तो प्रमुख जानता है कि तुम यहाँ हो।",
    "You heard her.": "तुमने उसे सुना।",
    "The charter stays.": "चार्टर यहीं रहता है।",
    "Mend. The rest will follow.": "सिलाई करो। बाकी पीछे आएगा।",
    # Ch007
    "A letter sealed in two waxes is a letter with two owners. Open it with one hand and you're": "दो मोम से सील किया ख़त दो मालिकों वाला ख़त है। एक हाथ से खोलो और तुम",
    "the only person who saw what it said — which means you're the only person anyone can blame.": "अकेली हो जो जानती हो उसमें क्या लिखा है — यानी अकेली तुम ही हो जिस पर कोई इल्ज़ाम लगा सके।",
    "So. Two hands. You take grey. I take crimson.": "तो। दो हाथ। तुम धूसर लो। मैं क़िरमिज़ी लूँगी।",
    "...Child.": "...बच्ची।",
    "This one's already open.": "यह पहले ही खुल चुका है।",
    "Is that entered?": "क्या यह दर्ज है?",
    "It came down your stair at some point in the last three nights and it was not entered,": "यह पिछली तीन रातों में कभी तुम्हारी सीढ़ी से नीचे आया और दर्ज नहीं हुआ,",
    "Reckoner. Nobody entered it. It was just *left*.": "रेखक। किसी ने दर्ज नहीं किया। यह बस *छोड़* दिया गया।",
    "Third register.": "तीसरा रजिस्टर।",
    "Say that again to yourself, mender. *Third register.*": "इसे फिर से अपने आप से कहो, सिलाईकर्ता। *तीसरा रजिस्टर।*",
    "Entries in the third register license nothing. They *inventory*.": "तीसरे रजिस्टर की प्रविष्टियाँ कुछ लाइसेंस नहीं करतीं। वे *सूचीबद्ध* करती हैं।",
    "Inventoried.": "सूचीबद्ध।",
    "You opened it with your hand on it.": "तुमने इसे हाथ पर रखकर खोला।",
    "...Right. Come here.": "...अच्छा। यहाँ आओ।",
    "Say the second part again.": "दूसरा हिस्सा फिर से कहो।",
    "The Mendery.": "मेंडरी।",
    "I have to go back in.": "मुझे वापस अंदर जाना है।",
    "You took your time.": "तुम्हें देर लगी।",
    "I didn't know I was invited.": "मुझे नहीं पता था कि मुझे बुलाया गया है।",
    "You were not invited. You were *scheduled.*": "तुम्हें बुलाया नहीं गया। तुम्हारा *समय तय* था।",
    "*The Roll of Hands.*": "*हाथों की सूची।*",
    "Whose?": "किसका?",
    "...Ask your mother. She is the only one on that roll who is allowed to say it.": "...अपनी माँ से पूछो। उस सूची में वह अकेली है जिसे इसे कहने की अनुमति है।",
    "Twenty years. Why did she stay bound for twenty years? She could have walked out of that chair": "बीस साल। वह बीस साल बँधी क्यों रही? वह उस कुर्सी से कभी भी",
    "the day the Council stopped watching.": "उठ सकती थी जिस दिन परिषद ने देखना बंद किया।",
    "That was the first part. There was a second.": "यह पहला हिस्सा था। दूसरा भी था।",
    "I'm not signing it. I'm not burning it either — burn it and in one Unspooling the school is his": "मैं इस पर दस्तख़त नहीं कर रही। जलाऊँगी भी नहीं — जलाओ और एक अनस्पूलिंग में विद्या उसकी",
    "by default, and she's in a cellar in Agnikhand with a book in her apron and nowhere to stand.": "हो जाएगी, और वह अग्निखंड की एक तहख़ाने में एप्रन में किताब लिए खड़ी होगी, बिना किसी जगह।",
    "Two ways out and neither one is out. Fine. Then I'm not taking either door.": "निकलने के दो रास्ते और कोई भी रास्ता नहीं। ठीक है। तो मैं कोई दरवाज़ा नहीं लूँगी।",
    "He can have the books.": "किताबें वह रख सकता है।",
    "I keep the reading.": "पढ़ना मैं रखती हूँ।",
    "Then I close the stitch.": "फिर मैं सिलाई बंद करती हूँ।",
    # Ch008
    "Good morning.": "सुप्रभात।",
    "The records stay. The room stays open, and I'll be in it every second bell.": "अभिलेख रहेंगे। कमरा खुला रहेगा, और मैं हर दूसरी घंटी में यहाँ रहूँगा।",
    "You know what you just did.": "तुम्हें पता है तुमने अभी क्या किया।",
    "I put the archive under his hand instead of yours.": "मैंने अभिलेख तुम्हारे बजाय उसके हाथ में रखा।",
    "Girl.": "बच्ची।",
    "What do I call you?": "तुम्हें क्या कहूँ?",
    "Jadi.": "जड़ी।",
    "You shut it.": "तुमने इसे बंद कर दिया।",
    "Two nights ago.": "दो रात पहले।",
    "I know what you are. I asked what you *are.*": "मुझे पता है तुम क्या हो। मैंने पूछा तुम *क्या* हो।",
    "You're the teacher.": "तुम शिक्षक हो।",
    "Pull it out.": "इसे निकाल दो।",
    "It doesn't come back. Hand's fine. Fingers are fine.": "यह वापस नहीं आता। हाथ ठीक है। उँगलियाँ ठीक हैं।",
    "Why did she take it? The Roll. It's been the question since she left and you're the first person": "उसने इसे क्यों लिया? सूची। यह उसके जाने के बाद से सवाल रहा है और तुम पहली इंसान हो",
    "who can answer it.": "जो जवाब दे सकती है।",
    "Because I told her to.": "क्योंकि मैंने उसे कहा था।",
    "What?": "क्या?",
    "No.": "नहीं।",
    "Say the three rules.": "तीन नियम कहो।",
    "Rule two.": "नियम दो।",
    "Rule three.": "नियम तीन।",
    "You'll need thread.": "तुम्हें धागा चाहिए होगा।",
    "I've got thread.": "मेरे पास धागा है।",
    "I can finish it.": "मैं इसे पूरा कर सकती हूँ।",
    "When is the lesson.": "अगला पाठ कब है।",
    "It doesn't feel different.": "यह अलग महसूस नहीं होता।",
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
    
    # Translate dialogue/caption lines.
    # Longest-first: a short key like "Third register." is a substring of a longer
    # key like "Say that again to yourself, mender. *Third register.*", so short
    # keys must not be applied before long ones or they break the longer match.
    for eng, hindi in sorted(HINDI.items(), key=lambda kv: -len(kv[0])):
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
    
    # Find characters mentioned.
    # Match on the full English name AND on the first name token, so that pages
    # which say "IRA:" or "Kessa" (rather than the full name) still list them.
    # Word boundaries stop "Ira" matching inside "Kshudra"-style words.
    def mentioned(eng_name):
        eng_name = eng_name.split(" — ")[0]
        if re.search(r"\b%s\b" % re.escape(eng_name), script_text, re.IGNORECASE):
            return True
        first = eng_name.split()[0]
        return re.search(r"\b%s\b" % re.escape(first), script_text, re.IGNORECASE) is not None

    found_chars = []
    for char_id, char_name in CHARS.items():
        if mentioned(char_name) or char_name.split(" — ")[1] in script_text:
            found_chars.append((char_id, char_name))

    # Ira is the POV character; she is on every page whether or not she is named.
    if not any(c[0] == "ira-sutar" for c in found_chars):
        found_chars.insert(0, ("ira-sutar", CHARS["ira-sutar"]))
    
    for char_id, char_name in found_chars:
        lines.append("## %s" % char_name)
        if char_id == "ira-sutar":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/ira-sutar.md`](../../chapter-001/characters/ira-sutar.md)")
        elif char_id == "kessa":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/kessa.md`](../../chapter-001/characters/kessa.md)")
        elif char_id == "rekhak-vahni":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/rekhak-vahni.md`](../../chapter-001/characters/rekhak-vahni.md)")
        elif char_id == "patra":
            lines.append("Full sheet (Ch. 001): [`../../chapter-001/characters/patra.md`](../../chapter-001/characters/patra.md)")
        elif char_id == "nandi":
            lines.append("Full sheet (Ch. 006): [`../../chapter-006/characters/nandi.md`](../../chapter-006/characters/nandi.md)")
        elif char_id == "jadi":
            lines.append("Full sheet (Ch. 008): [`jadi.md`](jadi.md)")
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
        "chapter-006": [
            ("School of the Braided Thread", "बुने धागे की विद्या", "Hand-school founded by Ira's mother. Charter in the Mendery archive."),
            ("Teacher's strand", "शिक्षक-तंतु", "The blank strand: the mother's thread, sewn into the student before speech."),
            ("Self-binding", "स्व-बंधन", "The mother bound herself voluntarily to keep the school alive."),
            ("Audit warrant", "लेखा-परवाना", "The Office's highest instrument: permits lockbox inspection."),
        ],
        "chapter-007": [
            ("Third register", "तीसरा रजिस्टर", "A crimson-bound private hand's book the Council keeps on a shelf. Entries inventory; they do not license."),
            ("Letter of provisional licence", "तदर्थ लाइसेंस-पत्र", "The principal's four-clause instrument. Clause four summons the founder."),
            ("Crease-writ", "मोड़-लेख", "A line drawn in sealing wax inside a fold — invisible unless the sheet is pressed perfectly flat. School method."),
            ("Two-pour seal", "दुहरा-सील", "A wax seal poured twice: broken, a bead removed, and the remainder pressed flat with a thumb."),
            ("Roll of Hands", "हाथों की सूची", "The school's pupil register: forty years of names, kinds, and the year each strand went in. Stolen by the mother."),
            ("Binding", "जिल्दसाज़ी", "Hand-sewing quires through the fold. Identified by sound: doubled cloth, heavy needle, slow turn."),
            ("Tally-thread", "गिनती-डोर", "Kessa's knotted cord ledger — the only record in Agnikhand that keeps no ink."),
            ("Supply chute", "आपूर्ति-नाली", "The Mendery's mortar drop: the road the mother's thread came up for forty years."),
        ],
        "chapter-008": [
            ("Book of the Hand", "हाथ की पुस्तक", "The school's method book. Knot diagrams for pupils who could not read; ends in forty years of first knots, one page per pupil, no names."),
            ("The hatch", "खिड़की-द्वार", "A forearm-sized hatch cut low in the Mendery's back door. The school's only address for forty years."),
            ("The Dating", "तिथि-करण", "The Office's nine-month practice of running a compliance chain across a palm and writing the enrollment year on a slate."),
            ("Unthreaded", "धागा-हीन", "A hand that has been dated: uninjured, and no longer knows what a needle is for. Forty-one measured; six unthreaded."),
            ("Unreadable", "अपठनीय", "A chain's return for a braided palm: both years at once. The Office has no procedure for it."),
            ("Pre-filing", "पूर्व-दाखिल", "The principal's method: entering a record before the event it describes. The entry predates the letter by eleven days."),
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
        "chapter-006": [
            ("THE MENDERY ARCHIVE", "मेंडरी अभिलेख", "Tall shelves of files. Council files in front, Kshudra files at the back. The mother's workshop behind the last door."),
            ("THE BINDING CHAIR", "बंधन-कुर्सी", "Modified with thread-holes in armrests. The mother bound herself voluntarily for twenty years."),
        ],
        "chapter-007": [
            ("THE KNOT & NAIL (NIGHT)", "गाँठ और कील (रात)", "Shuttered, one lamp, counter cleared. The letter is opened and answered here."),
            ("THE ARCHIVE FLOOR (DISBOUND)", "अभिलेख-तल (खुला)", "Every quire taken apart, spines cut at the stitching, sheets fanned and stacked. Four lamps lit. Three days of work."),
            ("THE BACK WALL", "पिछली दीवार", "The oldest Kshudra files in Agnikhand, knot-script labels, hand-cut boards — and one shelf standing empty."),
            ("THE SUPPLY CHUTE", "आपूर्ति-नाली", "A mortar drop in the Mendery's back stair. Forty years of thread came up through it; one letter goes down."),
        ],
        "chapter-008": [
            ("THE MENDERY (SEQUESTERED)", "मेंडरी (अधिकृत)", "The Office inside, a clerk on a crate with a slate by the stair, the disbound archive declared third-register property and left open."),
            ("THE BACK WALL", "पिछली दीवार", "The gap where the Roll stood, and beside it the Book of the Hand, standing there for forty years unread."),
            ("THE HATCH ALLEY", "खिड़की-गली", "The wet alley behind the Mendery. The hatch at knee height, its shutter worn shiny by forty years of forearms."),
            ("THE RECKONING OFFICE (WALL)", "लेखा-कार्यालय (दीवार)", "A hook, a compliance chain, a slate. One word written and underlined twice."),
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
    for ch in ["chapter-003", "chapter-004", "chapter-005", "chapter-006", "chapter-007", "chapter-008"]:
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
