import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


Age = ctrl.Antecedent(np.arange(0, 100 ,1), "Age")
Age["Child"] = fuzz.trapmf(Age.universe, [0, 0, 4.307, 12])
Age["Young"] = fuzz.trapmf(Age.universe, [9, 18.9, 27.1, 36.64])
Age["Adult"] = fuzz.trapmf(Age.universe, [32.9, 42.7, 53, 61.5079])
Age["Elder"] = fuzz.trapmf(Age.universe, [57.5, 85.3175, 100, 100])
Pulse = ctrl.Antecedent(np.arange(0, 220 ,1), "Pulse")
Pulse["VeryLow"] = fuzz.trapmf(Pulse.universe, [0, 0, 8.4392, 32.3])
Pulse["Low"] = fuzz.trapmf(Pulse.universe, [26.8, 34.6296, 50.3, 62.8])
Pulse["Normal"] = fuzz.trapmf(Pulse.universe, [59.0741, 73.6, 88.8, 102])
Pulse["High"] = fuzz.trapmf(Pulse.universe, [93.5, 116, 137, 162.672])
Pulse["VeryHigh"] = fuzz.trapmf(Pulse.universe, [155.6878, 205, 220, 220])
PLevels = ctrl.Consequent(np.arange(0, 100 ,1), "PLevels")
PLevels["BelowAV"] = fuzz.trapmf(PLevels.universe, [12.4, 16.8, 22.8836, 29.4])
PLevels["Excellent"] = fuzz.trapmf(PLevels.universe, [26.7, 32.672, 38.2, 43.4])
PLevels["AboveAV"] = fuzz.trapmf(PLevels.universe, [41.6, 50.7, 60.7143, 73.1])
PLevels["Low"] = fuzz.trapmf(PLevels.universe, [0, 0, 4.8942, 15])
PLevels["Very_High"] = fuzz.trapmf(PLevels.universe, [68.3862, 92.2, 101, 101])
regla1 = ctrl.Rule(Age["Child"] & Pulse["VeryLow"] , PLevels["Low"])
regla2 = ctrl.Rule(Age["Child"] & Pulse["Low"] , PLevels["Low"])
regla3 = ctrl.Rule(Age["Child"] & Pulse["Normal"] , PLevels["Excellent"])
regla4 = ctrl.Rule(Age["Child"] & Pulse["High"] , PLevels["Excellent"])
regla5 = ctrl.Rule(Age["Child"] & Pulse["VeryHigh"] , PLevels["AboveAV"])
regla6 = ctrl.Rule(Age["Young"] & Pulse["VeryLow"] , PLevels["Low"])
regla7 = ctrl.Rule(Age["Young"] & Pulse["Low"] , PLevels["BelowAV"])
regla8 = ctrl.Rule(Age["Young"] & Pulse["Normal"] , PLevels["Excellent"])
regla9 = ctrl.Rule(Age["Young"] & Pulse["High"] , PLevels["AboveAV"])
regla10 = ctrl.Rule(Age["Young"] & Pulse["VeryHigh"] , PLevels["Very_High"])
regla11 = ctrl.Rule(Age["Adult"] & Pulse["VeryLow"] , PLevels["Low"])
regla12 = ctrl.Rule(Age["Adult"] & Pulse["Low"] , PLevels["BelowAV"])
regla13 = ctrl.Rule(Age["Adult"] & Pulse["Normal"] , PLevels["Excellent"])
regla14 = ctrl.Rule(Age["Adult"] & Pulse["High"] , PLevels["AboveAV"])
regla15 = ctrl.Rule(Age["Adult"] & Pulse["VeryHigh"] , PLevels["Very_High"])
regla16 = ctrl.Rule(Age["Elder"] & Pulse["High"] , PLevels["Very_High"])
regla17 = ctrl.Rule(Age["Elder"] & Pulse["VeryHigh"] , PLevels["Very_High"])
regla18 = ctrl.Rule(Age["Elder"] & Pulse["VeryLow"] , PLevels["Low"])
regla19 = ctrl.Rule(Age["Elder"] & Pulse["Low"] , PLevels["Excellent"])
regla20 = ctrl.Rule(Age["Elder"] & Pulse["Normal"] , PLevels["Excellent"])
tipping_ctrl = ctrl.ControlSystem(
[regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13,regla14, regla15, regla16, regla17, regla18, regla19, regla20])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['Age'] = 50
tipping.input['Pulse'] = 110
tipping.compute()
print(tipping.output['PLevels'])


