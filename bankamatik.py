# bankamatik uygulaması 

RahmetullahHesap = {
    'ad' : 'Rahmetullah Gönül',
    'hesapNo' : '123456',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

AhmetHesap = {
    'ad' : 'Ahmet Gönül',
    'hesapNo' : '654321',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanımı = input('ek hesap kullanmak istiyo musunuz? (e/h)')

            if ekHesapKullanımı == 'e':
                ekHesapKullanılacakMiktar = hesap['bakiye']
                hesap['bakiye']= 0
                hesap['ekHesap'] -= ekHesapKullanılacakMiktar
                print('çekmek istediğiniz para ek hesap kullanılarak verilmiştir')
                bakiyeSorgula(hesap)
            else:
                print('para çekme işleminiz gerçekleştirilemedi')            
        else:
            print('üzgünüz bakiye yetersiz')


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL para bulunmaktadır ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır ")

paraCek(RahmetullahHesap, 3000)

print('**************')

paraCek(RahmetullahHesap, 2000)