"""
    tellurium 1.3.1

    auto-generated code (2016-03-04T16:17:48)
    sedmlDoc: L1V2  
    workingDir: /tmp/tmpIH4MZ__sedml/_te_testcase_03
    inputType: COMBINE_FILE
"""
from __future__ import print_function, division
import tellurium as te
from tellurium.sedml.mathml import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import libsedml
import pandas
import os.path

workingDir = '/tmp/tmpIH4MZ__sedml/_te_testcase_03'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
# Model <mod1>
mod1 = te.loadSBMLModel(os.path.join(workingDir, 'testcase_03.xml'))
# Model <mod2>
mod2 = te.loadSBMLModel(os.path.join(workingDir, 'testcase_03.xml'))
__var__S1 = mod2['S1']
mod2['S2'] = __var__S1 + 4

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
# Task <task1>
# execute simpleTask: <task1>
task1 = [None]
mod1.setIntegrator('cvode')
mod1.timeCourseSelections = ['S2', 'S1', 'time']
task1[0] = mod1.simulate(start=0.0, end=10.0, steps=100)

# Task <task2>
# execute simpleTask: <task2>
task2 = [None]
mod2.setIntegrator('cvode')
mod2.timeCourseSelections = ['S2', 'S1']
task2[0] = mod2.simulate(start=0.0, end=10.0, steps=100)

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
# DataGenerator <plot_0_0_0>
__var__task1_____time = np.transpose(np.array([sim['time'] for sim in task1]))
if len(__var__task1_____time.shape) == 1:
     __var__task1_____time.shape += (1,)
plot_0_0_0 = __var__task1_____time

# DataGenerator <plot_0_0_1>
__var__task1_____S1 = np.transpose(np.array([sim['S1'] for sim in task1]))
if len(__var__task1_____S1.shape) == 1:
     __var__task1_____S1.shape += (1,)
plot_0_0_1 = __var__task1_____S1

# DataGenerator <plot_0_1_1>
__var__task1_____S2 = np.transpose(np.array([sim['S2'] for sim in task1]))
if len(__var__task1_____S2.shape) == 1:
     __var__task1_____S2.shape += (1,)
plot_0_1_1 = __var__task1_____S2

# DataGenerator <plot_0_2_1>
__var__task2_____S1 = np.transpose(np.array([sim['S1'] for sim in task2]))
if len(__var__task2_____S1.shape) == 1:
     __var__task2_____S1.shape += (1,)
plot_0_2_1 = __var__task2_____S1

# DataGenerator <plot_0_3_1>
__var__task2_____S2 = np.transpose(np.array([sim['S2'] for sim in task2]))
if len(__var__task2_____S2.shape) == 1:
     __var__task2_____S2.shape += (1,)
plot_0_3_1 = __var__task2_____S2

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
# Output <plot_0>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_0_1[:,k], '-o', color='r', linewidth=1.5, markersize=4.0, alpha=0.8, label='task1.S1')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_0_1[:,k], '-o', color='r', linewidth=1.5, markersize=4.0, alpha=0.8)
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_1_1[:,k], '-o', color='b', linewidth=1.5, markersize=4.0, alpha=0.8, label='task1.S2')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_1_1[:,k], '-o', color='b', linewidth=1.5, markersize=4.0, alpha=0.8)
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_2_1[:,k], '-o', color='g', linewidth=1.5, markersize=4.0, alpha=0.8, label='task2.S1')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_2_1[:,k], '-o', color='g', linewidth=1.5, markersize=4.0, alpha=0.8)
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_3_1[:,k], '-o', color='m', linewidth=1.5, markersize=4.0, alpha=0.8, label='task2.S2')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_3_1[:,k], '-o', color='m', linewidth=1.5, markersize=4.0, alpha=0.8)
plt.title('ComputeChanges', fontweight='bold')
plt.xlabel('task1.time', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.show()
