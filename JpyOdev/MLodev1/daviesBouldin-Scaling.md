# Davies-Bouldin Metodu ve Scaling 

##  1. Davies-Bouldin Index Nedir?

Davies-Bouldin Index (DBI), kümeleme algoritmalarının kalitesini değerlendirmek için kullanılan bir metriktir. Kümeleme sonucunda elde edilen kümelerin birbirine olan benzerliği ve yoğunluğu göz önünde bulundurularak hesaplanır.

###  Nasıl Çalışır?
- Her küme için, kendi içindeki **ortalama mesafe içsel varyans ve diğer kümelere olan merkez mesafeleri  kullanılır.
- Küme ne kadar yoğun ve diğer kümelerden ne kadar uzak ise o kadar iyidir.

### Formül:
Davies-Bouldin skoru şöyle hesaplanır:

\[
DBI = \frac{1}{n} \sum_{i=1}^{n} \max_{j \neq i} \left( \frac{\sigma_i + \sigma_j}{d(c_i, c_j)} \right)
\]

- \( \sigma_i \): i. kümenin içsel yayılımı (örneğin ortalama mesafe)
- \( d(c_i, c_j) \): i ve j kümelerinin merkezleri arasındaki mesafe

###  Python ile Uygulama (Scikit-learn):
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score

# Veri oluştur
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Kümeleme
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Davies-Bouldin skoru
db_score = davies_bouldin_score(X, labels)
print("Davies-Bouldin Skoru:", db_score)
```

> **Not:** DBI skoru ne kadar düşükse kümeler o kadar iyidir.

---

## 2. Scaling 

Scaling, makine öğrenmesinde özelliklerin aynı ölçekte olmasını sağlamak için yapılan işlemdir. Özellikle **mesafeye dayalı algoritmalar (KNN, K-Means, SVM)** için önemlidir.

###  Neden Gerekli?
- Bazı değişkenler diğerlerinden çok daha büyük olabilir (örneğin yaş: 0–100, gelir: 1000–100000).
- Bu durumda büyük değerli değişkenler, modelin öğrenmesini yanlıs yapabilir.

###  Yöntemler:

####  1. **Min-Max Scaling**
Her değeri 0–1 aralığına getirir.
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

#### 2. **StandardScaler (Z-Score Normalizasyonu)**
Ortalama = 0, Standart sapma = 1 olacak şekilde dönüşüm yapar.
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## 3. **RobustScaler**
Aykırı değerlere karşı dayanıklıdır. Medyan ve IQR (çeyrek değer farkı) kullanır.
```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

---

###  Özet:
- **Davies-Bouldin Index**: Kümeleme başarısını ölçer. Düşük skor iyidir.
- **Scaling**: Özelliklerin aynı ölçekle ifade edilmesini sağlar. Özellikle mesafe bazlı algoritmalarda performansı doğrudan etkiler.
