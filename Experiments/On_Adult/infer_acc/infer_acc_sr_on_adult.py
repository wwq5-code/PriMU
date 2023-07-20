

import numpy as np
import matplotlib.pyplot as plt
import math
epsilon = 3
beta = 1 / epsilon


# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

x=[0, 20, 40, 60, 80]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

#labels = ['0%','20%', '40%', '60%', '80%', '99%' ]
labels = ['20%', '40%', '60%', '80%', '100%']

unl_hess_r = [95.77, 95.77, 95.77, 95.77, 95.77]
unl_vbu = [99.53, 99.53, 99.53, 99.53, 99.53]

unl_ss_w = [3107/100, 3285/100, 3601/100, 3852/100, 3919/100]
unl_ss_wo = [71.45, 70.74, 69.65, 70.62, 70.04]

with_replacement = []
without_replacement = []
for i in range(len(x)):
    with_replacement.append( 1- math.pow(99/100,x[i]))
    without_replacement.append(x[i]/100)

print(with_replacement)
print(without_replacement)

plt.figure()
l_w=5
m_s=12
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)

plt.plot(x, unl_vbu, color='r',  marker='p',  label='No-Protection (VBU)',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_hess_r, color='dodgerblue',  marker='o', linestyle='-.', label='Gradient (HBFU)',linewidth=l_w, markersize=m_s)
#plt.plot(x, without_replacement, color='palegreen',  marker='1',  label='RFU-SS',linewidth=l_w, markersize=m_s)

plt.plot(x, unl_ss_wo, color='orange',  marker='*', linestyle='--', label='MCFU$_{w/o}$',linewidth=l_w,  markersize=m_s)




#plt.plot(x, unl_vibu, color='silver',  marker='d',  label='VIBU',linewidth=4,  markersize=10)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Inference Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(0 ,110, 20)
plt.yticks(my_y_ticks,fontsize=20)
plt.xlabel('$\it{SR}$' , fontsize=20)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('infer_acc_sr_on_adult.png', dpi=200)
plt.show()