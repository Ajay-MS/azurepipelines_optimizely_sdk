import azurepipelines_optimizely_sdk as aps

## Define Project Id and experiment Id
PROJECT_ID = "12098094739"
EXPERIMENT_KEY = "python_experiment"

def testVariationKeyAndEvent():
    user1 = "user100"  # Fetch unique user id
    variationKey = apOptimizelySdk.getVariationKey(user1)
    print(variationKey)
    if(variationKey == "sort_by_name_py"): 
        print("Flow of model 1")
    elif (variationKey == "sort_by_price_py"):
        print("Flow of model 2")

    apOptimizelySdk.trackConversionEvent('item_buy_py', "user1")

# Test for production environment 
apOptimizelySdk = aps.AzurePipelinesOptimizelySdk(PROJECT_ID, EXPERIMENT_KEY)
testVariationKeyAndEvent()


apOptimizelySdk.getOptimizelyInstanceForEnvironment("https://cdn.optimizely.com/datafiles/8BseYq2XQSAbG3HtVL9mJx.json")
testVariationKeyAndEvent()
