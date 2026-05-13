from mishkal.tashkeel import TashkeelClass
tashkeel = TashkeelClass()
tests = [
    "ذهب الولد إلى المدرسة",
    "علم المعلم الطلاب الدرس",  # كلمة "علم" محتملة التشكيل
    "كتب الطالب الواجب",         # "كتب" فعل أم اسم؟
    "وضع الرجل الكتاب على المكتب ثم خرج من الغرفة",
]

for t in tests:
    print(f"الأصلي:  {t}")
    print(f"المشكّل: {tashkeel.tashkeel(t)}")
    print("---")