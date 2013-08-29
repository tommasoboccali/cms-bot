# A ridicously long mapping for categories. Good enough for now.
import re

CMSSW_L2 = {
  "Martin-Grunewald": ["hlt"],
  "perrotta": ["hlt"],
  "fwyzard": ["hlt"],
  "slava77": ["reconstruction"],
  "thspeer": ["reconstruction"],
  "vadler": ["analysis"],
  "vciulli": ["generators"],
  "civanch": ["simulation"],
  "giamman": ["fastsim", "simulation"],
  "mdhildred": ["simulation"],
  "Dr15Jones": ["core", "visualization", "geometry"],
  "ktf": ["core", "visualization", "geometry"],
  "ianna": ["geometry"],
  "rovere": ["dqm"],
  "deguio": ["dqm"],
  "ggovi": ["db"],
  "apfeiffer1": ["db"],
  "demattia": ["alca"],
  "rcastello": ["alca"],
  "franzoni": ["operations"],
  "fabiocos": ["operations"],
  "vlimant": ["operations"],
  "cmsdoxy": ["docs"],
  "mommsen": ["daq"],
}

CMSSW_CATEGORIES={"operations": ["Configuration/Applications",
  "Configuration/DataProcessing", "Configuration/GlobalRuns",
  "Configuration/PyReleaseValidation", "Configuration/Skimming",
  "Configuration/StandardSequences", "DPGAnalysis/Skims", "Validation/Tools"],
  "core": ["Configuration/EventContent", "Configuration/SVSuite",
  "FWCore/Catalog", "FWCore/Common", "FWCore/FWLite", "FWCore/Framework",
  "FWCore/GuiBrowsers", "FWCore/Integration", "FWCore/MessageLogger",
  "FWCore/MessageService", "FWCore/Modules", "FWCore/ParameterSet",
  "FWCore/PluginManager", "FWCore/PrescaleService", "FWCore/Python",
  "FWCore/PythonParameterSet", "FWCore/PythonUtilities",
  "FWCore/RootAutoLibraryLoader", "FWCore/ServiceRegistry", "FWCore/Services",
  "FWCore/Skeletons", "FWCore/Sources", "FWCore/TFWLiteSelector",
  "FWCore/TFWLiteSelectorTest", "FWCore/Utilities", "FWCore/Version",
  "PerfTools/Callgrind", "PerfTools/EdmEvent", "IOMC/Input", "IOMC/ParticleGuns",
  "IOMC/RandomEngine", "IOPool/Common", "IOPool/Input", "IOPool/Output",
  "IOPool/SecondaryInput", "IOPool/Streamer", "IOPool/TFileAdaptor",
  "IgTools/IgProf", "DataFormats/FWLite", "DataFormats/Histograms",
  "DataFormats/Provenance", "DataFormats/StdDictionaries",
  "DataFormats/Streamer", "DataFormats/TestObjects",
  "DataFormats/WrappedStdDictionaries", "DataFormats/CLHEP",
  "DataFormats/Common", "Validation/Performance", "Utilities/DCacheAdaptor",
  "Utilities/General", "Utilities/LStoreAdaptor", "Utilities/RFIOAdaptor",
  "Utilities/ReleaseScripts", "Utilities/StaticAnalyzers",
  "Utilities/StorageFactory", "Utilities/Testing", "Utilities/Timing",
  "Utilities/XrdAdaptor"], "docs": ["Documentation/CodingRules",
  "Documentation/PhysicsTools", "Documentation/ReferenceManualScripts", "Documentation/DataFormats"],
  "reconstruction": ["Configuration/EcalTB", "Configuration/JetMET",
  "CommonTools/CandAlgos", "CommonTools/CandUtils", "CommonTools/Clustering1D",
  "CommonTools/ParticleFlow", "CommonTools/RecoAlgos", "CommonTools/Statistics",
  "CommonTools/TrackerMap", "CommonTools/TriggerUtils", "CommonTools/UtilAlgos",
  "CommonTools/Utils", "CondCore/HIPlugins", "EventFilter/CSCRawToDigi",
  "EventFilter/CastorRawToDigi", "EventFilter/DTRawToDigi",
  "EventFilter/ESRawToDigi", "EventFilter/EcalRawToDigi",
  "EventFilter/EcalTBRawToDigi", "EventFilter/HcalRawToDigi",
  "EventFilter/LTCRawToDigi", "EventFilter/RPCRawToDigi",
  "EventFilter/ScalersRawToDigi", "EventFilter/SiPixelRawToDigi",
  "EventFilter/SiStripRawToDigi", "MagneticField/Engine",
  "MagneticField/GeomBuilder", "MagneticField/Interpolation",
  "MagneticField/Layers", "MagneticField/ParametrizedEngine",
  "MagneticField/Records", "MagneticField/UniformEngine",
  "MagneticField/VolumeBasedEngine", "MagneticField/VolumeGeometry",
  "DataFormats/DTRecHit", "DataFormats/EcalRecHit",
  "DataFormats/EgammaCandidates", "DataFormats/EgammaReco",
  "DataFormats/EgammaTrackReco", "DataFormats/FP420Cluster",
  "DataFormats/GsfTrackReco", "DataFormats/HcalIsolatedTrack",
  "DataFormats/HcalRecHit", "DataFormats/HeavyIonEvent", "DataFormats/JetReco",
  "DataFormats/Luminosity", "DataFormats/METObjects", "DataFormats/METReco",
  "DataFormats/Math", "DataFormats/MuonData", "DataFormats/MuonReco",
  "DataFormats/MuonSeed", "DataFormats/ParticleFlowCandidate",
  "DataFormats/ParticleFlowReco", "DataFormats/PixelMatchTrackReco",
  "DataFormats/RPCRecHit", "DataFormats/RecoCandidate", "DataFormats/Scalers",
  "DataFormats/SiPixelCluster", "DataFormats/SiStripCluster",
  "DataFormats/SiStripCommon", "DataFormats/TauReco",
  "DataFormats/TrackCandidate", "DataFormats/TrackReco",
  "DataFormats/TrackerCommon", "DataFormats/TrackerRecHit2D",
  "DataFormats/TrackingRecHit", "DataFormats/TrackingSeed",
  "DataFormats/TrajectorySeed", "DataFormats/TrajectoryState",
  "DataFormats/V0Candidate", "DataFormats/VZero", "DataFormats/VertexReco",
  "DataFormats/BTauReco", "DataFormats/BeamSpot", "DataFormats/CSCRecHit",
  "DataFormats/CaloRecHit", "DataFormats/CaloTowers", "DataFormats/CastorReco",
  "RecoLocalCalo/CaloRecCandCreator", "RecoLocalCalo/CaloTowersCreator",
  "RecoLocalCalo/Castor", "RecoLocalCalo/CastorReco",
  "RecoLocalCalo/Configuration", "RecoLocalCalo/EcalDeadChannelRecoveryAlgos",
  "RecoLocalCalo/EcalDeadChannelRecoveryProducers", "RecoLocalCalo/EcalRecAlgos",
  "RecoLocalCalo/EcalRecProducers", "RecoLocalCalo/HcalLaserReco",
  "RecoLocalCalo/HcalRecAlgos", "RecoLocalCalo/HcalRecProducers",
  "RecoLocalMuon/CSCEfficiency", "RecoLocalMuon/CSCRecHitD",
  "RecoLocalMuon/CSCSegment", "RecoLocalMuon/CSCValidation",
  "RecoLocalMuon/Configuration", "RecoLocalMuon/DTRecHit",
  "RecoLocalMuon/DTSegment", "RecoLocalMuon/RPCRecHit",
  "RecoLocalTracker/ClusterParameterEstimator", "RecoLocalTracker/Configuration",
  "RecoLocalTracker/Records", "RecoLocalTracker/SiPixelClusterizer",
  "RecoLocalTracker/SiPixelRecHits", "RecoLocalTracker/SiStripClusterizer",
  "RecoLocalTracker/SiStripRecHitConverter",
  "RecoLocalTracker/SiStripZeroSuppression",
  "RecoLocalTracker/SubCollectionProducers", "RecoLuminosity/LumiProducer",
  "RecoLuminosity/TCPReceiver", "RecoMET/Configuration", "RecoMET/METAlgorithms",
  "RecoMET/METProducers", "RecoMuon/Configuration",
  "RecoMuon/CosmicMuonProducer", "RecoMuon/DetLayers",
  "RecoMuon/GlobalMuonProducer", "RecoMuon/GlobalTrackFinder",
  "RecoMuon/GlobalTrackingTools", "RecoMuon/L2MuonIsolationProducer",
  "RecoMuon/L2MuonProducer", "RecoMuon/L2MuonSeedGenerator",
  "RecoMuon/L3MuonIsolationProducer", "RecoMuon/L3MuonProducer",
  "RecoMuon/L3TrackFinder", "RecoMuon/MeasurementDet",
  "RecoMuon/MuonIdentification", "RecoMuon/MuonIsolation",
  "RecoMuon/MuonIsolationProducers", "RecoMuon/MuonSeedGenerator",
  "RecoMuon/Navigation", "RecoMuon/Records", "RecoMuon/StandAloneMuonProducer",
  "RecoMuon/StandAloneTrackFinder", "RecoMuon/TrackerSeedGenerator",
  "RecoMuon/TrackingTools", "RecoMuon/TransientTrackingRecHit",
  "RecoParticleFlow/Benchmark", "RecoParticleFlow/Configuration",
  "RecoParticleFlow/PFBlockProducer", "RecoParticleFlow/PFClusterProducer",
  "RecoParticleFlow/PFClusterShapeProducer", "RecoParticleFlow/PFClusterTools",
  "RecoParticleFlow/PFProducer", "RecoParticleFlow/PFRootEvent",
  "RecoParticleFlow/PFSimProducer", "RecoParticleFlow/PFTracking",
  "RecoPixelVZero/PixelVZeroFinding", "RecoPixelVertexing/Configuration",
  "RecoPixelVertexing/PixelLowPtUtilities",
  "RecoPixelVertexing/PixelTrackFitting", "RecoPixelVertexing/PixelTriplets",
  "RecoPixelVertexing/PixelVertexFinding", "RecoRomanPot/Configuration",
  "RecoRomanPot/RecoFP420", "RecoTBCalo/EcalSimpleTBAnalysis",
  "RecoTBCalo/EcalTBAnalysisCoreTools",
  "RecoTBCalo/EcalTBHodoscopeReconstructor", "RecoTBCalo/EcalTBRecProducers",
  "RecoTBCalo/EcalTBTDCReconstructor", "RecoTBCalo/HcalPlotter",
  "RecoTBCalo/HcalTBObjectUnpacker", "RecoTBCalo/HcalTBTools",
  "RecoTBCalo/ZDCTBAnalysis", "RecoTauTag/Configuration",
  "RecoTauTag/ImpactParameter", "RecoTauTag/RecoTau", "RecoTauTag/TauTagTools",
  "RecoTracker/CkfPattern", "RecoTracker/Configuration",
  "RecoTracker/ConversionSeedGenerators", "RecoTracker/DeDx",
  "RecoTracker/DebugTools", "RecoTracker/FinalTrackSelectors",
  "RecoTracker/GeometryESProducer", "RecoTracker/IterativeTracking",
  "RecoTracker/MeasurementDet", "RecoTracker/NuclearSeedGenerator",
  "RecoTracker/Record", "RecoTracker/SingleTrackPattern",
  "RecoTracker/SpecialSeedGenerators", "RecoTracker/TkDetLayers",
  "RecoTracker/TkHitPairs", "RecoTracker/TkMSParametrization",
  "RecoTracker/TkNavigation", "RecoTracker/TkSeedGenerator",
  "RecoTracker/TkSeedingLayers", "RecoTracker/TkTrackingRegions",
  "RecoTracker/TrackProducer", "RecoTracker/TransientTrackingRecHit",
  "Validation/RecoHI", "RecoVZero/VZeroFinding",
  "RecoVertex/AdaptiveVertexFinder", "RecoVertex/AdaptiveVertexFit",
  "RecoVertex/BeamSpotProducer", "RecoVertex/ConfigurableVertexReco",
  "RecoVertex/Configuration", "RecoVertex/GaussianSumVertexFit",
  "RecoVertex/GhostTrackFitter", "RecoVertex/KalmanVertexFit",
  "RecoVertex/KinematicFit", "RecoVertex/KinematicFitPrimitives",
  "RecoVertex/LinearizationPointFinders", "RecoVertex/MultiVertexFit",
  "RecoVertex/NuclearInteractionProducer", "RecoVertex/PrimaryVertexProducer",
  "RecoVertex/TertiaryTracksVertexFinder",
  "RecoVertex/TrimmedKalmanVertexFinder", "RecoVertex/TrimmedVertexFit",
  "RecoVertex/V0Producer", "RecoVertex/VertexPrimitives",
  "RecoVertex/VertexTools", "TrackPropagation/NavGeometry",
  "TrackPropagation/NavPropagator", "TrackPropagation/RungeKutta",
  "TrackPropagation/SteppingHelixPropagator",
  "TrackingTools/AnalyticalJacobians", "TrackingTools/Configuration",
  "TrackingTools/DetLayers", "TrackingTools/GeomPropagators",
  "TrackingTools/GsfTools", "TrackingTools/GsfTracking", "TrackingTools/IPTools",
  "TrackingTools/KalmanUpdators", "TrackingTools/MaterialEffects",
  "TrackingTools/MeasurementDet", "TrackingTools/PatternTools",
  "TrackingTools/Producers", "TrackingTools/RecoGeometry",
  "TrackingTools/Records", "TrackingTools/TrackAssociator",
  "TrackingTools/TrackFitters", "TrackingTools/TrackRefitter",
  "TrackingTools/TrajectoryCleaning", "TrackingTools/TrajectoryFiltering",
  "TrackingTools/TrajectoryParametrization", "TrackingTools/TrajectoryState",
  "TrackingTools/TransientTrack", "TrackingTools/TransientTrackingRecHit",
  "Utilities/RelMon", "Validation/Configuration", "RecoBTag/BTagTools",
  "RecoBTag/Configuration", "RecoBTag/ImpactParameter",
  "RecoBTag/ImpactParameterLearning", "RecoBTag/PerformanceDB",
  "RecoBTag/Records", "RecoBTag/SecondaryVertex", "RecoBTag/Skimming",
  "RecoBTag/SoftLepton", "RecoBTag/TrackProbability", "RecoBTag/XMLCalibration",
  "RecoBTau/Configuration", "RecoBTau/JetCrystalsAssociator",
  "RecoBTau/JetTagComputer", "RecoBTau/JetTagMVALearning",
  "RecoCaloTools/EcalChannelKiller", "RecoCaloTools/MetaCollections",
  "RecoCaloTools/Navigation", "RecoCaloTools/Selectors",
  "RecoEcal/Configuration", "RecoEcal/EgammaClusterAlgos",
  "RecoEcal/EgammaClusterProducers", "RecoEcal/EgammaCoreTools",
  "RecoEgamma/Configuration", "RecoEgamma/EgammaElectronAlgos",
  "RecoEgamma/EgammaElectronProducers", "RecoEgamma/EgammaHFProducers",
  "RecoEgamma/EgammaIsolationAlgos", "RecoEgamma/EgammaMCTools",
  "RecoEgamma/EgammaPhotonAlgos", "RecoEgamma/EgammaPhotonProducers",
  "RecoEgamma/EgammaTools", "RecoEgamma/ElectronIdentification",
  "RecoEgamma/Examples", "RecoEgamma/PhotonIdentification",
  "RecoHI/Configuration", "RecoHI/HiCentralityAlgos", "RecoHI/HiEgammaAlgos",
  "RecoHI/HiEvtPlaneAlgos", "RecoHI/HiJetAlgos", "RecoHI/HiMuonAlgos",
  "RecoHI/HiTracking", "RecoJets/Configuration", "RecoJets/FFTJetAlgorithms",
  "RecoJets/FFTJetProducers", "RecoJets/JetAlgorithms", "RecoJets/JetAnalyzers",
  "RecoJets/JetAssociationAlgorithms", "RecoJets/JetAssociationProducers",
  "RecoJets/JetPlusTracks", "RecoJets/JetProducers"], "db":
  ["CondFormats/EgammaObjects", "CondFormats/GeometryObjects",
  "CondFormats/HIObjects", "CondFormats/HLTObjects", "CondFormats/HcalMapping",
  "CondFormats/HcalObjects", "CondFormats/JetMETObjects",
  "CondFormats/L1TObjects", "CondFormats/Luminosity",
  "CondFormats/OptAlignObjects", "CondFormats/PhysicsToolsObjects",
  "CondFormats/RPCObjects", "CondFormats/RecoMuonObjects", "CondFormats/RunInfo",
  "CondFormats/SiPixelObjects", "CondFormats/SiStripObjects", "CondTools/DQM",
  "CondTools/DT", "CondTools/Ecal", "CondTools/Geometry", "CondTools/HLT",
  "CondTools/Hcal", "CondTools/IntegrationTest", "CondTools/L1Trigger",
  "CondTools/O2OFramework", "CondTools/RPC", "CondTools/RunInfo",
  "CondTools/SiPixel", "CondTools/SiStrip", "CondTools/Utilities",
  "CommonTools/ConditionDBWriter", "CondCore/AlignmentPlugins",
  "CondCore/BTauPlugins", "CondCore/BeamSpotPlugins", "CondCore/CSCPlugins",
  "CondCore/CalibPlugins", "CondCore/CastorPlugins", "CondCore/DBCommon",
  "CondCore/DBOutputService", "CondCore/DQMPlugins", "CondCore/DTPlugins",
  "CondCore/ESPlugins", "CondCore/ESSources", "CondCore/EcalPlugins",
  "CondCore/EgammaPlugins", "CondCore/GeometryPlugins", "CondCore/HLTPlugins",
  "CondCore/HcalPlugins", "CondCore/IOVService", "CondCore/JetMETPlugins",
  "CondCore/L1TPlugins", "CondCore/LuminosityPlugins",
  "CondCore/MetaDataService", "CondCore/ORA", "CondCore/OptAlignPlugins",
  "CondCore/PhysicsToolsPlugins", "CondCore/PopCon", "CondCore/RPCPlugins",
  "CondCore/RecoMuonPlugins", "CondCore/RegressionTest",
  "CondCore/RunInfoPlugins", "CondCore/SiPixelPlugins",
  "CondCore/SiStripPlugins", "CondCore/Utilities", "CondFormats/Alignment",
  "CondFormats/AlignmentRecord", "CondFormats/BTauObjects",
  "CondFormats/BeamSpotObjects", "CondFormats/CSCObjects",
  "CondFormats/Calibration", "CondFormats/CastorObjects", "CondFormats/Common",
  "CondFormats/DQMObjects", "CondFormats/DTObjects", "CondFormats/DataRecord",
  "CondFormats/ESObjects", "CondFormats/EcalCorrections",
  "CondFormats/EcalObjects", "CaloOnlineTools/HcalOnlineDb",
  "OnlineDB/CSCCondDB", "OnlineDB/EcalCondDB", "OnlineDB/Oracle",
  "OnlineDB/SiStripConfigDb", "OnlineDB/SiStripESSources", "OnlineDB/SiStripO2O",
  "RecoLuminosity/LumiDB"], "geometry": ["Configuration/Geometry",
  "DetectorDescription/Algorithm", "DetectorDescription/Base",
  "DetectorDescription/Core", "DetectorDescription/ExprAlgo",
  "DetectorDescription/OfflineDBLoader", "DetectorDescription/OnlineDBLoader",
  "DetectorDescription/Parser", "DetectorDescription/RegressionTest",
  "DetectorDescription/Schema", "Geometry/CMSCommonData", "Geometry/CSCGeometry",
  "Geometry/CSCGeometryBuilder", "Geometry/CaloEventSetup",
  "Geometry/CaloGeometry", "Geometry/CaloTopology", "Geometry/CommonDetUnit",
  "Geometry/CommonTopologies", "Geometry/DTGeometry",
  "Geometry/DTGeometryBuilder", "Geometry/EcalAlgo", "Geometry/EcalCommonData",
  "Geometry/EcalMapping", "Geometry/EcalSimData", "Geometry/EcalTestBeam",
  "Geometry/FP420CommonData", "Geometry/FP420SimData",
  "Geometry/ForwardCommonData", "Geometry/ForwardGeometry",
  "Geometry/ForwardSimData", "Geometry/GEMGeometry",
  "Geometry/GEMGeometryBuilder", "Geometry/GlobalTrackingGeometryBuilder",
  "Geometry/HcalAlgo", "Geometry/HcalCommonData", "Geometry/HcalEventSetup",
  "Geometry/HcalSimData", "Geometry/HcalTestBeamData", "Geometry/HcalTowerAlgo",
  "Geometry/MTCCTrackerCommonData", "Geometry/MuonCommonData",
  "Geometry/MuonNumbering", "Geometry/MuonSimData", "Geometry/RPCGeometry",
  "Geometry/RPCGeometryBuilder", "Geometry/Records",
  "Geometry/TrackerCommonData", "Geometry/TrackerGeometryBuilder",
  "Geometry/TrackerNumberingBuilder", "Geometry/TrackerRecoData",
  "Geometry/TrackerSimData", "Geometry/TrackingGeometryAligner",
  "Geometry/TwentyFivePercentTrackerCommonData",
  "GeometryReaders/XMLIdealGeometryESSource", "DataFormats/DetId",
  "DataFormats/EcalDetId", "Validation/Geometry", "Validation/MuonRPCGeometry",
  "SLHCUpgradeSimulations/Geometry", "Validation/CheckOverlap"], "hlt":
  ["CondFormats/HLTObjects", "CondTools/HLT", "Configuration/HLT",
  "CondCore/HLTPlugins", "HLTrigger/Configuration", "HLTrigger/Egamma",
  "HLTrigger/HLTanalyzers", "HLTrigger/HLTcore", "HLTrigger/HLTexample",
  "HLTrigger/HLTfilters", "HLTrigger/JetMET", "HLTrigger/Muon",
  "HLTrigger/Timer", "HLTrigger/Tools", "HLTrigger/btau", "HLTrigger/special",
  "DataFormats/HLTReco", "RecoTauTag/HLTProducers", "RecoEgamma/EgammaHLTAlgos",
  "RecoEgamma/EgammaHLTProducers"], "analysis": ["CondFormats/JetMETObjects",
  "DPGAnalysis/SiStripTools", "CommonTools/CandAlgos", "CommonTools/CandUtils",
  "CommonTools/Clustering1D", "CommonTools/ParticleFlow",
  "CommonTools/RecoUtils", "CommonTools/Statistics", "CommonTools/TriggerUtils",
  "CommonTools/UtilAlgos", "CommonTools/Utils",
  "AnalysisAlgos/SiStripClusterInfoProducer", "AnalysisAlgos/TrackInfoProducer",
  "AnalysisDataFormats/EWK", "AnalysisDataFormats/Egamma",
  "AnalysisDataFormats/SUSYBSMObjects", "AnalysisDataFormats/SiStripClusterInfo",
  "AnalysisDataFormats/TopObjects", "AnalysisDataFormats/TrackInfo",
  "DiffractiveForwardAnalysis/Configuration",
  "DiffractiveForwardAnalysis/Skimming", "EgammaAnalysis/CSA07Skims",
  "EgammaAnalysis/Configuration", "EgammaAnalysis/ElectronIDESSources",
  "EgammaAnalysis/PhotonIDProducers", "ElectroWeakAnalysis/Configuration",
  "ElectroWeakAnalysis/Skimming", "ElectroWeakAnalysis/Utilities",
  "ElectroWeakAnalysis/WENu", "ElectroWeakAnalysis/WMuNu",
  "ElectroWeakAnalysis/ZEE", "ElectroWeakAnalysis/ZMuMu",
  "MuonAnalysis/Configuration", "MuonAnalysis/MomentumScaleCalibration",
  "MuonAnalysis/MuonAssociators", "PhysicsTools/CandAlgos",
  "PhysicsTools/CandUtils", "PhysicsTools/CondLiteIO",
  "PhysicsTools/Configuration", "PhysicsTools/FWLite",
  "PhysicsTools/HepMCCandAlgos", "PhysicsTools/IsolationAlgos",
  "PhysicsTools/IsolationUtils", "PhysicsTools/JetCharge",
  "PhysicsTools/JetExamples", "PhysicsTools/JetMCAlgos",
  "PhysicsTools/JetMCUtils", "PhysicsTools/KinFitter",
  "PhysicsTools/MVAComputer", "PhysicsTools/MVATrainer",
  "PhysicsTools/ParallelAnalysis", "PhysicsTools/PatAlgos",
  "PhysicsTools/PatExamples", "PhysicsTools/PatUtils",
  "PhysicsTools/PythonAnalysis", "PhysicsTools/RecoAlgos",
  "PhysicsTools/RecoUtils", "PhysicsTools/RooStatsCms",
  "HeavyFlavorAnalysis/Configuration", "HeavyFlavorAnalysis/Skimming",
  "HeavyIonsAnalysis/Configuration", "HiggsAnalysis/Configuration",
  "HiggsAnalysis/HiggsToGammaGamma", "HiggsAnalysis/Skimming",
  "JetMETAnalysis/Configuration", "JetMETAnalysis/METSkims",
  "JetMETCorrections/Algorithms", "JetMETCorrections/Configuration",
  "JetMETCorrections/FFTJetModules", "JetMETCorrections/FFTJetObjects",
  "JetMETCorrections/InterpolationTables", "JetMETCorrections/IsolatedParticles",
  "JetMETCorrections/JetParton", "JetMETCorrections/JetVertexAssociation",
  "JetMETCorrections/MCJet", "JetMETCorrections/MinBias",
  "JetMETCorrections/Modules", "JetMETCorrections/Objects",
  "JetMETCorrections/TauJet", "JetMETCorrections/Type1MET",
  "DataFormats/PatCandidates", "DataFormats/Candidate", "RecoMET/METFilters",
  "SUSYBSMAnalysis/Configuration", "SUSYBSMAnalysis/HSCP",
  "SUSYBSMAnalysis/Skimming", "TBDataFormats/EcalTBObjects",
  "TBDataFormats/HcalTBObjects", "TopQuarkAnalysis/Configuration",
  "TopQuarkAnalysis/Examples", "TopQuarkAnalysis/TopEventProducers",
  "TopQuarkAnalysis/TopEventSelection", "TopQuarkAnalysis/TopHitFit",
  "TopQuarkAnalysis/TopJetCombination", "TopQuarkAnalysis/TopKinFitter",
  "TopQuarkAnalysis/TopObjectResolutions", "TopQuarkAnalysis/TopPairBSM",
  "TopQuarkAnalysis/TopSkimming", "TopQuarkAnalysis/TopTools",
  "Utilities/BinningTools", "PhysicsTools/SelectorUtils",
  "PhysicsTools/TagAndProbe", "PhysicsTools/UtilAlgos", "PhysicsTools/Utilities",
  "QCDAnalysis/ChargedHadronSpectra", "QCDAnalysis/Configuration",
  "QCDAnalysis/Skimming", "QCDAnalysis/UEAnalysis"], "fastsim":
  ["FastSimDataFormats/External", "FastSimDataFormats/L1GlobalMuonTrigger",
  "FastSimDataFormats/NuclearInteractions", "FastSimDataFormats/PileUpEvents",
  "FastSimulation/BaseParticlePropagator", "FastSimulation/CaloGeometryTools",
  "FastSimulation/CaloHitMakers", "FastSimulation/CaloRecHitsProducer",
  "FastSimulation/CalorimeterProperties", "FastSimulation/Calorimetry",
  "FastSimulation/Configuration", "FastSimulation/EgammaElectronAlgos",
  "FastSimulation/Event", "FastSimulation/EventProducer",
  "FastSimulation/ForwardDetectors", "FastSimulation/HighLevelTrigger",
  "FastSimulation/L1CaloTriggerProducer", "FastSimulation/MaterialEffects",
  "FastSimulation/MuonSimHitProducer", "FastSimulation/Muons",
  "FastSimulation/Particle", "FastSimulation/ParticleDecay",
  "FastSimulation/ParticleFlow", "FastSimulation/ParticlePropagator",
  "FastSimulation/PileUpProducer", "FastSimulation/ShowerDevelopment",
  "FastSimulation/TrackerSetup", "FastSimulation/Tracking",
  "FastSimulation/TrackingRecHitProducer", "FastSimulation/TrajectoryManager",
  "FastSimulation/Utilities", "FastSimulation/Validation"], "visualization":
  ["Fireworks/Calo", "Fireworks/Candidates", "Fireworks/Core",
  "Fireworks/Electrons", "Fireworks/Eve", "Fireworks/FWInterface",
  "Fireworks/GenParticle", "Fireworks/Geometry", "Fireworks/Macros",
  "Fireworks/Muons", "Fireworks/ParticleFlow", "Fireworks/SimData",
  "Fireworks/TableWidget", "Fireworks/Tracks", "Fireworks/Vertices"],
  "generators": ["Configuration/Generator", "GeneratorInterface/AMPTInterface",
  "GeneratorInterface/AlpgenInterface", "GeneratorInterface/BeamHaloGenerator",
  "GeneratorInterface/CascadeInterface", "GeneratorInterface/Configuration",
  "GeneratorInterface/Core", "GeneratorInterface/CosmicMuonGenerator",
  "GeneratorInterface/ExhumeInterface", "GeneratorInterface/ExternalDecays",
  "GeneratorInterface/GenExtensions", "GeneratorInterface/GenFilters",
  "GeneratorInterface/Herwig6Interface", "GeneratorInterface/HiGenCommon",
  "GeneratorInterface/HijingInterface", "GeneratorInterface/HydjetInterface",
  "GeneratorInterface/LHEInterface", "GeneratorInterface/MCatNLOInterface",
  "GeneratorInterface/PartonShowerVeto", "GeneratorInterface/PomwigInterface",
  "GeneratorInterface/PyquenInterface", "GeneratorInterface/Pythia6Interface",
  "GeneratorInterface/Pythia8Interface",
  "GeneratorInterface/ReggeGribovPartonMCInterface",
  "GeneratorInterface/RivetInterface", "GeneratorInterface/SherpaInterface",
  "GeneratorInterface/ThePEGInterface", "DataFormats/HepMCCandidate",
  "Validation/EventGenerator"], "daq": ["Configuration/SiStripDAQ",
  "EventFilter/AutoBU", "EventFilter/Configuration", "EventFilter/Cosmics",
  "EventFilter/ESDigiToRaw", "EventFilter/EcalDigiToRaw",
  "EventFilter/FEDInterface", "EventFilter/Goodies",
  "EventFilter/Message2log4cplus", "EventFilter/Modules", "EventFilter/Playback",
  "EventFilter/Processor", "EventFilter/RawDataCollector",
  "EventFilter/ResourceBroker", "EventFilter/SMProxyServer",
  "EventFilter/ShmBuffer", "EventFilter/ShmReader",
  "EventFilter/SiStripChannelChargeFilter", "EventFilter/StorageManager",
  "EventFilter/Utilities", "IORawData/DaqSource", "DataFormats/FEDRawData"],
  "dqm": ["CondTools/DQM", "DQM/BeamMonitor", "DQM/CSCMonitorModule",
  "DQM/CastorMonitor", "DQM/DTMonitorClient", "DQM/DTMonitorModule",
  "DQM/DataScouting", "CommonTools/TrackerMap", "CondCore/DQMPlugins",
  "CondFormats/DQMObjects", "HLTriggerOffline/Common", "HLTriggerOffline/Egamma",
  "HLTriggerOffline/HeavyFlavor", "HLTriggerOffline/Higgs",
  "HLTriggerOffline/JetMET", "HLTriggerOffline/Muon", "HLTriggerOffline/SUSYBSM",
  "HLTriggerOffline/Tau", "HLTriggerOffline/Top", "DataFormats/Histograms",
  "DQM/EcalBarrelMonitorClient", "DQM/EcalBarrelMonitorDbModule",
  "DQM/EcalBarrelMonitorModule", "DQM/EcalBarrelMonitorTasks", "DQM/EcalCommon",
  "DQM/EcalEndcapMonitorClient", "DQM/EcalEndcapMonitorDbModule",
  "DQM/EcalEndcapMonitorModule", "DQM/EcalEndcapMonitorTasks",
  "DQM/EcalPreshowerMonitorClient", "DQM/EcalPreshowerMonitorModule",
  "DQM/HLTEvF", "DQM/HLXMonitor", "DQM/HcalMonitorClient",
  "DQM/HcalMonitorModule", "DQM/HcalMonitorTasks", "DQM/L1TMonitor",
  "DQM/L1TMonitorClient", "DQM/Physics", "DQM/PhysicsObjectsMonitoring",
  "DQM/RCTMonitor", "DQM/RPCMonitorClient", "DQM/RPCMonitorDigi",
  "DQM/SiPixelCommon", "DQM/SiPixelHistoricInfoClient",
  "DQM/SiPixelMonitorClient", "DQM/SiPixelMonitorCluster",
  "DQM/SiPixelMonitorDigi", "DQM/SiPixelMonitorRawData",
  "DQM/SiPixelMonitorRecHit", "DQM/SiPixelMonitorTrack",
  "DQM/SiStripCommissioningAnalysis", "DQM/SiStripCommissioningClients",
  "DQM/SiStripCommissioningDbClients", "DQM/SiStripCommissioningSources",
  "DQM/SiStripCommissioningSummary", "DQM/SiStripCommon",
  "DQM/SiStripHistoricInfoClient", "DQM/SiStripMonitorClient",
  "DQM/SiStripMonitorCluster", "DQM/SiStripMonitorDigi",
  "DQM/SiStripMonitorHardware", "DQM/SiStripMonitorPedestals",
  "DQM/SiStripMonitorSummary", "DQM/SiStripMonitorTrack", "DQM/TrackerCommon",
  "DQM/TrackerMonitorTrack", "DQM/TrackingMonitor", "DQM/TrigXMonitor",
  "DQM/TrigXMonitorClient", "DQMOffline/Alignment", "DQMOffline/CalibCalo",
  "DQMOffline/CalibMuon", "DQMOffline/CalibTracker", "DQMOffline/Configuration",
  "DQMOffline/EGamma", "DQMOffline/Ecal", "DQMOffline/Hcal", "DQMOffline/JetMET",
  "DQMOffline/L1Trigger", "DQMOffline/Muon", "DQMOffline/PFTau",
  "DQMOffline/RecoB", "DQMOffline/Trigger", "DQMServices/ClientConfig",
  "DQMServices/Components", "DQMServices/Core", "DQMServices/Diagnostic",
  "DQMServices/Examples", "DQMServices/FwkIO", "DQMServices/XdaqCollector",
  "Validation/GlobalDigis", "Validation/GlobalHits", "Validation/GlobalRecHits",
  "Validation/HcalDigis", "Validation/HcalHits", "Validation/HcalRecHits",
  "Validation/Mixing", "Validation/MuonCSCDigis", "Validation/MuonDTDigis",
  "Validation/MuonHits", "Validation/MuonIdentification",
  "Validation/MuonIsolation", "Validation/MuonRPCDigis", "Validation/RPCRecHits",
  "Validation/RecoB", "Validation/RecoEgamma", "Validation/RecoJets",
  "Validation/RecoMET", "Validation/RecoMuon", "Validation/RecoParticleFlow",
  "Validation/RecoPixelVertexing", "Validation/RecoTau", "Validation/RecoTrack",
  "Validation/RecoVertex", "Validation/TrackerConfiguration",
  "Validation/TrackerDigis", "Validation/TrackerHits",
  "Validation/TrackerRecHits", "Validation/TrackingMCTruth",
  "Validation/CSCRecHits", "Validation/CaloTowers", "Validation/Configuration",
  "Validation/DTRecHits", "Validation/EcalClusters", "Validation/EcalDigis",
  "Validation/EcalHits", "Validation/EcalRecHits"], "l1":
  ["CondFormats/L1TObjects", "CondTools/L1Trigger", "CondCore/L1TPlugins",
  "CalibCalorimetry/CaloTPG", "CalibCalorimetry/EcalTPGTools",
  "CalibCalorimetry/HcalTPGAlgos", "CalibCalorimetry/HcalTPGEventSetup",
  "CalibCalorimetry/HcalTPGIO", "EventFilter/CSCTFRawToDigi",
  "EventFilter/DTTFRawToDigi", "EventFilter/GctRawToDigi",
  "EventFilter/L1GlobalTriggerRawToDigi", "L1Trigger/TextToDigi",
  "L1TriggerConfig/CSCTFConfigProducers", "L1TriggerConfig/DTTPGConfig",
  "L1TriggerConfig/DTTPGConfigProducers", "L1TriggerConfig/DTTrackFinder",
  "L1TriggerConfig/GMTConfigProducers", "L1TriggerConfig/GctConfigProducers",
  "L1TriggerConfig/L1CSCTPConfigProducers",
  "L1TriggerConfig/L1GeometryProducers", "L1TriggerConfig/L1GtConfigProducers",
  "L1TriggerConfig/L1ScalesProducers", "L1TriggerConfig/RCTConfigProducers",
  "L1TriggerConfig/RPCTriggerConfig", "L1TriggerOffline/Configuration",
  "L1TriggerOffline/L1Analyzer", "L1Trigger/CSCCommonTrigger",
  "L1Trigger/CSCTrackFinder", "L1Trigger/CSCTriggerPrimitives",
  "L1Trigger/Configuration", "L1Trigger/DTBti", "L1Trigger/DTSectorCollector",
  "L1Trigger/DTTrackFinder", "L1Trigger/DTTraco", "L1Trigger/DTTrigger",
  "L1Trigger/DTTriggerServerPhi", "L1Trigger/DTTriggerServerTheta",
  "L1Trigger/DTUtilities", "L1Trigger/GlobalCaloTrigger",
  "L1Trigger/GlobalMuonTrigger", "L1Trigger/GlobalTrigger",
  "L1Trigger/GlobalTriggerAnalyzer", "L1Trigger/HardwareValidation",
  "L1Trigger/L1ExtraFromDigis", "L1Trigger/L1GctAnalyzer",
  "L1Trigger/RPCTechnicalTrigger", "L1Trigger/RPCTrigger",
  "L1Trigger/RegionalCaloTrigger", "L1Trigger/Skimmer",
  "DataFormats/L1CSCTrackFinder", "DataFormats/L1CaloTrigger",
  "DataFormats/L1DTTrackFinder", "DataFormats/L1GlobalCaloTrigger",
  "DataFormats/L1GlobalMuonTrigger", "DataFormats/L1GlobalTrigger",
  "DataFormats/L1Trigger", "DataFormats/LTCDigi", "DQMOffline/L1Trigger",
  "SimCalorimetry/EcalTrigPrimAlgos", "SimCalorimetry/EcalTrigPrimProducers",
  "SimCalorimetry/HcalTrigPrimAlgos", "SimCalorimetry/HcalTrigPrimProducers",
  "Validation/EcalTriggerPrimitives"], "alca":
  ["CondFormats/EgammaObjects", "CondFormats/GeometryObjects",
  "CondFormats/HIObjects", "CondFormats/HLTObjects", "CondFormats/HcalMapping",
  "CondFormats/HcalObjects", "CondFormats/L1TObjects", "CondFormats/Luminosity",
  "CondFormats/OptAlignObjects", "CondFormats/PhysicsToolsObjects",
  "CondFormats/RPCObjects", "CondFormats/RecoMuonObjects", "CondFormats/RunInfo",
  "CondFormats/SiPixelObjects", "CondFormats/SiStripObjects",
  "Configuration/AlCa", "CondCore/DBCommon", "CondCore/DBOutputService",
  "CondCore/ESSources", "CondCore/IOVService", "CondCore/MetaDataService",
  "CondCore/Modules", "CondCore/PluginSystem", "CondCore/PopCon",
  "CondCore/TagCollection", "CondFormats/Alignment",
  "CondFormats/AlignmentRecord", "CondFormats/BTauObjects",
  "CondFormats/BeamSpotObjects", "CondFormats/CSCObjects",
  "CondFormats/Calibration", "CondFormats/CastorObjects", "CondFormats/Common",
  "CondFormats/DTObjects", "CondFormats/DataRecord", "CondFormats/ESObjects",
  "CondFormats/EcalCorrections", "CondFormats/EcalObjects",
  "Alignment/CocoaAnalysis", "Alignment/CocoaApplication",
  "Alignment/CocoaDDLObjects", "Alignment/CocoaDaq", "Alignment/CocoaFit",
  "Alignment/CocoaModel", "Alignment/CocoaToDDL", "Alignment/CocoaUtilities",
  "Alignment/CommonAlignment", "Alignment/CommonAlignmentAlgorithm",
  "Alignment/CommonAlignmentMonitor", "Alignment/CommonAlignmentParametrization",
  "Alignment/CommonAlignmentProducer", "Alignment/Geners",
  "Alignment/HIPAlignmentAlgorithm", "Alignment/KalmanAlignmentAlgorithm",
  "Alignment/LaserAlignment", "Alignment/LaserAlignmentSimulation",
  "Alignment/LaserDQM", "Alignment/MillePedeAlignmentAlgorithm",
  "Alignment/MuonAlignment", "Alignment/MuonAlignmentAlgorithms",
  "Alignment/OfflineValidation", "Alignment/ReferenceTrajectories",
  "Alignment/SurveyAnalysis", "Alignment/TrackerAlignment",
  "Alignment/TwoBodyDecay", "CalibCalorimetry/CaloMiscalibTools",
  "CalibCalorimetry/CaloTPG", "CalibCalorimetry/CastorCalib",
  "CalibCalorimetry/Configuration", "CalibCalorimetry/EcalCorrectionModules",
  "CalibCalorimetry/EcalCorrelatedNoiseAnalysisAlgos",
  "CalibCalorimetry/EcalCorrelatedNoiseAnalysisModules",
  "CalibCalorimetry/EcalLaserAnalyzer", "CalibCalorimetry/EcalLaserCorrection",
  "CalibCalorimetry/EcalLaserSorting", "CalibCalorimetry/EcalPedestalOffsets",
  "CalibCalorimetry/EcalSRTools", "CalibCalorimetry/EcalTBCondTools",
  "CalibCalorimetry/EcalTPGTools", "CalibCalorimetry/EcalTrivialCondModules",
  "CalibCalorimetry/HcalAlgos", "CalibCalorimetry/HcalPlugins",
  "CalibCalorimetry/HcalStandardModules", "CalibCalorimetry/HcalTPGAlgos",
  "CalibCalorimetry/HcalTPGEventSetup", "CalibCalorimetry/HcalTPGIO",
  "CalibFormats/CaloObjects", "CalibFormats/CaloTPG",
  "CalibFormats/CastorObjects", "CalibFormats/HcalObjects",
  "CalibFormats/SiPixelObjects", "CalibFormats/SiStripObjects",
  "CalibMuon/CSCCalibration", "CalibMuon/Configuration",
  "CalibMuon/DTCalibration", "CalibMuon/DTDigiSync", "CalibMuon/RPCCalibration",
  "CalibTracker/Configuration", "CalibTracker/Records",
  "CalibTracker/SiPixelConnectivity", "CalibTracker/SiPixelESProducers",
  "CalibTracker/SiPixelErrorEstimation", "CalibTracker/SiPixelGainCalibration",
  "CalibTracker/SiPixelIsAliveCalibration", "CalibTracker/SiPixelLorentzAngle",
  "CalibTracker/SiPixelSCurveCalibration", "CalibTracker/SiPixelTools",
  "CalibTracker/SiStripAPVAnalysis", "CalibTracker/SiStripChannelGain",
  "CalibTracker/SiStripCommon", "CalibTracker/SiStripDCS",
  "CalibTracker/SiStripESProducers", "CalibTracker/SiStripHitEfficiency",
  "CalibTracker/SiStripLorentzAngle", "CalibTracker/SiStripQuality",
  "Calibration/EcalAlCaRecoProducers", "Calibration/EcalCalibAlgos",
  "Calibration/EcalTBTools", "Calibration/HcalAlCaRecoProducers",
  "Calibration/HcalCalibAlgos", "Calibration/HcalConnectivity",
  "Calibration/HcalIsolatedTrackReco", "Calibration/IsolatedParticles",
  "Calibration/TkAlCaRecoProducers", "Calibration/Tools",
  "CaloOnlineTools/EcalTools", "IORawData/CaloPatterns",
  "IORawData/DTCommissioning", "IORawData/HcalTBInputService",
  "IORawData/SiPixelInputSources", "DataFormats/HcalCalibObjects",
  "DataFormats/Alignment", "RecoVertex/BeamSpotProducer"], "simulation":
  ["Mixing/Base", "IOMC/EventVertexGenerators", "DataFormats/DTDigi",
  "DataFormats/EcalDigi", "DataFormats/EcalRawData", "DataFormats/FP420Digi",
  "DataFormats/GeometryCommonDetAlgo", "DataFormats/GeometrySurface",
  "DataFormats/GeometryVector", "DataFormats/HcalDetId", "DataFormats/HcalDigi",
  "DataFormats/MuonDetId", "DataFormats/RPCDigi", "DataFormats/SiPixelDetId",
  "DataFormats/SiPixelDigi", "DataFormats/SiPixelRawData",
  "DataFormats/SiStripDetId", "DataFormats/SiStripDigi", "DataFormats/CSCDigi",
  "SimCalorimetry/CaloSimAlgos", "SimCalorimetry/CastorSim",
  "SimCalorimetry/Configuration", "SimCalorimetry/EcalElectronicsEmulation",
  "SimCalorimetry/EcalSelectiveReadoutAlgos",
  "SimCalorimetry/EcalSelectiveReadoutProducers", "SimCalorimetry/EcalSimAlgos",
  "SimCalorimetry/EcalSimProducers", "SimCalorimetry/EcalTestBeam",
  "SimCalorimetry/EcalTestBeamAlgos", "SimCalorimetry/EcalZeroSuppressionAlgos",
  "SimCalorimetry/EcalZeroSuppressionProducers", "SimCalorimetry/HcalSimAlgos",
  "SimCalorimetry/HcalSimProducers", "SimCalorimetry/HcalTestBeam",
  "SimCalorimetry/HcalZeroSuppressionProducers", "SimDataFormats/CaloHit",
  "SimDataFormats/CaloTest", "SimDataFormats/CrossingFrame",
  "SimDataFormats/DigiSimLinks", "SimDataFormats/EcalTestBeam",
  "SimDataFormats/EncodedEventId", "SimDataFormats/Forward",
  "SimDataFormats/GeneratorProducts", "SimDataFormats/HcalTestBeam",
  "SimDataFormats/HiGenData", "SimDataFormats/JetMatching",
  "SimDataFormats/PileupSummaryInfo", "SimDataFormats/RPCDigiSimLink",
  "SimDataFormats/RandomEngine", "SimDataFormats/SimHitMaker",
  "SimDataFormats/Track", "SimDataFormats/TrackerDigiSimLink",
  "SimDataFormats/TrackingAnalysis", "SimDataFormats/TrackingHit",
  "SimDataFormats/ValidationFormats", "SimDataFormats/Vertex", "SimG4CMS/Calo",
  "SimG4CMS/CherenkovAnalysis", "SimG4CMS/EcalTestBeam", "SimG4CMS/FP420",
  "SimG4CMS/Forward", "SimG4CMS/HcalTestBeam", "SimG4CMS/Muon",
  "SimG4CMS/ShowerLibraryProducer", "SimG4CMS/Tracker", "SimG4Core/Application",
  "SimG4Core/CheckSecondary", "SimG4Core/Configuration",
  "SimG4Core/CountProcesses", "SimG4Core/CustomPhysics", "SimG4Core/GFlash",
  "SimG4Core/Generators", "SimG4Core/Geometry", "SimG4Core/GeometryProducer",
  "SimG4Core/HelpfulWatchers", "SimG4Core/KillSecondaries",
  "SimG4Core/MagneticField", "SimG4Core/Notification", "SimG4Core/Physics",
  "SimG4Core/PhysicsLists", "SimG4Core/PrintGeomInfo",
  "SimG4Core/PrintTrackNumber", "SimG4Core/SaveSimTrackAction",
  "SimG4Core/SensitiveDetector", "SimG4Core/TrackingVerbose",
  "SimG4Core/Watcher", "SimGeneral/Configuration", "SimGeneral/DataMixingModule",
  "SimGeneral/GFlash", "SimGeneral/HepPDTESSource", "SimGeneral/HepPDTRecord",
  "SimGeneral/MixingModule", "SimGeneral/NoiseGenerators",
  "SimGeneral/PileupInformation", "SimGeneral/TrackingAnalysis",
  "SimMuon/CSCDigitizer", "SimMuon/Configuration", "SimMuon/DTDigitizer",
  "SimMuon/MCTruth", "SimMuon/Neutron", "SimMuon/RPCDigitizer",
  "SimRomanPot/Configuration", "SimRomanPot/SimFP420", "SimTracker/Common",
  "SimTracker/Configuration", "SimTracker/Records",
  "SimTracker/SiPixelDigitizer", "SimTracker/SiStripDigitizer",
  "SimTracker/TrackAssociation", "SimTracker/TrackAssociatorESProducer",
  "SimTracker/TrackHistory", "SimTracker/TrackerFilters",
  "SimTracker/TrackerHitAssociation", "SimTracker/TrackerMaterialAnalysis",
  "SimTracker/VertexAssociation", "SimTracker/VertexAssociatorESProducer",
  "SimTransport/HectorProducer", "TauAnalysis/MCEmbeddingTools",
  "TrackPropagation/Geant4e", "Validation/Configuration"]}
