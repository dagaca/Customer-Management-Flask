# Customer-Management-Flask

Bu repoda bulunan Flask uygulaması, müşteri bilgilerini yönetmeyi amaçlamaktadır.


## Proje Ağacı

Customer-Management-Flask/

│

├── static/

│ ├── css/

│ │ └── style.css

│

├── templates/

│ └── customer_list.html

│ └── add_customer.html

│

├── README.md

├── app.py

├── requirements.txt


## Kurulum

1. **Projeyi İndirin veya Klonlayın:**

    ```bash
    git clone https://github.com/dagaca/Customer-Management-Flask.git
    ```

2. **Proje Klasörüne Gidin:**

    ```bash
    cd Customer-Management-Flask
    ```

3. **Virtual Environment Oluşturun:**

    ```bash
    python -m venv venv
    ```

4. **Virtual Environment'ı Etkinleştirin:**

    - **Windows:**

    ```bash
    .\venv\Scripts\activate
    ```

    - **Linux veya MacOS:**

    ```bash
    source venv/bin/activate
    ```

5. **Gerekli Bağımlılıkları Yükleyin:**

    ```bash
    pip install -r requirements.txt
    ```


## Kullanım

- Ana sayfada müşteri listesini görüntüleyebilir ve sıralayabilirsiniz.
- "Add Customer" sayfasından yeni müşteri ekleyebilirsiniz.


## Veritabanı Ayarları

Bu projede, PostgreSQL veritabanı kullanılmaktadır. Veritabanı bağlantı ayarları `app.py` dosyasında `db_params` değişkeni içinde belirtilmiştir. Bu bilgileri kendi PostgreSQL ve pgAdmin kurulumunuza uygun şekilde düzenlemelisiniz.

```python
# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}
```

- Yukarıdaki parametreleri kendi PostgreSQL kurulumunuzun bilgileriyle güncelleyin. Örneğin, your_database_name kısmına oluşturduğunuz veritabanının adını, your_username kısmına PostgreSQL kullanıcı adınızı, your_password kısmına şifrenizi, your_host kısmına PostgreSQL sunucu adresinizi, ve your_port kısmına PostgreSQL'in çalıştığı port numarasını ekleyin.


## Katkıda Bulunma
Eğer bu projeye katkıda bulunmak istiyorsanız, lütfen forklayın ve pull request gönderin.
