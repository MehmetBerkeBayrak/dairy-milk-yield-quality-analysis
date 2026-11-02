"""Rebuild descriptive milk analysis from the attributed source workbook.
No database/network connection is required. No hypothesis tests are performed.
"""
from pathlib import Path
import json, hashlib, html, platform
import pandas as pd
import numpy as np
import openpyxl
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw/DMI_milk_yield_and_composition.xlsx'
OUT=ROOT/'data/processed';OUT.mkdir(parents=True,exist_ok=True)
HEADERS=['Animal ID','Genetic Group','THI Range','Replication No','DMI (kg)','Milk Yield (L/day/cow)','SCC cells per mL','Fat%','SNF%','Protein %','Salt%','Lactose%','pH']
COLS=['hayvan_id','genetik_grup','thi_grubu','tekrar_no','kuru_madde_kg','sut_litre_gun','somatik_hucre_ml','yag_yuzde','yagsiz_kuru_madde_yuzde','protein_yuzde','tuz_yuzde','laktoz_yuzde','ph']
df=pd.read_excel(RAW,dtype={'Animal ID':str})
assert list(df.columns)==HEADERS,'Unexpected workbook schema'
df.columns=COLS
for c in COLS[:3]:df[c]=df[c].astype(str).str.strip()
for c in COLS[3:]:df[c]=pd.to_numeric(df[c].astype(str).str.strip().str.replace(',','.',regex=False),errors='raise')
key=['hayvan_id','genetik_grup','thi_grubu','tekrar_no']
assert len(df)==750 and df['hayvan_id'].nunique()==50
assert set(df.genetik_grup)=={'Local','HF50','HF62.5','HF75','HF87.5'}
assert set(df.thi_grubu)=={'T0','T1','T2'}
assert not df.duplicated(key).any()
assert not df[COLS].isna().any().any()
assert (df[['sut_litre_gun','somatik_hucre_ml']]>=0).all().all()
counts=df.groupby(COLS[:3]).size()
assert len(counts)==150 and counts.eq(5).all()
assert df.groupby('hayvan_id').genetik_grup.nunique().eq(1).all()
assert df.groupby('hayvan_id').thi_grubu.nunique().eq(3).all()
assert df.groupby(COLS[:3]).tekrar_no.apply(lambda s:set(s)=={1,2,3,4,5}).all()
def csv(frame,name):frame.to_csv(OUT/name,index=False,encoding='utf-8',float_format='%.12g')
csv(df,'sut_verisi.csv')
df['yag_gostergesi']=df.sut_litre_gun*df.yag_yuzde/100
df['protein_gostergesi']=df.sut_litre_gun*df.protein_yuzde/100
metrics=['sut_litre_gun','yag_yuzde','protein_yuzde','somatik_hucre_ml','yag_gostergesi','protein_gostergesi']
a=df.groupby(COLS[:3],as_index=False)[metrics].mean()
a['olcum_sayisi']=5
csv(a,'hayvan_ortalamalari.csv')
g=a.groupby(['genetik_grup','thi_grubu'],as_index=False)[metrics].mean();g['hayvan_sayisi']=a.groupby(['genetik_grup','thi_grubu']).size().to_numpy()
assert g.hayvan_sayisi.eq(10).all();csv(g,'grup_ozeti.csv')
t0=a[a.thi_grubu.eq('T0')].drop(columns=['thi_grubu','olcum_sayisi'])
t2=a[a.thi_grubu.eq('T2')].drop(columns=['thi_grubu','olcum_sayisi'])
p=t0.merge(t2,on=['hayvan_id','genetik_grup'],suffixes=('_t0','_t2'),validate='one_to_one')
p=p.rename(columns={'sut_litre_gun_t0':'sut_t0','sut_litre_gun_t2':'sut_t2','somatik_hucre_ml_t0':'hucre_t0','somatik_hucre_ml_t2':'hucre_t2'})
p['sut_kaybi_yuzde']=100*(p.sut_t0-p.sut_t2)/p.sut_t0
p['hucre_artisi_yuzde']=100*(p.hucre_t2-p.hucre_t0)/p.hucre_t0
p=p.sort_values(['genetik_grup','hayvan_id'])
paired=p[['hayvan_id','genetik_grup','sut_t0','sut_t2','hucre_t0','hucre_t2','sut_kaybi_yuzde','hucre_artisi_yuzde']]
assert len(paired)==50;assert (paired.sut_kaybi_yuzde>0).all() and (paired.hucre_artisi_yuzde>0).all()
csv(paired,'hayvan_degisimleri.csv')
st=[];corr=[]
for group,d in paired.groupby('genetik_grup'):
 r=d.sut_kaybi_yuzde.corr(d.hucre_artisi_yuzde)
 corr.append({'genetik_grup':group,'hayvan_sayisi':len(d),'pearson_korelasyon':r})
 row={'genetik_grup':group,'hayvan_sayisi':len(d),'sutu_azalan':int((d.sut_kaybi_yuzde>0).sum()),'hucresi_artan':int((d.hucre_artisi_yuzde>0).sum())}
 for c in ['sut_kaybi_yuzde','hucre_artisi_yuzde']:
  for name,fn in [('ortalama','mean'),('std','std'),('min','min'),('max','max')]:row[c+'_'+name]=getattr(d[c],fn)()
 st.append(row)
summary=pd.DataFrame(st);correlations=pd.DataFrame(corr)
csv(summary,'bireysel_degisim_ozeti.csv');csv(correlations,'korelasyon.csv')
change=[];composition=[]
for group,d in g.groupby('genetik_grup'):
 d=d.set_index('thi_grubu');row={'genetik_grup':group}
 for c in ['sut_litre_gun','yag_yuzde','protein_yuzde','somatik_hucre_ml']:
  row[c+'_t0']=d.loc['T0',c];row[c+'_t2']=d.loc['T2',c]
  row[c+'_degisim_yuzde']=100*(d.loc['T2',c]-d.loc['T0',c])/d.loc['T0',c]
 change.append(row);row={'genetik_grup':group}
 for c in ['yag_gostergesi','protein_gostergesi']:
  for t in ['T0','T1','T2']:row[c+'_'+t.lower()]=d.loc[t,c]
  row[c+'_t0_t1_degisim_yuzde']=100*(d.loc['T1',c]-d.loc['T0',c])/d.loc['T0',c]
  row[c+'_t0_t2_degisim_yuzde']=100*(d.loc['T2',c]-d.loc['T0',c])/d.loc['T0',c]
 composition.append(row)
changes=pd.DataFrame(change);comp=pd.DataFrame(composition)
csv(changes,'grup_degisimleri.csv');csv(comp,'bilesim_gostergeleri.csv')
csv(df.loc[df.hayvan_id.eq('104') & df.thi_grubu.isin(['T0','T2']),COLS],'hayvan_104_kontrol.csv')
# Reconcile against rounded user-supplied PostgreSQL results, not a new DB execution.
expected={'HF50':(19.51,52.02,.528,-22.23,-25.68),'HF62.5':(15.73,41.26,.492,-18.18,-21.33),'HF75':(15.01,43.65,-.003,-18.08,-21.95),'HF87.5':(8.54,33.72,.149,-10.98,-15.34),'Local':(45.78,57.81,.177,-49.25,-51.48)}
for group,e in expected.items():
 s=summary.set_index('genetik_grup').loc[group];c=correlations.set_index('genetik_grup').loc[group];b=comp.set_index('genetik_grup').loc[group]
 actual=[s.sut_kaybi_yuzde_ortalama,s.hucre_artisi_yuzde_ortalama,c.pearson_korelasyon,b.protein_gostergesi_t0_t2_degisim_yuzde,b.yag_gostergesi_t0_t2_degisim_yuzde]
 assert all(abs(x-y)<tol for x,y,tol in zip(actual,e,[.006,.006,.0006,.006,.006])),(group,actual,e)
# Static SVG figures are generated from reviewed computed data, not Power BI screenshots.
colors=['#00897B','#3974CB','#D38B25','#8B5CB8','#C7557A'];groups=sorted(expected)
def esc(s):return html.escape(str(s))
def text(x,y,s,size=15,color='#172B4D',weight='normal'):
 return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{esc(s)}</text>'
def make_svg(language):
 tr=language=='TR';W,H=1200,740
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<rect width="1200" height="740" fill="#F3F5F9"/>']
 svg+=[text(38,48,'T0–T2: Süt kaybı ve somatik hücre artışı' if tr else 'T0–T2: Milk loss and somatic cell increase',26,weight='bold'),text(38,78,'Hayvan bazındaki yüzde değişimlerin grup ortalaması | Her grupta 10 hayvan' if tr else 'Group means of individual percentage changes | 10 animals per group',15,'#64748B')]
 for panel,(field,title) in enumerate([('sut_kaybi_yuzde_ortalama','Süt kaybı (%)' if tr else 'Milk loss (%)'),('hucre_artisi_yuzde_ortalama','Hücre artışı (%)' if tr else 'SCC increase (%)')]):
  ox=38+panel*580;svg+=[f'<rect x="{ox}" y="110" width="550" height="480" rx="12" fill="white"/>',text(ox+20,146,title,19,weight='bold')]
  scale=350/70
  for tick in range(0,71,10):
   x=ox+115+tick*scale;svg.append(f'<line x1="{x}" y1="170" x2="{x}" y2="548" stroke="#E5E7EB"/>');svg.append(text(x-6,570,tick,12,'#64748B'))
  for i,group in enumerate(groups):
   val=float(summary.set_index('genetik_grup').loc[group,field]);y=190+i*70
   svg+=[text(ox+18,y+24,group,15),f'<rect x="{ox+115}" y="{y}" width="{val*scale}" height="36" rx="3" fill="{colors[i]}"/>',text(ox+124+val*scale,y+24,f'{val:.2f}',13)]
 svg+=[text(38,632,'Kaynak: Mendeley Data, DOI 10.17632/954f6g36sb.2 | Analiz: Mehmet Berke Bayrak' if tr else 'Source: Mendeley Data, DOI 10.17632/954f6g36sb.2 | Analysis: Mehmet Berke Bayrak',13,'#64748B'),text(38,663,'Betimsel sonuçlar; nedensellik veya klinik tanı göstermez.' if tr else 'Descriptive findings; not evidence of causality or a clinical diagnosis.',14,'#64748B'),text(38,692,'Veri: 50 eşleştirilmiş hayvan, T0 ve T2 için beşer ölçümün ortalaması.' if tr else 'Data: 50 paired animals; five observations averaged within each T0/T2 condition.',13,'#64748B'),'</svg>']
 (ROOT/f'images/group_changes_{language.lower()}.svg').write_text('\n'.join(svg),encoding='utf-8')
def scatter_svg(language):
 tr=language=='TR';svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="870" viewBox="0 0 1200 870">','<rect width="1200" height="870" fill="#F3F5F9"/>',text(30,40,'Hücre artışı ile süt kaybı: hayvan bazında' if tr else 'SCC increase and milk loss: individual cows',25,weight='bold')]
 for i,group in enumerate(groups):
  ox=30+(i%3)*390;oy=75+(i//3)*350
  svg.append(f'<rect x="{ox}" y="{oy}" width="370" height="330" rx="10" fill="white"/>')
  r=correlations.set_index('genetik_grup').loc[group,'pearson_korelasyon'];svg.append(text(ox+15,oy+28,f'{group} | n=10 | r={r:.3f}',17,weight='bold'))
  for tick in [0,20,40,60,80]:
   x=ox+45+tick/80*295;svg+=[f'<line x1="{x}" y1="{oy+50}" x2="{x}" y2="{oy+270}" stroke="#E5E7EB"/>',text(x-7,oy+289,tick,11,'#64748B')]
  for tick in [0,20,40,60]:
   y=oy+270-tick/70*220;svg+=[f'<line x1="{ox+45}" y1="{y}" x2="{ox+340}" y2="{y}" stroke="#E5E7EB"/>',text(ox+15,y+4,tick,11,'#64748B')]
  for row in paired[paired.genetik_grup.eq(group)].itertuples():
   x=ox+45+row.hucre_artisi_yuzde/80*295;y=oy+270-row.sut_kaybi_yuzde/70*220
   svg.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="5" fill="{colors[i]}" fill-opacity=".85"><title>ID {row.hayvan_id}: SCC +{row.hucre_artisi_yuzde:.2f}%, milk loss {row.sut_kaybi_yuzde:.2f}%</title></circle>')
  svg.append(text(ox+60,oy+314,'Hücre artışı (%)' if tr else 'SCC increase (%)',12,'#64748B'))
 svg+=[text(30,805,'Y ekseni: süt kaybı (%) | Her nokta bir hayvan | Eksenler tüm panellerde aynı' if tr else 'Y axis: milk loss (%) | One point per cow | Identical scales across panels',14,'#64748B'),text(30,836,'Mendeley Data 10.17632/954f6g36sb.2 | Korelasyon nedensellik göstermez.' if tr else 'Mendeley Data 10.17632/954f6g36sb.2 | Correlation does not establish causality.',13,'#64748B'),'</svg>']
 (ROOT/f'images/individual_scatter_{language.lower()}.svg').write_text('\n'.join(svg),encoding='utf-8')
for lang in ['TR','EN']:make_svg(lang);scatter_svg(lang)
validation={'raw_workbook_sha256':hashlib.sha256(RAW.read_bytes()).hexdigest(),'rows':len(df),'animals':50,'animal_condition_rows':len(a),'group_condition_rows':len(g),'paired_animals':len(paired),'repeat_count_per_animal_condition':5,'duplicate_measurement_keys':0,'missing_cells':0,'all_animals_milk_loss':True,'all_animals_scc_increase':True,'reconciled_with_user_sql_outputs':True,'sql_executed_in_this_environment':False,'powerbi_desktop_render_tested':False,'data_source':'https://doi.org/10.17632/954f6g36sb.2','python':platform.python_version(),'pandas':pd.__version__,'openpyxl':openpyxl.__version__,'numpy':np.__version__}
(ROOT/'reports/validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'requirements-validated.txt').write_text(f'pandas=={pd.__version__}\nopenpyxl=={openpyxl.__version__}\nnumpy=={np.__version__}\n',encoding='utf-8')
print(json.dumps(validation,ensure_ascii=True,indent=2))
