"""Génère le site vitrine d'Illiyun (pages statiques, 3 langues).

    python build.py

Écrit fr/, ar/, en/ (index, privacy, delete-account, donate) et la page
racine index.html (choix de la langue). Rien à installer : Python 3 seul.
Modifier les textes ci-dessous, relancer, puis commiter les fichiers générés.
"""

from pathlib import Path

ROOT = Path(__file__).parent

# ── Réglages ─────────────────────────────────────────────────────────────
CONTACT_EMAIL = "contact@illiyun.app"
# Lien Google Play : None tant que l'app n'est pas publiée.
PLAY_URL = None
# Responsable du traitement (loi 09-08) : à compléter (nom, ville).
CONTROLLER = {
    "fr": "Noure ZENATI, éditeur de l'application Illiyun (Rabat, Maroc)",
    "en": "Noure ZENATI, publisher of the Illiyun app (Rabat, Morocco)",
    "ar": "Noure ZENATI، ناشر تطبيق عِلِّيُّون (الرباط، المغرب)",
}
# Numéro de déclaration CNDP : None tant qu'il n'existe pas.
CNDP_DECLARATION = None
UPDATED = {
    "fr": "25 octobre 2026",
    "en": "25 October 2026",
    "ar": "25 أكتوبر 2026",
}

LANGS = ["fr", "ar", "en"]
LANG_NAMES = {"fr": "Français", "ar": "العربية", "en": "English"}

# Sourate al-Muṭaffifīn 83:18-19, d'où vient le nom de l'app (texte Hafs du
# Mushaf, police Uthmanic Hafs ; les numéros sont dessinés dans la rosace).
VERSE_WORDS = [
    "كـَلَّآ", "إِنَّ", "كِتَٰبَ", "ٱلۡأَبۡرَارِ", "لَفِي", "عِلِّيِّينَ", "#١٨",
    "وَمَآ", "أَدۡرَىٰكَ", "مَا", "عِلِّيُّونَ", "#١٩",
]

STAR = (
    '<svg class="star" viewBox="0 0 28 28" aria-hidden="true">'
    '<path fill="none" stroke="currentColor" stroke-width="1.4" '
    'd="M7 7h14v14H7zM14 4.1 23.9 14 14 23.9 4.1 14z"/></svg>'
)

# ── Textes communs ───────────────────────────────────────────────────────
T = {
    "fr": {
        "nav_privacy": "Confidentialité",
        "nav_delete": "Supprimer un compte",
        "nav_donate": "Soutenir",
        "nav_contact": "Contact",
        "credits": (
            "Texte du Coran et polices : Complexe du Roi Fahd (KFGQPC), "
            "Quran Foundation. Tafsirs et traductions : QuranEnc, Quran.com, "
            "QUL. Dictionnaires : al-Mufradāt (OpenITI), Lane's Lexicon."
        ),
        "verse_ref": "Sourate al-Muṭaffifīn, versets 18 et 19",
        "home_title": "Illiyun, le Coran à lire et à comprendre",
        "home_desc": (
            "Application gratuite et sans publicité pour lire le Coran en "
            "Hafs ou en Warsh, page par page, avec tafsir, traductions et "
            "dictionnaire."
        ),
    },
    "en": {
        "nav_privacy": "Privacy",
        "nav_delete": "Delete an account",
        "nav_donate": "Support",
        "nav_contact": "Contact",
        "credits": (
            "Quran text and fonts: King Fahd Complex (KFGQPC), Quran "
            "Foundation. Tafsirs and translations: QuranEnc, Quran.com, QUL. "
            "Dictionaries: al-Mufradāt (OpenITI), Lane's Lexicon."
        ),
        "verse_ref": "Surah al-Muṭaffifīn, verses 18 and 19",
        "home_title": "Illiyun, the Quran to read and understand",
        "home_desc": (
            "A free, ad-free app to read the Quran in Hafs or Warsh, page by "
            "page, with tafsir, translations and a dictionary."
        ),
    },
    "ar": {
        "nav_privacy": "الخصوصية",
        "nav_delete": "حذف حساب",
        "nav_donate": "ادعم التطبيق",
        "nav_contact": "اتصل بنا",
        "credits": (
            "نص القرآن والخطوط: مجمع الملك فهد لطباعة المصحف الشريف، "
            "Quran Foundation. التفاسير والترجمات: QuranEnc وQuran.com وQUL. "
            "المعاجم: المفردات للراغب (OpenITI)، ومعجم لين."
        ),
        "verse_ref": "سورة المطففين، الآيتان 18 و19",
        "home_title": "عِلِّيُّون، القرآن قراءةً وفهمًا",
        "home_desc": (
            "تطبيق مجاني بلا إعلانات لقراءة القرآن برواية حفص أو ورش، صفحةً "
            "صفحة، مع التفسير والترجمات والمعجم."
        ),
    },
}

# ── Accueil ──────────────────────────────────────────────────────────────
HOME = {
    "fr": {
        "h1": "Illiyun",
        "lead": (
            "Lire le Coran page par page, tel qu'il est imprimé, puis "
            "comprendre chaque verset et chaque mot."
        ),
        "status": "Bientôt sur Google Play.",
        "play": "Télécharger sur Google Play",
        "body": f"""
<h2>Lire</h2>
<p>Le mushaf de Médine en Hafs, et le mushaf du Complexe du Roi Fahd en Warsh,
avec la mise en page exacte de chaque page. Chaque mot se touche : un appui le
marque, un double appui ouvre sa définition, un appui long marque tout le
verset.</p>
<p>Pour le confort des yeux : grand texte en Warsh, trait plus épais, contraste
élevé, mode sombre, et en Hafs les couleurs du tajwīd.</p>

<h2>Comprendre</h2>
<p>Pour chaque verset, un tafsir au choix (al-Muyassar, as-Saʿdī, Ibn Kathīr,
al-Mukhtaṣar en français et en anglais) et des traductions en français et en
anglais. Le verset s'affiche à sa place dans le mushaf, et chaque mot mène à
sa traduction mot à mot, à sa racine et à l'article d'al-Mufradāt ou de Lane.</p>

<h2>Garder le fil</h2>
<p>Reprise de la lecture là où vous vous êtes arrêté, signets de pages et de
versets, rappel quotidien. Un compte est facultatif : il sert seulement à
retrouver vos réglages et vos signets sur un autre téléphone.</p>

{STAR}

<h2>Gratuit, sans publicité</h2>
<p>Illiyun n'a ni publicité, ni fonction payante, ni mesure d'audience. Si
vous souhaitez participer à ses frais, la page <a href="donate.html">Soutenir</a>
explique comment.</p>
""",
    },
    "en": {
        "h1": "Illiyun",
        "lead": (
            "Read the Quran page by page, as it is printed, then understand "
            "each verse and each word."
        ),
        "status": "Coming soon to Google Play.",
        "play": "Get it on Google Play",
        "body": f"""
<h2>Read</h2>
<p>The Madinah mushaf in Hafs, and the King Fahd Complex mushaf in Warsh, with
the exact layout of every page. Every word responds to touch: a tap marks it, a
double tap opens its definition, a long press marks the whole verse.</p>
<p>For tired eyes: large text in Warsh, thicker strokes, high contrast, dark
mode, and tajweed colours in Hafs.</p>

<h2>Understand</h2>
<p>For each verse, a tafsir of your choice (al-Muyassar, as-Saʿdī, Ibn Kathīr,
al-Mukhtaṣar in English and French) and English and French translations. The
verse is shown in its place in the mushaf, and each word leads to its
word-by-word translation, its root and the entry in al-Mufradāt or Lane.</p>

<h2>Keep your place</h2>
<p>Resume where you stopped, bookmark pages and verses, get a daily reminder.
An account is optional: it only brings your settings and bookmarks to another
phone.</p>

{STAR}

<h2>Free, without ads</h2>
<p>Illiyun has no ads, no paid features and no audience tracking. If you would
like to help with its costs, the <a href="donate.html">Support</a> page
explains how.</p>
""",
    },
    "ar": {
        "h1": "عِلِّيُّون",
        "lead": (
            "اقرأ القرآن صفحةً صفحة كما هو في المصحف المطبوع، ثم افهم كل آية "
            "وكل كلمة."
        ),
        "status": "قريبًا على Google Play.",
        "play": "حمّله من Google Play",
        "body": f"""
<h2>القراءة</h2>
<p>مصحف المدينة برواية حفص، ومصحف مجمع الملك فهد برواية ورش، بترتيب كل صفحة
كما هو في المطبوع. كل كلمة تستجيب للمس: لمسة تُبرزها، ولمستان تفتحان معناها،
والضغط المطوّل يُبرز الآية كلها.</p>
<p>ولراحة العين: خط كبير في ورش، وحبر أعرض، وتباين عالٍ، ووضع داكن، وألوان
التجويد في حفص.</p>

<h2>الفهم</h2>
<p>لكل آية تفسير تختاره (الميسر، والسعدي، وابن كثير، والمختصر بالفرنسية
والإنجليزية)، مع ترجمات بالفرنسية والإنجليزية. تظهر الآية في موضعها من المصحف،
وكل كلمة تقود إلى ترجمتها كلمةً كلمة، وإلى جذرها، وإلى مادتها في المفردات أو
في معجم لين.</p>

<h2>متابعة القراءة</h2>
<p>استئناف القراءة من حيث توقفت، وعلامات للصفحات والآيات، وتذكير يومي. الحساب
اختياري، وفائدته الوحيدة أن تجد إعداداتك وعلاماتك على هاتف آخر.</p>

{STAR}

<h2>مجاني بلا إعلانات</h2>
<p>ليس في عِلِّيُّون إعلانات ولا ميزات مدفوعة ولا تتبّع للزوار. إن أردت المساهمة
في نفقاته، فصفحة <a href="donate.html">ادعم التطبيق</a> تشرح الطريقة.</p>
""",
    },
}

# ── Confidentialité ──────────────────────────────────────────────────────
def privacy(lang: str) -> tuple[str, str]:
    e = CONTACT_EMAIL
    mail = f'<a href="mailto:{e}">{e}</a>'
    cndp = CNDP_DECLARATION
    if lang == "fr":
        cndp_line = (
            f"<p>Déclaration auprès de la CNDP : {cndp}.</p>" if cndp else ""
        )
        return "Politique de confidentialité", f"""
<h1 class="page-title">Politique de confidentialité</h1>
<p class="updated">Mise à jour : {UPDATED['fr']}</p>

<h2>En bref</h2>
<p>Illiyun fonctionne sans compte. Sans compte, vos réglages, vos signets et vos
dernières pages restent sur votre téléphone. Il n'y a ni publicité, ni mesure
d'audience, ni revente de données.</p>

<h2>Sans compte</h2>
<ul>
<li><strong>Sur votre téléphone :</strong> réglages, signets, dernière page lue,
heure du rappel quotidien, suivi de la mémorisation (versets marqués, dates de
révision). Ces données ne quittent pas l'appareil et
disparaissent quand vous désinstallez l'app.</li>
<li><strong>Téléchargements :</strong> l'app télécharge des fichiers (pages du
mushaf Warsh, tafsirs, dictionnaire, polices du mushaf) depuis GitHub et Quran
Foundation. Comme pour toute page web, ces services voient l'adresse IP de
votre téléphone. Aucun identifiant n'est envoyé.</li>
<li><strong>Recherche :</strong> le texte que vous cherchez est envoyé au serveur
de recherche d'Illiyun, sans identifiant, pour trouver les versets.</li>
<li><strong>Rappel quotidien :</strong> notification programmée sur le
téléphone, sans serveur.</li>
<li><strong>Suivi de la récitation</strong> (si la fonction est disponible) : la
voix est traitée par le service de reconnaissance vocale de votre téléphone
(Google sur Android). Illiyun n'enregistre pas l'audio.</li>
<li><strong>Ville du ciel de l'accueil :</strong> le ciel suit le soleil de votre
ville. Par défaut, elle est déduite du fuseau horaire du téléphone, sans rien
demander. Vous pouvez aussi choisir votre ville dans une liste, ou appuyer sur
« Me localiser » : la position approximative du téléphone est alors lue une
fois, pour trouver la ville la plus proche. Seule la ville est gardée, sur le
téléphone ; la position n'est envoyée nulle part.</li>
</ul>

<h2>Avec un compte (facultatif)</h2>
<p>Le compte sert uniquement à retrouver vos réglages et vos signets sur un
autre téléphone. Il conserve :</p>
<ul>
<li>votre adresse e-mail, qui sert à vous connecter avec un code à usage
unique (pas de mot de passe) ;</li>
<li>vos réglages, vos signets, vos dernières pages lues et votre suivi de
mémorisation (état des versets, dates de révision des pages), avec leur date de
modification.</li>
</ul>
<p>Ces données sont hébergées par Supabase, dans l'Union européenne (Francfort,
Allemagne). Les codes de connexion sont envoyés par un service d'envoi
d'e-mails. Elles sont gardées tant que le compte existe et effacées à sa
suppression.</p>

<h2>Vos droits</h2>
<p>Vous pouvez accéder à vos données, les corriger ou les faire supprimer
(loi marocaine 09-08 et règles équivalentes). Pour supprimer votre compte, voir
<a href="delete-account.html">Supprimer un compte</a>. Pour toute autre demande :
{mail}.</p>

<h2>Responsable</h2>
<p>Le responsable du traitement est {CONTROLLER['fr']}. Contact : {mail}.</p>
{cndp_line}

<h2>Ce site</h2>
<p>Ce site ne dépose aucun cookie et ne mesure pas son audience. Il est hébergé
par GitHub Pages, qui reçoit l'adresse IP des visiteurs pour servir les
pages.</p>

<h2>Changements</h2>
<p>Toute modification de cette politique sera publiée sur cette page, avec sa
date.</p>
"""
    if lang == "en":
        cndp_line = (
            f"<p>Declaration to the CNDP (Morocco): {cndp}.</p>" if cndp else ""
        )
        return "Privacy policy", f"""
<h1 class="page-title">Privacy policy</h1>
<p class="updated">Updated: {UPDATED['en']}</p>

<h2>In short</h2>
<p>Illiyun works without an account. Without one, your settings, bookmarks and
last pages stay on your phone. There are no ads, no audience tracking and no
sale of data.</p>

<h2>Without an account</h2>
<ul>
<li><strong>On your phone:</strong> settings, bookmarks, last page read, daily
reminder time, memorisation tracking (marked verses, review dates). This data never leaves the device and is removed when you
uninstall the app.</li>
<li><strong>Downloads:</strong> the app downloads files (Warsh mushaf pages,
tafsirs, dictionary, mushaf fonts) from GitHub and Quran Foundation. As with any
web page, these services see your phone's IP address. No identifier is
sent.</li>
<li><strong>Search:</strong> the text you search for is sent to Illiyun's search
server, without any identifier, to find the verses.</li>
<li><strong>Daily reminder:</strong> a notification scheduled on the phone, with
no server.</li>
<li><strong>Recitation follow-along</strong> (where available): your voice is
processed by your phone's speech recognition service (Google on Android).
Illiyun does not record the audio.</li>
<li><strong>City of the home sky:</strong> the sky follows the sun of your city.
By default it is inferred from the phone's time zone, without asking anything.
You can also choose your city from a list, or tap “Locate me”: the phone's
approximate position is then read once, to find the nearest city. Only the city
is kept, on the phone; the position is sent nowhere.</li>
</ul>

<h2>With an account (optional)</h2>
<p>The account only brings your settings and bookmarks to another phone. It
stores:</p>
<ul>
<li>your email address, used to sign in with a one-time code (no
password);</li>
<li>your settings, bookmarks, last pages read and memorisation tracking (verse
states, page review dates), with the time they changed.</li>
</ul>
<p>This data is hosted by Supabase in the European Union (Frankfurt, Germany).
Sign-in codes are sent by an email delivery service. The data is kept while the
account exists and erased when it is deleted.</p>

<h2>Your rights</h2>
<p>You can access, correct or erase your data (Moroccan law 09-08 and
equivalent rules). To delete your account, see
<a href="delete-account.html">Delete an account</a>. For any other request:
{mail}.</p>

<h2>Controller</h2>
<p>The data controller is {CONTROLLER['en']}. Contact: {mail}.</p>
{cndp_line}

<h2>This website</h2>
<p>This website sets no cookies and does not track its visitors. It is hosted
by GitHub Pages, which receives visitors' IP addresses to serve the pages.</p>

<h2>Changes</h2>
<p>Any change to this policy will be published on this page, with its
date.</p>
"""
    cndp_line = (
        f"<p>رقم التصريح لدى اللجنة الوطنية لمراقبة حماية المعطيات ذات الطابع "
        f"الشخصي: {cndp}.</p>"
        if cndp
        else ""
    )
    return "سياسة الخصوصية", f"""
<h1 class="page-title">سياسة الخصوصية</h1>
<p class="updated">آخر تحديث: {UPDATED['ar']}</p>

<h2>باختصار</h2>
<p>يعمل عِلِّيُّون دون حساب. ومن غير حساب تبقى إعداداتك وعلاماتك وآخر صفحاتك على
هاتفك. لا إعلانات، ولا تتبّع للمستخدمين، ولا بيع للمعطيات.</p>

<h2>من غير حساب</h2>
<ul>
<li><strong>على هاتفك:</strong> الإعدادات، والعلامات، وآخر صفحة قرأتها، ووقت
التذكير اليومي، ومتابعة الحفظ (الآيات المعلَّمة ومواعيد المراجعة). لا تغادر هذه المعطيات الجهاز، وتُمحى عند حذف التطبيق.</li>
<li><strong>التنزيلات:</strong> ينزّل التطبيق ملفات (صفحات مصحف ورش، والتفاسير،
والمعجم، وخطوط المصحف) من GitHub ومن Quran Foundation. وكما في أي صفحة ويب،
ترى هذه الخدمات عنوان IP لهاتفك. ولا يُرسَل أي مُعرِّف.</li>
<li><strong>البحث:</strong> يُرسَل النص الذي تبحث عنه إلى خادم البحث الخاص
بعِلِّيُّون، دون أي مُعرِّف، للعثور على الآيات.</li>
<li><strong>التذكير اليومي:</strong> إشعار مبرمج على الهاتف نفسه، دون خادم.</li>
<li><strong>متابعة التلاوة</strong> (إن كانت متاحة): يعالج صوتَك نظامُ التعرّف
على الكلام في هاتفك (Google على أندرويد). ولا يسجّل عِلِّيُّون الصوت.</li>
<li><strong>مدينة سماء الصفحة الرئيسية:</strong> تتبع السماء شمس مدينتك. وتُستنتج
افتراضيًا من المنطقة الزمنية للهاتف دون طلب أي شيء. ويمكنك أيضًا اختيار مدينتك من
قائمة، أو الضغط على «حدِّد موقعي»: فيُقرأ الموقع التقريبي للهاتف مرة واحدة لمعرفة
أقرب مدينة. ولا تُحفظ إلا المدينة، على الهاتف؛ ولا يُرسَل الموقع إلى أي جهة.</li>
</ul>

<h2>مع حساب (اختياري)</h2>
<p>فائدة الحساب الوحيدة أن تجد إعداداتك وعلاماتك على هاتف آخر. وهو يحفظ:</p>
<ul>
<li>بريدك الإلكتروني، ويُستعمل للدخول برمز يُستعمل مرة واحدة (دون كلمة
مرور)؛</li>
<li>إعداداتك وعلاماتك وآخر صفحاتك ومتابعة حفظك (حالة الآيات ومواعيد مراجعة
الصفحات)، مع تاريخ تعديلها.</li>
</ul>
<p>تُستضاف هذه المعطيات لدى Supabase في الاتحاد الأوروبي (فرانكفورت، ألمانيا).
وتُرسَل رموز الدخول عبر خدمة لإرسال البريد. وتُحفظ ما دام الحساب قائمًا، وتُمحى
عند حذفه.</p>

<h2>حقوقك</h2>
<p>يحق لك الاطلاع على معطياتك وتصحيحها وطلب محوها (القانون المغربي 09-08 وما
يماثله). لحذف حسابك، انظر صفحة <a href="delete-account.html">حذف حساب</a>.
ولأي طلب آخر: {mail}.</p>

<h2>المسؤول</h2>
<p>المسؤول عن المعالجة هو {CONTROLLER['ar']}. للتواصل: {mail}.</p>
{cndp_line}

<h2>هذا الموقع</h2>
<p>لا يضع هذا الموقع أي ملفات تعريف ارتباط ولا يتتبّع زواره. وهو مستضاف على
GitHub Pages، التي تتلقى عناوين IP للزوار لعرض الصفحات.</p>

<h2>التعديلات</h2>
<p>يُنشر أي تعديل لهذه السياسة في هذه الصفحة مع تاريخه.</p>
"""


# ── Suppression de compte ────────────────────────────────────────────────
def delete_account(lang: str) -> tuple[str, str]:
    e = CONTACT_EMAIL
    if lang == "fr":
        subject = "Suppression de compte Illiyun"
        mail = f'<a href="mailto:{e}?subject={subject.replace(" ", "%20")}">{e}</a>'
        return "Supprimer un compte", f"""
<h1 class="page-title">Supprimer votre compte Illiyun</h1>
<p class="updated">Mise à jour : {UPDATED['fr']}</p>

<p>Le compte Illiyun est facultatif. Le supprimer efface définitivement, sur nos
serveurs : votre adresse e-mail, vos réglages synchronisés, vos signets, vos
dernières pages lues et votre suivi de mémorisation. Rien n'est conservé.</p>

<h2>Depuis l'application</h2>
<ol>
<li>Ouvrez les réglages : <span class="path">Settings</span>, ou
<bdi class="path" lang="ar">الإعدادات</bdi> si l'application est en
arabe.</li>
<li>Dans la section <span class="path">Account</span>
(<bdi class="path" lang="ar">الحساب</bdi>), touchez
<span class="path">Delete my account</span>
(<bdi class="path" lang="ar">حذف حسابي</bdi>).</li>
<li>Confirmez. La suppression est immédiate.</li>
</ol>

<h2>Sans l'application</h2>
<p>Écrivez à {mail} depuis l'adresse e-mail de votre compte, avec pour objet
« {subject} ». Votre compte et ses données sont supprimés dans un délai de
30 jours, et vous recevez une confirmation par e-mail.</p>

<h2>Sur votre téléphone</h2>
<p class="note">Les réglages et signets enregistrés sur le téléphone restent
sur l'appareil, même sans compte. Ils disparaissent quand vous désinstallez
l'application.</p>
"""
    if lang == "en":
        subject = "Illiyun account deletion"
        mail = f'<a href="mailto:{e}?subject={subject.replace(" ", "%20")}">{e}</a>'
        return "Delete an account", f"""
<h1 class="page-title">Delete your Illiyun account</h1>
<p class="updated">Updated: {UPDATED['en']}</p>

<p>An Illiyun account is optional. Deleting it permanently erases, on our
servers: your email address, your synced settings, your bookmarks, your last
pages read and your memorisation tracking. Nothing is kept.</p>

<h2>From the app</h2>
<ol>
<li>Open <span class="path">Settings</span>.</li>
<li>In the <span class="path">Account</span> section, tap
<span class="path">Delete my account</span>.</li>
<li>Confirm. Deletion is immediate.</li>
</ol>

<h2>Without the app</h2>
<p>Write to {mail} from your account's email address, with the subject
“{subject}”. Your account and its data are deleted within 30 days, and you
receive a confirmation by email.</p>

<h2>On your phone</h2>
<p class="note">Settings and bookmarks saved on the phone stay on the device,
even without an account. They are removed when you uninstall the app.</p>
"""
    subject = "حذف حساب عليون"
    mail = f'<a href="mailto:{e}?subject={subject.replace(" ", "%20")}">{e}</a>'
    return "حذف حساب", f"""
<h1 class="page-title">حذف حسابك في عِلِّيُّون</h1>
<p class="updated">آخر تحديث: {UPDATED['ar']}</p>

<p>الحساب في عِلِّيُّون اختياري. وحذفه يمحو نهائيًا من خوادمنا: بريدك الإلكتروني،
وإعداداتك المتزامنة، وعلاماتك، وآخر صفحاتك، ومتابعة حفظك. ولا يُحتفظ بشيء.</p>

<h2>من التطبيق</h2>
<ol>
<li>افتح <span class="path">الإعدادات</span>.</li>
<li>في قسم <span class="path">الحساب</span>، المس
<span class="path">حذف حسابي</span>.</li>
<li>أكّد. يتم الحذف فورًا.</li>
</ol>

<h2>من غير التطبيق</h2>
<p>راسلنا على {mail} من البريد الإلكتروني المرتبط بحسابك، بعنوان
«{subject}». يُحذف حسابك ومعطياته في أجل أقصاه 30 يومًا، وتصلك رسالة تأكيد.</p>

<h2>على هاتفك</h2>
<p class="note">تبقى الإعدادات والعلامات المحفوظة على الهاتف في الجهاز، حتى دون
حساب، وتُمحى عند حذف التطبيق.</p>
"""


# ── Soutenir ─────────────────────────────────────────────────────────────
def donate(lang: str) -> tuple[str, str]:
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
    if lang == "fr":
        return "Soutenir", f"""
<h1 class="page-title">Soutenir Illiyun</h1>
<p>Illiyun est gratuit, sans publicité et sans fonction payante, et le restera.
Les dons servent à le faire fonctionner et à l'améliorer : serveurs, envoi des
e-mails de connexion, publication sur les boutiques d'applications, travail sur
de nouvelles fonctions.</p>
<p>Les dons en ligne ouvriront prochainement sur cette page. D'ici là, pour
proposer votre aide, écrivez à {mail}.</p>
<p class="note">Faire connaître l'application autour de vous, ou signaler une
erreur dans le texte, est aussi une aide précieuse.</p>
"""
    if lang == "en":
        return "Support", f"""
<h1 class="page-title">Support Illiyun</h1>
<p>Illiyun is free, without ads and without paid features, and will stay that
way. Donations keep it running and improving: servers, sign-in emails, app
store publication, work on new features.</p>
<p>Online donations will open on this page soon. Until then, to offer your
help, write to {mail}.</p>
<p class="note">Telling others about the app, or reporting a mistake in the
text, is valuable help too.</p>
"""
    return "ادعم التطبيق", f"""
<h1 class="page-title">ادعم عِلِّيُّون</h1>
<p>عِلِّيُّون مجاني بلا إعلانات ولا ميزات مدفوعة، وسيبقى كذلك. وتعين التبرعات على
تشغيله وتحسينه: الخوادم، ورسائل الدخول، والنشر في متاجر التطبيقات، والعمل على
ميزات جديدة.</p>
<p>سيُفتح باب التبرع عبر الإنترنت قريبًا في هذه الصفحة. وإلى ذلك الحين، إن أردت
المساعدة فراسلنا على {mail}.</p>
<p class="note">والتعريف بالتطبيق لمن حولك، أو التنبيه على خطأ في النص، عونٌ
ثمين كذلك.</p>
"""


# ── Gabarit ──────────────────────────────────────────────────────────────
def verse_html() -> str:
    parts = []
    for w in VERSE_WORDS:
        if w.startswith("#"):
            parts.append(f'<span class="w mark">{w[1:]}</span>')
        else:
            parts.append(f'<span class="w">{w}</span>')
    return " ".join(parts)


def page(lang: str, slug: str, title: str, body: str, hero: str = "") -> str:
    t = T[lang]
    rtl = ' dir="rtl"' if lang == "ar" else ""
    langs = "\n".join(
        f'<li><a href="../{l}/{slug}" lang="{l}"'
        + (' aria-current="true"' if l == lang else "")
        + f">{LANG_NAMES[l]}</a></li>"
        for l in LANGS
    )
    full_title = t["home_title"] if slug == "index.html" else f"{title} — Illiyun"
    return f"""<!doctype html>
<html lang="{lang}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{t['home_desc']}">
<meta name="theme-color" content="#0b5d4b">
<link rel="icon" href="../assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="top">
<div class="wrap">
<a class="brand" href="index.html">{'عِلِّيُّون' if lang == 'ar' else 'Illiyun'}</a>
<ul class="langs">
{langs}
</ul>
</div>
</header>
{hero}
<main>
<div class="wrap">
{body}
</div>
</main>
<footer>
<div class="wrap">
<nav aria-label="{t['nav_contact']}">
<ul>
<li><a href="privacy.html">{t['nav_privacy']}</a></li>
<li><a href="delete-account.html">{t['nav_delete']}</a></li>
<li><a href="donate.html">{t['nav_donate']}</a></li>
<li><a href="mailto:{CONTACT_EMAIL}">{t['nav_contact']}</a></li>
</ul>
</nav>
<p class="credits">{t['credits']}</p>
</div>
</footer>
{'<script src="../assets/flow.js" defer></script>' if hero else ''}
</body>
</html>
"""


def home(lang: str) -> str:
    h = HOME[lang]
    t = T[lang]
    cta = (
        f'<p class="status"><a href="{PLAY_URL}" style="color:inherit">{h["play"]}</a></p>'
        if PLAY_URL
        else f'<p class="status">{h["status"]}</p>'
    )
    hero = f"""<section class="hero">
<div class="wrap">
<p class="verse" lang="ar">{verse_html()}</p>
<p class="verse-ref">{t['verse_ref']}</p>
<h1>{h['h1']}</h1>
<p class="lead">{h['lead']}</p>
{cta}
</div>
</section>"""
    return page(lang, "index.html", h["h1"], h["body"], hero)


def root_index() -> str:
    links = " ".join(
        f'<a href="{l}/" lang="{l}">{LANG_NAMES[l]}</a>' for l in LANGS
    )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Illiyun — عِلِّيُّون</title>
<meta http-equiv="refresh" content="2; url=fr/">
<script>
// Langue du navigateur : arabe, anglais, sinon français.
(function () {{
  var l = (navigator.language || "fr").slice(0, 2);
  location.replace(l === "ar" ? "ar/" : l === "en" ? "en/" : "fr/");
}})();
</script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main><div class="wrap"><p>{links}</p></div></main>
</body>
</html>
"""


def main() -> None:
    for lang in LANGS:
        out = ROOT / lang
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(home(lang), encoding="utf-8")
        for slug, fn in (
            ("privacy.html", privacy),
            ("delete-account.html", delete_account),
            ("donate.html", donate),
        ):
            title, body = fn(lang)
            (out / slug).write_text(page(lang, slug, title, body), encoding="utf-8")
    (ROOT / "index.html").write_text(root_index(), encoding="utf-8")
    print("Site généré :", ", ".join(LANGS))


if __name__ == "__main__":
    main()
