
# make an exact clone of our existing model
radmodel_noH2O = climlab.process_like(radmodel)
# change the name of our new model
radmodel_noH2O.name = 'Radiation (no H2O)'

# set the water vapor profile to all zeros
radmodel_noH2O.specific_humidity *= 0.

# run the model to equilibrium
radmodel_noH2O.step_forward()
while np.abs(radmodel_noH2O.ASR - radmodel_noH2O.OLR) > 0.01:
    radmodel_noH2O.step_forward()

skew = make_skewT()
for model in [radmodel, radmodel_noH2O]:
    add_profile(skew, model)