## Otomatik E-posta Yanıtlayıcı ve Bildirici

Bu Python betiği, belirtilen bir e-posta adresine gelen yeni e-postaları kontrol eder, otomatik e-postaları filtreler ve insanlardan gelen e-postalara otomatik bir yanıt gönderir. Ayrıca, her yeni e-posta için belirtilen bir bildirim adresine bir bildirim gönderir.

### Özellikler

* **Otomatik Yanıt:**  İnsanlardan gelen yeni e-postalara otomatik olarak yanıt verirken, otomatik yanıtları ve bildirimleri filtreler.
* **E-posta Bildirimleri:**  Her yeni e-posta için belirtilen bir adrese bildirim gönderir.
* **HTML E-posta Şablonu:**  `mail.html` dosyasından yüklenen özelleştirilebilir bir HTML şablonu kullanarak otomatik yanıtlar gönderir.
* **Kolay Kurulum:**  Gerekli ayarları `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `IMAP_SERVER`, `IMAP_PORT`, `SMTP_SERVER`, `SMTP_PORT`, `NOTIFF_MAIL` ve `NON_REPLY_KEYWORDS` değişkenlerinde kolayca yapılandırabilirsiniz.

### Gereksinimler

* Python 3.6 veya üstü
* `imaplib`, `email`, `smtplib`, `time` kütüphaneleri


### Kurulum

1. Bu depoyu klonlayın veya indirin.
2. `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `IMAP_SERVER`, `IMAP_PORT`, `SMTP_SERVER`, `SMTP_PORT` ve `NOTIFF_MAIL` değişkenlerini kendi bilgilerinizle güncelleyin.
3. Otomatik yanıt için kullanmak istediğiniz HTML şablonunu `mail.html` dosyasına yerleştirin.
4. Betiği çalıştırın:
   ```bash
   python mail.py
   ```

### Kullanım

Betik çalıştırıldığında, gelen kutunuzu 30 saniyede bir yeni e-postalar için kontrol eder. Yeni bir e-posta bulunduğunda:

* E-posta otomatik bir yanıt olarak sınıflandırılmazsa, `mail.html` dosyasındaki şablon kullanılarak otomatik bir yanıt gönderilir.
* `NOTIFF_MAIL` değişkeninde belirtilen adrese yeni e-posta hakkında bir bildirim gönderilir.

### Özelleştirme

* **Otomatik Yanıt Şablonu:** Otomatik yanıtların içeriğini özelleştirmek için `mail.html` dosyasını düzenleyin. `[Gönderen Adı]` metni, e-postayı gönderen kişinin adıyla değiştirilecektir.
* **Bildirim Mesajı:**  `bildirim_epostası_gönder` fonksiyonunu düzenleyerek bildirim mesajının formatını değiştirebilirsiniz.
