import Airmineral

if __name__=="__main__":

    listurutan=[1,2,3,4,5]
    listhargabeli=[1500,2000,2000,2500,3000]
    listbanyakbeli=[15,20,25,30,27]
    listhargajual=[2000,2500,2500,3000,3500]
    listterjual=[15,20,25,30,27]
    
    listAirmineral=[]

for i in range(5):
    listAirmineral.append(Airmineral.Airmineral(listurutan[i], listhargabeli[i], listbanyakbeli[i], listhargajual[i], listterjual[i]))
    
for Airmineral in listAirmineral:
    Airmineral.tampilkan_macam()
    Airmineral.biaya_beli()
    Airmineral.perkiraan_untung()
    Airmineral.untung_asli()
