// l1TauValidation.C
//
// Produces a set of standard plots for L1 tau validation
// 
// Expects the following input files :
//   single_tau.root
//

void l1TauValidation()
{

  // Postscript file
  TPostScript* ps =new TPostScript("l1validation.ps", 112);
  
  // Canvas
  TCanvas *c1 = new TCanvas("c1","c1",800,800);
  
  
  /// single muon plots ///
//   TFile *f = new TFile("single_mu.root");
  
//   // muon resolutions & efficiencies
//   TString dir = "L1AnalyzerMuonMC";
  
//   Plot(f,dir+"/Resolutions/EtRes","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtCor","E_{T, Ref} (GeV)","E_{T, L1} (GeV)"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtaRes","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}"); c1->Update();
//   Plot(f,dir+"/Resolutions/PhiRes","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/PhiCor","#phi_{Ref} (rad)","#phi_{L1} (rad)"); c1->Update();
//   Plot(f,dir+"/Efficiencies/EtEff","E_{T} (GeV)","Efficiency","e"); c1->Update();
//   Plot(f,dir+"/Efficiencies/EtaEff","#eta","Efficiency","e"); c1->Update();
//   Plot(f,dir+"/Efficiencies/PhiEff","#phi (rad)","Efficiency","e"); c1->Update();

//   f->Close();
  
  /// single electron plots ///
  TFile *f = new TFile("single_e.root");
  
  // iso EM resolutions & efficiencies
  TString dir = "L1AnalyzerIsoEmMC";
  
  Plot(f,dir+"/Resolutions/EtRes","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/EtCor","E_{T, Ref} (GeV)","E_{T, L1} (GeV)"); c1->Update();
  Plot(f,dir+"/Resolutions/EtaRes","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}"); c1->Update();
  Plot(f,dir+"/Resolutions/PhiRes","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/PhiCor","#phi_{Ref} (rad)","#phi_{L1} (rad)"); c1->Update();
  Plot(f,dir+"/Efficiencies/EtEff","E_{T} (GeV)","Efficiency","e"); c1->Update();
  Plot(f,dir+"/Efficiencies/EtaEff","#eta","Efficiency","e"); c1->Update();
  Plot(f,dir+"/Efficiencies/PhiEff","#phi (rad)","Efficiency","e"); c1->Update();

  // non-iso EM resolutions & efficiencies
  TString dir = "L1AnalyzerNonIsoEmMC";
  
  Plot(f,dir+"/Resolutions/EtRes","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/EtCor","E_{T, Ref} (GeV)","E_{T, L1} (GeV)"); c1->Update();
  Plot(f,dir+"/Resolutions/EtaRes","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}"); c1->Update();
  Plot(f,dir+"/Resolutions/PhiRes","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}","No. of entries"); c1->Update();
  Plot(f,dir+"/Resolutions/PhiCor","#phi_{Ref} (rad)","#phi_{L1} (rad)"); c1->Update();
  Plot(f,dir+"/Efficiencies/EtEff","E_{T} (GeV)","Efficiency","e"); c1->Update();
  Plot(f,dir+"/Efficiencies/EtaEff","#eta","Efficiency","e"); c1->Update();
  Plot(f,dir+"/Efficiencies/PhiEff","#phi (rad)","Efficiency","e"); c1->Update();

  // make iso/non-iso sum histograms
  PlotCombinedEff(f,"L1AnalyzerIsoEmMC","L1AnalyzerNonIsoEmMC","", "Eta", "#eta","Efficiency","e"); c1->Update();

  f->Close();
  
  ps->Close();

}

// void validation(TString dir="", TString fileName="")
// {
//   // Open the file
//   TFile *f = new TFile(fileName);

//   // First the simple histograms
  
//   Plot(f,dir+"/L1Candidates/Et","E_{T} (GeV)","No. of entries"); c1->Update();
//   Plot(f,dir+"/L1Candidates/Eta","#eta","No. of entries"); c1->Update();
//   Plot(f,dir+"/L1Candidates/Phi","#phi (rad)","No. of entries"); c1->Update();

//   Plot(f,dir+"/RefCandidates/Et","E_{T} (GeV)","No. of entries"); c1->Update();
//   Plot(f,dir+"/RefCandidates/Eta","#eta","No. of entries"); c1->Update();
//   Plot(f,dir+"/RefCandidates/Phi","#phi (rad)","No. of entries"); c1->Update();
 
//   Plot(f,dir+"/Resolutions/DeltaR","#Delta R (L1,Ref)","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtRes","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtCor","E_{T, Ref} (GeV)","E_{T, L1} (GeV)"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtProf","E_{T, Ref} (GeV)","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}"); c1->Update();

//   Plot(f,dir+"/Resolutions/EtaRes","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}"); c1->Update();
//   Plot(f,dir+"/Resolutions/EtaProf","#eta_{Ref}","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}"); c1->Update();

//   Plot(f,dir+"/Resolutions/PhiRes","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}","No. of entries"); c1->Update();
//   Plot(f,dir+"/Resolutions/PhiCor","#phi_{Ref} (rad)","#phi_{L1} (rad)"); c1->Update();
//   Plot(f,dir+"/Resolutions/PhiProf","#phi_{Ref} (rad)","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}"); c1->Update();

//   ps->Close();

// }

void Plot(TFile* f, TString Hist, TString XAxisLabel, TString YAxisLabel="Events", TString Opt="")
{

  // Get the histograms from the files
  TH1D *H   = (TH1D*)f->Get(Hist);

  // Add the X axis label
  H->GetXaxis()->SetTitle(XAxisLabel);
  H->GetYaxis()->SetTitle(YAxisLabel);

  // plot 
  H->Draw(Opt);

}

// Sum two/three L1 histos, divide by ref, and plot
// Use for eg. total EM efficiency, rather than iso and non-iso separately
void PlotCombinedEff(TFile* f, TString DirA, TString DirB, TString DirC, TString Hist, TString XAxisLabel, TString YAxisLabel="Events", TString Opt="")
{

  // Get the histograms from the files
  TH1D * HistA = (TH1D*)f->Get(DirA+"/L1Candidates/"+Hist);
  TH1D * HistB = (TH1D*)f->Get(DirB+"/L1Candidates/"+Hist);
  TH1D * HistC;
  if (!DirC.IsNull()) HistC = (TH1D*)f->Get(DirC+"/L1Candidates/"+Hist);
  TH1D * Ref   = (TH1D*)f->Get(DirA+"/RefCandidates/"+Hist);
  
  //TH1D * H = new TH1D(*HistA);
  //H->Add(HistB);
  //  if (Ref->GetEntries() > 0) H->Divide(Ref);
  
  // Add the X axis label
  //H->GetXaxis()->SetTitle(XAxisLabel);
  //H->GetYaxis()->SetTitle(YAxisLabel);

  // plot 
  Ref->Draw(Opt);



}
