import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

hltVertexTable = cms.EDProducer("HLTVertexTableProducer",
                                skipNonExistingSrc = cms.bool(True),
                                pvSrc = cms.InputTag("hltOfflinePrimaryVertices"),
                                goodPvCut = cms.string("!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0"), 
                                pfSrc = cms.InputTag("hltParticleFlowTmp"),
                                dlenMin = cms.double(0),
                                dlenSigMin = cms.double(3),
                                pvName = cms.string("hltPrimaryVertex"),
                                )
