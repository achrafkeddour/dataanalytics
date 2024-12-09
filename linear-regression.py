# نستورد المكتبات
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# بيانات التدريب (X و y)
X = np.array([[1], [2], [3], [4], [5]])  # الساعات
y = np.array([10, 15, 20, 25, 30])       # النقاط

# ننشئ النموذج وندربه على البيانات
model = LinearRegression()
model.fit(X, y)

# نطبع المعادلة: Y = aX + b
a = model.coef_[0]  # الميل
b = model.intercept_  # الثابت
print(f"المعادلة: Y = {a:.2f}X + {b:.2f}")

# بيانات جديدة (A) للتجربة (ندخلها يدويًا)
A = np.array([[6], [7], [8]])  # مثال: الساعات الجديدة

# نعمل توقعات على البيانات الجديدة
predictions = model.predict(A)

# نعرض النتائج
print("القيم الجديدة (A):", A.flatten())
print("القيم المتوقعة (Y):", np.round(predictions, 2))

# الرسم
plt.scatter(X, y, color='blue', label='بيانات التدريب')  # النقاط الأصلية
plt.plot(X, model.predict(X), color='red', label='الخط المستقيم')  # الخط الناتج
plt.scatter(A, predictions, color='green', label='التوقعات الجديدة', marker='x', s=100)  # النقاط الجديدة

# تسميات المحاور والعنوان
plt.xlabel('عدد الساعات')
plt.ylabel('النقاط')
plt.title('توقع النقاط بناءً على عدد الساعات')
plt.legend()

# عرض الرسم
plt.show()