import pandas as pd
import re
import difflib  # Library untuk Fuzzy Matching (Pencocokan Kemiripan)

def restore_columns():
    print("Memulai proses pencocokan data tingkat lanjut (Fuzzy Matching)...")
    print("Mohon tunggu sebentar, proses ini mungkin memakan waktu 10-30 detik...\n")

    # 1. BACA DATA ASLI (2000 Data)
    try:
        df_ori = pd.read_csv('../filter_manual/opinion_final.csv')
        df_ori.columns = df_ori.columns.str.replace(';', '').str.strip() 
        
        required_cols = ['id', 'clean_text', 'createdAt']
        missing_cols = [col for col in required_cols if col not in df_ori.columns]
        if missing_cols:
            print(f"\n[!] ERROR: Kolom {missing_cols} TIDAK DITEMUKAN di file data aslimu!")
            return

        print(f"Berhasil membaca data asli: {len(df_ori)} baris.")

        # Membuat "join_key" (Sekarang MEMPERTAHANKAN SPASI agar Fuzzy Match lebih akurat)
        df_ori['join_key'] = df_ori['clean_text'].astype(str).str.lower()
        # Hanya sisakan huruf, angka, dan spasi (\s)
        df_ori['join_key'] = df_ori['join_key'].str.replace(r'[^a-z0-9\s]', '', regex=True)
        # Rapikan spasi yang berlebihan menjadi 1 spasi saja
        df_ori['join_key'] = df_ori['join_key'].str.replace(r'\s+', ' ', regex=True).str.strip()
        
        df_ori = df_ori.drop_duplicates(subset=['join_key'])
        
        # Membuat Dictionary untuk pencarian yang sangat cepat
        ori_dict = df_ori.set_index('join_key')[['id', 'createdAt']].to_dict('index')
        ori_keys = list(ori_dict.keys()) 

    except FileNotFoundError:
        print("Error: File asli tidak ditemukan. Pastikan path filenya benar.")
        return

    # 2. BACA DATA SPLIT (Train, Val, Test)
    try:
        df_train = pd.read_csv('../data_labelling/train_labeled.csv')
        df_val = pd.read_csv('../data_labelling/val_labeled.csv')
        df_test = pd.read_csv('../data_labelling/test_labeled.csv')
        print(f"Berhasil membaca data split: Train({len(df_train)}), Val({len(df_val)}), Test({len(df_test)})")
    except FileNotFoundError as e:
        print(f"Error membaca file split: {e}")
        return

    # 3. FUNGSI UNTUK MENGGABUNGKAN DATA DENGAN FUZZY MATCHING
    def merge_data(df_split, name):
        # Format join_key disamakan (pertahankan spasi)
        df_split['join_key'] = df_split['cleaned_text'].astype(str).str.lower()
        df_split['join_key'] = df_split['join_key'].str.replace(r'[^a-z0-9\s]', '', regex=True)
        df_split['join_key'] = df_split['join_key'].str.replace(r'\s+', ' ', regex=True).str.strip()

        matched_ids = []
        matched_created_at = []
        missing_count = 0

        # Iterasi baris per baris untuk mencocokkan
        for key in df_split['join_key']:
            # Coba pencocokan persis (Sangat Cepat)
            if key in ori_dict:
                matched_ids.append(ori_dict[key]['id'])
                matched_created_at.append(ori_dict[key]['createdAt'])
            else:
                # Gunakan Fuzzy Matching dengan cutoff diturunkan ke 0.5 (50% mirip)
                # agar lebih toleran jika ada kata yang hilang (karena preprocessing dll)
                matches = difflib.get_close_matches(key, ori_keys, n=1, cutoff=0.5)
                if matches:
                    best_match = matches[0]
                    matched_ids.append(ori_dict[best_match]['id'])
                    matched_created_at.append(ori_dict[best_match]['createdAt'])
                else:
                    # Gagal total
                    matched_ids.append(None)
                    matched_created_at.append(None)
                    missing_count += 1
        
        # Masukkan hasil pencocokan ke dalam dataframe
        df_split['id'] = matched_ids
        df_split['createdAt'] = matched_created_at
        
        if missing_count > 0:
            print(f"[!] PERINGATAN di data {name}: Masih ada {missing_count} baris yang gagal total.")
        else:
            print(f"[OK] Data {name} berhasil dicocokkan 100%.")
        
        # Susun ulang kolom
        df_merged = df_split[['id', 'cleaned_text', 'label', 'createdAt']]
        return df_merged

    # 4. PROSES PENGGABUNGAN
    print("\n--- Proses Matching Sedang Berjalan ---")
    train_final = merge_data(df_train, "Train")
    val_final = merge_data(df_val, "Validation")
    test_final = merge_data(df_test, "Test")

    # 5. SIMPAN HASILNYA KE CSV BARU DENGAN PENANGANAN ERROR
    print("\nMenyimpan hasil...")
    try:
        train_final.to_csv('train_lengkap.csv', index=False)
        val_final.to_csv('val_lengkap.csv', index=False)
        test_final.to_csv('test_lengkap.csv', index=False)
        
        print("\nSUKSES! Semua data telah dicocokkan dan disimpan sebagai:")
        print("- train_lengkap.csv")
        print("- val_lengkap.csv")
        print("- test_lengkap.csv")
    except PermissionError:
        print("\n[!] GAGAL MENYIMPAN: Akses Ditolak (Permission Error)!")
        print("--> File 'train_lengkap.csv' (atau yang lainnya) SEDANG TERBUKA DI EXCEL.")
        print("--> Solusi: Harap TUTUP file tersebut di Excel terlebih dahulu, lalu jalankan ulang program ini.")

if __name__ == "__main__":
    restore_columns()