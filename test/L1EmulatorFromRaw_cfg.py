#
# cfg file to re-run L1 Trigger emulator on a raw data file 
#
# V M Ghete 2009-02-27

###################### user choices ######################


# choose the type of sample used (True for RelVal, False for data)
useRelValSample = True 
#useRelValSample=False 

# choose the global tag type for RelVal
useGlobalTag = 'IDEAL'
#useGlobalTag='STARTUP'

# explicit choice of the L1 menu - available choices:
l1Menu = '8E29'
#l1Menu = '1E31'
#l1Menu == 'CRAFT2008'

###################### end user choices ###################


import FWCore.ParameterSet.Config as cms

# process
process = cms.Process('L1')

# number of events to be processed and source file
process.maxEvents = cms.untracked.PSet(
    input=cms.untracked.int32(200)
)

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
process.source = cms.Source ('PoolSource', fileNames=readFiles, secondaryFileNames=secFiles)

# type of sample used (True for RelVal, False for data)

if useRelValSample == True :
    if useGlobalTag == 'IDEAL':

        #/RelValTTbar/CMSSW_2_2_4_IDEAL_V11_v1/GEN-SIM-DIGI-RAW-HLTDEBUG
        dataset = cms.untracked.vstring('RelValTTbar_CMSSW_2_2_4_IDEAL_V11_v1')
        
        readFiles.extend([
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/IDEAL_V11_v1/0000/02697009-5CF3-DD11-A862-001D09F2423B.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/IDEAL_V11_v1/0000/064657A8-59F3-DD11-ACA5-000423D991F0.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/IDEAL_V11_v1/0000/0817F6DE-5BF3-DD11-880D-0019DB29C5FC.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/IDEAL_V11_v1/0000/0899697C-5AF3-DD11-9D21-001617DBD472.root'
            ]);


        secFiles.extend([
            ])

    elif useGlobalTag == 'STARTUP':

        #/RelValTTbar/CMSSW_2_2_4_STARTUP_V8_v1/GEN-SIM-DIGI-RAW-HLTDEBUG
        dataset = cms.untracked.vstring('RelValTTbar_CMSSW_2_2_4_STARTUP_V8_v1')
        
        readFiles.extend([
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/069AA022-5BF3-DD11-9A56-001617E30D12.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/08DA99A6-5AF3-DD11-AAC1-001D09F24493.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/0A725E15-5BF3-DD11-8B4B-000423D99CEE.root',
            '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/0AF5B676-5AF3-DD11-A22F-001617DBCF1E.root'
            ]);


        secFiles.extend([
            ])
    else :
        print 'Error: Global Tag ', useGlobalTag, ' not defined.'    

else : 

    # CRAFT data FIXME
    dataset = ''
    
    readFiles.extend([
        ]);

    secFiles.extend([
        ])


# unpack raw data
process.load('Configuration.StandardSequences.RawToDigi_cff')

# run trigger primitive generation on unpacked digis, then central L1
process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')
process.load('L1Trigger.Configuration.SimL1Emulator_cff')

#
#process.simEcalTriggerPrimitiveDigis.Label = 'ecalDigis'
#process.simHcalTriggerPrimitiveDigis.inputLabel = cms.InputTag('hcalDigis')
##
#process.simDtTriggerPrimitiveDigis.digiTag = 'muonDTDigis'
##
##process.simCscTriggerPrimitiveDigis.CSCComparatorDigiProducer = cms.InputTag('muonCSCDigis',
##                                                                             'MuonCSCComparatorDigi')
##process.simCscTriggerPrimitiveDigis.CSCWireDigiProducer = cms.InputTag('muonCSCDigis',
##                                                                       'MuonCSCWireDigi')
##
#process.simRpcTriggerDigis.label = 'muonRPCDigis'


# load and configure modules via Global Tag
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions

process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

if useRelValSample == True :
    if useGlobalTag == 'IDEAL':
        process.GlobalTag.globaltag = 'IDEAL_V11::All'

    elif useGlobalTag == 'STARTUP':
        process.GlobalTag.globaltag = 'STARTUP_V8::All'

    else :
        print 'Error: Global Tag ', useGlobalTag, ' not defined.'    

else :
    process.GlobalTag.globaltag = 'CRAFT_ALL_V8::All'


# explicit choice of the L1 menu

if l1Menu == '8E29' :
    process.load('L1Trigger.Configuration.L1StartupConfig_cff')
    process.load('L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v0_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff')
    
elif l1Menu == 'CRAFT2008' :
    process.load('L1Trigger.Configuration.L1StartupConfig_cff')
    process.load('L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v4_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff')
    
elif l1Menu == '1E31' :
    process.load('L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v0_L1T_Scales_20080922_Imp0_Unprescaled_cff')
else :
    print 'No such L1 menu: ', l1menu  
      

# Example for what collections are needed to re-run HLT
process.out = cms.OutputModule('PoolOutputModule',
    outputCommands=cms.untracked.vstring(
        #'keep FEDRawDataCollection_*_*_L1',
        #'keep *_simGtDigis_*_L1',
        #'keep *_simGmtDigis_*_L1',
        #'keep *_simGctDigis_*_L1',
        'keep *_hltGtDigis_*_HLT',
        'keep *_*_*_L1'
    ),
    fileName=cms.untracked.string('L1EmulatorFromRaw.root')
)

#process.p = cms.Path(process.ecalDigis 
#    * process.hcalDigis 
#    * process.muonDTDigis 
#    * process.muonCSCDigis 
#    * process.muonRPCDigis 
#    * process.CaloTriggerPrimitives 
#    * process.SimL1Emulator
#)

process.p = cms.Path(process.SimL1Emulator)

# Message Logger
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.debugModules = ['*']
process.MessageLogger.categories = ['*']
process.MessageLogger.destinations = ['cout']
process.MessageLogger.cout = cms.untracked.PSet(
    #threshold=cms.untracked.string('DEBUG'),
    #threshold = cms.untracked.string('INFO'),
    threshold = cms.untracked.string('ERROR'),
    DEBUG=cms.untracked.PSet(
        limit=cms.untracked.int32(-1)
    ),
    INFO=cms.untracked.PSet(
        limit=cms.untracked.int32(-1)
    ),
    WARNING=cms.untracked.PSet(
        limit=cms.untracked.int32(-1)
    ),
    ERROR=cms.untracked.PSet(
        limit=cms.untracked.int32(-1)
    )
)

process.o = cms.EndPath(process.out)
