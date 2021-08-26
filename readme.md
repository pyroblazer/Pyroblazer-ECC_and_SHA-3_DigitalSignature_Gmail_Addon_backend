# ECC_and_SHA-3_DigitalSignature_Gmail
Ini merupakan e-mail client menggunakan Gmail API yang dapat melakukan enkripsi dengan block cipher Shamaq dan digital signature dengan Elliptic Curve Digital Signature Algorithm (ECDSA) yang menggunakan fungsi hash SHA3-256 (Keccak).

## Anggota Kelompok dan Persentase Pengerjaan 
|NIM           | NAMA                       |PERSENTASE PENGERJAAN |
|--------------|----------------------------|----------------------|
|13517044      | Ignatius Timothy Manullang | 40%                  |
|13517059      | Fatur Rahman               | 40%                  |
|13517090      | Aliffiqri Agwar            | 20%                  |
|~~13516055~~  | ~~Nathaniel Evan Gunawan~~ | 0%                   |

## Prerequisite
|No | Prerequisite                                                                      |
|---|-----------------------------------------------------------------------------------|
|1. | Email yang dapat digunakan hanya email yang ***telah*** terdaftar pada gmail      |
|2. | Versi python >=3.9                                                                |
|3. | Pastikan Anda terkoneksi dengan internet untuk mengakses gmail dan remote backend |

## Run program
1. Jalankan server python dari terminal
`python -m http.server 8000`
2. Buka browser di localhost:8000 dan locate file index.html nya
3. Tekan tombol "Authorize"
4. Sign in menggunakan akun gmail
5. Grant permission dengan menekan tombol "Allow" untuk semua prompt Grant permission dan confirm choices
6. Tampilan utama GUI akan muncul

## Sending message
1. Tekan tombol "Compose"
2. Isi alamat tujuan (To), subjek (Subject), dan pesan (Message) email
3. Pengguna dapat memilih untuk mengenkripsi pesan dan/atau menambahkan tanda tangan digital
4. Jika ingin mengenkripsi pesan, isi key encryption, tekan "Encrypt" dan hasil ciphertext akan ditampilkan ke layar
5. Jika ingin menandatangani pesan secara digital, isi key signature dengan private key, tekan "Add Signature" dan digital signature akan ditampilkan ke layar
6. Tekan tombol "Send" untuk mengirim pesan

## Receiving message
1. Buka tab "Inbox"
2. Pilih salah satu email
3. Email akan terbuka dan isi pesan terlihat
4. Pengguna dapat memilih untuk mendekripsi pesan dan/atau memverifikasi tanda tangan digital
5. Jika mendekripsi pesan, isi key decryption, tekan "Decrypt" dan hasil plaintext akan ditampilkan ke layar
6. Jika verifikasi digital signature, isi key signature, tekan "Add Signature" dan hasil verifikasi akan ditampilkan ke layar

## Backend Deployment
https://ecc-sha3-digitalsignature-back.herokuapp.com/
To deploy in Heroku, remember to link this repository and
1. Add heroku/python buildpack
2. Add the free "gunicorn app:app --log-level debug" on dyno formation
