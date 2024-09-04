import tkinter as tk
from tkinter import messagebox
import subprocess

# active key 
keys = {
    "Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "Home N": "3KHY7-WNT83-DGQKR-F7HPR-844BM",
    "Home Single Language": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
    "Home Country Specific": "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
    "Professional": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "Professional N": "MH37W-N47XK-V7XM9-C7227-GCQG9",
    "Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    "Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
    "Enterprise N": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
} 

# قائمة خيارات الويندوز وإصداراته
os_options = [ "Windows 11",
                "Windows 10",
                "Windows 8",
                "Windows 7"
            ] 
version_options = [
    "Home",
    "Home N",
    "Home Single Language",
    "Home Country Specific",
    "Professional",
    "Professional N",
    "Education",
    "Enterprise",
    "Enterprise N"
]

def update_version_menu(*args):
    # تحديث قائمة الإصدارات بناءً على اختيار نظام التشغيل
    selected_os = os_var.get()
    available_versions = version_options.copy()
    
    # تحديث قائمة الإصدارات
    version_menu['menu'].delete(0, 'end')
    for version in available_versions:
        version_menu['menu'].add_command(label=version, command=tk._setit(version_var, version))

def on_submit():
    selected_os = os_var.get()
    selected_version = version_var.get()
    
    if selected_os == "اختر نوع الويندوز" or selected_version == "اختر إصدار الويندوز":
        result_label.config(text="يرجى اختيار نوع الويندوز وإصداره.", foreground="#d9534f")
    else:
        key = keys.get(selected_version, 'مفتاح غير متوفر')
        result_label.config(text=f"{key}", foreground="#5bc0de")
        if key != 'مفتاح غير متوفر':
            try:
                # دمج الأوامر في سلسلة واحدة
                command = f'slmgr /ipk {key} && slmgr /ato'
                # تشغيل cmd كمسؤول وتنفيذ الأوامر
                subprocess.run(['powershell', '-Command', f'Start-Process cmd -ArgumentList "/c {command}" -Verb RunAs'], check=True)
            except subprocess.CalledProcessError as e:
                # إظهار نافذة منبثقة تحتوي على رسالة الخطأ
                messagebox.showerror("خطأ", f"حدث خطأ أثناء تنفيذ الأوامر: {str(e)}")

def on_hover(event):
    event.widget.config(bg="#f0ad4e", foreground="white")

def on_leave(event):
    event.widget.config(bg="#0275d8", foreground="white")

# إنشاء نافذة البرنامج الرئيسية
root = tk.Tk()
root.title("اختيار نظام التشغيل وإصداره")
root.geometry("600x400")  # تعيين حجم النافذة
root.resizable(True, True)  # جعل النافذة قابلة للتغيير

# تحسين مظهر النافذة
root.configure(bg="#e9ecef")

# قائمة خيارات نظام التشغيل
os_label = tk.Label(root, text="اختر نوع الويندوز:", font=("Arial", 16, "bold"), background="#e9ecef", padx=10, pady=5)
os_label.pack(pady=(20, 10), anchor='w')

os_var = tk.StringVar()
os_var.set("اختر نوع الويندوز")  # تعيين القيمة الافتراضية

os_menu = tk.OptionMenu(root, os_var, *os_options)
os_menu.config(font=("Arial", 12), width=25, relief="flat", bg="#ffffff", fg="#333333", highlightthickness=0)
os_menu.pack(pady=5, fill='x', padx=20)
os_var.trace("w", update_version_menu)  # تتبع تغييرات os_var

# قائمة خيارات إصدار الويندوز
version_label = tk.Label(root, text="اختر إصدار الويندوز:", font=("Arial", 16, "bold"), background="#e9ecef", padx=10, pady=5)
version_label.pack(pady=(20, 10), anchor='w')

version_var = tk.StringVar()
version_var.set("اختر إصدار الويندوز")  # تعيين القيمة الافتراضية

version_menu = tk.OptionMenu(root, version_var, *version_options)
version_menu.config(font=("Arial", 12), width=25, relief="flat", bg="#ffffff", fg="#333333", highlightthickness=0)
version_menu.pack(pady=5, fill='x', padx=20)

# زر لإرسال الاختيارات
submit_button = tk.Button(root, text="تأكيد الاختيارات", command=on_submit, font=("Arial", 12, "bold"), bg="#0275d8", fg="white", relief="flat", padx=10, pady=5)
submit_button.pack(pady=20)

# تسمية النتيجة
result_label = tk.Label(root, text="", font=("Arial", 14), background="#e9ecef")
result_label.pack(pady=10)

# إضافة تأثيرات
submit_button.bind("<Enter>", on_hover)
submit_button.bind("<Leave>", on_leave)

# تحسين تنسيق الزر
root.mainloop()
