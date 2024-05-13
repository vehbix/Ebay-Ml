import socket
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import os
from ebaysdk.finding import Connection 
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import joblib
import time
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


hc="a*/"

#%%
class DataCollect(object):
    def __init__(self,API_KEY):
        self.api_key=API_KEY
        
    def al(self,cevap):
        self.cevap=cevap
    def fetch(self):
        print(self.cevap)
        try:
            api=Connection(appid=self.api_key, config_file=None)
            # cevap=input("Aranacak kelimeyi giriniz: ")
            cevap=self.cevap.replace(" ",",")
            
            response=api.execute('findItemsByKeywords',{'keywords':cevap})
            items_list = []
            for item in response.reply.searchResult.item:    
                try:
                    title=item.title
                except AttributeError:
                    title="N/A"
                try:
                    category=item.primaryCategory.categoryName
                except AttributeError:
                    category="N/A"
                try:
                    price=item.sellingStatus.currentPrice.value
                except AttributeError:
                    price="N/A"
                try:
                    shippingCost=item.shippingInfo.shippingServiceCost.value
                except AttributeError:
                    shippingCost="N/A"
                try:
                    shippingType=item.shippingInfo.shippingType
                except AttributeError:
                    shippingType="N/A"
                try:
                    shippingLocations=item.shippingInfo.shipToLocations
                except AttributeError:
                    shippingLocations="N/A"
                try:
                    oneDayShipping=item.shippingInfo.oneDayShippingAvailable
                except AttributeError:
                    oneDayShipping="N/A"
                try:
                    handlingTime=item.shippingInfo.handlingTime
                except AttributeError:
                    handlingTime="N/A"
                try:
                    bestOffer=item.listingInfo.bestOfferEnabled
                except AttributeError:
                    bestOffer="N/A"
                try:
                    buyItNow=item.listingInfo.buyItNowAvailable
                except AttributeError:
                    buyItNow="N/A"
                try:
                    gift=item.listingInfo.gift
                except AttributeError:
                    gift="N/A"
                try:
                    watchCount=item.listingInfo.watchCount
                except AttributeError:
                    watchCount="N/A"
                try:
                    returns=item.returnsAccepted
                except AttributeError:
                    returns="N/A"
                try:
                    condition=item.condition.conditionDisplayName
                except AttributeError:
                    condition="N/A"
                try:
                    topRated=item.topRatedListing
                except AttributeError:
                    topRated="N/A"

                item_info = {
                    'Title': title,
                    'Category': category,
                    'Price': price,
                    'ShippingCost': shippingCost,
                    'ShippingType': shippingType,
                    'ShippingLocations': shippingLocations,
                    'OneDayShipping': oneDayShipping,
                    'HandlingTime': handlingTime,
                    'BestOffer': bestOffer,
                    'BuyItNow': buyItNow,
                    'Gift': gift,
                    'WatchCount': watchCount,
                    'Returns': returns,
                    'Condition': condition,
                    'TopRated': topRated

                }
                items_list.append(item_info)
            self.items=items_list
            if items_list:
                file_name = 'ebay_items.csv'
                if os.path.exists(file_name):
                    existing_data = pd.read_csv(file_name,sep=";")
                    updated_data = pd.DataFrame(items_list)
                    new_data = pd.concat([existing_data, updated_data])
                    new_data.to_csv(file_name, sep=";", index=False)
                    print("Items appended to ebay_items.csv")
                    
                else:
                    df = pd.DataFrame(items_list)
                    df.to_csv(file_name, sep=";", index=False)
                    print("Items saved to ebay_items.csv")
                    
            else:
                print("No items found.")
                return "No items found."

        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    def response(self):
        parseItems=[]
        for item in self.items:           
            parseItems.append([item['Title'],item['Price']])
        return parseItems
    def parse(self):
        pass
#%%
class SellingAnalize():
    def __init__(self) -> None:
        pass

    def read_csv(self,csv_file):
        # Verilerin bulunduğu CSV dosyasını oku
        df = pd.read_csv(csv_file, delimiter=";")
        #boş verileri sil
        df.dropna(inplace=True)

        try:
            df['Price'] = pd.to_numeric(df['Price'].str.replace(',', '.'), errors='coerce')
        except AttributeError:
            pass

        df= df.sample(frac=1).reset_index(drop=True)
        return df

    def littleCategoryDelete(self,df):
        for category in df['Category'].unique():    
            category_data = df[df['Category'] == category]
            if len(category_data) < 10:
                df = df[df['Category'] != category]                
        return df

    def standartDeviation(self,df):
        for category in df['Category'].unique():    
            category_data = df[df['Category'] == category]
            prices = category_data['Price']            
            price_averages = prices.mean()
            distance_rates = abs((prices - price_averages) / price_averages)
            large_deviations = distance_rates > 0.8

            df = df[~(df['Category'] == category) | ~large_deviations]
        print(len(df))
        return df

    def dataProcess(self,df,repeat):
        df = self.littleCategoryDelete(df)
        for i in range(repeat):
            df = self.standartDeviation(df)
        return df

    def dataTitleProcess(self,df,df_All):
        vectorizer = CountVectorizer(min_df=0.01, max_df=0.95)
        X = vectorizer.fit_transform(df_All['Title'])


        X_veri=X[-1:]
        X=X[:X.shape[0]-1]


        y = df['Price']
        return X,X_veri,y

    def dataAllProcess(self,df,df_All):
        df_numeric=df_All[['ShippingCost','OneDayShipping','BestOffer','BuyItNow','Gift','WatchCount','HandlingTime','Returns','TopRated']]
        df_categorical = df_All[['Category','ShippingType','ShippingLocations','Condition']]
        categorical_columns = ['Category','ShippingType','ShippingLocations','Condition']

        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), categorical_columns)
            ],
            remainder='passthrough'
        )

        vectorizer = CountVectorizer()
        # print(df['Title'])

        X_title = vectorizer.fit_transform(df_All['Title'])
        X_categorical = preprocessor.fit_transform(df_categorical)
        X = np.hstack((X_title.toarray(),df_numeric,X_categorical.toarray() ))
        y = df['Price']

        X_veri=X[-1:]
        X=X[:len(X)-1]
        return X,X_veri,y
    
    def modelGenerate(self,X,y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=22)
        model = RandomForestRegressor(n_estimators=80, max_depth=7, random_state=42) #%9
        model.fit(X_train, y_train)
        return model,X_train,X_test,y_train,y_test

    def modelPredict(self,y_test,X_test,model):
        ornekMiktar = len(y_test)
        X_test_sample = X_test[:ornekMiktar]
        predictions = model.predict(X_test_sample)
        return predictions,ornekMiktar
    
    def modelSave(self,model,filename):
        pickle.dump(model, open(filename, 'wb'))
    def modelLoad(self, filename):
        model = joblib.load(filename)
        # model = pickle.load(open(filename, 'rb'))
        return model


#Görselleştirme
    def kategoriAnaliz(self,df):
        kategori_dict = {}
        # Her bir kategoriyi al
        for kategori in df['Category'].unique():   
            category_data = df[df['Category'] == kategori]   
            if len(category_data) > 10:  
                kategori_verileri = df[df['Category'] == kategori]
                    
                # Bu kategoriye ait tüm başlıkları birleştir
                basliklar = ' '.join(kategori_verileri['Title'])
                
                # Küçük harfe dönüştür ve noktalama işaretlerini kaldır
                basliklar = basliklar.lower().replace(',', '').replace('.', '').replace('"', '').replace("'", "")
                
                # Boşluklara göre kelimelere ayır
                kelimeler = basliklar.split()
                
                # Sözcük sayısını say
                kelime_sayisi = Counter(kelimeler)
                
                # En sık geçen 10 kelimeyi al
                en_sik_gecenler = kelime_sayisi.most_common(20)
                
                # Kategoriyi anahtar olarak kullanarak, en sık geçen kelimeleri ve sayılarını sakla
                kategori_dict[kategori] = en_sik_gecenler
        return kategori_dict

    def standartDeviationPlt(self,df):
        plt.figure(figsize=(19.2, 9.7))
        c = 1  # subplot indeksi
        for category in df['Category'].unique():
            category_data = df[df['Category'] == category]
            if len(category_data) < 10:
                continue
            titles = range(0, len(category_data['Title']))
            prices = category_data['Price']
            price_averages = prices.mean()
            
            distance_rates = abs((prices - price_averages) / price_averages)
            large_deviations = distance_rates > 0.8
            
            if c % 25 == 0:
                plt.subplots(figsize=(19.2, 9.7))
                plt.subplots_adjust(left=0.04, right=0.989, top=0.967, bottom=0.14, wspace=0.166)
                plt.tight_layout()
                mng = plt.get_current_fig_manager()
            
            for i, (title, fiyat) in enumerate(zip(titles, prices)):
                color = 'red' if large_deviations.iloc[i] else 'blue'
                plt.subplot(5, 5, c % 25 + 1)
                plt.scatter(title, fiyat, color=color)
                
                plt.xlabel('Başlık')
                plt.ylabel('Fiyat')
                plt.title('{}'.format(category))
                plt.xticks(rotation=45)
                c += 1
                
            df = df[~((df['Category'] == category) & large_deviations)]
        print(len(df))
        plt.show()
        return df

    def kategoriAnalizPlt(self,kategori_dict):
        plt.figure(figsize=(19.2, 9.7))
        c = 1  # subplot indeksi
        for i, (kategori, kelimeler) in enumerate(kategori_dict.items(), start=1):
            if c % 16 == 0:
                plt.subplots()
                plt.tight_layout()
            plt.subplot(4, 4, c % 16 +1 )
            
            kelime_listesi, sayi_listesi = zip(*kelimeler)
            plt.bar(kelime_listesi, sayi_listesi, color='skyblue')
            plt.xlabel('Kelime')
            plt.ylabel('Frekans')
            plt.title( kategori)
            plt.xticks(rotation=90)
            
            c += 1

        # Alt başlıklar arasındaki çakışmayı önlemek için düzenleme yap
        plt.subplots_adjust(left=0.04, right=0.989, top=0.967, bottom=0.14, wspace=0.166)
        plt.tight_layout()
        # mng = plt.get_current_fig_manager()

        # Tüm figürleri göster
        plt.show()
        return kategori_dict

    def kategoriFiyatAnaliz(self,df):
        plt.figure(figsize=(15, 10))
        for kategori in df['Category'].unique():
            kategori_verileri = df[df['Category'] == kategori]
            plt.hist(kategori_verileri['Price'], bins=20, alpha=0.5, label=kategori)

        plt.xlabel('Fiyat')
        plt.ylabel('Frekans')
        plt.title('Kategorilere Göre Fiyat Dağılımı')
        plt.legend()
        plt.grid(True)
        plt.show()

    def predictPrint(self,predictions,y_test,ornekMiktar):
        # Tahminlerin yanında gerçek fiyatı ve sample ismini yazdır
        print("Tahminler:")
        for i, (prediction, actual) in enumerate(zip(predictions, y_test[:ornekMiktar]), start=1):
            pass
            # Tahmin edilen fiyatı 2 ondalık basamağa kadar sınırla
            formatted_prediction = "{:.2f}".format(prediction)
            # Gerçek fiyatı 2 ondalık basamağa kadar sınırla
            formatted_actual = "{:.2f}".format(actual)
            # if ((actual-prediction)/actual) > 0.1 :
            if ((actual-prediction)/actual) > 0.6 :
                print(f"Tahmin {i} : Tahmin Edilen Fiyat: {formatted_prediction}, Gerçek Fiyat: {formatted_actual}")
            # print(f"Tahmin {i} : Tahmin Edilen Fiyat: {formatted_prediction}, Gerçek Fiyat: {formatted_actual}")

    def featureImportance(self,model,preprocessor,vectorizer,categorical_columns):
        # RandomForestRegressor gibi bir ağaç tabanlı modelin feature_importances_ özelliğini kullanarak özellik önemini alın
        feature_importance = model.feature_importances_

        # Özellik isimlerini alın
        # Kategorik sütun isimleri
        categorical_column_names = preprocessor.named_transformers_['cat'].get_feature_names_out(input_features=categorical_columns)

        # Özellik isimlerini birleştirin
        feature_names = list(vectorizer.get_feature_names_out()) + list(categorical_column_names)

        # Özellik isimleri ve önemini birleştirin ve öneme göre sıralayın
        feature_importance_list = list(zip(feature_names, feature_importance))
        feature_importance_list.sort(key=lambda x: x[1], reverse=False)

        # Özellik isimleri ve önemlerini yazdırın
        print("Özelliklerin Önemi:")
        for feature, importance in feature_importance_list:
            print(f"{feature}: {importance}")

    def modelEvaluation(self,model,X_train,y_train,X_test,y_test,predictions):
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        # Gerçek ve tahmini fiyatları kullanarak farklı metrikleri hesaplayın
        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, predictions)
        # Sonuçları yazdırın
        print("Ortalama Mutlak Hata (MAE):", mae)
        print("Ortalama Kare Hata (MSE):", mse)
        print("Kök Ortalama Kare Hata (RMSE):", rmse)
        print("R² (R Kare) Değeri:", r2)
        print(f"Eğitim Skoru: {train_score}")
        print(f"Test Skoru: {test_score}")

    def modelPlot(self,model,predictions,X_train,y_train,y_test,ornekMiktar):
        predicted_prices = predictions[:ornekMiktar]  # Sadece ilk 10 tahmini alır
        actual_prices = y_test[:ornekMiktar]  # Sadece ilk 10 gerçek fiyatı alır

        # Tahmin edilen fiyatlar ve gerçek fiyatlar arasındaki sapmayı hesapla
        sapma = actual_prices - predicted_prices

        # R-kare değerini hesapla
        r_squared = r2_score(actual_prices, predicted_prices)

        # Toplam sapma miktarını hesapla
        toplam_sapma = sum(abs(sapma))

        # Toplam sapma miktarının oransal olarak yüzde olarak hesaplanması
        toplam_veri_sayisi = len(predicted_prices)
        oransal_toplam_sapma = (toplam_sapma / (sum(actual_prices) + sum(predicted_prices))) * 100

        # Modelin performansını değerlendir
        train_score = model.score(X_train, y_train)
        # test_score = model.score(X_test, y_test)

        # Nokta grafiğini çiz
        plt.figure(figsize=(10, 6))
        plt.scatter(range(1, ornekMiktar+1), predicted_prices, color='red', label='Tahmin Edilen Fiyatlar')
        plt.scatter(range(1, ornekMiktar+1), actual_prices, color='blue', label='Gerçek Fiyatlar')

        # Noktalar arasında çizgi çekme
        plt.plot(range(1, ornekMiktar+1), predicted_prices, color='red', linestyle='-', linewidth=0.5)
        plt.plot(range(1, ornekMiktar+1), actual_prices, color='blue', linestyle='-', linewidth=0.5)

        # İki çizgi arasındaki alanı karala
        plt.fill_between(range(1, ornekMiktar+1), predicted_prices, actual_prices, color='gray', alpha=0.3)

        plt.xlabel('Örnekler')
        plt.ylabel('Fiyatlar')
        plt.title(f'Tahmin Edilen ve Gerçek Fiyatlar (Train: {train_score*100:.2f}, R-kare: {r_squared*100:.2f}, Toplam Sapma: {toplam_sapma:.2f}, Oransal Toplam Sapma: {oransal_toplam_sapma:.2f}%)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def columnEffects(self,df,model):
        column_effects = {}

        # Sayısal özniteliklerin hazırlanması
        df_numeric = df[['ShippingCost','OneDayShipping','BestOffer','BuyItNow','Gift','WatchCount','HandlingTime','Returns','TopRated']]

        # Kategorik özniteliklerin hazırlanması
        df_categorical = df[['Category','ShippingType','ShippingLocations','Condition']]
        categorical_columns = ['Category','ShippingType','ShippingLocations','Condition']
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), categorical_columns)
            ],
            remainder='passthrough'
        )
        X_categorical = preprocessor.fit_transform(df_categorical)

        # 'Title' sütununun vektörize edilmiş hali
        vectorizer = CountVectorizer()
        X_title = vectorizer.fit_transform(df['Title'])

        # Tüm özniteliklerin birleştirilmiş hali
        X = np.hstack((X_title.toarray(), df_numeric, X_categorical.toarray()))

        # Bağımlı değişken ve bağımsız değişkenleri ayarlayın
        y = df['Price']

        # Tüm sütunların isimlerini alın
        all_columns = ['Title', 'Category', 'ShippingCost', 'ShippingType', 'ShippingLocations', 
                    'OneDayShipping', 'HandlingTime', 'BestOffer', 'BuyItNow', 'Gift', 'WatchCount', 
                    'Returns', 'Condition', 'TopRated']

        # Her bir sütun için etkisini hesaplamak için bir döngü oluşturun
        for column in all_columns:
            print(f"Sütun: {column}")
            
            # Belirli bir sütunu seçin
            if column == 'Title':
                X_column = X_title
            elif column in df_numeric.columns:
                X_column = df_numeric[[column]]
            else:
                column_index = df_categorical.columns.get_loc(column)
                start_index = X_title.shape[1] + len(df_numeric.columns)
                end_index = start_index + X_categorical.shape[1]
                X_column = X[:, start_index:end_index]
            
            # Modeli eğitin
            model.fit(X_column, y)
            
            # Tahmin yapın
            predictions = model.predict(X_column)
            
            # R² değerini hesaplayın
            r2 = r2_score(y, predictions)
            
            # Sonucu sözlüğe kaydedin
            column_effects[column] = r2
            
            # Sonucu yazdırın
            print(f"R² = {r2}")

        # Her bir sütunun etkisini yazdırın
        print("Sütun Etkileri:")
        for column, effect in column_effects.items():
            print(f"{column}: R² = {effect}")

    #DATA
    def dataSetup(self,df):
                
            df_numeric=df[['ShippingCost','OneDayShipping','BestOffer','BuyItNow','Gift','WatchCount','HandlingTime','Returns','TopRated']]

            df_categorical = df[['Category','ShippingType','ShippingLocations','Condition']]
            categorical_columns = ['Category','ShippingType','ShippingLocations','Condition']
            print(categorical_columns)

            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(), categorical_columns)
                ],
                remainder='passthrough'
            )

            vectorizer = CountVectorizer()
            X_title = vectorizer.fit_transform(df['Title'])

            X_categorical = preprocessor.fit_transform(df_categorical)

            X = np.hstack((X_title.toarray(),df_numeric,X_categorical.toarray() ))
            y = df['Price']

            return X,y,preprocessor,vectorizer,categorical_columns



#Kernel
    def title(self,girdi):
        know=veriTitle(str(girdi),"")
        veri_df=pd.DataFrame([vars(know)], columns=vars(know).keys())

        df = self.read_csv("ebay_items.csv")
        df = self.dataProcess(df, 2)
        df=df[["Title","Price"]]
        df_All = pd.concat([df, veri_df], ignore_index=True)

        X,X_veri,y=self.dataTitleProcess(df,df_All)        
        model,X_train,X_test,y_train,y_test=self.modelGenerate(X,y)
        self.modelSave(model,'finalized_model_title.sav')
        self.modelLoad('finalized_model_title.sav')

        predictions = model.predict(X_veri)[0].round(2)
        return predictions



    def all(self,know):
        veri_df=pd.DataFrame([vars(know)], columns=vars(know).keys())        

        df = self.read_csv("ebay_items.csv")
        df = self.dataProcess(df, 2)
        veri_df= veri_df.sample(frac=1).reset_index(drop=True)
        df_All = pd.concat([df, veri_df], ignore_index=True)
        X,X_veri,y=self.dataAllProcess(df,df_All)        

        model,X_train,X_test,y_train,y_test=self.modelGenerate(X,y)
        self.modelSave(model,'finalized_model_all_data.sav')
        self.modelLoad('finalized_model_all_data.sav')

        predictions = model.predict(X_veri)[0].round(2)
        return predictions


class veriTitle():
    def __init__(self, Title,Price):
        self.Title=Title
        self.Price=Price

class veriAll():
    def __init__(self, Title, Category,  ShippingCost, ShippingType, ShippingLocations, OneDayShipping, HandlingTime, BestOffer, BuyItNow, Gift, WatchCount, Returns, Condition, TopRated):
        self.Title=Title
        self.Price=""
        self.Category=Category
        self.ShippingCost=ShippingCost
        self.ShippingType=ShippingType
        self.ShippingLocations=ShippingLocations
        self.OneDayShipping=OneDayShipping
        self.HandlingTime=HandlingTime
        self.BestOffer=BestOffer
        self.BuyItNow=BuyItNow
        self.Gift=Gift
        self.WatchCount=WatchCount
        self.Returns=Returns
        self.Condition=Condition
        self.TopRated=TopRated


def main(girdi):    
    load_dotenv()
    API_KEY = os.getenv("api_key")
    getir=DataCollect(API_KEY)

    seller=SellingAnalize()

    girdiList=girdi.split(hc)
    nemList=[]
    
    for i in range(len(girdiList)):
        if girdiList[i]==hc:
            continue
        else:
            nemList.append(girdiList[i])

    print(len(nemList))
    if len(nemList)==2:
        return seller.title(nemList[0])
    elif len(nemList)==3:
        getir.al(str(nemList[0]))
        getir.fetch()
        veriler=getir.response()
        return veriler

    elif len(nemList)==14:
        know=veriAll("HP laptop Chromebook 11 G5 N3060 1.60GHz 4GB 16GB SSD 11.6 WEBCAM BLUETOOTH WIFI","PC Laptops & Netbooks",0.0,"Free","Worldwide",False,3,False,False,False,1422.0,True,"Used",False)
        girdi=seller.all(know)
    else:
        return "Hata oluştu"
    
    return girdi

def sunucu():
    # Sunucunun IP adresi ve port numarası
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 12345

    # Bağlantı bekleyeceğimiz maksimum istemci sayısı
    MAX_CLIENTS = 5

    # Soket oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Yeniden kullanılabilir portu ayarla
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Sunucu soketini belirtilen IP adresi ve port numarasına bağla
    server_socket.bind((SERVER_IP, SERVER_PORT))

    # İstemci bağlantılarını kabul etmeye başla
    server_socket.listen(MAX_CLIENTS)

    print(f"Sunucu {SERVER_IP}:{SERVER_PORT} üzerinde çalışıyor...")

    while True:
        # Yeni bir bağlantı isteği bekleyin
        client_socket, client_address = server_socket.accept()
        print(f"{client_address} adresinden bağlantı alındı.")

        # İstemciden gelen mesajı al
        message = client_socket.recv(1024).decode()
        print(f"{client_address} adresinden gelen mesaj: {str(message)}")
        try:
            respons = main(message)
        except:
            respons = "Hata oluştu"

        if type(respons)==list:
            response=""
            for item in respons:
                response += str(item[1])+" "+str(item[0])+"\n"
            
        else:            
            response = str(respons)

        # İstemciye yanıt gönder
        client_socket.send(response.encode())

        #İstemci soketini kapat
        client_socket.close()


sunucu()