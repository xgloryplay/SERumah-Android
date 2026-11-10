# SERumah Android

Project Android terpisah untuk membungkus aplikasi web SERumah menggunakan Capacitor 6.

## Aplikasi tujuan

`https://satuproyeksi.com/profiles/serumah/`

**Catatan:** versi ini memuat aplikasi dari server HTTPS dan membutuhkan koneksi internet. Ini bukan versi offline dan tidak menyalin source code website ke dalam APK.

## Build APK otomatis

1. Buat repository GitHub baru bernama `SERumah-Android` (jangan gunakan repository Android/Reconciler).
2. Upload seluruh isi folder project ini ke root repository baru, termasuk folder tersembunyi `.github`.
3. Commit ke branch `main`.
4. Buka tab **Actions** → **Build SERumah APK** → **Run workflow**.
5. Setelah selesai, unduh artifact **serumah-debug-apk**.
6. Ekstrak artifact ZIP, lalu instal `app-debug.apk` di perangkat Android.

Push pertama ke `main` juga otomatis menjalankan build.

## Plugin perangkat

Plugin Capacitor Camera, Geolocation, dan Local Notifications sudah dimasukkan sebagai dependensi. Keberadaan plugin saja belum otomatis membuat fitur kamera, GPS, atau notifikasi berfungsi. Website SERumah perlu memanggil plugin/API yang sesuai dan meminta izin saat fitur digunakan.

## Status distribusi

Workflow ini menghasilkan **debug APK untuk pengujian**. Untuk distribusi resmi, perlu release signing dengan Android keystore dan kredensial yang disimpan sebagai GitHub Actions Secrets. Jangan pernah commit keystore atau password ke repository.
