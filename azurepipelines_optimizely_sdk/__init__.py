from azurepipelines_optimizely_sdk import optimizely_config_manager as ocm

class AzurePipelinesOptimizelySdk:

    # For production environment provide project Id, for other environments provide SDK key as project id
    def __init__(self, projectId, experimentKey):
        self.projectId = projectId
        self.experimentKey = experimentKey
        self.optimizelyConfigManager = ocm.OptimizelyConfigManager(projectId)
        self.optimizelyInstance = self.optimizelyConfigManager.getOptimizelyInstance()

    # create optimizely instance for an environment
    def getOptimizelyInstanceForEnvironment(self, url):
        self.optimizelyConfigManager.setOptimizelyInstance(url)
        self.optimizelyInstance = self.optimizelyConfigManager.getOptimizelyInstance()

    def setExperimentKey(self, experimentKey):
        self.experimentKey = experimentKey

    def getVariationKey(self, userId):
        variationKey = self.optimizelyInstance.activate(self.experimentKey, userId)
        return variationKey

    def trackConversionEvent(self, eventKey, userId):
        self.optimizelyInstance.track(eventKey, userId)
