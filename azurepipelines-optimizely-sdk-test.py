import azurepipelines_optimizely_sdk as aps

## Define Project Id and experiment Id
PROJECT_ID = "12098094739"
EXPERIMENT_KEY = "python_experiment"

apOS = aps.AzurePipelinesOptimizelySdk(PROJECT_ID, EXPERIMENT_KEY)


user1 = "user100"  # Fetch unique user id
variationKey = apOS.getVariationKey(user1)
print(variationKey)
if(variationKey == "sort_by_name_py"): 
    print("Flow of model 1")
elif (variationKey == "sort_by_price_py"):
    print("Flow of model 2")
