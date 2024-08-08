#data
import pickle as p
#grp1 data
mp1=['−259.16°C','180°C','98°C','63°C','39°C','28°C','21°C']
bp1=['−252.879°C','468°C','1090°C','1484°C','1377°C','1845°C','1500°C']
ec1=['1s1','[He]2s1','[Ne]3s1','[Ar]4s1','[Kr]5s1','[Xe]6s1','[Rn]7s1']
an1=['1','3','11','19','37','55','87']
bl1=['s','s','s','s','s','s','s']
st1=['gas','solid','solid','solid','solid','solid','solid']
app1=['A colourless, odourless gas. It has the lowest density of all gases','A soft, silvery metal. It has the lowest density of all metals. It reacts vigorously with water','sodium is a soft metal that tarnishes within seconds of being exposed to the air. It also reacts vigorously with water.','A soft, silvery metal that tarnishes in air within minutes.','A soft metal that ignites in the air and reacts violently with water.','Caesium is a soft, gold-coloured metal that is quickly attacked by air and reacts explosively in water.','An intensely radioactive metal.']
#grp2 data
mp2=['1287°C','650°C','842°C','777°C','727°C','696°C']
bp2=['2468°C','1090°C','1484°C','1377°C','1845°C','1500°C']
ec2=['[He] 2s2','[Ne] 3s2','[Ar] 4s2','[Kr] 5s2 ','[Xe] 6s2 ','[Rn] 7s2']
an2=['4','12','20','38','56','88']
bl2=['s','s','s','s','s','s']
st2=['solid','solid','solid','solid','solid','solid']
app2=['Beryllium is a silvery-white metal. It is relatively soft and has a low density','A silvery-white metal that ignites easily in air and burns with a bright light.','Calcium is a silvery-white, soft metal that tarnishes rapidly in air and reacts with water.','A soft, silvery metal that burns in air and reacts with water.','Barium is a soft, silvery metal that rapidly tarnishes in air and reacts with water.','A soft, shiny and silvery radioactive metal.']
#grp18 data
mp18=['Unknown ','−248.59°C','−189.34°C','−157.37°C','−111.75°C','−71°C','Unknown']
bp18=['−268.928°C','−246.046°C','−185.848°C','−153.415°C','−108.099°C','−61.7°C','Unkown']
ec18=['1s2 ','[He] 2s22p6 ','[Ne] 3s23p6','[Ar] 3d104s24p6 ','[Kr] 4d105s25p6','[Xe] 4f145d106s26p6 ','[Rn] 5f146d107s27p6']
an18=['2','10','18','36','54','86','118']
bl18=['p','s','s','s','s','s','s']
st18=['gas','gas','gas','gas','gas','gas','solid']
app18=['A colourless, odourless gas that is totally unreactive.','A colourless, odourless gas. Neon will not react with any other substance.','Argon is a colourless, odourless gas that is totally inert to other substances.','Krypton is a gas with no colour or smell. It does not react with anything except fluorine gas.','A colourless, odourless gas. It is very unreactive.','Radon is a colourless and odourless gas. It is chemically inert, but radioactive.','A highly radioactive metal, of which only a few atoms have ever been made.']
#lanthanoide data
mpla=['799°C','931°C','1016°C','1042°C','1072°C','822°C','1313°C','1359°C','1412°C','1472°C','1529°C','1545°C','824°C','1663°C']
bpla=['3443°C','3520°C','3074°C','3000°C','1794°C','1529°C','3273°C','3230°C','2567°C','2700°C','2868°C','1950°C','1196°C','3402°C']
ecla=['[Xe] 4f15d16s2 ','[Xe] 4f36s2 ','[Xe] 4f46s2 ','[Xe] 4f56s2 ','[Xe] 4f66s2 ','[Xe] 4f76s2','[Xe] 4f75d16s2 ','[Xe] 4f96s2 ','[Xe] 4f106s2 ','[Xe] 4f116s2 ','[Xe] 4f126s2 ','[Xe] 4f136s2 ','[Xe] 4f146s2 ','[Xe] 4f145d16s2']
anla=['58','59','60','61','62','63','64','65','66','67','68','69','70','71']
blla=['f','f','f','f','f','f','f','f','f','f','f','f','f','f']
stla=['solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid']
appla=['Cerium is a grey metal. It is little used because it tarnishes easily, reacts with water and burns when heated.','A soft, silvery metal.','A silvery-white metal. It rapidly tarnishes in air.','A radioactive metal.','A silvery-white metal.','A soft, silvery metal that tarnishes quickly and reacts with water.','A soft, silvery metal that reacts with oxygen and water.','A soft, silvery metal.','A bright, silvery metallic element.','A bright, silvery metal.','A soft, silvery metallic element.','A bright, silvery metal.','A soft, silvery metal. It slowly oxidises in air, forming a protective surface layer.','A silvery-white, hard, dense metal.']
#actinoide data
mpac=['1750°C','1572°C','1135°C','644°C','640°C','1176°C','1345°C','986°C','900°C','860°C','1527°C','827°C','827°C','1627°C']
bpac=['4785°C','4000°C','4131°C','3902°C','3228°C','2011°C','Unknown ','Unknown ','Unknown ','Unknown ','Unknown ','Unknown ','Unknown ','Unknown ']
ecac=['[Rn] 6d27s2 ','[Rn] 5f26d17s2 ','[Rn] 5f36d17s2 ','[Rn] 5f46d17s2 ','[Rn] 5f67s2 ','[Rn] 5f77s2 ','[Rn] 5f76d17s2 ','[Rn] 5f97s2 ','[Rn] 5f107s2 ','[Rn] 5f117s2 ','[Rn] 5f127s2 ','[Rn] 5f137s2 ','[Rn] 5f147s2 ','[Rn] 5f147s27p1']
anac=['90','91','92','93','94','95','96','97','98','99','100','101','102','103']
blac=['f','f','f','f','f','f','f','f','f','f','f','f','f','f']
stac=['solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid','solid']
appac=['A weakly radioactive, silvery metal.','A silvery, radioactive metal.','A radioactive, silvery metal.','A radioactive metal.','A radioactive, silvery metal.','Americium is a silvery, shiny radioactive metal.','A radioactive metal that is silver in colour. It tarnishes rapidly in air.','Berkelium is a radioactive, silvery metal.','Californium is a radioactive metal.','A radioactive metal, only a few milligrams of which are made each year.','A radioactive metal obtained only in microgram quantities.','A radioactive metal, of which only a few atoms have ever been created.','Nobelium is a radioactive metal. Only a few atoms have ever been made. Its half-life is only 58 minutes.','A radioactive metal of which only a few atoms have ever been created.']
#grp13 data
mp13=['2077°C','660.323°C','29.76°C','156.6°C','304°C','unknown']
bp13=['4000°C','2519°C','2229°C','2027°C','1473°C','unknown']
ec13=['[He] 2s22p1','[Ne] 3s23p1','[Ar] 3d104s24p1','[Kr] 4d105s25p1','[Xe] 4f145d106s26p1','[Rn] 5f146d107s27p1']
an13=['5','13','31','49','81','113']
bl13=['p','p','p','p','p','p']
st13=['solid','solid','solid','solid','solid','solid']
app13=['Pure boron is a dark amorphous powder.','Aluminium is a silvery-white, lightweight metal. It is soft and malleable.','Gallium is a soft, silvery-white metal, similar to aluminium.','A soft, silvery metal that is stable in air and water.','A soft, silvery-white metal that tarnishes easily','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp14 data
mp14=['3825°C','1414°C','938.25°C','231.92°C','327.46°C','unknown']
bp14=['3825°C','3265°C','2833°C','2586°C','1749°C','unknown']
ec14=['[He] 2s22p2','[Ne] 3s23p2','[Ar] 3d104s24p2','[Kr] 4d105s25p2','[Xe] 4f145d106s26p2','[Rn] 5f146d107s27p2']
an14=['6','14','32','50','82','114']
bl14=['p','p','p','p','p','p']
st14=['solid','solid','solid','solid','solid','solid']
app14=['There are a number of pure forms of this element including graphite, diamond, fullerenes and graphene.','The element, when ultrapure, is a solid with a blue-grey metallic sheen.','A silvery-white semi-metal. It is brittle.','A soft, pliable metal. Below 13°C it slowly changes to a powder form.','A dull, silvery-grey metal. It is soft and easily worked into sheets.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp15 data
mp15=['-210°C','44.15°C','616°C','630.62°C','271.4°C','unknown']
bp15=['-195.79°C','280.5°C','616°C','1587°C','1564°C','unknown']
ec15=['[He] 2s22p3','[Ne] 3s23p3','[Ar] 3d104s24p3','[Kr] 4d105s25p3','[Xe] 4f145d106s26p3','[Rn] 5f146d107s27p3']
an15=['7','15','33','51','83','115']
bl15=['p','p','p','p','p','p']
st15=['gas','solid','solid','solid','solid','solid']
app15=['A colourless, odourless gas.','White phosphorus is a poisonous waxy solid and contact with skin can cause severe burns.','Arsenic is a semi-metal. In its metallic form it is bright, silver-grey and brittle.','Antimony is a semi-metal. In its metallic form it is silvery, hard and brittle.','Bismuth is a high-density, silvery, pink-tinged metal.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp16 data
mp16=['-218.79°C','115.21°C','220.8°C','449.51°C','254°C','unknown']
bp16=['-182.96°C','444.61°C','685°C','988°C','962°C','unknown']
ec16=['[He] 2s22p4','[Ne] 3s23p4','[Ar] 3d104s24p4','[Kr] 4d105s25p4','[Xe] 4f145d106s26p4','[Rn] 5f146d107s27p4']
an16=['8','16','34','52','84','116']
bl16=['p','p','p','p','p','p']
st16=['gas','solid','solid','solid','solid','solid']
app16=['A colourless, odourless gas.','There are several allotropes of sulfur. The most common appears as yellow crystals or powder.','A semi-metal that can exist in two forms: as a silvery metal or as a red powder.','A semi-metal usually obtained as a grey powder.','A silvery-grey, radioactive semi-metal','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp17 data
mp17=['-219.67°C','-101.5°C','-7.2°C','113.7°C','300°C','unknown']
bp17=['-188.11°C','-34.04°C','58.8°C','184.4°C','350°C','unknown']
ec17=['[He] 2s22p5','[Ne] 3s23p5','[Ar] 3d104s24p5','[Kr] 4d105s25p5','[Xe] 4f145d106s26p5','[Rn] 5f146d107s27p5']
an17=['9','17','35','53','85','117']
bl17=['p','p','p','p','p','p']
st17=['gas','gas','liquid','solid','solid','solid']
app17=['A very pale yellow-green, dangerously reactive gas.','A yellowy-green dense gas with a choking smell.','Bromine is a deep-red, oily liquid with a sharp smell. It is toxic.','A black, shiny, crystalline solid. When heated, iodine sublimes to form a purple vapour.','Astatine is a dangerously radioactive element.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp3 data
mp3=['1541°C','1522°C','920°C','1050°C']
bp3=['2836°C','3345°C','3464°C','3200°C']
ec3=['[Ar] 3d14s2','[Kr] 4d15s2','[Xe] 5d16s2','[Rn] 6d17s2']
an3=['21','39','57','89']
bl3=['d','d','d','d']
st3=['solid','solid','solid','solid']
app3=['A silvery metal that tarnishes in air, burns easily and reacts with water.',',A soft, silvery metal.',',A soft, silvery-white metal. It rapidly tarnishes in air and burns easily when ignited.',',Actinium is a soft, silvery-white radioactive metal. It glows blue in the dark because its intense radioactivity excites the air around it.']
#grp4 data
mp4=['1670°C','1854°C','2233°C','unknown']
bp4=['3287°C','4406°C','4600°C','unknown']
ec4=['[Ar] 3d24s2','[Kr] 4d25s2','[Xe] 4f145d26s2','[Rn] 5f146d27s2']
an4=['22','40','72','104']
bl4=['d','d','d','d']
st4=['solid','solid','solid','solid']
app4=['A hard, shiny and strong metal.','A hard, silvery metal that is very resistant to corrosion.','A shiny, silvery metal that resists corrosion and can be drawn into wires.','A radioactive metal that does not occur naturally. Relatively few atoms have ever been made.']
#grp5 data
mp5=['1910°C','2477°C','3017°C','unknown']
bp5=['3407°C','4741°C','5455°C','unknown']
ec5=['[Ar] 3d34s2','[Kr] 4d45s1','[Xe] 4f145d36s2 ','[Rn] 5f146d37s2 ']
an5=['23','41','73','105']
bl5=['d','d','d','d']
st5=['solid','solid','solid','solid']
app5=['A silvery metal that resists corrosion.','A silvery metal that is very resistant to corrosion due to a layer of oxide on its surface.','A shiny, silvery metal that is very resistant to corrosion.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp6 data
mp6=['1907°C','2622°C','3414°C','unknown']
bp6=['2671°C','4639°C','5555°C','unknown']
ec6=['[Ar] 3d54s1','[Kr] 4d55s1','[Xe] 4f145d46s2','[Rn] 5f146d47s2']
an6=['24','42','74','106']
bl6=['d','d','d','d']
st6=['solid','solid','solid','solid']
app6=['A hard, silvery metal with a blue tinge.','A shiny, silvery metal.','A shiny, silvery-white metal.','A radioactive metal that does not occur naturally. Only a few atoms have ever been made.']
#grp7 data
mp7=['1246°C','2157°C','3185°C','unknown']
bp7=['2061°C','4262°C','5590°C','unknown']
ec7=['[Ar] 3d54s2','[Kr] 4d55s2','[Xe] 4f145d56s2','[Rn] 5f146d57s2']
an7=['25','43','75','107']
bl7=['d','d','d','d']
st7=['solid','solid','solid','solid']
app7=['A hard, brittle, silvery metal.','A radioactive, silvery metal that does not occur naturally.','A metal with a very high melting point.  Tungsten is the only metallic element with a higher melting point.','Bohrium is a highly radioactive metal.']
#grp8 data
mp8=['1538°C','2333°C','3033°C','unknown']
bp8=['2861°C','4147°C','5008°C','unknown']
ec8=['[Ar] 3d64s2','[Kr] 4d75s1','[Xe] 4f145d66s2','[Rn] 5f146d67s2']
an8=['26','44','76','108']
bl8=['d','d','d','d']
st8=['solid','solid','solid','solid']
app8=['A shiny, greyish metal that rusts in damp air.','A shiny, silvery metal.','A shiny, silver metal that resists corrosion. It is the densest of all the elements and is twice as dense as lead.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp9 data
mp9=['1495°C','1963°C','2446°C','unknown']
bp9=['2927°C','3695°C','4428°C','unknown']
ec9=['[Ar] 3d74s2','[Kr] 4d85s1','[Xe] 4f145d76s2','[Rn] 5f146d77s2']
an9=['27','45','77','109']
bl9=['d','d','d','d']
st9=['solid','solid','solid','solid']
app9=['A lustrous, silvery-blue metal. It is magnetic.','A hard, shiny, silvery metal.','Iridium is a hard, silvery metal. It is almost as unreactive as gold. It has a very high density and melting point.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp10 data
mp10=['1455°C','1554.8°C','1768.2°C','unknown']
bp10=['2913°C','2963°C','3825°C','unknown']
ec10=['[Ar] 3d84s2','[Kr] 4d10','[Xe] 4f145d96s1','[Rn] 5f146d97s1']
an10=['28','46','78','110']
bl10=['d','d','d','d']
st10=['solid','solid','solid','solid']
app10=['A silvery metal that resists corrosion even at high temperatures.','A shiny, silvery-white metal that resists corrosion.','A shiny, silvery-white metal as resistant to corrosion as gold.','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp11 data
mp11=['1084.62°C','961.78°C','1064.18°C','unknown']
bp11=['2560°C','2162°C','2836°C','unknown']
ec11=['Ar] 3d104s1','[Kr] 4d105s1','[Xe] 4f145d106s1','[Rn] 5f146d107s1']
an11=['29','47','79','111']
bl11=['d','d','d','d']
st11=['solid','solid','solid','solid']
app11=['A reddish-gold metal that is easily worked and drawn into wires.','Silver is a relatively soft, shiny metal. It tarnishes slowly in air as sulfur compounds react with the surface forming black silver sulfide.','A soft metal with a characteristic yellow colour. It is chemically unreactive, although it will dissolve in aqua regia (a mixture of nitric and hydrochloric acids).','A highly radioactive metal, of which only a few atoms have ever been made.']
#grp12 data
mp12=['419.52°C','321.06°C','-38.82°C','unknown']
bp12=['907°C','767°C','356.61°C','unknown']
ec12=['[Ar] 3d104s2','[Kr] 4d105s2','[Xe] 4f145d106s2','[Rn] 5f146d107s2']
an12=['30','48','80','112']
bl12=['d','d','d','d']
st12=['solid','solid','liquid','solid']
app12=['A silvery-white metal with a blue tinge. It tarnishes in air.','Cadmium is a silvery metal with a bluish tinge to its surface.','A liquid, silvery metal.','A highly radioactive metal, of which only a few atoms have ever been made. It is thought to be unreactive and more like a noble gas than a metal.']


#writing grp1 data onto file
f=open('grp1.dat','wb')
l=[]
for i in range(7):
    l.append(['melting point:'+mp1[i],'boiling point:'+bp1[i],'electronic configuration:'+ec1[i],'atomic number:'+an1[i],'block:'+bl1[i],'state:'+st1[i],'appearance:'+app1[i]])
p.dump(l,f)    
f.close()
#writing grp2 data onto file
l1=[]
f1=open('grp2.dat','wb')
for j in range(6):
    l1.append(['melting point:'+mp2[j],'boiling point:'+bp2[j],'electronic configuration:'+ec2[j],'atomic number:'+an2[j],'block:'+bl2[j],'state:'+st2[j],'appearance:'+app2[j]])
p.dump(l1,f1)
f1.close()
#writing grp18 data onto file
l2=[]
f2=open('grp18.dat','wb')
for j in range(7):
    l2.append(['melting point:'+mp18[j],'boiling point:'+bp18[j],'electronic configuration:'+ec18[j],'atomic number:'+an18[j],'block:'+bl18[j],'state:'+st18[j],'appearance:'+app18[j]])
p.dump(l2,f2)
f2.close()
#writing lantanoides data onto file
l2=[]
f2=open('grpla.dat','wb')
for j in range(14):
    l2.append(['melting point:'+mpla[j],'boiling point:'+bpla[j],'electronic configuration:'+ecla[j],'atomic number:'+anla[j],'block:'+blla[j],'state:'+stla[j],'appearance:'+appla[j]])
p.dump(l2,f2)
f2.close() 
l2=[]
#writing actinoides data onto file
f2=open('grpac.dat','wb+')
for j in range(14):
    l2.append(['melting point:'+mpac[j],'boiling point:'+bpac[j],'electronic configuration:'+ecac[j],'atomic number:'+anac[j],'block:'+blac[j],'state:'+stac[j],'appearance:'+appac[j]])
p.dump(l2,f2)
f2.close() 
#writing p block data onto file
#writing grp13 data onto file
f=open('grp13.dat','wb')
l2=[]
for i in range(6):
        l2.append(['melting point:'+mp13[i],'boiling point:'+bp13[i],'electronic configuration:'+ec13[i],'atomic number:'+an13[i],'block:'+bl13[i],'state:'+st13[i],'appearance:'+app13[i]])
p.dump(l2,f)
f.close()
#writing grp14 data onto file
f=open('grp14.dat','wb')
l2=[]
for i in range(6):
        l2.append(['melting point:'+mp14[i],'boiling point:'+bp14[i],'electronic configuration:'+ec14[i],'atomic number:'+an14[i],'block:'+bl14[i],'state:'+st14[i],'appearance:'+app14[i]])
p.dump(l2,f)
f.close()

#writing grp 15 data onto file
f=open('grp15.dat','wb')
l2=[]
for i in range(6):
        l2.append(['melting point:'+mp15[i],'boiling point:'+bp15[i],'electronic configuration:'+ec15[i],'atomic number:'+an15[i],'block:'+bl15[i],'state:'+st15[i],'appearance:'+app15[i]])
p.dump(l2,f)
f.close()

#writing grp16 data onto file
f=open('grp16.dat','wb')
l2=[]
for i in range(6):
        l2.append(['melting point:'+mp16[i],'boiling point:'+bp16[i],'electronic configuration:'+ec16[i],'atomic number:'+an16[i],'block:'+bl16[i],'state:'+st16[i],'appearance:'+app16[i]])
p.dump(l2,f)
f.close()

#writing grp17 data onto file
l2=[]
f2=open('grp17.dat','wb')
for j in range(6):
    l2.append(['melting point:'+mp17[j],'boiling point:'+bp17[j],'electronic configuration:'+ec17[j],'atomic number:'+an17[j],'block:'+bl17[j],'state:'+st17[j],'appearance:'+app17[j]])
p.dump(l2,f2)
f2.close()

#writing grp3 data onto file
l2=[]
f2=open('grp3.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp3[j],'boiling point:'+bp3[j],'electronic configuration:'+ec3[j],'atomic number:'+an3[j],'block:'+bl3[j],'state:'+st3[j],'appearance:'+app3[j]])
p.dump(l2,f2)
f2.close()
#writing grp4 data onto file        
l2=[]
f2=open('grp4.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp4[j],'boiling point:'+bp4[j],'electronic configuration:'+ec4[j],'atomic number:'+an4[j],'block:'+bl4[j],'state:'+st4[j],'appearance:'+app4[j]])
p.dump(l2,f2)
f2.close()    

#writing grp5 data onto file        
l2=[]
f2=open('grp5.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp5[j],'boiling point:'+bp5[j],'electronic configuration:'+ec5[j],'atomic number:'+an5[j],'block:'+bl5[j],'state:'+st5[j],'appearance:'+app5[j]])
p.dump(l2,f2)
f2.close()  

#writing grp6 data onto file        
l2=[]
f2=open('grp6.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp6[j],'boiling point:'+bp6[j],'electronic configuration:'+ec6[j],'atomic number:'+an6[j],'block:'+bl6[j],'state:'+st6[j],'appearance:'+app6[j]])
p.dump(l2,f2)
f2.close()    

#writing grp7 data onto file        
l2=[]
f2=open('grp7.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp7[j],'boiling point:'+bp7[j],'electronic configuration:'+ec7[j],'atomic number:'+an7[j],'block:'+bl7[j],'state:'+st7[j],'appearance:'+app7[j]])
p.dump(l2,f2)
f2.close()  

#writing grp8 data onto file        
l2=[]
f2=open('grp8.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp8[j],'boiling point:'+bp8[j],'electronic configuration:'+ec8[j],'atomic number:'+an8[j],'block:'+bl8[j],'state:'+st8[j],'appearance:'+app8[j]])
p.dump(l2,f2)
f2.close()    

#writing grp9 data onto file        
l2=[]
f2=open('grp9.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp9[j],'boiling point:'+bp9[j],'electronic configuration:'+ec9[j],'atomic number:'+an9[j],'block:'+bl9[j],'state:'+st9[j],'appearance:'+app9[j]])
p.dump(l2,f2)
f2.close()    

#writing grp10 data onto file        
l2=[]
f2=open('grp10.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp10[j],'boiling point:'+bp10[j],'electronic configuration:'+ec10[j],'atomic number:'+an10[j],'block:'+bl10[j],'state:'+st10[j],'appearance:'+app10[j]])
p.dump(l2,f2)
f2.close()    

#writing grp11 data onto file        
l2=[]
f2=open('grp11.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp11[j],'boiling point:'+bp11[j],'electronic configuration:'+ec11[j],'atomic number:'+an11[j],'block:'+bl11[j],'state:'+st11[j],'appearance:'+app11[j]])
p.dump(l2,f2)
f2.close()    

#writing grp12 data onto file        
l2=[]
f2=open('grp12.dat','wb')
for j in range(4):
    l2.append(['melting point:'+mp12[j],'boiling point:'+bp12[j],'electronic configuration:'+ec12[j],'atomic number:'+an12[j],'block:'+bl12[j],'state:'+st12[j],'appearance:'+app12[j]])
p.dump(l2,f2)
f2.close()
