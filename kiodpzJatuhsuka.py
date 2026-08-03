import time
import sys
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ketik_dengan_delay_per_kata(teks, daftar_delay, delay_akhir=0.5):  
    """
    Ngetik per kata dengan delay yang bisa diatur per kata
    daftar_delay = list delay setelah setiap kata (termasuk spasi)
    delay_akhir = jeda setelah seluruh baris selesai
    """
    kata_list = teks.split(' ')
    
    for i, kata in enumerate(kata_list):
        for huruf in kata:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(0.09)  
        
        
        if i < len(kata_list) - 1:
            sys.stdout.write(' ')
            sys.stdout.flush()
            if i < len(daftar_delay):
                time.sleep(daftar_delay[i])
    
    time.sleep(delay_akhir)

def main():
    bersihkan_layar()
    
    # HEADER
    print("="*50)
    print("   🎵  K I O U D A P Z • J A T U H  S U K A  ")
    print("="*50)
    print()
    time.sleep(1)
    
    
    lirik = [
        {
            "teks": "Bila kau lihat ku tanpa sengaja",
            "delay": [0.3, 0.3, 1.7, 0.3, 0.3],  
            "delay_akhir": 2.8  
        },
        {
            "teks": "Beginikah surga?",
            "delay": [0.1],
            "delay_akhir": 0.8
        },
        {
            "teks": "Bayangkan bila kau ajakku bicara",
            "delay": [1.3, 1.0, 0.3, 0.5],
            "delay_akhir": 4.5
        },
        {
            "teks": "Ini semua bukan salahmu",
            "delay": [0.2, 0.2, 0.3],
            "delay_akhir": 3.2
        },
        {
            "teks": "Punya magis perekat yang sekuat itu",
            "delay": [0.1, 0.1, 0.1, 0.1, 0.2],
            "delay_akhir": 1.5
        },
        {
            "teks": "Dari lahir sudah begitu",
            "delay": [0.2, 0.2, 0.3],
            "delay_akhir": 2.2
        },
        {
            "teks": "Maafkan...",
            "delay": [],
            "delay_akhir": 4.5
        },
        {
            "teks": "Aku jatuh suka",
            "delay": [0.2, 0.2],
            "delay_akhir": 0.5
        },
    ]
    
    for idx, item in enumerate(lirik):
        sys.stdout.write("   ")
        sys.stdout.flush()
        
        ketik_dengan_delay_per_kata(
            item["teks"], 
            item["delay"],
            item["delay_akhir"] 
        )
        print()  
        
    
    # FOOTER
    print()
    print("="*50)
    print(" D I N G G E W O N G - K O N O - K A E ")
    print("="*50)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Sampai jumpa!")