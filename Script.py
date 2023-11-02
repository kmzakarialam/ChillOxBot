# @km-zakaria-alam-akib


class script(object):
    START_TXT = """<b>Hello {}, My Name <a href=https://t.me/{}>{}</a>, I'm a Powerful Auto Filter Bot Bot + File Store Bot + Manual Filter + Video Search and Download Bot</b>"""

    HELP_TXT = """<b>Hey {}
Here is The Help For My Commands...!</b>"""

    ABOUT_TXT = """<b>⍟───[ My Details ]───⍟
‣ My Name : <a href=https://t.me/ChillOxBot>ChillOx Bot</a>
 ‣ My Best Friend : <a href='tg://settings'>This Person</a> 
 ‣ Developer : <a href='https://t.me/THExAkib'>AKIB</a> 
 ‣ Library : <a href='https://docs.pyrogram.org/'>Pyrogram</a> 
 ‣ Language : <a href='https://www.python.org/download/releases/3.0/'>Python3</a> 
 ‣ Database : <a href='https://www.mongodb.com/'>MongoDB</a> 
 ‣ Bot Server : <a href='https://heroku.com'>Heroku</a> 
 ‣ Build Status : ᴠ2.7.1 [ Stable ]</b>"""

    SOURCE_TXT = """
<b>Hey, This Is a Open Project

This Bot Has Latest and Advanced Features⚡️

Where is Source Code? - <a href='https://github.com/km-zakaria-alam-akib/ChillOxBot'>Click Here</a></b>


Developer - <a href='https://t.me/THExAkib'>Click Here</a></b>"""



    MANUELFILTER_TXT = """Help: <b>Filter</b>
- Filter is a Feature Where Users Can Set Automated Replies For Purticular Keywards and I Respond Whenever a Keyward Found in the Message
<b>Note :</b>
1. This Bot SHould Have Admin Privilage
2. Only Admins Can Add Filters to a Chat
3. Alert Buttons Have Limit of 64 Characters
Coomands and Usage:
• /filter - Add a Filter in a Chat
• /filters - List of All Filter in a Chat
• /del - Delete a Specific Filter in a Chat
• /delall - Delete The Whole Filter in a Chat (Chat Owner Only)"""




    BUTTON_TXT = """Help: <b>Button</b>
 This Bot Supports Bot URL and Alert Inline Buttons
<b>Note :</b>
1. Telegram Will Not Allow To Send Buttons Without and Content, So Content It's Mandattory.
2. This Bot Supports Buttons With any Telegram Media Type.
3. Buttons Should Be Properly Parsed as Markdown Format
<b>URL Buttons:</b>
[Button Text](buttonurl:https://t.me/telegram.me/kingupdates2/3)
<b>ᴀʟᴇʀᴛ Buttons:</b>
[Button Text](buttonalert: This is an Alert Message)"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>Note : File Index</b>
1. Make The Admin Of Your Channel If It's private
2. Make Sure That Your Channel Does Not Contain Any Camrips, Porn or Fake Files.
3. Forward The Last message With Quotes. I'll add All Files in That Channel To My DB.

<b>Note : Auto Filter</b>
1. Add The Bot as Admin In Your Group
2. Use/Connect and Connect Your Group To The Bot
3. Use/Settings on Bot's PM and Turn On Auto Filter On The Settings Menu"""

    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to Connect Bot to PM For Managing Filters 
- lIt Helps To Avoid Spaming In Groups
<b>Note :</b>
1. Only Admin Can Add a Connection
2. Send /Connect For Connecting Me to Your PM
Coomands and Usage:
• /connect  - Connect a Particular Chat to Your PM
• /disconnect  - Disconnect From a Chat
• /connections - List of All Your Connections"""


    EXTRAMOD_TXT = """Help: Extra Modules
<b>Note :</b>
my features Stay here new features coming soon...  
 <b>✯ Maintained by : <a href=https://t.me/THExAkib>AKIB</a></b>
  
 <b>✯ Join here : <a href=https://t.me/Korean_Drama_In_Hindi_Dubbed_4u>Join Main Channel</a></b> 
  
 ./id - Get a ID of a Specific User</ 
 code> 
  
 ./info  - Get Infomation about a User 
  
 ./song - Download any song [example /song Song Name] 
  
 ./telegraph - Telegraph Generator: Send under 5MB video or photo I'll give telegraph link 
  
 ./tts - This command usage text to voice converter 
  
 ./video - This command usage any YouTube video download hd [example /video YouTube Video Link]

./font - This command usage stylish and cool font generator [example /font Hi]"""


    ADMIN_TXT = """Help: Amdin MODS
<b>Note :</b>
This Module Only Works For My Admins
Coomands and Usage:
• /logs - To Get The Recent Errors
• /stats - To Get Status of Files In DB. [This Command Can Be Used By Anyone]
• /delete - To Delete a Specific Files From DB.
• /users - To Get List of My Users and IDs
• /chats - To Get List Of My Chats and IDs
• /leave  - To Leave From a Chat
• /disable  -  To Disable a Chat
• /ban  - To Ban a User
• /unban  - To Unban a User
• /channel - To Get List Of Total Connected Channels/Groups
• /broadcast - To Broadcast Messages To Users
• /grp_broadcast - To Broadcast Messages To All Connected Groups
• /gfilter - To Add Global Filters
• /gfilters - To View List of Global Filters
• /delg - To Delete a Specific Filter
• /request - To Send a Movie/Series Request To Bot Admins. Only Works on Support Group. [This Command Can Be Used By Anyone]
• /delallg - To Delete all GFilters From Bot's Database.
• /deletefiles - To Delete Camrip and PreDVD Files From The Bot's Database"""

    STATUS_TXT = """<b>★ Total Files: {}
★ Total Users: {}
★ Total Chats: {}
★ Used Storage: {}
★ Free Storage: {}</b>"""

    LOG_TEXT_G = """#NewGroup
Grooup = {}({})
Total Members = {}
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - {}
Name - {}"""

    ALRT_TXT = """Hello {},
This is Not Your Movie Request,
Request Your's...!"""

    OLD_ALRT_TXT = """Hey {},
You Are Using One Of My Old Message, 
Please Send The Request Again"""

    CUDNT_FND = """I Couldn't Find Anything Related TO {}
Did You Mean Any One of These?"""

    I_CUDNT = """<b>Sorry No Files were Found at Your Request {} 😕

Check Your Spelling in Google and Try Again 😃

Movie Request Format 👇

Example : Uncharted or Uncharted 2022 or Uncharted En

Series Request Format 👇

Example : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 Don't Use ➠ ':(!,./)</b>"""

    I_CUD_NT = """I Couldn't Find any Movie Related To {}.
Please Check the Spelling on Google or IMDb...!"""

    MVE_NT_FND = """Movie Not Found In Database...!"""

    TOP_ALRT_MSG = """Checking For Movie In The Database...!"""

    MELCOW_ENG = """<b>Hello {} 😍, and Welcome To {} Grooup ❤️</b>"""

    SHORTLINK_INFO = """

🫵 Select Your Language And Earn Money 💰"""

    REQINFO = """
⚠ Information ⚠

after 5 Minutes This Message Will Be Automatically Deleted

If You Don't See The Requested Movie / Series File, Look at The Next Page"""

    SELECT = """
Movies ➢ Select "Languages"

Series ➢ Select "Seasons"

Tip: Select "Languages" or "Seasons" Button and Click "Send All" To Gel All FIles Link in a SIngle Click"""

    SINFO = """
🫣 Movie Venumna Join Panni Try Again Buttana Click Pannu!😅"""

    NORSLTS = """ 
★ No Results ★

ID <b>: {}</b>

Name <b>: {}</b>

Messsage <b>: {}</b>"""

    CAPTION = """<b>📂 File Name : {file_name}

<b> Size ⚙️: {file_size}</b>""" 

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : {languages}
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : {countries}


⏰ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by : {message.from_user.mention}</b>"""
    
    ALL_FILTERS = """
<b>Hey {}, These are my Three Types Of Filter</b>"""
    
    GFILTER_TXT = """
<b>Welcome To Global Filters. Global Filters are The Filters Set By Admin Which will Work in Every Groups</b>
    
Available Commands:
• /gfilter - To Create a Global Filter
• /gfilters - To View All Global Filters
• /delg - To Delete a Particular Global Filter
• /delallg - To Delete Global Filters"""
    
    FILE_STORE_TXT = """
<b>File Store Is a FeatureWhich Will Create a Shareable Link  of Single or Miltiple Files</b>

Available Commands:
• /batch - To Create a Batch Link or Multiple Links
• /link - To Create a Single File Store Link
• /pbatch - Just Like /batch, But The Files Will Be Send With Forward Restictions
• /plink - Just Like /link, But The File Will Be Send With Forward Restictions"""

    SONG_TXT = """<b>Song Download Module</b> 
      
 <b>Song Download Module, For Those Who Love Music. You Can Use This Feature To Download and Songs at Super Speed.Works In Bot and group Only...!</b> 
  
 <b>Commands</b> :<b>/song Song Name</b></b>""" 
  
    YTDL_TXT = """<b>Helps You To Download Videos From YouTube 
  
 Usage : You Can Download Videos from YouTube
  
How To Use: Type - /video or /mp4 
  
 Example :/mp4 YouTube Video Link</b>""" 
  
    TTS_TXT = """<b>TTS 🎤 Module : Translate Text To Speech 
  
 Commands and Usage : /tts Convert Text To Speech</b>""" 
  
    GTRANS_TXT = """<b>Help: Google Translator
  
This Command Helps You To Translate Codes To text In Any Language You Want. This Command Works Both in Group and PM
  
 Commands and Usage : /tr - To Translate Codes To a Specific Language
  
 Note : While Using /tr You Should Specify The Language Code 
  
 Example: /tr Ml 
 • En = English 
 • Ml = Malaylam 
 • Hi = Hindi</b>""" 
  
    TELE_TXT = """<b>Help: Telegraph Do As You Wish With Telegra.ph Module! 
  
 Usage: /telegraph - Send Me Picture or Video Under (5MB)
  
 Note : 
This Command Is Available In Groups and PMs
This Command Can Be Used By Everyone</b>""" 
  
    CORONA_TXT = """<b>Help: Covid 
  
 This Command Helps You To Know Daily Infomation About Covid
  
 Commands and Usage: 
  
 /covid - use This Command With Your Country Name To Get Covid Information 
 Example:/covid India 
  
 ⚠️ The Service Has Been Stopped 
  
 </b>""" 
  
    ABOOK_TXT = """<b>Help: Aduio Book 
  
You Can Convert Any PDF File To Audio FIle Using This Command ✯ 
  
 Commands and Usage: 
 /audiobook: Reply This Command To Any PDF To Generate Any Audio
</b>""" 
  
 
    PINGS_TXT = """<b>Ping Testing : Helps You To Know Your Ping🪄 
  
 Commands: 
 • /alive - To Check I'm Alive or Not
 • /help - To Get Help
 • /ping - To Get Your Ping
  
 Usage : 
 • This Command Can Be Used In Groups and PM 
 • This Command Can Be Used By Everyone In Groups or Bots PM
 • Share Us For More Features
  </b>""" 
  
    STICKER_TXT = """<b>You Can Use This Module To Find Any Sticker ID. 
 • Usage : To Get Sticker 
   
 ⭕ How To Use
 ◉ Reply To Any Sticker [/stickerid]  
 </b>""" 
  
    FONT_TXT= """<b>Usage 
  
 You Can Use This Module To Change Font Style   
  
 Command : /font Your Text (Optional)
 EG:- /font Hello 
  
 </b>""" 
  
    PURGE_TXT = """<b>Purge 
      
Delete a Lot Of Messages From a Group!  
      
  Admin  
  
 ◉ /purge :- Delete All Messages From  All Replied Messages, To The Currrent Message</b>""" 
  
    WHOIS_TXT = """<b>ho Is Module
  
 Note :- Give Me User Details 
 /whois :- Give Me User Full Details 📑 
 </b>""" 
  
    JSON_TXT = """<b> 
 JSON:  
Bot Return JSON For All Replied Messages With /json
  
 Features: 
  
1. Message Editing JSON
2. PM Support
3. Group Support 
  
 Note : 
  
 Everyone Can Use This Command, If Spamming Happens Bot Will Automatically Ban You From The Group</b>""" 
  
    URLSHORT_TXT = """<b>Help: URL Shortner
  
 <i><b>This Command Helps You To Make Short YRL</i></b> 
  
 Commands and Usage: 
  
 /short: <b>Use This Command With Your Link to get Short Links</b> 
 Example:/short YouTube Video Link</b>""" 
  
    CARB_TXT = """<b>Help For Carbon
  
Carbon Is a Feature to Make the Imageas Shown in The Top Of The Texts 
For Using The Module Just Send Me Text and OpenAI It With Carbon Command The Bot will Replay with The Carbon Image
</b>""" 
    GEN_PASS = """<b>Help: Password Genarator
  
There's Nothing To Know More. Send Me Yoour password Limit
 - I'll Give The Password of That Limit
  
Commands and Usages: 
 • /genpassword or /genpw 20
  
 NOTE:
 • Only Digits are Allowed
 • Maximum Allowed Digits Till 84
 (I Can't Genarate Password Above Length 34))
 • IMDb Should Have Admin Previlage
 • These Command Works Both PM and Group
 • These Command Can Be Used By Any Group Member</b>""" 
  
    SHARE_TXT = """<b>/share {Your Text}
  
 - Ex :- /share hi da 
  
 </b>""" 
  
    PIN_TXT = """<b>Pin Module 
 Pin a Message...!
  
 All Pin Related Commands Can Be Found Here:
  
 📌Command and Usages📌 
  
 /pin :- To Pin Message In Your Chat
 /unpin :- To Unpin The Current Pinned Messege</b>"""

 
    RESTART_TXT = """
<b>Bot Restarted!

📅 Date : {}
⏰ Time : {}
🌐 Timezone : Asia/Kolkata
🛠️ Build Status : 2.7.1 [ Stable ]</b>"""

    LOGO = """

BOT WORKING PROPERLY"""
 
    TAMIL_INFO = """
ஏய் <a href='tg://settings'>My Friend</a> 


 இப்போது டெலிகிராமிலும் பணம் சம்பாதிக்கலாம்.

 தந்தி மூலம் பணம் சம்பாதிக்க உங்களிடம் 1 குழு இருக்க வேண்டும்.
 உங்களிடம் குழு இருந்தால், எங்கள் bot ஐ உங்கள் குழுவில் சேர்ப்பதன் மூலம் நீங்கள் பணம் சம்பாதிக்கலாம்.

 உங்கள் குழுவில் அதிக உறுப்பினர்கள் இருந்தால், உங்கள் வருமானம் அதிகரிக்கும்.

 எப்படி மற்றும் என்ன செய்ய வேண்டும்

 படி 1: இந்த ChillOxBot போட் உங்கள் குழுவை நிர்வாகியாக்குங்கள்

 படி 2: உங்கள் இணையதளம் மற்றும் API ஐச் சேர்க்கவும்

 Exp: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 வீடியோவைச் சேர்க்கவும்

 👇 எப்படி சேர்ப்பது 👇

 Exp: /set_tutorial video link

மேலும் உங்கள் குழுவில் பயிற்சி வீடியோ தொகுப்பு ஆகிடும்..."""

    ENGLISH_INFO = """
Hey <a href='tg://settings'>My Friend</a> 


 Now you can earn money on Telegram too.

 You must have 1 group to earn money by telegram.
 If you have a group, you can earn money by adding our bot to your group.

 The more members you have in your group, the higher your income will be.

 How and what to do

 Step 1: Administer this ChillOxBot bot to your group

 Step 2: Add your website and API

 Exp: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 Add a video

 👇 How to add 👇

 Exp: /set_tutorial video link

Also your tutorial will be Added Your Group..."""

    TELUGU_INFO = """
హే <a href='tg://settings'>My Friend</a> 


 ఇప్పుడు మీరు టెలిగ్రామ్‌లో కూడా డబ్బు సంపాదించవచ్చు.

 టెలిగ్రామ్ ద్వారా డబ్బు సంపాదించడానికి మీరు తప్పనిసరిగా 1 గ్రూప్‌ని కలిగి ఉండాలి.
 మీకు గ్రూప్ ఉన్నట్లయితే, మా బాట్‌ను మీ గ్రూప్‌కి జోడించడం ద్వారా మీరు డబ్బు సంపాదించవచ్చు.

 మీ గ్రూప్‌లో ఎంత ఎక్కువ మంది సభ్యులు ఉంటే మీ ఆదాయం అంత ఎక్కువగా ఉంటుంది.

 ఎలా మరియు ఏమి చేయాలి

 దశ 1: ఈ ChillOxBot బాట్‌ని మీ సమూహానికి నిర్వహించండి

 దశ 2: మీ వెబ్‌సైట్ మరియు APIని జోడించండి

 గడువు: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 వీడియోను జోడించండి

 👇 ఎలా జోడించాలి 👇

 గడువు: /set_tutorial వీడియో లింక్

అలాగే మీ బృందం వీడియో సేకరణకు శిక్షణ ఇస్తుంది..."""

    HINDI_INFO = """
अरे <a href='tg://settings'>My Friend</a> 


 अब आप टेलीग्राम पर भी पैसे कमा सकते हैं।

 टेलीग्राम से पैसे कमाने के लिए आपके पास 1 ग्रुप होना चाहिए।
 यदि आपके पास एक समूह है, तो आप हमारे बॉट को अपने समूह में जोड़कर पैसा कमा सकते हैं।

 आपके समूह में जितने अधिक सदस्य होंगे, आपकी आय उतनी ही अधिक होगी।

 कैसे और क्या करना है

 चरण 1: इस थैलेपैथी-फ़िल्टर-बॉट बॉट को अपने समूह में प्रशासित करें

 चरण 2: अपनी वेबसाइट और एपीआई जोड़ें

 एक्सप: /शॉर्टलिंक omegalinks.in 4b392f8eb6ad711fbe58

 एक वीडियो जोड़ें

 👇कैसे जोड़ें 👇

 ऍक्स्प: /set_tutorial वीडियो लिंक

साथ ही आपकी टीम वीडियो संग्रह का प्रशिक्षण भी देगी..."""

    MALAYALAM_INFO = """
ഹേയ് <a href='tg://settings'>My Friend</a> 


 ഇപ്പോൾ നിങ്ങൾക്ക് ടെലിഗ്രാമിലും പണം സമ്പാദിക്കാം.

 ടെലിഗ്രാം വഴി പണം സമ്പാദിക്കാൻ നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടായിരിക്കണം.
 നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് ഞങ്ങളുടെ ബോട്ട് ചേർത്തുകൊണ്ട് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം.

 നിങ്ങളുടെ ഗ്രൂപ്പിൽ കൂടുതൽ അംഗങ്ങൾ ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ വരുമാനം ഉയർന്നതായിരിക്കും.

 എങ്ങനെ, എന്ത് ചെയ്യണം

 ഘട്ടം 1: ഈ തലപതി-ഫിൽട്ടർ-ബോട്ട് ബോട്ട് നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് നൽകുക

 ഘട്ടം 2: നിങ്ങളുടെ വെബ്‌സൈറ്റും API-യും ചേർക്കുക

 കാലഹരണപ്പെടൽ: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 ഒരു വീഡിയോ ചേർക്കുക

 👇 എങ്ങനെ ചേർക്കാം 👇

 കാലഹരണപ്പെടൽ: /set_tutorial വീഡിയോ ലിങ്ക്

നിങ്ങളുടെ ടീം വീഡിയോ ശേഖരണവും പരിശീലിപ്പിക്കും..."""

    URTU_INFO = """
 <a href='tg://settings'>My Friend</a> 


 اب آپ ٹیلی گرام پر بھی پیسے کما سکتے ہیں۔

 ٹیلی گرام کے ذریعے پیسے کمانے کے لیے آپ کے پاس 1 گروپ ہونا ضروری ہے۔
 اگر آپ کا کوئی گروپ ہے، تو آپ ہمارے بوٹ کو اپنے گروپ میں شامل کر کے پیسے کما سکتے ہیں۔

 آپ کے گروپ میں جتنے زیادہ ممبر ہوں گے آپ کی آمدنی اتنی ہی زیادہ ہوگی۔

 کیسے اور کیا کرنا ہے۔

 مرحلہ 1: اپنے گروپ میں اس ChillOxBot بوٹ کا انتظام کریں۔

 مرحلہ 2: اپنی ویب سائٹ اور API شامل کریں۔

 Exp: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 ایک ویڈیو شامل کریں۔

 👇 کیسے شامل کریں 👇

 Exp: /set_tutorial ویڈیو لنک

نیز آپ کی ٹیم ویڈیو جمع کرنے کی تربیت دے گی..."""

    GUJARATI_INFO = """
અરે <a href='tg://settings'>My Friend</a> 


 હવે તમે ટેલિગ્રામ પર પણ પૈસા કમાઈ શકો છો.

 ટેલિગ્રામ દ્વારા પૈસા કમાવવા માટે તમારી પાસે 1 જૂથ હોવું આવશ્યક છે.
 જો તમારી પાસે જૂથ છે, તો તમે અમારા બોટને તમારા જૂથમાં ઉમેરીને પૈસા કમાઈ શકો છો.

 તમારા જૂથમાં તમારા જેટલા વધુ સભ્યો હશે તેટલી તમારી આવક વધુ હશે.

 કેવી રીતે અને શું કરવું

 પગલું 1: તમારા જૂથમાં આ ChillOxBot બોટનું સંચાલન કરો

 પગલું 2: તમારી વેબસાઇટ અને API ઉમેરો

 સમાપ્તિ: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 વિડિઓ ઉમેરો

 👇 કેવી રીતે ઉમેરવું 👇

 સમાપ્તિ: /set_tutorial વિડિઓ લિંક

તેમજ તમારી ટીમ વિડિયો કલેક્શનની તાલીમ આપશે..."""

    KANNADA_INFO = """
ಹೇ {message.from_user.mention}

 ಈಗ ನೀವು ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿಯೂ ಹಣ ಗಳಿಸಬಹುದು.

 ಟೆಲಿಗ್ರಾಮ್ ಮೂಲಕ ಹಣ ಗಳಿಸಲು ನೀವು 1 ಗುಂಪನ್ನು ಹೊಂದಿರಬೇಕು.
 ನೀವು ಗುಂಪನ್ನು ಹೊಂದಿದ್ದರೆ, ನಮ್ಮ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಗಳಿಸಬಹುದು.

 ನಿಮ್ಮ ಗುಂಪಿನಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಸದಸ್ಯರನ್ನು ಹೊಂದಿದ್ದರೆ, ನಿಮ್ಮ ಆದಾಯವು ಹೆಚ್ಚಾಗುತ್ತದೆ.

 ಹೇಗೆ ಮತ್ತು ಏನು ಮಾಡಬೇಕು

 ಹಂತ 1: ಈ ಥಲಪತಿ-ಫಿಲ್ಟರ್-ಬಾಟ್ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ನಿರ್ವಹಿಸಿ

 ಹಂತ 2: ನಿಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು API ಸೇರಿಸಿ

 ಅವಧಿ: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 ವೀಡಿಯೊ ಸೇರಿಸಿ

 👇 ಸೇರಿಸುವುದು ಹೇಗೆ 👇

 ಅವಧಿ: /set_tutorial ವೀಡಿಯೊ ಲಿಂಕ್

ನಿಮ್ಮ ತಂಡವು ವೀಡಿಯೋ ಸಂಗ್ರಹಣೆಗೆ ತರಬೇತಿ ನೀಡಲಿದೆ..."""

    BANGLADESH_INFO = """
আরে <a href='tg://settings'>My Friend</a> 

 এখন আপনি টেলিগ্রামেও অর্থ উপার্জন করতে পারেন।

 টেলিগ্রামের মাধ্যমে অর্থ উপার্জন করতে আপনার অবশ্যই 1টি গ্রুপ থাকতে হবে।
 আপনার যদি একটি গ্রুপ থাকে, আপনি আপনার গ্রুপে আমাদের বট যোগ করে অর্থ উপার্জন করতে পারেন।

 আপনার গ্রুপে যত বেশি সদস্য থাকবেন আপনার আয় তত বেশি হবে।

 কিভাবে এবং কি করতে হবে

 ধাপ 1: আপনার গ্রুপে এই ChillOxBot বট পরিচালনা করুন

 ধাপ 2: আপনার ওয়েবসাইট এবং API যোগ করুন

 মেয়াদ: /shortlink omegalinks.in 4b392f8eb6ad711fbe58

 একটি ভিডিও যোগ করুন

 👇 কিভাবে যোগ করবেন 👇

 মেয়াদ: /set_tutorial ভিডিও লিঙ্ক

এছাড়াও আপনার দল ভিডিও সংগ্রহের প্রশিক্ষণ দেবে..."""


    DEVELOPER_TXT = """
special Thanks To ❤️ Developers -

-Dev [Owner of this Bot ]<a href='https://t.me/THExAkib'>AKIB</a>

"""

