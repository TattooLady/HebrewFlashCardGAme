#!/usr/bin/python3
# GUI for Hebrew Flash Cards App
# This is the UI for a flashcards application developed by Lydia Scherr

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

  

dictionary = {'give her':'תנ לה', 'give me': 'תני לי', 'give us': 'תן לנו'
        ,'give him': 'תן לו', 'give them': 'תן להם' 
        , 'give to them (f)': 'תן להן' , 'receive (m)': 'לקבל'
        , 'receive (f)': 'לקבלת', 'never mind' : 'לא משנה' , 'sort of': 'בערך'
        , 'breakfast': 'ארוחת בוקר', 'email': 'אימייל' , 'gift': 'מתנה'
        , 'Hebrew': 'עברית', 'one': 'אחד', 'two': 'שתיים', 'three': 'שלוש'
        , 'four': 'ארבע', 'five': 'חמש', 'six': 'שש', 'seven': 'שבע'
        , 'eight': 'שמונה', 'nine': 'תשע', 'ten': 'עשר', 'I have': 'יש לי'
        , 'She has': 'יש לה', 'He has': 'יש לו', 'We have': 'יש לנו'
        , 'They have': 'יש להם' , 'You have (m)': 'יש לך', 'You have (f)': 'יש לך'
        , 'cappuccino': 'קפוצינו', 'help': 'עזרה' , 'if_' : 'אם', 'on my way!': 'בדרכי'
        , 'to go': 'ללכת', 'to come': 'לבוא', 'enough': 'מספיק', 'time': 'זמן'
        , 'ready (m)': 'מוכן', 'not yet': 'עד לא', 'office': 'משרד', 'cake': 'עוגה'
        , 'where': 'איפה', 'bathroom': 'שירותים', 'to know (m)': 'יודע'
        , 'to know (f)': 'יודעת', 'to need (f)': ' צריכה', 'they know': 'הם יודעים'
        , 'ready (f)': 'מוכנה', 'you know (f)': 'יודעת'
        , 'we know': 'אנחנו יודעים'
        , 'to need (m)': 'צריך', 'they need (m)': 'הם צריכים', 'we need': 'אנחנו צריכים'
        , 'you need (m)': 'אתה צריך'
        , 'you need (f)': 'צריכות', 'can (m)': 'יכול', 'can (f)': 'יכולה', 'can (pm)': 'יכולים'
        , 'can (pf)': 'יכולות', 'beach': 'ים', 'Tel Aviv': 'תל אביב', 'busy (m)': 'עסוק'
        , 'today': 'היום', 'busy (f)': 'עסוקה', 'work': 'עבודה', 'working': 'עובד'
        , 'hot': 'חם', 'cold': 'קר', 'when': 'מתי', 'think (m)': 'לחשוב'
        , 'think (f)': 'חושבת', 'he': 'הוא', 'she': 'היא', 'but': 'אבל'
        , 'exactly': 'בדיוק', 'nothing': 'קלום', 'really': 'מַמָשׁ', 'maybe': 'אולי'
        , 'store': 'חנות', 'weird': 'מוזר', 'very': 'מאוד', 'fun': 'כיף'
        , 'tomorrow': 'מחר', 'super market': 'סופר', 'correct': 'נכון', 'wine': 'יין'
        , 'red': 'אדום', 'white': 'לבן', 'blue': 'כחול', 'yellow': 'צהוב'
        , 'green': 'ירוק', 'black': 'שחור', 'sure': 'בטוח', 'why': 'למה'
        , 'weekend': 'סוף שבוע', 'yes': 'קן', 'to': 'ל', 'the': 'ה'
        , 'from': 'מ', 'at': 'בְּ', 'that': 'זה', 'most': 'הֲכִי'
        , 'more': 'יותר', 'learns (m)': 'לומד', 'learns (f)': 'לומדת', 'fast': 'מהר'
        , 'pretty': 'יפה', 'again': 'עוֹד פַּעַם', 'depends': 'תלוי'
        , 'we': 'אנחנו', 'keys': 'מפתחות', 'everybody': 'כולם'
        , 'nobody': 'אף אחד', 'clue': 'מוּשָׂג', 'I have no clue': 'אין לי מושג'
        , 'about': 'על', 'right here': 'ה׳נה', 'moment': 'רגע'
        , 'just': 'רַק', 'it appears to me': 'נראה לי', 'much': 'הַרבֵּה'
        , 'people': 'אנשים', 'hour': 'שעה', 'come': 'לבוא'
        , 'bridge': 'גשר', 'round about': 'כיכר', 'traffic light': 'רמזור'
        , 'intersection': 'צומת', 'helmet': 'קסדה', 'regular': 'רגיל'
        , 'careful': 'זהיר', 'to take away': 'לקחת', 'service taxi': 'מונית שירות'
        , 'driver': 'נהג', 'train': 'רכבת', 'meter': 'מטר'
        , 'number': 'מספר', 'platform': 'רָצִיף', 'line': 'קו'
        , 'next': 'הבא', 'station': 'תחנה', 'bus': 'אוטובוס'
        , 'pleasant': 'נעים', 'bicycle': 'אופניים', 'bicycle lane': 'שביל אופניים'
        , 'slow': 'איטי', 'say': 'אומרים', 'how': 'איך'
        , 'paper': 'עיתון', 'mug': 'ספל', 'book': 'ספר'
        , 'movie': 'סרט', 'street': 'רחוב', 'floor': 'קוֹמָה'
        , 'Appartment': 'דירה', 'to go': 'ללכת', 'got it': 'מבינה'
        , 'class': 'שיעור', 'like / love': 'אהבה', 'charger': 'מטען'
        , 'almost': 'כמעט', 'always': 'תמיד', 'month': 'חודש'
        , 'year': 'שנה', 'years': 'שנים', 'months': 'חודשים'
        , 'name': 'שם', 'before': 'לפני', 'after': 'לאחר'
        , 'Ordering food for him': 'rawr', 'Ordering food for her': 'rawr', 'Ordering food for me': 'rawr'
        , 'thats it' : 'rawr', 'I feel like': 'באלי', 'you feel like': 'באלך'
        , 'we/they feel like (m)': 'rawr', 'we/they feel like (f)': 'rawr', 'neither': 'גַם לֹא'
        , 'Sunday': 'יום ראשון', 'Monday': 'יום שני', 'Tuesday': 'יום שלישי'
        , 'Wednesday': 'יום רביעי', 'Thursday': 'יום חמישי', 'Friday': 'יום שישי'
        , 'Saturday': 'יום שבת', 'January': 'ינואר', 'Februrary': 'פברואר', 'March': 'מרץ'
        , 'April': 'אפריל', 'May': 'מאי', 'June': 'יוני'
        , 'July': 'יולי', 'August': 'אוגוסט', 'September': 'ספטמבר'
        , 'October': 'אוקטובר', 'November': 'נובמבר', 'December': 'דצמבר'
        , 'with me': 'איתי', 'with you': 'איתך', 'with him': 'איתו'
        , 'with her': 'איתה', 'with us': 'איתנו', 'totally': 'לגמרי'
        , 'which': 'איזה כיף', 'what a bummer': 'איזה באסה', 'how nice': 'איזה יופי'
        , 'how great': 'איזה כיף', 'what a mess': 'איזה בלאגן', 'what a coincidence': 'איזה קטע'
        , 'how lucky': 'איזה מזל', 'obviously': 'ברור'
        , 'familiar': 'מכיר', 'up': 'למעלה', 'down': 'למטה'
        , 'left': 'שמאלה', 'right': 'ימינה', 'paying': 'משלם'
        , 'to pay': 'לשלם', 'speaking': 'מדבר', 'to speak': 'לדבר'
        , 'to hear': 'לשמוע', 'listening': 'שמיעה', 'they hear (pf)': 'שומעות'
        , 'we hear (pm)': 'אנחנו שומעים', 'one hundred': 'מאה', 'she pays': 'היא משלמת'
        , 'he wants to pay': 'הוא רוצה לשלם', 'we are paying': 'אנחנו משלמים', 'how much': 'כמה'
        , 'with me': 'איתי', 'with you': 'איתך', 'with him': 'איתו'
        , 'with her': 'איתה', 'with us': 'איתנו', 'with them': 'איתם'
        , 'both': 'זה וזה', 'also': 'גם', 'remember (m)': 'זכור', 'remember (f)': 'זוכרת'
        , 'forget': 'לא זוכר', 'money': 'כסף', 'something': 'משהו'
        , 'someone': 'מישהו', 'to drink': 'לשתות', 'to eat': 'לאכול'
        , 'I am from': 'אני מ', 'want (m)': 'רוצה', 'want (f)': 'רוצה'
        , 'usually': 'בדרך כלל', 'cold (p)': 'קרים', 'hot (p)': 'חמים'
        , 'doesnt matter': 'לא משנה', 'about': 'על', 'complicated': 'מסובך', 'too': 'מדי', 'always': 'תמיד'
        , 'policitcs': 'פוליטיקה', 'yesterday': 'אתמול', 'outside': 'בחוץ', 'inside': 'בתוך'
        , 'long story short': 'בקיצור', 'asking (m)':'שואל', 'asking (f)':'שואלת', 'sad':'עצוב', 'happy':'שמח', 'alone':'לבד'
        ,'looking':'מחפש', 'neighborhood':'שכונה', 'spicy':'חריף', 'sweet':'מתוק', 'difficult':'קשה', 'easy':'קל', 'first time': 'פעם ראשונה'
        , 'once':'פעם', 'twice':'פעמיים', 'times':'פעמים', 'sometimes':'לפעמים', 'never':'לעולם לא', 'travel':'', 'next to':'ליד'
        ,'across from':'מול', '1/3':'שליש', '1/2': 'חצי', 'in truth':'באמת', 'actually':'בעצם'
        ,'appointment':'פְּגִישָׁה', 'close':'סגור', 'window':'חלון', 'open':'פתוח', 'he said':'אמר'
        ,'says':'אומר', 'they said':'הם אמרו', 'she said':'היא אמרה', 'to search':'לחפש', 'situation':'מצב'
        , 'receive':'לקבל', 'I need to go':'אני צריך ללכת', 'We need to go':'אנחנו צריכים ללכת', 'They need to go':'הם צריכים ללכת', 'She needs to go':'היא צריכה ללכת'
        , 'I cannot hear you':'אני לא שומע אותך', 'she cannot hear you':'היא לא יכולה לשמוע אותך', 'we cannot hear you':'אנחנו לא יכולים לשמוע אותך', 'Do you like Tel Aviv?':'אתה אוהב את תל אביב?', 'I am already at the office':'אני כבר במשרד'
        , 'angry':'כועס', 'He is going to a movie':'הוא הולך לסרט', 'I cannot drink this, it is not coffee':'אני לא יכול לשתות את זה זה לא קפה', 'Do you want anything from the store?':'אתה רוצה משהו מהחנות', 'sidewalk':'מדרכה'
        , 'scooter':'קוֹרקִינֶט', 'stop':'עצור', 'one hundred percent':'מאה אחוז', 'Are you sure?':'האם אתה בטוח?', 'Even she did not go':'אפילו היא לא הלכה', 'Even he did not eat':'אפילו הוא לא אכל'
        , 'Restaurant':'מסעדה', 'plates':'צלחות', 'plate':'צלחת', 'to see':'לראות'
        , 'I do not remember where I put it':'אני לא זוכר איפה שמתי את זה', 'First of all':'קודם כל', 'Afterwards':'אחר כך', 'When did you get up toay':'מתי קמת היום'
        , 'Where did you put the plates':'איפה הנחת את הצלחות?', 'I wish':'הלוואי', 'table':'שולחן', 'closet':'ארון'
        , 'perfect':'מושלם', 'return':'לחזור', 'I do not care':'לא אכפת לי', 'to do':'לעשות'}


        
class Hebrew:
    
    def __init__(self, master):    
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        # self.logo = PhotoImage(file = '/Users/las/Desktop/Hebrew/israelflag.png')
        # ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Button(self.frame_header, text = 'Quit', command = self.Quit).grid(row=0, column=3)
        
        self.question = ttk.Label(self.frame_header, wraplength = 350)
        self.question.grid(row=2, column=1)
        

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'English:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
       
        self.user_input = ttk.Entry(self.frame_content, text = "Your Answer?", width = 24)
        self.user_input.grid(row = 1, column = 1, padx = 5)
        
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        ttk.Button(self.frame_content, text = 'Next', command = self.next).grid(row = 3, column = 2, padx = 5, pady = 5, sticky = 'w')
        
        self.next()
        
    def submit(self):
        user_input = self.user_input.get().strip()
        if user_input == self.answer:
            print ("Correct")
        else:
            print ("!לא נכון ", "The answer is:", self.answer)
           
    def clear(self):
        self.user_input.delete(0, 'end')

    def next(self):
        self.answer = random.choice(list(dictionary.keys()))
        self.question.config(text="Hebrew Word: "+dictionary[self.answer])

    def Quit(self):
        self.command = main.destroy()
        

def main():
    root = Tk()
    hebrew = Hebrew(root)
    root.mainloop()

if __name__ == "__main__":
     main()
