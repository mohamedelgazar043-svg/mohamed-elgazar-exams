# -*- coding: utf-8 -*-
# Redesign preview (v2 visuals, same grounded content as live v1). NOT for publish before review.
import html, os, re

BASE = os.environ.get("BASE_URL", "https://mohamed-elgazar-exams.pages.dev")
CANON_BASE = os.environ.get("CANON_BASE", BASE)
OUT = os.environ.get("OUT_DIR", "/downloads/google-site-redesign")
TEACHER = "مستر محمد الجزار"

recs = [
 {'eid':0,'grade':'تالتة إعدادي','unit':'الوحدة الرابعة','term':'الترم الأول','date':'23 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1169','name':'امتحان الوحدة الرابعة الدرس الأول (السجل الحفري) علوم تالتة إعدادي'},
 {'eid':1,'grade':'تالتة إعدادي','unit':'الوحدة الرابعة','term':'الترم الأول','date':'23 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1170','name':'إجابة امتحان الوحدة الرابعة الدرس الأول (السجل الحفري) علوم تالتة إعدادي'},
 {'eid':2,'grade':'تالتة إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'23 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1171','name':'امتحان الوحدة الأولى الدرس الأول (أنواع التفاعلات الكيميائية) علوم تالتة إعدادي 25 درجة'},
 {'eid':3,'grade':'تالتة إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'23 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1172','name':'نموذج إجابة امتحان الوحدة الأولى الدرس الأول (أنواع التفاعلات الكيميائية) علوم تالتة إعدادي من إعداد المعلم'},
 {'eid':4,'grade':'تالتة إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'23 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1173','name':'ملخص الوحدة الأولى (التفاعلات الكيميائية وآثارها البيئية) علوم تالتة إعدادي'},
 {'eid':5,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'24 نوفمبر 2026','typ':'مراجعة','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/83','name':'ملخص الوحدة الأولى: النظام البيئي المائي، العلوم المتكاملة أولى ثانوي'},
 {'eid':6,'grade':'رابعة ابتدائي','unit':'الفصل الأول','term':'الترم الأول','date':'24 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1174','name':'ملخص الفصل الأول: الطبيعة من حولنا، علوم رابعة ابتدائي'},
]

def CNT(k):
    n = sum(1 for r in recs if r['grade'] == k)
    return 'ملف واحد' if n == 1 else f'{n} ملفات'
GRADES = {
 'تالتة إعدادي': dict(slug='3prep', title='الصف تالتة إعدادي', short='تالتة إعدادي', stage='إعدادي', meta='علوم تالتة إعدادي', desc='امتحانات ومراجعات العلوم للصف الثالث الإعدادي الترم الأول.'),
 'رابعة ابتدائي': dict(slug='4prim', title='الصف الرابع الابتدائي', short='رابعة ابتدائي', stage='ابتدائي', meta='علوم رابعة ابتدائي', desc='ملخصات ومراجعات العلوم للصف الرابع الابتدائي الترم الأول.'),
 'أولى ثانوي': dict(slug='1sec', title='الصف أولى ثانوي', short='أولى ثانوي', stage='ثانوي', meta='علوم أولى ثانوي', desc='ملخصات ومراجعات العلوم للصف الأول الثانوي الترم الأول.'),
}
SVG_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/></svg>'
SVG_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg>'
SVG_BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 5c2.5-1 5-1 8 1v13c-3-2-5.5-2-8-1z"/><path d="M20 5c-2.5-1-5-1-8 1v13c3-2 5.5-2 8-1z"/></svg>'
SVG_FLASK = '<svg viewBox="0 0 24 24" fill="none" stroke="#3a2a05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6"/><path d="M10 3v6l-5 9c-.8 1.5.4 3 2.1 3h9.8c1.7 0 2.9-1.5 2.1-3l-5-9V3"/><path d="M7.5 15h9"/></svg>'
TYPES = {'امتحان/تدريب':('امتحان','#0b6e4f','#e8f5f0',SVG_DOC),
         'إجابات':('نموذج إجابة','#0a4d8f','#e9f1fa',SVG_CHECK),
         'مراجعة':('مراجعة/ملخص','#9a6a00','#fbf3e0',SVG_BOOK)}

TG = 'https://t.me/mo7amed_elgazar'
TG2 = 'https://t.me/mohamedsciencem'
YT = 'https://www.youtube.com/@mo7amedelgazar'
WA = 'https://wa.me/201220896257'
FB = [('المجتمع الرئيسي لمعلمي المواد العلمية', 'https://www.facebook.com/share/g/18FELAupsn/'), ('مُعلّمي الأحياء', 'https://www.facebook.com/share/g/1CqjWjEs3K/'), ('مُعلّمي الكيمياء', 'https://www.facebook.com/share/g/1L6SXdvNHV/'), ('مُعلّمي الفيزياء', 'https://www.facebook.com/share/g/1L6SXdvNHV/'), ('مُعلّمي الأون لاين', 'https://www.facebook.com/share/g/1EcjepZALZ/')] + [('بيت المعلمين (عام)','https://www.facebook.com/share/g/1c9RQN5jXY/'),('مُعلّمي العلوم','https://www.facebook.com/share/g/18pDyms9sw/'),('مُعلّمي العلوم المتكاملة','https://www.facebook.com/share/g/1E3jr6cEhb/'),('مُعلّمي الأحياء (رابط آخر)','https://www.facebook.com/share/g/18QdaEeFGb/'),('مُعلمي الكيمياء (رابط آخر)','https://www.facebook.com/share/g/18YtBzawzN/'),('مُعلّمي الفيزياء (رابط آخر)','https://www.facebook.com/share/g/1L5x5q2vx9/'),('مُعلّمي الأون لاين (رابط آخر)','https://www.facebook.com/share/g/18aBnGvpUU/'),('مُعلّمي الحصة','https://www.facebook.com/share/g/18wWnYSGyU/'),('بيت أولياء الأمور','https://www.facebook.com/share/g/1MPLDakK76/')]

WAC='https://whatsapp.com/channel/0029VagGGT66WaKex7G92V0m'
FBPAGE='https://www.facebook.com/share/1EBo6MKVhs/'
YT_USER='https://youtube.com/@mo7amedelgazar?si=GrOsoMjIsN3lovwV'
COMM=[
 ('معلمو العلوم',[('واتساب (عام)','https://chat.whatsapp.com/IjXgzGRcagkK8rklrumZxo','wa'),('واتساب (ابتدائي)','https://chat.whatsapp.com/BwxbGlpEF516JegvfwhZ2w','wa'),('واتساب (Science)','https://chat.whatsapp.com/KWK3KfRiwTdI31EbN7Dhlo','wa'),('تليجرام','https://t.me/teacher_s_e','tg')]),
 ('معلمو العلوم المتكاملة',[('واتساب','https://chat.whatsapp.com/C0dEjHy37RBIJkz0kGLnu0','wa'),('واتساب (لغات)','https://chat.whatsapp.com/KWK3KfRiwTdI31EbN7Dhlo','wa'),('تليجرام','https://t.me/teacher_s_mm','tg')]),
 ('معلمو الأحياء',[('واتساب','https://chat.whatsapp.com/DDq0HDzaNVH4ARleCdBMdM','wa'),('تليجرام','https://t.me/teacher_a7iaa','tg')]),
 ('معلمو الكيمياء',[('واتساب','https://chat.whatsapp.com/Hhc4AJSHzCY7xvkL6V39xK','wa'),('تليجرام','https://t.me/teacher_c7','tg')]),
 ('معلمو الفيزياء',[('واتساب','https://chat.whatsapp.com/FTEJRO4Us3D2HIMMC6JFyI','wa'),('تليجرام','https://t.me/teacher_p7','tg')]),
 ('معلمو الأونلاين',[('واتساب','https://chat.whatsapp.com/Jx0zuKZd6PhAhi41ulwp5V','wa'),('واتساب (الإعلانات)','https://chat.whatsapp.com/KMq1QcQGnvy6HnFkfM18RI','wa'),('تليجرام','https://telegram.me/scienceoo','tg')]),
]
FOLLOW=[('الصفحة الرئيسية على فيسبوك',FBPAGE,'fb'),('قناة يوتيوب',YT_USER,'yt'),('قناة واتساب',WAC,'wa'),('قناة تليجرام (علوم)','https://t.me/mo7amed_elgazar','tg'),('قناة تليجرام (علوم متكاملة)','https://t.me/mohamedsciencem','tg')]

def esc(s): return html.escape(str(s or ''), quote=True)

CSS = """
:root{--navy:#0a2e52;--deep:#071f3a;--green:#0e7a55;--mint:#e8f5f0;--gold:#e9a13b;--ink:#182230;--mut:#5b6675;--bg:#f4f6f8;--card:#fff;--line:#e5e9ee;--rad:18px}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:'Cairo','Segoe UI',Tahoma,sans-serif;line-height:1.75}
a{text-decoration:none;color:inherit}
.wrap{max-width:1020px;margin:0 auto;padding:0 18px}
.topbar{position:sticky;top:0;z-index:50;background:rgba(7,31,58,.92);backdrop-filter:blur(8px);color:#fff}
.topbar .wrap{display:flex;align-items:center;justify-content:space-between;height:58px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.05rem}
.logo{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--gold),#f6c46b);display:flex;align-items:center;justify-content:center}
.logo svg{width:20px;height:20px}
.topnav a{opacity:.85;font-size:.92rem;margin-inline-start:18px}
.topnav a:hover{opacity:1;color:var(--gold)}
.hero{position:relative;overflow:hidden;background:linear-gradient(120deg,var(--deep) 0%,var(--navy) 45%,var(--green) 100%);color:#fff;padding:64px 0 74px}
.hero .pattern{position:absolute;inset:0;opacity:.07;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140' viewBox='0 0 140 140'%3E%3Cg fill='none' stroke='%23ffffff' stroke-width='2'%3E%3Ccircle cx='35' cy='35' r='14'/%3E%3Ccircle cx='35' cy='35' r='4' fill='%23ffffff'/%3E%3Cpath d='M90 95h28M104 81v28'/%3E%3Ccircle cx='110' cy='30' r='9'/%3E%3Cpath d='M25 105l14-14 8 8 14-14'/%3E%3C/g%3E%3C/svg%3E")}
.hero .wrap{position:relative}
.kicker{display:inline-block;background:rgba(233,161,59,.16);border:1px solid rgba(233,161,59,.5);color:#f6c46b;border-radius:999px;padding:3px 16px;font-size:.85rem;font-weight:700;margin-bottom:16px}
.hero h1{font-size:2.6rem;font-weight:900;line-height:1.3;margin-bottom:10px}
.hero .sub{font-size:1.08rem;opacity:.92;max-width:560px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
.btn{display:inline-flex;align-items:center;gap:8px;border-radius:12px;padding:12px 26px;font-weight:800;font-size:.98rem;transition:transform .15s}
.btn:hover{transform:translateY(-2px)}
.btn-gold{background:linear-gradient(135deg,var(--gold),#f2b45a);color:#3a2a05}
.btn-ghost{border:2px solid rgba(255,255,255,.55);color:#fff}
.stats{display:flex;gap:26px;margin-top:34px;flex-wrap:wrap}
.stat b{font-size:1.5rem;display:block}
.stat span{font-size:.85rem;opacity:.85}
section{padding:44px 0 8px}
.sec-head{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:6px;margin-bottom:18px}
.sec-head h2{font-size:1.45rem;font-weight:900;color:var(--navy)}
.sec-head h2::after{content:'';display:block;width:52px;height:4px;border-radius:4px;background:var(--gold);margin-top:6px}
.sec-head .more{font-size:.88rem;color:var(--green);font-weight:700}
.cards{display:grid;grid-template-columns:1fr;gap:14px}
@media(min-width:680px){.cards{grid-template-columns:1fr 1fr}}
.ecard{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:18px;position:relative;overflow:hidden;box-shadow:0 1px 3px rgba(10,46,82,.05)}
.ecard::before{content:'';position:absolute;top:0;right:0;left:0;height:4px;background:var(--tc,#0e7a55)}
.etype{display:inline-flex;align-items:center;gap:6px;background:var(--tbg,#e8f5f0);color:var(--tc,#0e7a55);border-radius:999px;padding:2px 12px;font-size:.78rem;font-weight:800;margin-bottom:10px}
.etype svg{width:13px;height:13px;flex:none}
.ecard h3{font-size:1.02rem;font-weight:800;line-height:1.8;margin:6px 0 14px;clear:both;overflow-wrap:break-word}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.chip{background:#f0f3f7;border-radius:8px;padding:2px 10px;font-size:.76rem;color:var(--mut);font-weight:700}
.ecard .date{font-size:.78rem;color:var(--mut)}
.tg-btn{display:inline-flex;align-items:center;gap:7px;background:#229ed9;color:#fff;border-radius:10px;padding:8px 18px;font-weight:800;font-size:.86rem;margin-top:12px}
.channels{display:grid;grid-template-columns:1fr;gap:14px}
@media(min-width:680px){.channels{grid-template-columns:repeat(3,1fr)}}
.chan{border-radius:var(--rad);padding:20px;color:#fff;min-height:128px;display:flex;flex-direction:column;justify-content:space-between}
.chan h3{font-size:1.08rem;font-weight:800}
.chan p{font-size:.84rem;opacity:.92}
.chan .go{margin-top:12px;font-weight:800;font-size:.85rem;background:rgba(255,255,255,.18);border-radius:9px;padding:6px 14px;align-self:flex-start}
.chan.tg{background:linear-gradient(135deg,#1b83c4,#31a8e0)}
.chan.yt{background:linear-gradient(135deg,#b31217,#e52d27)}
.chan.wa{background:linear-gradient(135deg,#0d7a43,#25d366);grid-column:auto}
.fbgrid{display:flex;flex-wrap:wrap;gap:9px}
.fbpill{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:8px 18px;font-size:.86rem;font-weight:700;color:var(--navy)}
.fbpill:hover{border-color:var(--gold);color:var(--green)}
.note{background:var(--mint);border:1px solid #cfe8dc;border-radius:var(--rad);padding:16px 18px;font-size:.9rem;color:#14543d}
footer{background:var(--deep);color:#b9c6d4;padding:30px 0;margin-top:46px;font-size:.84rem;text-align:center}
footer b{color:#fff}
.crumbs{font-size:.84rem;color:var(--mut);margin:16px 0}
.crumbs a{color:var(--green);font-weight:700}
.grade-card{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:26px;text-align:center}
.grade-card h3{color:var(--navy);font-weight:900;font-size:1.15rem}
.grade-card p{color:var(--mut);font-size:.86rem;margin-top:4px}
.detail-head{background:linear-gradient(120deg,var(--deep),var(--navy));color:#fff;padding:44px 0}
.detail-head h1{font-size:1.5rem;font-weight:900;line-height:1.5}
.meta-table{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);overflow:hidden}
.meta-table .row{display:flex;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line);font-size:.92rem}
.meta-table .row:last-child{border-bottom:none}
.meta-table .k{min-width:120px;font-weight:800;color:var(--navy)}

.cm-grid{display:grid;grid-template-columns:1fr;gap:14px}
@media(min-width:680px){.cm-grid{grid-template-columns:1fr 1fr}}
.cm-card{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:18px}
.cm-card h3{font-size:1.05rem;font-weight:800;color:var(--navy);margin-bottom:10px}
.cm-links{display:flex;flex-wrap:wrap;gap:8px}
.cm-l{display:inline-block;border-radius:999px;padding:6px 16px;font-size:.88rem;font-weight:700;color:#fff}
.cm-l.wa{background:#12994f}.cm-l.tg{background:#1b83c4}.cm-l.yt{background:#c4161c}.cm-l.fb{background:#1a5ab8}
@media(max-width:520px){.brand{font-size:.88rem;white-space:nowrap}.topnav a{margin-inline-start:10px;font-size:.82rem}.topnav a:last-child{display:none}.hero h1{font-size:2rem}}
"""

def head(title, desc, canon):
    canon = CANON_BASE + canon[len(BASE):] if canon.startswith(BASE) else canon
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canon)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_EG">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
"""

TOPBAR = """<div class="topbar"><div class="wrap">
<div class="brand"><span class="logo">{flask}</span> مستر محمد الجزار</div>
<nav class="topnav"><a href="{base}/">الرئيسية</a><a href="{base}/exams/">الملفات</a><a href="{base}/community">المجتمع</a><a href="{tg}" target="_blank" rel="noopener">تليجرام</a></nav>
</div></div>
""".replace('{base}', BASE).replace('{tg}', TG).replace('{flask}', SVG_FLASK)

FOOT = f"""<footer><div class="wrap">
<b>{esc(TEACHER)}</b> — امتحانات ومذكرات العلوم<br>
المصدر الرسمي للملفات: قنوات تليجرام الخاصة بالمستر · آخر تحديث: {recs[-1]["date"]}
</div></footer>
</body></html>
"""

def ecard(r):
    lbl, tc, tbg, ic = TYPES.get(r['typ'], TYPES['مراجعة'])
    return f"""<div class="ecard" style="--tc:{tc};--tbg:{tbg}">
<span class="etype">{ic} {esc(lbl)}</span>
<h3>{esc(r['name'])}</h3>
<div class="chips"><span class="chip">{esc(r['grade'])}</span><span class="chip">{esc(r['term'])}</span><span class="chip">{esc(r['unit'])}</span></div>
<div class="date">{esc(r['date'])}</div>
<a class="tg-btn" href="{esc(r['link'])}" target="_blank" rel="noopener">فتح الملف على تليجرام</a>
</div>
"""

os.makedirs(os.path.join(OUT, 'exams'), exist_ok=True)

# HOME
latest = sorted(recs, key=lambda r: -r['eid'])[:4]
home = head('مستر محمد الجزار | امتحانات العلوم ومجتمع المعلمين',
            'امتحانات ومراجعات العلوم من إعداد مستر محمد الجزار، مرتبة بالصف والفصل الدراسي، بروابط مباشرة من تليجرام.',
            BASE + '/') + TOPBAR + f"""
<header class="hero"><div class="pattern"></div><div class="wrap">
<span class="kicker">منصة امتحانات العلوم</span>
<h1>امتحانات ومراجعات تفهم منها، مش بس تحفظها</h1>
<p class="sub">كل ملفات العلوم من إعداد {esc(TEACHER)} — امتحانات، نماذج إجابة، وملخصات مرتبة بالصف والوحدة والترم، بروابط تحميل مباشرة من قنواته الرسمية على تليجرام.</p>
<div class="cta"><a class="btn btn-gold" href="{BASE}/exams/">تصفح الملفات ({len(recs)})</a><a class="btn btn-ghost" href="{TG}" target="_blank" rel="noopener">قناة تليجرام الرئيسية</a></div>
<div class="stats"><div class="stat"><b>{len(recs)}</b><span>ملف منشور</span></div><div class="stat"><b>2</b><span>قناة تليجرام</span></div><div class="stat"><b>{len(set(u for _, u in FB))}</b><span>مجتمع فيسبوك</span></div></div>
</div></header>
<section><div class="wrap">
<div class="sec-head"><h2>أحدث الملفات</h2><a class="more" href="{BASE}/exams/">كل الملفات ←</a></div>
<div class="cards">{''.join(ecard(r) for r in latest)}</div>
<div style="text-align:center;margin-top:18px"><a class="btn btn-gold" href="{BASE}/exams/">عرض كل الملفات ({len(recs)})</a></div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>القنوات الرسمية</h2></div>
<div class="channels">
<a class="chan tg" href="{TG}" target="_blank" rel="noopener"><div><h3>تليجرام — القناة الرئيسية</h3><p>كل الامتحانات والمذكرات أول بأول</p></div><span class="go">متابعة القناة</span></a>
<a class="chan tg" style="background:linear-gradient(135deg,#0a4d8f,#1b83c4)" href="{TG2}" target="_blank" rel="noopener"><div><h3>تليجرام — العلوم المتكاملة</h3><p>ملفات مادة العلوم المتكاملة</p></div><span class="go">متابعة القناة</span></a>
<a class="chan wa" href="{WAC}" target="_blank" rel="noopener"><div><h3>قناة واتساب</h3><p>تابع الجديد على واتساب</p></div><span class="go">متابعة القناة</span></a>
<a class="chan" style="background:linear-gradient(135deg,#1a5ab8,#3b82e0)" href="{FBPAGE}" target="_blank" rel="noopener"><div><h3>صفحة فيسبوك</h3><p>الصفحة الرئيسية للمستر</p></div><span class="go">زيارة الصفحة</span></a>
<a class="chan yt" href="{YT_USER}" target="_blank" rel="noopener"><div><h3>يوتيوب</h3><p>شروحات وفيديوهات المنهج</p></div><span class="go">اشترك في القناة</span></a>
</div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>مجتمع معلمي المواد العلمية</h2></div>
<div class="fbgrid">{''.join(f'<a class="fbpill" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in FB)}</div>
<div style="text-align:center;margin-top:18px"><a class="btn btn-gold" href="{BASE}/community">كل روابط المجتمع (واتساب وتليجرام وفيسبوك)</a></div>
</div></section>
<section><div class="wrap"><div class="note">للتواصل المباشر مع المستر: <a href="{WA}" target="_blank" rel="noopener" style="font-weight:800;color:var(--green)">واتساب</a></div></div></section>
""" + FOOT
open(os.path.join(OUT, 'index.html'), 'w').write(home)

# EXAMS INDEX
idx = head('ملفات العلوم | مستر محمد الجزار', 'كل امتحانات ومراجعات العلوم من إعداد مستر محمد الجزار مرتبة بالصف والترم.',
           BASE + '/exams/') + TOPBAR + f"""
<div class="wrap"><nav class="crumbs"><a href="{BASE}/">الرئيسية</a> ‹ الملفات</nav></div>
<header class="detail-head"><div class="wrap"><h1>ملفات العلوم</h1><p style="opacity:.9">من إعداد {esc(TEACHER)} — {len(recs)} ملفات</p></div></header>
<section><div class="wrap">
<div class="sec-head"><h2>الصفوف المتاحة</h2></div>
<div class="cards">{''.join(f'<a class="grade-card" href="{BASE}/exams/{G["slug"]}"><h3>{G["title"]}</h3><p>{CNT(k)} · الترم الأول</p></a>' for k,G in GRADES.items() if any(r["grade"]==k for r in recs))}</div>
<div class="sec-head" style="margin-top:26px"><h2>كل الملفات</h2></div>
<div class="cards">{''.join(ecard(r) for r in recs)}</div>
</div></section>
""" + FOOT
open(os.path.join(OUT, 'exams', 'index.html'), 'w').write(idx)

# GRADE PAGES
for k, G in GRADES.items():
    gr = [r for r in recs if r['grade'] == k]
    if not gr: continue
    g = head(G['meta'] + ' | مستر محمد الجزار', G['desc'], BASE + '/exams/' + G['slug']) + TOPBAR + f"""
<div class="wrap"><nav class="crumbs"><a href="{BASE}/">الرئيسية</a> ‹ <a href="{BASE}/exams/">الملفات</a> ‹ {G['short']}</nav></div>
<header class="detail-head"><div class="wrap"><h1>العلوم — {G['title']}</h1><p style="opacity:.9">الترم الأول · {len(gr)} ملفات</p></div></header>
<section><div class="wrap"><div class="cards">{''.join(ecard(r) for r in gr)}</div></div></section>
""" + FOOT
    open(os.path.join(OUT, 'exams', G['slug'] + '.html'), 'w').write(g)

# EXAM DETAIL PAGES
for r in recs:
    lbl, tc, tbg, ic = TYPES.get(r['typ'], TYPES['مراجعة'])
    pg = head(r['name'] + ' | مستر محمد الجزار', r['name'], BASE + f"/exams/e{r['eid']}") + TOPBAR + f"""
<div class="wrap"><nav class="crumbs"><a href="{BASE}/">الرئيسية</a> ‹ <a href="{BASE}/exams/">الملفات</a> ‹ {esc(lbl)}</nav></div>
<header class="detail-head"><div class="wrap">
<span class="etype" style="--tc:{tc};--tbg:{tbg}">{ic} {esc(lbl)}</span>
<h1 style="margin-top:10px">{esc(r['name'])}</h1></div></header>
<section><div class="wrap">
<div class="meta-table">
<div class="row"><span class="k">المادة</span><span>{esc(r.get("subj","العلوم"))}</span></div>
<div class="row"><span class="k">الصف</span><span>{esc(r['grade'])} ({GRADES[r['grade']]['stage']})</span></div>
<div class="row"><span class="k">الفصل الدراسي</span><span>{esc(r['term'])}</span></div>
<div class="row"><span class="k">الوحدة</span><span>{esc(r['unit'])}</span></div>
<div class="row"><span class="k">النوع</span><span>{esc(lbl)}</span></div>
<div class="row"><span class="k">تاريخ النشر</span><span>{esc(r['date'])}</span></div>
<div class="row"><span class="k">الإعداد والمصدر</span><span>إعداد: مستر محمد الجزار</span></div>
</div>
<div style="text-align:center;margin-top:22px"><a class="tg-btn" style="font-size:1rem;padding:12px 30px" href="{esc(r['link'])}" target="_blank" rel="noopener">فتح الملف على تليجرام</a></div>
</div></section>
""" + FOOT
    open(os.path.join(OUT, 'exams', f"e{r['eid']}.html"), 'w').write(pg)

# COMMUNITY
def cl(n,u,k): return f'<a class="cm-l {k}" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>'
cm = head('مجتمع معلمي المواد العلمية | مستر محمد الجزار','روابط مجموعات وقنوات معلمي العلوم والمواد العلمية على فيسبوك وواتساب وتليجرام.',BASE+'/community') + TOPBAR + f"""
<div class="wrap"><nav class="crumbs"><a href="{BASE}/">الرئيسية</a> ‹ المجتمع</nav></div>
<header class="detail-head"><div class="wrap"><h1>مجتمع معلمي المواد العلمية</h1><p style="opacity:.9">كل المجموعات والقنوات في مكان واحد</p></div></header>
<section><div class="wrap">
<div class="sec-head"><h2>تابع {esc(TEACHER)}</h2></div>
<div class="cm-card"><div class="cm-links">{''.join(cl(*x) for x in FOLLOW)}</div></div>
<div class="sec-head" style="margin-top:26px"><h2>مجموعات الفيسبوك</h2></div>
<div class="fbgrid">{''.join(f'<a class="fbpill" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in FB)}</div>
<div class="sec-head" style="margin-top:26px"><h2>مجموعات وقنوات المواد</h2></div>
<div class="cm-grid">{''.join('<div class="cm-card"><h3>'+esc(t)+'</h3><div class="cm-links">'+''.join(cl(*x) for x in ls)+'</div></div>' for t,ls in COMM)}</div>
</div></section>
""" + FOOT
open(os.path.join(OUT, 'community.html'), 'w').write(cm)

urls = [BASE + '/', BASE + '/exams/', BASE + '/exams/3prep', BASE + '/exams/1sec', BASE + '/exams/4prim', BASE + '/community'] + [BASE + f'/exams/e{r["eid"]}' for r in recs]
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'<url><loc>{u}</loc></url>' for u in urls) + '\n</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: ' + BASE + '/sitemap.xml\n')
open(os.path.join(OUT, 'googlee0bf8f8fe2eace5f.html'), 'w').write('google-site-verification: googlee0bf8f8fe2eace5f.html')
print('OK', len(os.listdir(os.path.join(OUT, 'exams'))) + 4, 'files in', OUT)
