# Hands-On Jaringan Nirkabel: Interaksi Bluetooth Low Energy (BLE) & Polar Verity Sense

Proyek ini dibuat sebagai bagian dari tugas mata kuliah **Jaringan Nirkabel**. Program ini mendemonstrasikan bagaimana berinteraksi dengan perangkat *Internet of Things* (IoT) dan *wearables* menggunakan protokol komunikasi Bluetooth Low Energy (BLE). 

Fokus utama dari proyek ini adalah melakukan pemindaian (scanning) perangkat BLE di sekitar dan melakukan koneksi ke sensor **Polar Verity Sense** untuk mengekstraksi data detak jantung (*Heart Rate / HR*) secara *real-time*.

---

## Tech Stack & Dependencies

Proyek ini dibangun menggunakan teknologi berikut:

*   **Bahasa Pemrograman:** [Python 3.7+](https://www.python.org/) - Dipilih karena kemudahan pembacaan sintaks dan dukungan library IoT yang kuat.
*   **Library Utama:** `bleak` (*Bluetooth Low Energy platform Agnostic Klient*) - Sebuah pustaka klien GATT BLE untuk Python yang bersifat *cross-platform* (bekerja di Windows, macOS, dan Linux).
*   **Library Pendukung:** `asyncio` - Digunakan untuk menangani operasi *asynchronous* (*non-blocking*), mengingat komunikasi nirkabel (seperti proses scanning dan penantian aliran data notifikasi BLE) membutuhkan penanganan berbasis *event-loop*.

---

## Konsep Komunikasi (GATT Protocol)

Program ini mengandalkan profil standar **GATT (Generic Attribute Profile)** dalam arsitektur BLE:
1.  **Heart Rate Service:** Pengekstraksian data difokuskan pada Service standar BLE dengan UUID `0x180D`.
2.  **Heart Rate Measurement Characteristic:** Program melakukan *subscribe* (mendengarkan notifikasi) pada Characteristic dengan UUID `00002a37-0000-1000-8000-00805f9b34fb` untuk menerima data mentah berupa *byte array* (mengandung *flags* dan *BPM*).

---

## Struktur File

Proyek ini terbagi menjadi dua skrip utama:
1.  `1_ble_scanner.py`: Skrip untuk memindai paket *advertisement* BLE di udara. Skrip ini akan mencetak *MAC Address* dan *Device Name* dari seluruh perangkat Bluetooth yang aktif di sekitar.
2.  `2_hr_monitor.py`: Skrip inti yang berfungsi melakukan koneksi (*pairing* nirkabel via MAC Address) ke perangkat Polar Verity Sense, menerjemahkan data *byte* dari BLE, dan menampilkannya dalam format detak jantung (BPM).

---

## Cara Menjalankan Program

### 1. Instalasi Environment
Pastikan Python sudah terinstal, lalu jalankan perintah berikut pada terminal/command prompt untuk menginstal pustaka yang dibutuhkan:
```bash
pip install bleak
```

### 2. Mencari MAC Address Perangkat
Nyalakan Polar Verity Sense, kemudian jalankan skrip pemindai:
```bash
python 1_ble_scanner.py
```
Catat **MAC Address** (atau UUID jika di macOS) dari perangkat yang bernama "Polar Sense" atau sejenisnya.

### 3. Mengambil Data Detak Jantung
Buka file `2_hr_monitor.py` menggunakan teks editor pilihan Anda (seperti VSCode), dan ubah nilai pada variabel `POLAR_MAC_ADDRESS` dengan alamat perangkat yang didapatkan dari langkah ke-2.

Simpan, lalu jalankan:
```bash
python 2_hr_monitor.py
```
Program akan terhubung ke sensor dan menampilkan data detak jantung (BPM) secara *real-time* ke layar konsol selama durasi yang ditentukan.
