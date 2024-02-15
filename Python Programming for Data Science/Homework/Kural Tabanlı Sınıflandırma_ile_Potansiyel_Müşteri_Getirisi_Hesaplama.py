# Görev 1: Aşağıdaki Soruları Yanıtlayınız
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

    # Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
    df = pd.read_csv("Datasets/persona.csv")
    df.head()
    # Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
    df["SOURCE"].nunique()
    df["SOURCE"].value_counts()
    # Soru 3: Kaç unique PRICE vardır?
    df["PRICE"].nunique()
    # Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
    df["PRICE"].value_counts()
    # Soru 5: Hangi ülkeden kaçar tane satış olmuş?
    df["COUNTRY"].value_counts()
    # Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
    df.groupby('COUNTRY')['PRICE'].sum()
    # Soru 7: SOURCE türlerine göre satış sayıları nedir?
    df["SOURCE"].value_counts()
    # Soru 8: Ülkelere göre PRICE ortalamaları nedir?
    df.groupby('COUNTRY')['PRICE'].mean()
    # Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
    df.groupby('SOURCE')['PRICE'].mean()
    # Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
    df.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean()

# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean().round(2).head()

# Görev 3: Çıktıyı PRICE’a göre sıralayınız.

grouped_means = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean().round(2)

agg_df = grouped_means.sort_values(ascending=False).head()

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

grouped_means = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean().round(2)
agg_df = grouped_means.sort_values(ascending=False).reset_index()
agg_df.columns = ['COUNTRY', 'SOURCE', 'SEX', 'AGE', 'PRICE']
agg_df.head()

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

ages = [0, 18, 23, 30, 40, 70]
ages_range = ['0_18', '19_23', '24_30', '31_40', '41_70']
agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=ages, labels=ages_range)
agg_df.head()

# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.

agg_df['customers_level_based'] = (agg_df['COUNTRY'].str.upper() + '_'
                                   + agg_df['SOURCE'].str.upper() + '_'
                                   + agg_df['SEX'].str.upper() + '_'
                                   + agg_df['AGE_CAT'].astype(str))
agg_df[['customers_level_based', 'PRICE']].head()

# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.

agg_df['SEGMENT'] = pd.cut(agg_df['PRICE'], 4, labels=['D', 'C', 'B', 'A'])
segment_summary = agg_df.groupby('SEGMENT')['PRICE'].agg(['mean', 'max', 'sum'])
segment_summary.columns = ['Mean', 'Max', 'Sum']

# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

# 33 yaşında Android kullanan bir Türk Kaıdnı hangi segmente aittir ve ortalama ne kadar gelir getirir
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# 35 yaşında IOS kullanan bir Fransız kadın hangi segmente aittir ve ortalama ne kadar gelir getirir
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
