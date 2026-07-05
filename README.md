# EduManage - نظام SaaS لإدارة المدارس

نظام SaaS لإدارة المدارس (EduManage) هو تطبيق ويب متكامل يهدف إلى تسهيل عملية إدارة بيانات الطلاب والمواد الدراسية. يوفر النظام واجهات سهلة الاستخدام للمدرسين والإداريين، مع صلاحيات مرنة وعزل بيانات كامل لكل مؤسسة تعليمية.

---

## ✨ الميزات الرئيسية الموجودة

- **إدارة الطلاب** (إضافة، تعديل، حذف، عرض) مع صلاحيات.
- **نظام تسجيل دخول وإنشاء حساب** مع أدوار (طالب، مدرس، مشرف).
- **عزل بيانات** لكل مؤسسة (Multi-Tenancy).
- **واجهات API** محمية بـ JWT.
- **نشر سحابي** على Render مع CI/CD عبر GitHub Actions.

### قيد التطوير (قادم)
- المواد الدراسية والدرجات

---

## 🛠️ التقنيات المستخدمة

- **الواجهة الخلفية**: Django (Python) + Django REST Framework
- **الواجهة الأمامية**: Django Templates
- **قاعدة البيانات**: PostgreSQL
- **المصادقة**: JWT (API) + Sessions (UI)
- **النشر**: Render (سحابة)
- **CI/CD**: GitHub Actions

**مخطط له مستقبلاً**: المواد الدراسية والدرجات.

---

## 🚀 التشغيل المحلي (Local Development)

### المتطلبات الأساسية
- Python 3.10 أو أحدث
- PostgreSQL (محلياً أو عبر Docker)
- Git

### خطوات التشغيل

1. **استنساخ المستودع**
```bash
git clone https://github.com/hamzaabdalla305-cmyk/school-project.git
cd school-project
```

2. **إنشاء وتفعيل البيئة الافتراضية**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **تثبيت التبعيات**
```bash
pip install -r requirements.txt
```

4. **إعداد قاعدة البيانات**
   - أنشئ قاعدة بيانات PostgreSQL باسم `school_db`
   - عدّل إعدادات الاتصال في `settings.py` أو استخدم متغيرات البيئة

5. **تنفيذ الهجرات وإنشاء المستخدم المشرف**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **تشغيل الخادم**
```bash
python manage.py runserver
```

الآن يمكنك فتح المتصفح على `http://127.0.0.1:8000`

---

## 🌐 النشر السحابي

التطبيق منشور على Render ويمكن الوصول إليه عبر الرابط التالي:

🔗 https://school-project-0hkr.onrender.com

> ملاحظة: لإنشاء حساب أدمن على النسخة المنشورة، استخدم أمر `createsuperuser` عبر Shell الخاص بالخدمة على Render، أو من خلال صفحة التسجيل ثم تعديل الصلاحية يدوياً.

---

## 📂 هيكل المشروع

```
school_project/
├── school_management/     # إعدادات المشروع
├── schools/                # التطبيق الرئيسي
│   ├── models.py           # نماذج قاعدة البيانات
│   ├── views.py             # منطق العرض (UI + API)
│   ├── serializers.py       # محولات الـ API
│   ├── forms.py             # نماذج الواجهات
│   └── urls.py               # مسارات التطبيق
├── templates/               # ملفات HTML
├── static/                   # الملفات الثابتة (CSS, JS)
├── manage.py                # أداة إدارة Django
└── requirements.txt          # تبعيات المشروع
```

---

## 🤝 المساهمة

1. انسخ المستودع (Fork)
2. أنشئ فرعاً جديداً (`git checkout -b feature/amazing-feature`)
3. أضف تعديلاتك (`git commit -m 'Add some amazing feature'`)
4. ارفع التغييرات (`git push origin feature/amazing-feature`)
5. افتح طلب سحب (Pull Request)

---

## 📜 الترخيص

هذا المشروع مرخص تحت MIT License.

---

## 📧 التواصل

- **الاسم**: عبدالله حمزة هارون عبدالله
- **البريد الإلكتروني**: hamzaabdalla305@gmail.com
- **رابط المشروع**: https://github.com/hamzaabdalla305-cmyk/school-project

---

## 🙏 شكر وتقدير

- Django
- PostgreSQL
- Render
- Bootstrap

---

صنع بـ ❤️ بواسطة عبدالله حمزة هارون عبدالله
