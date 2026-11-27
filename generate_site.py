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
 {'eid':7,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'24 نوفمبر 2026','typ':'امتحان/تدريب','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/84','name':'اختبار الدرس الأول: الغلاف المائي على كوكب الأرض، العلوم المتكاملة أولى ثانوي'},
 {'eid':8,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'إجابات','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/85','name':'إجابة اختبار الدرس الأول: الغلاف المائي على كوكب الأرض، العلوم المتكاملة أولى ثانوي'},
 {'eid':9,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'امتحان/تدريب','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/86','name':'اختبار الدرس الثاني: الخواص الكيميائية للماء، العلوم المتكاملة أولى ثانوي'},
 {'eid':10,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'إجابات','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/87','name':'إجابة اختبار الدرس الثاني: الخواص الكيميائية للماء، العلوم المتكاملة أولى ثانوي'},
 {'eid':11,'grade':'سادسة ابتدائي','unit':'الفصل الأول','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1175','name':'ملخص الفصل الأول: شروط الاحتراق، علوم سادسة ابتدائي'},
 {'eid':12,'grade':'سادسة ابتدائي','unit':'الفصل الأول','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1176','name':'امتحان الفصل الأول: شروط الاحتراق، علوم سادسة ابتدائي'},
 {'eid':13,'grade':'سادسة ابتدائي','unit':'الفصل الأول','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1177','name':'نموذج إجابة امتحان الفصل الأول: شروط الاحتراق، علوم سادسة ابتدائي'},
 {'eid':14,'grade':'رابعة ابتدائي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1178','name':'مراجعة بيت العلوم: ملخص وأسئلة شهر نوفمبر، علوم رابعة ابتدائي'},
 {'eid':15,'grade':'خامسة ابتدائي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1179','name':'مراجعة بيت العلوم: تدريبات وأسئلة شهر نوفمبر، علوم خامسة ابتدائي'},
 {'eid':16,'grade':'سادسة ابتدائي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1180','name':'مراجعة بيت العلوم: تدريبات وأسئلة شهر نوفمبر، علوم سادسة ابتدائي'},
 {'eid':17,'grade':'أولى إعدادي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1181','name':'مراجعة بيت العلوم: ملخص وأسئلة شهر نوفمبر، علوم أولى إعدادي'},
 {'eid':18,'grade':'تانية إعدادي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1182','name':'مراجعة بيت العلوم: مراجعة نوفمبر، علوم تانية إعدادي'},
 {'eid':19,'grade':'تالتة إعدادي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mo7amed_elgazar/1183','name':'مراجعة بيت العلوم: مراجعة ما تم دراسته حتى نهاية نوفمبر، علوم تالتة إعدادي'},
 {'eid':20,'grade':'أولى ثانوي','unit':'مراجعة شهر نوفمبر','term':'الترم الأول','month':'نوفمبر 2026','date':'25 نوفمبر 2026','typ':'مراجعة شهرية','link':'https://t.me/mohamedsciencem/88','name':'مراجعة بيت العلوم: ملخص وأسئلة شهر نوفمبر، العلوم المتكاملة أولى ثانوي','subj':'العلوم المتكاملة'},
 {'eid':21,'grade':'أولى إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1184','name':'ملخص الوحدة الأولى: المادة، علوم أولى إعدادي'},
 {'eid':22,'grade':'أولى إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1185','name':'امتحان الدرس الأول: تركيب الذرة، علوم أولى إعدادي'},
 {'eid':23,'grade':'أولى إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'25 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1186','name':'نموذج إجابة امتحان الدرس الأول: تركيب الذرة، علوم أولى إعدادي'},
 {'eid':24,'grade':'تانية إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'26 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1187','name':'ملخص الوحدة الأولى: المادة والطاقة، علوم تانية إعدادي'},
 {'eid':25,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'26 نوفمبر 2026','typ':'امتحان/تدريب','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/89','name':'اختبار الدرس الثالث: الخواص الفيزيائية للماء، العلوم المتكاملة أولى ثانوي'},
 {'eid':26,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'26 نوفمبر 2026','typ':'إجابات','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/90','name':'إجابة اختبار الدرس الثالث: الخواص الفيزيائية للماء، العلوم المتكاملة أولى ثانوي'},
 {'eid':27,'grade':'تانية إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'26 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1188','name':'امتحان الدرس الأول: حالات المادة، علوم تانية إعدادي'},
 {'eid':28,'grade':'تانية إعدادي','unit':'الوحدة الأولى','term':'الترم الأول','date':'26 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1189','name':'نموذج إجابة امتحان الدرس الأول: حالات المادة، علوم تانية إعدادي'},
 {'eid':29,'grade':'رابعة ابتدائي','unit':'الفصل الثاني','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1190','name':'ملخص الفصل الثاني: كيف تنمو الحشرات؟، علوم رابعة ابتدائي'},
 {'eid':30,'grade':'خامسة ابتدائي','unit':'الفصل الثاني','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1191','name':'ملخص الفصل الثاني: التغيرات في الفصول، علوم خامسة ابتدائي'},
 {'eid':31,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/91','name':'اختبار الدرس الرابع: المحاليل المائية وخواصها، العلوم المتكاملة أولى ثانوي'},
 {'eid':32,'grade':'أولى ثانوي','unit':'الوحدة الأولى','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/92','name':'إجابة اختبار الدرس الرابع: المحاليل المائية وخواصها، العلوم المتكاملة أولى ثانوي'},
 {'eid':33,'grade':'سادسة ابتدائي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1192','name':'مراجعة شاملة للترم الأول، علوم سادسة ابتدائي'},
 {'eid':34,'grade':'سادسة ابتدائي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1193','name':'أسئلة مراجعة على الترم الأول، علوم سادسة ابتدائي'},
 {'eid':35,'grade':'أولى إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1194','name':'مراجعة شاملة للترم الأول، علوم أولى إعدادي'},
 {'eid':36,'grade':'أولى إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1195','name':'أسئلة مراجعة على الترم الأول، علوم أولى إعدادي'},
 {'eid':37,'grade':'تالتة إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1196','name':'مراجعة شاملة للترم الأول، علوم تالتة إعدادي'},
 {'eid':38,'grade':'تالتة إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1197','name':'أسئلة مراجعة على الترم الأول، علوم تالتة إعدادي'},
 {'eid':39,'grade':'أولى ثانوي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/95','name':'مراجعة شاملة للترم الأول، العلوم المتكاملة أولى ثانوي'},
 {'eid':40,'grade':'أولى ثانوي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','subj':'العلوم المتكاملة','link':'https://t.me/mohamedsciencem/96','name':'أسئلة مراجعة على الترم الأول، العلوم المتكاملة أولى ثانوي'},
 {'eid':41,'grade':'تانية إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1198','name':'مراجعة شاملة للترم الأول، علوم تانية إعدادي'},
 {'eid':42,'grade':'تانية إعدادي','unit':'مراجعة شاملة للترم الأول','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'مراجعة','link':'https://t.me/mo7amed_elgazar/1199','name':'أسئلة مراجعة على الترم الأول، علوم تانية إعدادي'},
 {'eid':43,'grade':'تالتة إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1200','name':'نموذج امتحان شامل (1) الترم الأول، علوم تالتة إعدادي'},
 {'eid':44,'grade':'تالتة إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1201','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول، علوم تالتة إعدادي'},
 {'eid':45,'grade':'تانية إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1202','name':'نموذج امتحان شامل (1) الترم الأول، علوم تانية إعدادي'},
 {'eid':46,'grade':'تانية إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1203','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول، علوم تانية إعدادي'},
 {'eid':47,'grade':'أولى إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1204','name':'نموذج امتحان شامل (1) الترم الأول، علوم أولى إعدادي'},
 {'eid':48,'grade':'أولى إعدادي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1205','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول، علوم أولى إعدادي'},
 {'eid':49,'grade':'سادسة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1206','name':'نموذج امتحان شامل (1) الترم الأول، علوم سادسة ابتدائي'},
 {'eid':50,'grade':'سادسة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1207','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول، علوم سادسة ابتدائي'},
 {'eid':51,'grade':'خامسة ابتدائي','unit':'نماذج امتحانات','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1208','name':'نموذج امتحان (1) الترم الأول (الفصلان 1 و2)، علوم خامسة ابتدائي'},
 {'eid':52,'grade':'خامسة ابتدائي','unit':'نماذج امتحانات','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1209','name':'نموذج إجابة الامتحان (1) الترم الأول (الفصلان 1 و2)، علوم خامسة ابتدائي'},
 {'eid':53,'grade':'رابعة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1210','name':'نموذج امتحان شامل (1) الترم الأول، علوم رابعة ابتدائي'},
 {'eid':54,'grade':'رابعة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1211','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول، علوم رابعة ابتدائي'},
 {'eid':55,'grade':'خامسة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'امتحان/تدريب','link':'https://t.me/mo7amed_elgazar/1212','name':'نموذج امتحان شامل (1) الترم الأول (الفصول 1 إلى 9)، علوم خامسة ابتدائي'},
 {'eid':56,'grade':'خامسة ابتدائي','unit':'نماذج امتحانات شاملة','term':'الترم الأول','date':'27 نوفمبر 2026','typ':'إجابات','link':'https://t.me/mo7amed_elgazar/1213','name':'نموذج إجابة الامتحان الشامل (1) الترم الأول (الفصول 1 إلى 9)، علوم خامسة ابتدائي'},
]

def CNT(k):
    n = sum(1 for r in recs if r['grade'] == k)
    return 'ملف واحد' if n == 1 else f'{n} ملفات'
GRADES = {
 'رابعة ابتدائي': dict(slug='4prim', title='الصف الرابع الابتدائي', short='رابعة ابتدائي', stage='ابتدائي', meta='علوم رابعة ابتدائي', desc='ملخصات ومراجعات العلوم للصف الرابع الابتدائي الترم الأول.'),
 'خامسة ابتدائي': dict(slug='5prim', title='الصف الخامس الابتدائي', short='خامسة ابتدائي', stage='ابتدائي', meta='علوم خامسة ابتدائي', desc='مراجعات العلوم للصف الخامس الابتدائي الترم الأول.'),
 'سادسة ابتدائي': dict(slug='6prim', title='الصف السادس الابتدائي', short='سادسة ابتدائي', stage='ابتدائي', meta='علوم سادسة ابتدائي', desc='ملخصات وامتحانات العلوم للصف السادس الابتدائي الترم الأول.'),
 'أولى إعدادي': dict(slug='1prep', title='الصف الأول الإعدادي', short='أولى إعدادي', stage='إعدادي', meta='علوم أولى إعدادي', desc='مراجعات العلوم للصف الأول الإعدادي الترم الأول.'),
 'تانية إعدادي': dict(slug='2prep', title='الصف الثاني الإعدادي', short='تانية إعدادي', stage='إعدادي', meta='علوم تانية إعدادي', desc='مراجعات العلوم للصف الثاني الإعدادي الترم الأول.'),
 'تالتة إعدادي': dict(slug='3prep', title='الصف تالتة إعدادي', short='تالتة إعدادي', stage='إعدادي', meta='علوم تالتة إعدادي', desc='امتحانات ومراجعات العلوم للصف الثالث الإعدادي الترم الأول.'),
 'أولى ثانوي': dict(slug='1sec', title='الصف أولى ثانوي', short='أولى ثانوي', stage='ثانوي', meta='علوم أولى ثانوي', desc='ملخصات ومراجعات العلوم للصف الأول الثانوي الترم الأول.'),
}
SVG_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/></svg>'
SVG_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg>'
SVG_BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 5c2.5-1 5-1 8 1v13c-3-2-5.5-2-8-1z"/><path d="M20 5c-2.5-1-5-1-8 1v13c3-2 5.5-2 8-1z"/></svg>'
SVG_FLASK = '<svg viewBox="0 0 24 24" fill="none" stroke="#3a2a05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6"/><path d="M10 3v6l-5 9c-.8 1.5.4 3 2.1 3h9.8c1.7 0 2.9-1.5 2.1-3l-5-9V3"/><path d="M7.5 15h9"/></svg>'
TYPES = {'امتحان/تدريب':('امتحان','#0b6e4f','#e8f5f0',SVG_DOC),
         'إجابات':('نموذج إجابة','#0a4d8f','#e9f1fa',SVG_CHECK),
         'مراجعة شهرية':('مراجعة بيت العلوم · نوفمبر','#6a3fb0','#f0eaf9',SVG_BOOK),
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

import json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assets_data import ICON_B64, FAV_B64, HERO_B64

# ---- v7 identity (Beit Eloloum): teal #006b5a, deep #004d40, mid #00897b, gold #c9a227, Noto Kufi Arabic
TYPES = {'امتحان/تدريب':('امتحان','#006b5a','#e3f2ee',SVG_DOC),
         'إجابات':('نموذج إجابة','#8a6a0a','#fbf3d9',SVG_CHECK),
         'مراجعة شهرية':('مراجعة بيت العلوم · نوفمبر','#5b3fa0','#efeaf8',SVG_BOOK),
         'مراجعة':('مراجعة/ملخص','#0a6f8a','#e1f2f7',SVG_BOOK)}
MONTHS = {'يناير':1,'فبراير':2,'مارس':3,'أبريل':4,'مايو':5,'يونيو':6,'يوليو':7,'أغسطس':8,'سبتمبر':9,'أكتوبر':10,'نوفمبر':11,'ديسمبر':12}
def iso(d):
    p = d.split()
    return f"{int(p[2]):04d}-{MONTHS[p[1]]:02d}-{int(p[0]):02d}"
LASTMOD = max(iso(r['date']) for r in recs)
ICON = f'data:image/webp;base64,{ICON_B64}'
FAVI = f'data:image/png;base64,{FAV_B64}'
HERO = f'data:image/webp;base64,{HERO_B64}'
OGIMG = CANON_BASE + '/og.png'
WMARK = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='90' viewBox='0 0 120 90'%3E%3Cg fill='%23ffffff'%3E%3Cpath d='M10 40L40 14l30 26-4 3-26-22-26 22z'/%3E%3Crect x='34' y='34' width='5' height='5' rx='1.2'/%3E%3Crect x='41' y='34' width='5' height='5' rx='1.2'/%3E%3Crect x='34' y='41' width='5' height='5' rx='1.2'/%3E%3Crect x='41' y='41' width='5' height='5' rx='1.2'/%3E%3C/g%3E%3C/svg%3E"

CSS = """
:root{--teal:#006b5a;--deep:#004d40;--mid:#00897b;--gold:#c9a227;--goldl:#e6c65a;--ink:#1f2d3a;--mut:#5a6b78;--bg:#f3f7f6;--card:#fff;--line:#d5e5e1;--rad:16px}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:'Noto Kufi Arabic','Noto Naskh Arabic','Segoe UI',Tahoma,sans-serif;line-height:1.8;font-size:15px}
a{text-decoration:none;color:inherit}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:6px}
.wrap{max-width:1040px;margin:0 auto;padding:0 18px}
.skip{position:absolute;right:8px;top:-60px;background:var(--gold);color:#2b2200;padding:8px 16px;border-radius:8px;z-index:100;font-weight:700}.skip:focus{top:8px}
.topbar{position:sticky;top:0;z-index:50;background:linear-gradient(90deg,var(--deep),var(--mid));border-bottom:3px solid var(--gold);color:#fff}
.topbar .wrap{display:flex;align-items:center;justify-content:space-between;height:60px}
.brand{display:flex;align-items:center;gap:10px}
.brand img{height:30px;width:auto;display:block}
.brand b{display:block;font-size:1.02rem;font-weight:800;line-height:1.2}
.brand small{display:block;font-size:.68rem;color:var(--goldl);font-weight:700;letter-spacing:.2px}
.topnav{display:flex;gap:4px}
.topnav a{font-size:.88rem;font-weight:600;padding:6px 13px;border-radius:999px;opacity:.92}
.topnav a:hover,.topnav a.on{background:rgba(255,255,255,.16);opacity:1}
.hero{position:relative;overflow:hidden;background:linear-gradient(125deg,var(--deep) 0%,var(--teal) 55%,var(--mid) 100%);color:#fff;padding:54px 0 64px}
.hero::before{content:'';position:absolute;inset:-40%;background-image:url("__WM__");background-size:120px 90px;transform:rotate(-24deg);opacity:.06}
.hero .wrap{position:relative;display:grid;grid-template-columns:minmax(0,1fr);gap:26px;align-items:center}.hero .wrap>*{min-width:0}
@media(min-width:820px){.hero .wrap{grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr)}}
.hero-logo{justify-self:center}.hero-logo img{width:min(300px,62vw);height:auto;display:block;filter:drop-shadow(0 8px 24px rgba(0,0,0,.25))}
.kicker{display:inline-block;background:rgba(201,162,39,.18);border:1px solid rgba(230,198,90,.6);color:var(--goldl);border-radius:999px;padding:3px 16px;font-size:.8rem;font-weight:700;margin-bottom:14px}
.hero h1{font-size:2.05rem;font-weight:800;line-height:1.5;margin-bottom:10px}
.hero .sub{font-size:.98rem;opacity:.92;max-width:540px}
.search{display:flex;gap:8px;margin-top:22px;max-width:520px}
.search input{flex:1;min-width:0;border:2px solid transparent;border-radius:12px;padding:12px 16px;font:inherit;font-size:.92rem;background:#fff;color:var(--ink)}
.search input:focus{outline:none;border-color:var(--gold)}
.search button{border:0;cursor:pointer;border-radius:12px;padding:0 22px;font:inherit;font-weight:800;background:linear-gradient(135deg,var(--gold),var(--goldl));color:#2b2200}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.btn{display:inline-flex;align-items:center;gap:8px;border-radius:12px;padding:11px 24px;font-weight:800;font-size:.92rem;transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(0,0,0,.18)}
.btn-gold{background:linear-gradient(135deg,var(--gold),var(--goldl));color:#2b2200}
.btn-teal{background:var(--teal);color:#fff}
.btn-ghost{border:2px solid rgba(255,255,255,.55);color:#fff}
.stats{display:flex;gap:28px;margin-top:26px;flex-wrap:wrap}
.stat b{font-size:1.5rem;display:block;color:var(--goldl);line-height:1.3}.stat span{font-size:.8rem;opacity:.88}
section{padding:40px 0 6px}
.sec-head{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:6px;margin-bottom:18px}
.sec-head h2{font-size:1.28rem;font-weight:800;color:var(--deep)}
.sec-head h2::after{content:'';display:block;width:46px;height:4px;border-radius:4px;background:var(--gold);margin-top:6px}
.sec-head .more{font-size:.84rem;color:var(--teal);font-weight:700}
.cards{display:grid;grid-template-columns:minmax(0,1fr);gap:14px}
@media(min-width:680px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ecard{background:var(--card);border:1px solid var(--line);border-right:5px solid var(--tc,#006b5a);border-radius:var(--rad);padding:16px 18px;box-shadow:0 1px 3px rgba(0,77,64,.06);transition:transform .15s,box-shadow .15s;display:flex;flex-direction:column}
.ecard:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,77,64,.12)}
.etype{display:inline-flex;align-items:center;gap:6px;align-self:flex-start;background:var(--tbg,#e3f2ee);color:var(--tc,#006b5a);border-radius:999px;padding:2px 13px;font-size:.74rem;font-weight:800}
.etype svg{width:13px;height:13px;flex:none}
.ecard h3{font-size:.96rem;font-weight:700;line-height:1.85;margin:10px 0 12px;overflow-wrap:break-word}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.chip{background:#eef4f2;border-radius:8px;padding:1px 10px;font-size:.72rem;color:var(--mut);font-weight:600}
.ecard .foot{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:auto;padding-top:6px}
.ecard .date{font-size:.74rem;color:var(--mut)}
.tg-btn{display:inline-flex;align-items:center;gap:7px;background:#229ed9;color:#fff;border-radius:10px;padding:7px 16px;font-weight:700;font-size:.82rem}
.tg-btn:hover{background:#1b8bc0}
.tg-btn::before{content:'';width:15px;height:15px;background:no-repeat center/contain url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M21.9 4.1L2.7 11.5c-1.3.5-1.3 1.3-.2 1.6l4.9 1.5 1.9 5.8c.2.6.1.8.7.8.5 0 .7-.2 1-.5l2.4-2.3 4.9 3.6c.9.5 1.5.2 1.7-.8l3.2-15.2c.3-1.3-.5-1.9-1.3-1.5zM8.4 13.8l9.8-6.2c.5-.3.9-.1.5.2l-8.1 7.3-.3 3.3z'/%3E%3C/svg%3E")}
.grades{display:grid;grid-template-columns:repeat(auto-fit,minmax(118px,1fr));gap:12px}
.grade-card{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:18px 12px;text-align:center;position:relative;overflow:hidden;transition:transform .15s,box-shadow .15s}
.grade-card::after{content:'';position:absolute;left:0;right:0;bottom:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--gold))}
.grade-card:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,77,64,.12)}
.grade-card .stage{font-size:.7rem;font-weight:700;color:var(--gold);letter-spacing:.3px}
.grade-card h3{color:var(--deep);font-weight:800;font-size:.98rem;margin-top:2px}
.grade-card p{color:var(--mut);font-size:.78rem;margin-top:2px}
.channels{display:grid;grid-template-columns:1fr;gap:12px}
@media(min-width:680px){.channels{grid-template-columns:repeat(3,1fr)}}
.chan{border-radius:var(--rad);padding:18px;color:#fff;min-height:118px;display:flex;flex-direction:column;justify-content:space-between;transition:transform .15s}
.chan:hover{transform:translateY(-3px)}
.chan h3{font-size:1rem;font-weight:800}.chan p{font-size:.8rem;opacity:.92}
.chan .go{margin-top:10px;font-weight:700;font-size:.8rem;background:rgba(255,255,255,.2);border-radius:9px;padding:4px 14px;align-self:flex-start}
.chan.tg{background:linear-gradient(135deg,#1b83c4,#31a8e0)}.chan.tg2{background:linear-gradient(135deg,#0a4d8f,#1b83c4)}
.chan.yt{background:linear-gradient(135deg,#b31217,#e52d27)}.chan.wa{background:linear-gradient(135deg,#0d7a43,#25d366)}.chan.fb{background:linear-gradient(135deg,#1a5ab8,#3b82e0)}
.fbgrid{display:flex;flex-wrap:wrap;gap:9px}
.fbpill{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:7px 17px;font-size:.82rem;font-weight:600;color:var(--deep)}
.fbpill:hover{border-color:var(--gold);color:var(--teal)}
.note{background:#e3f2ee;border:1px solid #c5e0d9;border-right:5px solid var(--teal);border-radius:var(--rad);padding:14px 18px;font-size:.88rem;color:var(--deep)}
.note a{font-weight:800;color:var(--teal)}
footer{background:linear-gradient(90deg,var(--deep),#00382e);color:#bcd5cf;margin-top:48px;border-top:3px solid var(--gold);font-size:.8rem}
footer .wrap{display:flex;flex-wrap:wrap;gap:18px;justify-content:space-between;align-items:center;padding-top:24px;padding-bottom:24px}
footer b{color:#fff}.fnav{display:flex;gap:16px;flex-wrap:wrap}.fnav a{color:var(--goldl);font-weight:600}
.crumbs{font-size:.8rem;color:var(--mut);margin:16px 0}.crumbs a{color:var(--teal);font-weight:700}
.page-head{background:linear-gradient(125deg,var(--deep),var(--teal));color:#fff;padding:36px 0;border-bottom:3px solid var(--gold);position:relative;overflow:hidden}
.page-head::before{content:'';position:absolute;inset:-40%;background-image:url("__WM__");background-size:120px 90px;transform:rotate(-24deg);opacity:.05}
.page-head .wrap{position:relative}
.page-head h1{font-size:1.4rem;font-weight:800;line-height:1.6}.page-head p{opacity:.9;font-size:.9rem}
.meta-table{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);overflow:hidden}
.meta-table .row{display:flex;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line);font-size:.9rem}
.meta-table .row:nth-child(odd){background:#f8fbfa}.meta-table .row:last-child{border-bottom:none}
.meta-table .k{min-width:120px;font-weight:800;color:var(--deep)}
.cm-grid{display:grid;grid-template-columns:1fr;gap:14px}
@media(min-width:680px){.cm-grid{grid-template-columns:1fr 1fr}}
.cm-card{background:var(--card);border:1px solid var(--line);border-right:5px solid var(--teal);border-radius:var(--rad);padding:16px 18px}
.cm-card h3{font-size:1rem;font-weight:800;color:var(--deep);margin-bottom:10px}
.cm-links{display:flex;flex-wrap:wrap;gap:8px}
.cm-l{display:inline-block;border-radius:999px;padding:5px 15px;font-size:.84rem;font-weight:700;color:#fff}
.cm-l.wa{background:#12994f}.cm-l.tg{background:#1b83c4}.cm-l.yt{background:#c4161c}.cm-l.fb{background:#1a5ab8}
.tools{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:16px 18px;margin-bottom:20px;position:sticky;top:68px;z-index:20;box-shadow:0 4px 14px rgba(0,77,64,.08)}
.tools input{width:100%;border:2px solid var(--line);border-radius:12px;padding:11px 16px;font:inherit;font-size:.9rem;background:#fbfdfc}
.tools input:focus{outline:none;border-color:var(--teal)}
.fl{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px;align-items:center}
.fl .lab{font-size:.74rem;font-weight:800;color:var(--mut);margin-inline-end:4px}
.fchip{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:3px 14px;font:inherit;font-size:.78rem;font-weight:700;color:var(--deep);cursor:pointer}
.fchip:hover{border-color:var(--teal)}.fchip[aria-pressed=true]{background:var(--teal);border-color:var(--teal);color:#fff}
.count{font-size:.8rem;color:var(--mut);margin:0 2px 12px;font-weight:600}
.empty{display:none;text-align:center;padding:40px 10px;color:var(--mut);background:var(--card);border:1px dashed var(--line);border-radius:var(--rad)}
.unit-h{font-size:1rem;font-weight:800;color:var(--teal);margin:22px 0 10px;padding-right:12px;border-right:4px solid var(--gold)}
.otherg{display:flex;flex-wrap:wrap;gap:8px}
html,body{max-width:100%;overflow-x:hidden}
.topbar .wrap{gap:8px}.topnav{min-width:0}.brand{min-width:0;flex:none}
@media(max-width:640px){.topnav a:last-child{display:none}.topnav a{padding:5px 9px;font-size:.8rem}.brand small{display:none}.brand img{height:26px;width:auto}}
@media(max-width:400px){.topnav a:first-child{display:none}.topnav a{padding:5px 8px;font-size:.78rem}.brand b{font-size:.92rem}.wrap{padding:0 14px}}
@media(max-width:560px){.hero h1{font-size:1.6rem}.tools{position:static}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
""".replace('__WM__', WMARK)

SITE_NAME = 'مستر محمد الجزار | بيت العلوم'
def jld(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '</script>'
def cu(u): return CANON_BASE + u[len(BASE):] if u.startswith(BASE) else u
PERSON = {"@type": "Person", "name": TEACHER, "jobTitle": "معلم علوم", "url": CANON_BASE + "/", "sameAs": [TG, TG2, YT_USER, FBPAGE]}
def crumbs_ld(items):
    return jld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": cu(u)} for i, (n, u) in enumerate(items)]})

def head(title, desc, canon, extra=''):
    canon = cu(canon)
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#004d40">
<link rel="canonical" href="{esc(canon)}">
<link rel="icon" href="{FAVI}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_EG">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:url" content="{esc(canon)}">
<meta property="og:image" content="{OGIMG}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{extra}
</head>
<body>
<a class="skip" href="#main">تخطي إلى المحتوى</a>
"""

def topbar(on=''):
    def a(k, href, t): return f'<a href="{href}"' + (' class="on"' if k == on else '') + f'>{t}</a>'
    return f"""<header class="topbar"><div class="wrap">
<a class="brand" href="{BASE}/"><img src="{ICON}" alt="" width="90" height="30"><span><b>بيت العلوم</b><small>{TEACHER}</small></span></a>
<nav class="topnav" aria-label="التنقل الرئيسي">{a('home', BASE + '/', 'الرئيسية')}{a('files', BASE + '/exams/', 'الملفات')}{a('comm', BASE + '/community', 'المجتمع')}<a href="{TG}" target="_blank" rel="noopener">تليجرام</a></nav>
</div></header>
<main id="main">
"""

FOOT = f"""</main>
<footer><div class="wrap">
<div><b>{esc(TEACHER)}</b> · بيت العلوم<br>امتحانات ومراجعات العلوم · المصدر الرسمي للملفات: قنوات تليجرام الخاصة بالمستر · تتم إضافة الملفات الجديدة باستمرار</div>
<nav class="fnav" aria-label="روابط سريعة"><a href="{BASE}/exams/">الملفات</a><a href="{BASE}/community">المجتمع</a><a href="{TG}" target="_blank" rel="noopener">تليجرام</a><a href="{YT_USER}" target="_blank" rel="noopener">يوتيوب</a><a href="{WA}" target="_blank" rel="noopener">واتساب</a></nav>
</div></footer>
</body></html>
"""

def ecard(r):
    lbl, tc, tbg, ic = TYPES.get(r['typ'], TYPES['مراجعة'])
    q = ' '.join([r['name'], r['grade'], r['unit'], lbl, r.get('subj', 'العلوم')])
    return f"""<article class="ecard" style="--tc:{tc};--tbg:{tbg}" data-q="{esc(q)}" data-g="{esc(r['grade'])}" data-t="{esc(lbl)}">
<span class="etype">{ic} {esc(lbl)}</span>
<h3><a href="{BASE}/exams/e{r['eid']}">{esc(r['name'])}</a></h3>
<div class="chips"><span class="chip">{esc(r['grade'])}</span><span class="chip">{esc(r['term'])}</span><span class="chip">{esc(r['unit'])}</span></div>
<div class="foot"><span class="date">{esc(r['date'])}</span><a class="tg-btn" href="{esc(r['link'])}" target="_blank" rel="noopener">فتح على تليجرام</a></div>
</article>
"""

def grade_cards():
    return ''.join(f'<a class="grade-card" href="{BASE}/exams/{G["slug"]}"><span class="stage">{G["stage"]}</span><h3>{G["short"]}</h3><p>{CNT(k)}</p></a>' for k, G in GRADES.items() if any(r["grade"] == k for r in recs))

os.makedirs(os.path.join(OUT, 'exams'), exist_ok=True)
NG = len({r['grade'] for r in recs})
WEBSITE_LD = jld({"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": SITE_NAME, "url": CANON_BASE + "/", "inLanguage": "ar-EG", "publisher": PERSON,
     "potentialAction": {"@type": "SearchAction", "target": CANON_BASE + "/exams/?q={search_term_string}", "query-input": "required name=search_term_string"}},
    PERSON]})

# HOME
latest = sorted(recs, key=lambda r: -r['eid'])[:6]
home = head('مستر محمد الجزار | بيت العلوم: امتحانات ومراجعات العلوم',
            'امتحانات ومراجعات وملخصات العلوم من إعداد مستر محمد الجزار، مرتبة بالصف والوحدة، بروابط مباشرة من قنوات تليجرام.',
            BASE + '/', WEBSITE_LD) + topbar('home') + f"""
<div class="hero"><div class="wrap">
<div>
<span class="kicker">بيت العلوم · مستر محمد الجزار</span>
<h1>امتحانات ومراجعات العلوم، مرتبة وجاهزة ليك</h1>
<p class="sub">امتحانات ونماذج إجابة وملخصات لكل الصفوف، بالصف والوحدة والترم، وبروابط مباشرة من قنوات المستر الرسمية على تليجرام.</p>
<form class="search" role="search" action="{BASE}/exams/" method="get"><input type="search" name="q" placeholder="ابحث عن امتحان أو ملخص أو صف..." aria-label="بحث في الملفات"><button type="submit">بحث</button></form>
<div class="cta"><a class="btn btn-gold" href="{BASE}/exams/">تصفح كل الملفات ({len(recs)})</a><a class="btn btn-ghost" href="{TG}" target="_blank" rel="noopener">قناة تليجرام</a></div>
<div class="stats"><div class="stat"><b>{len(recs)}</b><span>ملف منشور</span></div><div class="stat"><b>{NG}</b><span>صفوف دراسية</span></div><div class="stat"><b>2</b><span>قناة تليجرام</span></div></div>
</div>
<div class="hero-logo"><img src="{HERO}" alt="شعار بيت العلوم - مستر محمد الجزار" width="300" height="214"></div>
</div></div>
<section><div class="wrap">
<div class="sec-head"><h2>تصفح حسب الصف</h2></div>
<div class="grades">{grade_cards()}</div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>أحدث الملفات</h2><a class="more" href="{BASE}/exams/">كل الملفات ←</a></div>
<div class="cards">{''.join(ecard(r) for r in latest)}</div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>القنوات الرسمية</h2></div>
<div class="channels">
<a class="chan tg" href="{TG}" target="_blank" rel="noopener"><div><h3>تليجرام: القناة الرئيسية</h3><p>كل الامتحانات والمذكرات أول بأول</p></div><span class="go">متابعة القناة</span></a>
<a class="chan tg2" href="{TG2}" target="_blank" rel="noopener"><div><h3>تليجرام: العلوم المتكاملة</h3><p>ملفات مادة العلوم المتكاملة</p></div><span class="go">متابعة القناة</span></a>
<a class="chan wa" href="{WAC}" target="_blank" rel="noopener"><div><h3>قناة واتساب</h3><p>تابع الجديد على واتساب</p></div><span class="go">متابعة القناة</span></a>
<a class="chan fb" href="{FBPAGE}" target="_blank" rel="noopener"><div><h3>صفحة فيسبوك</h3><p>الصفحة الرئيسية للمستر</p></div><span class="go">زيارة الصفحة</span></a>
<a class="chan yt" href="{YT_USER}" target="_blank" rel="noopener"><div><h3>يوتيوب</h3><p>شروحات وفيديوهات المنهج</p></div><span class="go">اشترك في القناة</span></a>
</div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>مجتمع معلمي المواد العلمية</h2><a class="more" href="{BASE}/community">كل الروابط ←</a></div>
<div class="fbgrid">{''.join(f'<a class="fbpill" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in FB)}</div>
</div></section>
<section><div class="wrap"><div class="note">للتواصل المباشر مع المستر: <a href="{WA}" target="_blank" rel="noopener">واتساب</a></div></div></section>
""" + FOOT
open(os.path.join(OUT, 'index.html'), 'w').write(home)

# EXAMS INDEX with search + filters (works without JS: all cards visible)
types_used = []
for r in recs:
    l = TYPES.get(r['typ'], TYPES['مراجعة'])[0]
    if l not in types_used: types_used.append(l)
grades_used = [k for k in GRADES if any(r['grade'] == k for r in recs)]
JS = """<script>
(function(){var q=document.getElementById('q'),cards=[].slice.call(document.querySelectorAll('.ecard')),cnt=document.getElementById('cnt'),emp=document.getElementById('emp'),G='',T='';
function norm(s){return (s||'').toLowerCase().replace(/[\\u064B-\\u0652\\u0640]/g,'').replace(/[أإآ]/g,'ا').replace(/ى/g,'ي').replace(/ة/g,'ه')}
function run(){var v=norm(q.value).split(/\\s+/).filter(Boolean),n=0;cards.forEach(function(c){var t=norm(c.dataset.q),ok=v.every(function(w){return t.indexOf(w)>-1})&&(!G||c.dataset.g===G)&&(!T||c.dataset.t===T);c.style.display=ok?'':'none';if(ok)n++});
cnt.textContent=n+' من '+cards.length+' ملف';emp.style.display=n?'none':'block'}
function bind(sel,set){[].forEach.call(document.querySelectorAll(sel),function(b){b.addEventListener('click',function(){var on=b.getAttribute('aria-pressed')==='true';[].forEach.call(document.querySelectorAll(sel),function(x){x.setAttribute('aria-pressed','false')});if(!on)b.setAttribute('aria-pressed','true');set(on?'':b.dataset.v);run()})})}
bind('.fg',function(v){G=v});bind('.ft',function(v){T=v});q.addEventListener('input',run);
var m=location.search.match(/[?&]q=([^&]*)/);if(m){try{q.value=decodeURIComponent(m[1].replace(/\\+/g,' '))}catch(e){}}run()})();
</script>"""
items_ld = jld({"@context": "https://schema.org", "@type": "CollectionPage", "name": "ملفات العلوم", "url": CANON_BASE + "/exams/", "inLanguage": "ar-EG",
    "mainEntity": {"@type": "ItemList", "numberOfItems": len(recs), "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": CANON_BASE + f"/exams/e{r['eid']}", "name": r['name']} for i, r in enumerate(sorted(recs, key=lambda r: -r['eid']))]}})
idx = head('ملفات العلوم | مستر محمد الجزار', 'كل امتحانات ومراجعات وملخصات العلوم من إعداد مستر محمد الجزار مرتبة بالصف والترم، مع بحث وفلاتر.',
           BASE + '/exams/', items_ld + crumbs_ld([('الرئيسية', BASE + '/'), ('الملفات', BASE + '/exams/')])) + topbar('files') + f"""
<div class="wrap"><nav class="crumbs" aria-label="مسار التنقل"><a href="{BASE}/">الرئيسية</a> ‹ الملفات</nav></div>
<div class="page-head"><div class="wrap"><h1>ملفات العلوم</h1><p>من إعداد {esc(TEACHER)} · {len(recs)} ملف في {NG} صفوف</p></div></div>
<section><div class="wrap">
<div class="tools"><input id="q" type="search" placeholder="ابحث بالاسم أو الصف أو الوحدة..." aria-label="بحث في الملفات" autocomplete="off">
<div class="fl"><span class="lab">الصف:</span>{''.join(f'<button type="button" class="fchip fg" aria-pressed="false" data-v="{esc(k)}">{esc(GRADES[k]["short"])}</button>' for k in grades_used)}</div>
<div class="fl"><span class="lab">النوع:</span>{''.join(f'<button type="button" class="fchip ft" aria-pressed="false" data-v="{esc(t)}">{esc(t)}</button>' for t in types_used)}</div></div>
<div class="count" id="cnt" aria-live="polite">{len(recs)} من {len(recs)} ملف</div>
<div class="cards">{''.join(ecard(r) for r in sorted(recs, key=lambda r: -r['eid']))}</div>
<div class="empty" id="emp">مفيش ملفات مطابقة للبحث. جرّب كلمة تانية أو شيل الفلاتر.</div>
</div></section>
{JS}
""" + FOOT
open(os.path.join(OUT, 'exams', 'index.html'), 'w').write(idx)

# GRADE PAGES (grouped by unit)
for k, G in GRADES.items():
    gr = [r for r in recs if r['grade'] == k]
    if not gr: continue
    units = []
    for r in gr:
        if r['unit'] not in units: units.append(r['unit'])
    body = ''.join(f'<h2 class="unit-h">{esc(u)}</h2><div class="cards">{"".join(ecard(r) for r in gr if r["unit"] == u)}</div>' for u in units)
    others = ''.join(f'<a class="fbpill" href="{BASE}/exams/{G2["slug"]}">{G2["short"]}</a>' for k2, G2 in GRADES.items() if k2 != k and any(r["grade"] == k2 for r in recs))
    g = head(G['meta'] + ' | مستر محمد الجزار', G['desc'], BASE + '/exams/' + G['slug'],
             crumbs_ld([('الرئيسية', BASE + '/'), ('الملفات', BASE + '/exams/'), (G['short'], BASE + '/exams/' + G['slug'])])) + topbar('files') + f"""
<div class="wrap"><nav class="crumbs" aria-label="مسار التنقل"><a href="{BASE}/">الرئيسية</a> ‹ <a href="{BASE}/exams/">الملفات</a> ‹ {G['short']}</nav></div>
<div class="page-head"><div class="wrap"><h1>العلوم: {G['title']}</h1><p>الترم الأول · {CNT(k)}</p></div></div>
<section><div class="wrap">{body}
<div class="sec-head" style="margin-top:34px"><h2>صفوف تانية</h2></div><div class="otherg">{others}</div>
</div></section>
""" + FOOT
    open(os.path.join(OUT, 'exams', G['slug'] + '.html'), 'w').write(g)

# EXAM DETAIL PAGES
for r in recs:
    lbl, tc, tbg, ic = TYPES.get(r['typ'], TYPES['مراجعة'])
    G = GRADES[r['grade']]
    rel = [x for x in recs if x['grade'] == r['grade'] and x['eid'] != r['eid'] and x['unit'] == r['unit']][:4]
    relh = (f'<div class="sec-head" style="margin-top:34px"><h2>ملفات مرتبطة</h2><a class="more" href="{BASE}/exams/{G["slug"]}">كل ملفات {G["short"]} ←</a></div><div class="cards">{"".join(ecard(x) for x in rel)}</div>') if rel else ''
    ld = jld({"@context": "https://schema.org", "@type": "LearningResource", "name": r['name'], "url": CANON_BASE + f"/exams/e{r['eid']}", "inLanguage": "ar-EG",
              "learningResourceType": lbl, "educationalLevel": f"{G['title']} ({G['stage']})", "teaches": r.get('subj', 'العلوم'), "datePublished": iso(r['date']),
              "author": PERSON, "isAccessibleForFree": True, "sameAs": r['link']})
    pg = head(r['name'] + ' | مستر محمد الجزار', f"{r['name']} · {G['title']} · {r['term']} · من إعداد {TEACHER}.", BASE + f"/exams/e{r['eid']}",
              ld + crumbs_ld([('الرئيسية', BASE + '/'), ('الملفات', BASE + '/exams/'), (G['short'], BASE + '/exams/' + G['slug']), (r['name'], BASE + f"/exams/e{r['eid']}")])) + topbar('files') + f"""
<div class="wrap"><nav class="crumbs" aria-label="مسار التنقل"><a href="{BASE}/">الرئيسية</a> ‹ <a href="{BASE}/exams/">الملفات</a> ‹ <a href="{BASE}/exams/{G['slug']}">{G['short']}</a> ‹ {esc(lbl)}</nav></div>
<div class="page-head"><div class="wrap">
<span class="etype" style="--tc:{tc};--tbg:{tbg}">{ic} {esc(lbl)}</span>
<h1 style="margin-top:10px">{esc(r['name'])}</h1></div></div>
<section><div class="wrap">
<div class="meta-table">
<div class="row"><span class="k">المادة</span><span>{esc(r.get("subj","العلوم"))}</span></div>
<div class="row"><span class="k">الصف</span><span>{esc(r['grade'])} ({G['stage']})</span></div>
<div class="row"><span class="k">الفصل الدراسي</span><span>{esc(r['term'])}</span></div>
<div class="row"><span class="k">الوحدة</span><span>{esc(r['unit'])}</span></div>
{('<div class="row"><span class="k">الشهر</span><span>'+esc(r['month'])+'</span></div>') if r.get('month') else ''}
<div class="row"><span class="k">النوع</span><span>{esc(lbl)}</span></div>
<div class="row"><span class="k">تاريخ النشر</span><span>{esc(r['date'])}</span></div>
<div class="row"><span class="k">الإعداد والمصدر</span><span>إعداد: {TEACHER}</span></div>
</div>
<div style="text-align:center;margin-top:22px"><a class="btn btn-teal" style="background:#229ed9" href="{esc(r['link'])}" target="_blank" rel="noopener">فتح الملف على تليجرام</a></div>
{relh}
</div></section>
""" + FOOT
    open(os.path.join(OUT, 'exams', f"e{r['eid']}.html"), 'w').write(pg)

# COMMUNITY
def cl(n, u, k): return f'<a class="cm-l {k}" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>'
cm = head('مجتمع معلمي المواد العلمية | مستر محمد الجزار', 'روابط مجموعات وقنوات معلمي العلوم والمواد العلمية على فيسبوك وواتساب وتليجرام.', BASE + '/community',
          crumbs_ld([('الرئيسية', BASE + '/'), ('المجتمع', BASE + '/community')])) + topbar('comm') + f"""
<div class="wrap"><nav class="crumbs" aria-label="مسار التنقل"><a href="{BASE}/">الرئيسية</a> ‹ المجتمع</nav></div>
<div class="page-head"><div class="wrap"><h1>مجتمع معلمي المواد العلمية</h1><p>كل المجموعات والقنوات في مكان واحد</p></div></div>
<section><div class="wrap">
<div class="sec-head"><h2>تابع {esc(TEACHER)}</h2></div>
<div class="cm-card"><div class="cm-links">{''.join(cl(*x) for x in FOLLOW)}</div></div>
<div class="sec-head" style="margin-top:26px"><h2>مجموعات الفيسبوك</h2></div>
<div class="fbgrid">{''.join(f'<a class="fbpill" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in FB)}</div>
<div class="sec-head" style="margin-top:26px"><h2>مجموعات وقنوات المواد</h2></div>
<div class="cm-grid">{''.join('<div class="cm-card"><h3>'+esc(t)+'</h3><div class="cm-links">'+''.join(cl(*x) for x in ls)+'</div></div>' for t, ls in COMM)}</div>
</div></section>
""" + FOOT
open(os.path.join(OUT, 'community.html'), 'w').write(cm)

# 404
nf = head('الصفحة غير موجودة | مستر محمد الجزار', 'الصفحة المطلوبة غير موجودة.', BASE + '/404.html', '<meta name="robots" content="noindex">') + topbar() + f"""
<section><div class="wrap" style="text-align:center;padding:60px 0"><h1 style="color:var(--deep)">الصفحة دي مش موجودة</h1><p style="color:var(--mut);margin:12px 0 22px">ممكن الرابط اتغير. تقدر تدور على الملف من هنا.</p>
<a class="btn btn-teal" href="{BASE}/exams/">تصفح الملفات</a> <a class="btn btn-gold" href="{BASE}/">الرئيسية</a></div></section>
""" + FOOT
open(os.path.join(OUT, '404.html'), 'w').write(nf)

urls = [(BASE + '/', LASTMOD), (BASE + '/exams/', LASTMOD)] + [(BASE + '/exams/' + G['slug'], max(iso(r['date']) for r in recs if r['grade'] == k)) for k, G in GRADES.items() if any(r['grade'] == k for r in recs)] + [(BASE + '/community', LASTMOD)] + [(BASE + f'/exams/e{r["eid"]}', iso(r['date'])) for r in recs]
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'<url><loc>{u}</loc><lastmod>{m}</lastmod></url>' for u, m in urls) + '\n</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: ' + BASE + '/sitemap.xml\n')
open(os.path.join(OUT, 'googlee0bf8f8fe2eace5f.html'), 'w').write('google-site-verification: googlee0bf8f8fe2eace5f.html')
import shutil
if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'og.png')): shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'og.png'), os.path.join(OUT, 'og.png'))
print('OK', sum(len(f) for _, _, f in os.walk(OUT)), 'files in', OUT)
