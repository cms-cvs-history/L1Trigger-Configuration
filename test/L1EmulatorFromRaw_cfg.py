import FWCore.ParameterSet.Config as cms

process = cms.Process("L1")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("L1Trigger.Configuration.L1Config_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("L1Trigger.Configuration.SimL1Emulator_cff")

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring()
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.ecalTriggerPrimitiveDigis.Label = 'ecalDigis'
process.hcalTriggerPrimitiveDigis.inputLabel = 'hcalDigis'
process.dtTriggerPrimitiveDigis.digiTag = 'muonDTDigis'
process.cscTriggerPrimitiveDigis.CSCComparatorDigiProducer = 'muonCSCDigis'
process.rpcTriggerDigis.label = 'muonRPCDigis'


process.p = cms.Path(process.ecalDigis*process.hcalDigis*process.muonDTDigis*process.muonCSCDigis*process.muonRPCDigis)

process.PoolSource.fileNames = ['/store/relval/2008/2/5/RelVal-QCD_Pt_80_120-1202115095-HLT/0000/0C84C079-D8D3-DC11-BD81-001617E30E28.root']

