'''import numpy as np
import matplotlib.pyplot as plt
objects = ("NL","DE","MILTON","US","CA")
incomes=[2000,1800,1400,4000,1000]
y_pos = np.arange(len(objects))
plt.bar(y_pos, incomes, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Income')
plt.xlabel('Country')
plt.title('avergage per country')
plt.savefig('foo.png',dpi=100)
plt.show()
'''
    os.remove(r'C:\Users\Admin\Desktop\graf\static\foo100.png')
    time.sleep(3)