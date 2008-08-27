import FWCore.ParameterSet.Config as cms

process = cms.Process("L1")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/relval/CMSSW_2_1_2/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_10TeV_v1/0005/162A3A26-5774-DD11-B0B6-001617C3B6DE.root',
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# standard includes
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "STARTUP_V6::All"


# unpack raw data
process.load("Configuration.StandardSequences.RawToDigi_cff")

# run trigger primitive generation on unpacked digis, then central L1
process.load("L1Trigger.Configuration.CaloTriggerPrimitives_cff")
process.load("L1Trigger.Configuration.SimL1Emulator_cff")
process.simEcalTriggerPrimitiveDigis.Label = 'ecalDigis'
process.simHcalTriggerPrimitiveDigis.inputLabel = 'hcalDigis'
process.simDtTriggerPrimitiveDigis.digiTag = 'muonDTDigis'
process.simCscTriggerPrimitiveDigis.CSCComparatorDigiProducer = cms.InputTag("muonCSCDigis","MuonCSCComparatorDigi")
process.simCscTriggerPrimitiveDigis.CSCWireDigiProducer = cms.InputTag("muonCSCDigis","MuonCSCWireDigi")
process.simRpcTriggerDigis.label = 'muonRPCDigis'

# L1 configuration
process.load('L1Trigger.Configuration.L1DummyConfig_cff')

# optional trigger configurations
#process.load('L1Trigger.Configuration.L1StartupConfig_cff')
#process.load('L1Trigger.Configuration.L1CruzetConfig_cff')

# Example for what collections are needed to re-run HLT
process.load('L1Trigger.Configuration.L1Trigger_EventContent_cff')
process.L1TriggerFEVTDEBUG.outputCommands.append(
    'keep FEDRawDataCollection_*_*_*'
)
process.out = cms.OutputModule("PoolOutputModule",
    process.L1TriggerFEVTDEBUG,
    fileName = cms.untracked.string("rerunL1.root")
)

process.p = cms.Path(
    process.ecalDigis
    *process.hcalDigis
    *process.muonDTDigis
    *process.muonCSCDigis
    *process.muonRPCDigis
    *process.CaloTriggerPrimitives
    *process.SimL1Emulator
)

process.o = cms.EndPath( process.out )
