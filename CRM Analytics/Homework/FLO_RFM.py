
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 1000)

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
            df_ = pd.read_csv("Datasets/flo_data_20k.csv")
            df = df_.copy()
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                    df.head(10)
                     # b. Değişken isimleri,
                    df.columns
                     # c. Betimsel istatistik,
                    df.describe().T
                     # d. Boş değer,
                    df.isnull().sum()
                     # e. Değişken tipleri, incelemesi yapınız.
                    df.dtypes
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
            df["order_num_total"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
            df["customer_value_total"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
            date_columns = df.columns[df.columns.str.contains("date")]
            df[date_columns] = df[date_columns].apply(pd.to_datetime)
            df.info()

           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           df.groupby("order_channel").agg({'master_id' : 'count',
                                            'order_num_total': 'sum',
                                            'customer_value_total' : 'mean'})

           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
            df.groupby('master_id')['customer_value_total'].sum().sort_values(ascending=False).head(10)
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
            df.groupby('master_id')['order_num_total'].sum().sort_values(ascending=False).head(10)
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
            def data_preparation(df):
                df["order_num_total"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
                df["customer_value_total"] = df["customer_value_total_ever_online"] + df[
                    "customer_value_total_ever_offline"]
                df["first_order_date"] = pd.to_datetime(df["first_order_date"])
                df["last_order_date"] = pd.to_datetime(df["last_order_date"])
                df["last_order_date_online"] = pd.to_datetime(df["last_order_date_online"])
                df["last_order_date_offline"] = pd.to_datetime(df["last_order_date_offline"])
                customer_stats = df.groupby('order_channel').agg(customer_count=('master_id', 'count'),
                                                                 avg_order_num=('order_num_total_ever', 'mean'),
                                                                 avg_spending=('customer_value_total_ever', 'mean'))
                return df
# GÖREV 2: RFM Metriklerinin Hesaplanması
# Recency (Yenilik): Müşterinin son alışveriş tarihinden bugüne kadar geçen zaman. Bu değer genellikle gün cinsinden ifade edilir. Yani, müşterinin ne kadar süre önce alışveriş yaptığıdır.
# Frequency (Sıklık): Müşterinin belirli bir zaman dilimindeki toplam alışveriş sayısı. Bu değer genellikle müşterinin yaptığı toplam alışveriş sayısıdır.
# Monetary (Parasal Değer): Müşterinin yaptığı toplam harcama. Yani, müşterinin toplamda ne kadar para harcadığıdır.
df[["last_order_date", "last_order_date_online", "last_order_date_offline"]].max()
today_date= dt.datetime(2021, 6, 1)
rfm = df.groupby("master_id").agg({"last_order_date" : lambda last_order_date : (today_date- last_order_date.max()).days,
                                    "order_num_total_ever": lambda order_num_total_ever: order_num_total_ever.nunique(),
                                    "customer_value_total_ever": lambda customer_value_total_ever: customer_value_total_ever.sum()})
rfm.columns = ['recency', 'frequency', 'monetary']
rfm.describe().T
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması
rfm["recency_score"] = pd.qcut(rfm["recency"], q=5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], q=5, labels=[1, 2, 3, 4, 5])

rfm["RF_SCORE"] = (rfm["recency"].astype(str) + rfm["frequency"].astype(str) + rfm["monetary_score"].astype(str))

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)
# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
           rfm.groupby("segment").agg({'recency': 'mean', 'frequency': 'mean', 'monetary': 'mean'})
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
                    target_customers_a = target_customers_a[(target_customers_a['monetary'] > 250) & target_customers_a['interested_in_categories_12'].str.contains('KADIN', na=False)]
                    target_customers_a[['master_id']].to_csv('yeni_marka_hedef_müşteri_id.csv', index=False)
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.
                    target_customers_b = rfm[((rfm['segment'] == 'hibernating') | (rfm['segment'] == 'need_attention') | (rfm['segment'] == 'new_customers')) & (rfm['recency'] > 180)]
                    target_customers_b.to_csv("indirim_hedef_müşteri_ids.csv", columns=['recency', 'frequency', 'monetary'])

# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################


# 2. Veri setinde
        # a. İlk 10 gözlem,
        # b. Değişken isimleri,
        # c. Boyut,
        # d. Betimsel istatistik,
        # e. Boş değer,
        # f. Değişken tipleri, incelemesi yapınız.



# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.



# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.


# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)



# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız. 



# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.




# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.




# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.


###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi



# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe


###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi




# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi


###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme


###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.



# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.



# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.

def Flo_RFM(file_path):

    # Veriyi oku
    df = pd.read_csv(file_path)

    # Veri hazırla
    df["order_num_total_ever"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["customer_value_total_ever"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]
    df["first_order_date"] = pd.to_datetime(df["first_order_date"])
    df["last_order_date"] = pd.to_datetime(df["last_order_date"])
    df["last_order_date_online"] = pd.to_datetime(df["last_order_date_online"])
    df["last_order_date_offline"] = pd.to_datetime(df["last_order_date_offline"])

    # RFM Metriklerini hesapla
    today_date = dt.datetime(2021, 6, 1)
    rfm = df.groupby("master_id").agg(
        {"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
         "order_num_total_ever": lambda order_num_total_ever: order_num_total_ever.nunique(),
         "customer_value_total_ever": lambda customer_value_total_ever: customer_value_total_ever.sum()})
    rfm.columns = ['recency', 'frequency', 'monetary']
    rfm["recency_score"] = pd.qcut(rfm["recency"], q=5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm["monetary"], q=5, labels=[1, 2, 3, 4, 5])
    rfm["RF_SCORE"] = (rfm["recency"].astype(str) + rfm["frequency"].astype(str))

    # RF Skorlarını segmentlere dönüştür
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_Risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }
    rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)

    # Aksiyon zamanı!
    # Segmentlerin recency, frequnecy ve monetary ortalamalarını incele
    segment_stats = rfm.groupby("segment").agg({'recency': 'mean', 'frequency': 'mean', 'monetary': 'mean'})

    # Yeni marka hedef müşterileri bul ve kaydet
    target_customers_a = rfm[(rfm['segment'].isin(['champions', 'loyal_customers'])) & (rfm['monetary'] > 250)]
    target_customers_a = target_customers_a[
        target_customers_a['interested_in_categories_12'].str.contains('KADIN', na=False)]
    target_customers_a[['master_id']].to_csv('yeni_marka_hedef_müşteri_id.csv', index=False)

    # İndirim hedef müşterileri bul ve kaydet
    target_customers_b = rfm[((rfm['segment'] == 'hibernating') | (rfm['segment'] == 'need_attention') | (
                rfm['segment'] == 'new_customers')) & (rfm['recency'] > 180)]
    target_customers_b.to_csv("indirim_hedef_müşteri_ids.csv", columns=['recency', 'frequency', 'monetary'])
    return rfm